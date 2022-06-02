import datetime

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import pandas as pd
import re
import time
import os
import glob
df = pd.DataFrame()
df_1 = pd.read_csv('../result02.csv')
df_2 = pd.read_csv('../Munpia_crawling_data_final_of_final.csv')
df_3 = pd.read_csv('../Moonpia_crawling_data_series_final_revise.csv')

df = pd.concat([df, df_1], ignore_index=True)
df = pd.concat([df, df_2], ignore_index=True)
df = pd.concat([df, df_2], ignore_index=True)
df.reset_index(inplace=True, drop=True)

df.to_csv('./Munpia_crawling_data_finals.csv', index=False)
