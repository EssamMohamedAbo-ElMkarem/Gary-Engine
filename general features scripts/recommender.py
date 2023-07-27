from transformers import ElectraPreTrainedModel ,ElectraModel

class ElectraClassifier(ElectraPreTrainedModel):

  def __init__(self,config):
    super().__init__(config)
    self.n_classes = config.num_labels
    self.config = config
    self.electra = ElectraModel(config)
    self.classifier = ElectraClassificationHead(config)
    self.post_init()

  def forward(self, input_ids=None,attention_mask=None):
    discriminator_hidden_states = self.electra(input_ids, attention_mask)
    sequence_output = discriminator_hidden_states[0]
    logits = self.classifier(sequence_output)
    return logits


def classifyEmotions_new(text, trainer_model, tokenizer, emotions_categories, threshold=0.9):
    text_encoding = tokenizer(
        text,
        max_length = 64,
        truncation =True,
        padding = "max_length",
        add_special_tokens=True,
        return_token_type_ids=False,
        return_attention_mask = True,
        return_tensors="pt"
    )
    with torch.no_grad():
      pred = trainer_model(text_encoding["input_ids"],text_encoding["attention_mask"])
      pred= pred.flatten().numpy()
    

    pred_labels = []
    for i, label_name in enumerate(emotions_categories):
      label_prob = pred[i]
      if label_prob > threshold :
        pred_labels.append(label_name)

    
    return pred_labels


#open excel file
def open_excel(path):
    wb = openpyxl.load_workbook(path)
    sheet=wb.active
    return sheet

# save rows from text file to dictionary while mapping duration and type
def save_map_data(emotions, type_, duration):

    duration_maps = {
        "song": {"short": (2, 4), "medium": (4, 7), "long": (7, 13)},
        "video": {"short": (1, 8), "medium": (8, 20), "long": (20, 40)},
        "article": {"short": (1, 4), "medium": (4, 7), "long": (7, 16)}
    }  # Define mappings for duration for each type_
    duration_map = duration_maps.get(type_, {}).get(duration, None)
    duration = duration_map if duration_map else None
    return {"emotions": emotions, "type_": type_, "duration": duration}

def get_rows_with_emotions(sheet, type_, duration,emotions):

    # Initialize an empty list to store the matching rows
    matching_rows = []

    # Iterate over the rows in the sheet and check if the type_ and duration values match
    for row in sheet.iter_rows(min_row=2, values_only=True):  # assuming first row contains headers
        if( row[0] == type_ and (row[2] >= duration[0] and row[2] < duration[1])):
            emotions_row = [e.strip() for e in row[1].split(",")]

            # Count the number of matching items between the row's emotions and the emotions from the dictionary
            matching_count = sum(1 for e in emotions_row if e in emotions)
            
            # If the row only contains "neutral" emotion, append it
            if (len(emotions) == 1 and emotions[0] == "neutral"):
                matching_rows.append(row)
            # If the row contains other emotions, exclude "neutral" from the comparison
            elif (len(emotions) > 1 and "neutral" in emotions):
                emotions_row.remove("neutral")
                if matching_count >= 3:
                    matching_rows.append(row)
            # If the row contains non-neutral emotions only, compare all of them to the dictionary
            else:
                if matching_count >= 3:
                    matching_rows.append(row)


    # Return the list of matching rows
    return matching_rows


if __name__ == "__main__":
    import os
    import torch
    import argparse
    import openpyxl
    import pandas as pd
    import json
    import random
    from transformers import ElectraPreTrainedModel ,ElectraModel, AutoTokenizer
    from transformers import  ElectraTokenizerFast as ElectraTokenizer 
    from transformers.models.electra.modeling_electra import ElectraClassificationHead

    parser = argparse.ArgumentParser()
    parser.add_argument('--text', type=str, help='user input text')
    parser.add_argument('--type', type=str, help='article, song or movie')
    parser.add_argument('--duration', type=str, help='short, medium or long')
    opt = parser.parse_args()
    text = opt.text
    type_ = opt.type
    duration = opt.duration
    main_dir = os.getcwd()
    electra_dir = main_dir +  "/models/models/electra"
    output_dir = os.path.join(main_dir, "tmp_outputs/recommender_outputs")
    sheet_path = os.path.join(main_dir, "Scripts/data.xlsx")
    MODEL_NAME = "google/electra-base-discriminator"
    tokenizer = AutoTokenizer.from_pretrained(main_dir + '/models/models/electratokenizer')
    loaded_model = ElectraClassifier.from_pretrained(electra_dir)
    emotions_categories = ['admiration', 'amusement', 'anger', 'annoyance', 'approval', 'caring',
       'confusion', 'curiosity', 'desire', 'disappointment', 'disapproval',
       'disgust', 'embarrassment', 'excitement', 'fear', 'gratitude', 'grief',
       'joy', 'love', 'nervousness', 'optimism', 'pride', 'realization',
       'relief', 'remorse', 'sadness', 'surprise', 'neutral']

    emotions_list = classifyEmotions_new(text, loaded_model, tokenizer, emotions_categories, threshold=1)

    sheet = open_excel(sheet_path)
    data = save_map_data(emotions_list, type_, duration)
    rows = get_rows_with_emotions(sheet,data["type_"], data["duration"], data["emotions"])

    output = [{"title": row[3], "link": row[4]} for row in rows]
    if len(output) > 10:
        output = random.sample(output, 10)
        with open(output_dir + "/recommender_output.json", "w") as f:
            json.dump(output, f)
    else:
        with open(output_dir + "/recommender_output.json", "w") as f:
            json.dump(output, f)