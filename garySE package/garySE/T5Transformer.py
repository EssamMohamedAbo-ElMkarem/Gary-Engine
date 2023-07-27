import torch
import os
from Gary.garySE.cfg import *
from transformers import(
    AdamW,
    T5ForConditionalGeneration,
    T5TokenizerFast as T5Tokenizer
)
class T5Transformer(config):
    def __init__(self,text) -> None:
        self.text = text
        self.loaded_model = T5ForConditionalGeneration.from_pretrained(
            os.path.join(config.main_dir, "models\\Search_Bar\\Model"))
    def get_classes(self):
        
        tokenizer = T5Tokenizer.from_pretrained(os.path.join(config.main_dir, "models\\Search_Bar\\Tokenizer"))
        text_encoding = tokenizer(
            self.text,
            max_length = 150,
            padding = "max_length",
            truncation= True,
            return_attention_mask = True,
            add_special_tokens = True,
            return_tensors = "pt"
        )

        generated_ids = self.loaded_model.generate(
            input_ids = text_encoding["input_ids"],
            attention_mask = text_encoding["attention_mask"],
            max_length = 150,
            num_beams = 2,
            repetition_penalty = 2.5,
            length_penalty = 1.0,
            early_stopping = True
        )
        
        preds = [tokenizer.decode(gen_id, skip_special_tokens=True, clean_up_tokenization_spaces =True)
                  for gen_id in generated_ids]
        
        output = " ".join(preds) 
        return output