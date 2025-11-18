# coding: utf-8
from pandas import DataFrame,Series
sr=Series([2,20,10,3],index=[3,7,5,6])
sr[3]
#while slicing, this uses normal list slicing that are indexed normally 0 to len(sr)
sr[3:5]
#to avoid this we are gonna use the special indexer called loc which is an attribute of the series object
sr.loc[3:5]
