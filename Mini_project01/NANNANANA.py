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

df = pd.read_csv('../Munpia_data.csv')
df.rename(columns={'Column1':'titles', 'Column2':'intros', 'Column3':'genres'}, inplace=True)

df.to_csv('./Munpia_/Munpia_data_preprocessing.csv', index=False)
# df.replace(r'^\s*$',np.nan, regex=True)
#

