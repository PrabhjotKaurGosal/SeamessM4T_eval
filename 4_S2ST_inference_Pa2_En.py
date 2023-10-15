import torch
import torchaudio
from seamless_communication.models.inference import Translator

import pandas as pd

# Create empty dataframe to store the results ['English_translated_audio_filename', 'English_translated_text]

# Initialize a Translator object with a multitask model, vocoder on the GPU.
translator = Translator("seamlessM4T_large", "vocoder_36langs", torch.device("cuda:1"), torch.float16)

#Prediction
translated_text, translated_audio, sr = translator.predict("/home/prabhjot/Downloads/seamless/test_IndicSUPERB.wav", "s2st", "eng")
#print("The translated text is: ", translated_text)

# Save the translated audio generation.
torchaudio.save("/home/prabhjot/Downloads/seamless/S2ST_output_En/test_out4.mp3", translated_audio[0].cpu() ,sample_rate=sr)

#Update the dataframe with the results

#Get only the filename

#Put evrything in a loop to cover all the files in a directory




