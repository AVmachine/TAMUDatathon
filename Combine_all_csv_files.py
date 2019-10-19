import os
import pandas as pd
import glob

folder_path = '/ml_preds_csv'
dataframes_combination = []
for file in glob.glob(os.getcwd() + folder_path + '/*.csv'):
    new_dataframe = pd.read_csv(file)
    dataframes_combination.append(new_dataframe)

total_dataframe = pd.concat(dataframes_combination, ignore_index=True)
total_dataframe.to_csv('Master_ML_Preds_CSV.csv')
