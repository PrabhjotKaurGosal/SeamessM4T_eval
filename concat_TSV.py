import pandas as pd 
import os
  
# read tsv file into pandas DataFrame 
df_1 = pd.read_csv('/home/prabhjot/Desktop/S2ST/IndicSUPERB/train_001.tsv', sep='\t', skiprows=1, header = None)
df_1.reset_index(drop=True,inplace=True)

df_2 = pd.read_csv('/home/prabhjot/Desktop/S2ST/IndicSUPERB/train_002.tsv', sep='\t', skiprows=1, header = None)
df_2.reset_index(drop=True,inplace=True)


df = pd.concat([df_1, df_2], axis=0)
df.reset_index(drop=True,inplace=True)

new_path = '/media/mist1/Downloads/prabhjot/S2ST/TGT_AUDIO/train'
mapping = {df.columns[0]: new_path}
df_with_header = df.rename(columns=mapping)
# display DataFrame 
print(df_1)
print(df_2)
print(df_with_header)

df_with_header.to_csv(os.path.join('/home/prabhjot/Desktop/S2ST/IndicSUPERB','train.tsv'), sep="\t", index=False)
