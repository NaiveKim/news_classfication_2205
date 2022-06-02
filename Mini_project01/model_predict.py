import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # CPU를 쓰도록 강제
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split    #scikit-learn 설치
from konlpy.tag import Okt
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical
import pickle
from tensorflow.keras.models import load_model
pd.set_option('display.unicode.east_asian_width',True )
df = pd.read_csv('../Munpia_/Munpia_Combin_final_final.csv')
# df = pd.read_csv('./Munpia_/Munpia_team_name.csv')
# print(df.head())
# df.info()

X = df['titles']
Y = df['genres']

encoder = LabelEncoder()
labeled_Y = encoder.fit_transform(Y)
# # print(labeled_Y)
label = encoder.classes_
# print(label)
with open('../models/encoder_Munpia.pickle', 'wb') as f:# wb 는 write binary
    pickle.dump(encoder, f)

onehot_Y = to_categorical(labeled_Y)
print(onehot_Y)

okt = Okt()

for i in range(len(X)):
    X[i] = okt.morphs(X[i], stem=True)

stopwords = pd.read_csv('../crawling_data/stopwords.csv', index_col=0)

for j in range(len(X)):
    words_X = []
    for i in range(len(X[j])):
        if len(X[j][i]) > 1:
            if X[j][i] not in list(stopwords['stopword']):
                words_X.append(X[j][i])
    X[j] = ' '.join(words_X)

#
# print(X[:5])
print(words_X)
print(Y[:5])



token = Tokenizer()
token.fit_on_texts(X)
tokened_X = token.texts_to_sequences(X)
wordsize = len(token.word_index) + 1


# with open('./models/encoder_Munpia.pickle', 'wb') as f:
#     pickle.dump(token, f)

max = 0
for i in range(len(tokened_X)):
    if max < len(tokened_X[i]):
        max = len(tokened_X[i])
print(max)

X_pad = pad_sequences(tokened_X, max)
print(X_pad)

model = load_model('../models/Munpia_model_0.9324960708618164.h5')
preds = model.predict(X_pad)
predicts = []
for pred in preds:
    most = label[np.argmax(pred)]
    pred[np.argmax(pred)] = 0
    second = label[np.argmax(pred)]
    predicts.append([most, second])
df['predict'] = predicts


print(df.head(30))
# hdf5 에러 발생 시 찾아가서 지우면 된다.

df['OX'] = 0
for i in range(len(df)):
    if df.loc[i, 'genres'] in df.loc[i, 'predict']:
        df.loc[i, 'OX'] = '0'
    else:
        df.loc[i, 'OX'] = 'X'
print(df.head(30))


for i in range(len(df)):
    if df['genres'][i] != df['predict'][i]:
        print(df.iloc[i])
print(df['OX'].value_counts())
print(df['OX'].value_counts()/len(df))
