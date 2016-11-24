import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


limit_rows   = 800
df           = pd.read_csv("C:\Users\IBM_ADMIN\PycharmProjects\Python1\data",dtype={"PassengerID":int,
                                                    "Survived":bool,
                                                    "Pclass":int,
                                                    "Name":str,
                                                    "Sex":str,
                                                    "Age":int,
                                                    "SibSp":int,
                                                    "Parch":int,
                                                    "Ticket":str,
                                                    "Fare":float,
                                                    "Cabin":str,
                                                    "Embarked":str}, nrows=limit_rows)

unique_ids   = pd.Series(df['ncodpers'].unique())
limit_people = 1.2e4
unique_id    = unique_ids.sample(n=limit_people)
df           = df[df.ncodpers.isin(unique_id)]
df.describe()