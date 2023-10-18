import torch
import torchaudio
from seamless_communication.models.inference import Translator

import pandas as pd
import os

## Initialize a Translator object with a multitask model, vocoder on the GPU.
translator = Translator("seamlessM4T_large", "vocoder_36langs", torch.device("cuda:1"), torch.float16)


## Create an empty list to store the results ['English_translated_audio_filename', 'English_translated_text]
AudioName_Transcript_list = []

## Read contents in this directory , translate it and, save the translated audio and the text
input_dir = "/home/prabhjot/Downloads/seamless/audio"
output_dir = "/home/prabhjot/Downloads/seamless/S2ST_output_En"
count = 0
for file in os.listdir(input_dir):
    filename = os.fsencode(file)
    filename = filename.decode()
    if filename.endswith(".wav"):
        source_audio_path = (os.path.join(input_dir,filename)) 
        #print(source_audio_path)  
        count = count+1

        ## Prediction
        translated_text, translated_audio, sr = translator.predict(source_audio_path, "s2st", "eng")
        translated_text = str(translated_text)
        #print("The translated text is: ", translated_text)
        
        ## Save the translated audio generation.
        translated_audio_path = (os.path.join(output_dir,filename)) 
        #print(translated_audio_path)
        torchaudio.save(translated_audio_path, translated_audio[0].cpu(), sample_rate=sr)

        ## Update the dataframe with the results
        row_list = [filename, translated_text]
        AudioName_Transcript_list.append(row_list)


## Convert list to dafaframe and add a header
en_Translated_audio_transcript_mapping_df =  pd.DataFrame(AudioName_Transcript_list, columns=['English_translated_audio_filename', 'English_translated_text'])
#print("The list is: ", AudioName_Transcript_list)
#print("The dataframe is: ", en_Translated_audio_transcript_mapping_df)

## Save the dataframe
en_Translated_audio_transcript_mapping_df.to_pickle('/home/prabhjot/Downloads/seamless/en_Translated_audio_transcript_mapping_df.pkl')

print("Total files translated are: ", count)




