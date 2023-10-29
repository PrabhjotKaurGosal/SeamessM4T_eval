import pandas as pd 
  
# read text file into pandas DataFrame 
df = pd.read_pickle('/media/prabhjot/My Passport/Research/SUBERB_Indic_S2ST_Pa_En/English/audio_2_transcript_mapping_En_train_original_4.pkl') 

# display DataFrame 
print(df) 

# Save as text file
with open('/media/prabhjot/My Passport/Research/SUBERB_Indic_S2ST_Pa_En/English/audio_2_transcript_mapping_En_train_original_4.txt', 'a') as f:
    df_string = df.to_string(header=False, index=False)
    f.write(df_string)

