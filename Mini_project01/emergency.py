import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split # scikit-learn 설치
from konlpy.tag import Okt
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical
import pickle
import os

df = pd.read_csv('../Munpia_/Munpia_team_name.csv')
df_revise = pd.DataFrame()

for i in range(1, 6369):
    df['genres'][i] = df['genres'][i].split()[0]
for i in range(1, 6369):
    df['titles'][i] = df['titles'][i]+df['intros'][i]

df.drop('intros', axis = 1, inplace = True)

df.to_csv('./Munpia_/Munpia_Combin_final_final.csv', index=False)
#
# df = pd.read_csv('Munpia_/Munpia_team_name.csv')
#
# df.info()
