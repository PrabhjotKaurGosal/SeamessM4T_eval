import pandas as pd 
  
# read text file into pandas DataFrame 
df = pd.read_csv("/home/prabhjot/Desktop/seamless/Punjabi/audio_2_transcript_mapping_Pa_train_original.txt", sep='\t', header=None) 

# display DataFrame 
print(df) 

# Save pandas dataframe
df.to_pickle("/home/prabhjot/Desktop/seamless/Punjabi/audio_2_transcript_mapping_Pa_train_original.pkl")