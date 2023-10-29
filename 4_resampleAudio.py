import torchaudio
import os

resample_rate = 16000

## Read contents in this directory , and resample the audios
dir = "/home/prabhjot/Downloads/seamless/audio_5"

count = 0
for file in os.listdir(dir):
    filename = os.fsencode(file)
    filename = filename.decode()

    if filename.endswith(".wav"):
        waveform, sample_rate = torchaudio.load(os.path.join(dir,filename)) 
        resampler = torchaudio.transforms.Resample(sample_rate, resample_rate, dtype=waveform.dtype)
        resampled_waveform = resampler(waveform)
        torchaudio.save((os.path.join(dir,filename)) , resampled_waveform, resample_rate)

        count = count+1
        
print("Total files resampled are: ", count)