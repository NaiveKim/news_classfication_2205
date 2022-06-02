import pandas as pd

df_novels = pd.DataFrame()

df_novels.to_csv('./Munpia_crawling_data_final_revise.csv')

f = open('../Munpia_crawling_data_finals.csv', encoding='UTF8')
f2 = open('../Munpia_crawling_data_final_revise.csv', 'w', encoding='UTF8')

line = f.read().replace('선독점', '')
f2.write(line)

f.close()
f2.close()