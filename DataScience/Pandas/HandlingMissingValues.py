# coding: utf-8
import pandas as pd
import numpy as np
#handling missing values
a = np.random.randint(1,10,(3,4))
df = pd.DataFrame(a)
df
df.columns = list ('abcd')
df.iloc[0,0]
df.iloc[0,0] = np.nan
df
df.iloc[2,3] = np.nan
df.iloc[2,0] = np.nan
df
#detecting null values
np.isnull(df)
pd.isnull(df)
pd.notnull(df)
#dropping null values
#by default:
pd.dropna(df)
df.dropna()
#by default, drops the rows with null values
#parameters of the dropna() method of dataframe
#axis-"rows" or "columns"
#thresh - minimum no. of non-null values in the axis
#how - "all" or "any" ; checking whether all or any of the null values must be there in a axis to drop it
#by default, dropna(axis = 'rows', how = 'any'
df.dropna(thresh = 3)
df.dropna(how = 'all')
df.dropna(how = 'any')
df.dropna(how = 'any', axis = 'columns')
df.dropna(how = 'any', axis = 1)
#FILLING NULL VALUES
#manually:
#using isnull():
df[pd.notnull(df)] = 2
df
df
df = pd.DataFrame(a)
df[pd.isnull(df)] = "filled"
df
df
a
df.iloc[0,0]
df.iloc[0,0] = np.nan
df.iloc[2,3] = np.nan
df.iloc[2,0] = np.nan
df
df[pd.isnull(df)] = "filled val"
df
df[True if i == 'filled val' else False for i in df] = np.nan
df[(True if i == 'filled val' else False) for i in df] = np.nan
df == 'filled val'
df[df == 'filled val'] = np.nan
df
#FILLING NULL VALUES USING FILLNA()
df[pd.isnull(df)] = "filled val"
df.dtype
df.dtypes
#each columns in a DataFrame have their own dtype
#using fillna() method
df.fillna(-99)
df[df == 'filled val'] = np.nan
df.fillna(-99)
df[df == -99] = np.nan
#the method attribute:
df.fillna(method = 'ffill',axis = 0)
df.fillna(method = 'bfill')
get_ipython().run_line_magic('save', '')
