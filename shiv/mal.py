# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 11:14:25 2022

@author: SPTINT-06
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv("C:/Users/SPTINT-06/Desktop/train.csv")
#g=sns.countplot(x='Sex',hue='Survived',data=data)
#g=sns.countplot(x='Embarked',hue='Survived',data=data)
#g=sns.countplot(x='Embarked',hue='Pclass',data=data)
#g=sns.countplot(x='Pclass',hue='Survived',data=data)
#add family size column
def add_family(df):
    df['FamilySize']=df['SibSp'] + df['Parch'] + 1
    return  df
data=add_family(data)
print(data.head(10))
#g=sns.countplot(x='FamilySize',hue='Survived',data=data)
#g=sns.catplot(x="Embarked",hue="Sex",col="Survived",data=data,kind="count",height=4,aspect=.7)
#g=sns.catplot(x="Pclass",hue="Sex",col="Survived",data=data,kind="count",height=4,aspect=.7)
#add familysize column
def add_family(df):
    df['FamilySize']=df['SibSp'] + df['Parch'] + 1
    return df
data=add_family(data)
print(data.head(10))
#g=sns.catplot(x="FamilySize",hue="Survived",col="Sex",data=data,kind="count",height=4,aspect=.7);
#g=sns.displot(x="Fare",hue="Sex",col="Survived",data=data,kind='hist',height=4,aspect=.7)
#g=sns.displot(x="Embarked",hue="Sex",col="Survived",data=data,kind="hist",height=4,aspect=.7)
