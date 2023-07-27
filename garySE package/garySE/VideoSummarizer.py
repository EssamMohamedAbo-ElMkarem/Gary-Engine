import os
import torch
import pyttsx3
from moviepy.editor import *
import speech_recognition as sr
from Gary.garySE.cfg import config
from transformers import AutoTokenizer, T5ForConditionalGeneration, T5Config


class VideoSummarizer(config):
    def __init__(self, video_path: str):
        self.video_path = video_path


    def summarize(self):

        r = sr.Recognizer()
        sound = AudioFileClip(self.video_path)
        sound.write_audiofile(os.path.join(config.output_dir, "tmp_audio.wav"))
        with sr.AudioFile(os.path.join(config.output_dir, "tmp_audio.wav")) as source:
            audio = r.record(source)
        
        print("Recognizing the speech ...\n\n")
        txt = r.recognize_google(audio)
        
        
        model = T5ForConditionalGeneration.from_pretrained(os.path.join(config.main_dir, 'models/t5smallmodel'))
        tokenizer = AutoTokenizer.from_pretrained(os.path.join(config.main_dir, 'models/t5small'))
        device = torch.device('cpu')
        preprocess_text = txt.strip().replace("\n","")
        t5_prepared_Text = "summarize: "+preprocess_text
        print ("original text preprocessed: \n", preprocess_text)

        tokenized_text = tokenizer.encode(t5_prepared_Text, return_tensors="pt").to(device)


        # summmarize 
        summary_ids = model.generate(tokenized_text,
                                            num_beams=4,
                                            no_repeat_ngram_size=2,
                                            min_length=30,
                                            max_length=100,
                                            early_stopping=True)

        output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        print ("\n\nSummarized text: \n",output)
        c = input('Do you want to Gary  to speak the answer? (y/n)')
        if c == 'y':
            engine = pyttsx3.init()
            engine.say(output)
            engine.runAndWait()
        else:
            print("Gary is always happy to help...")
        input('press any key to exit...')