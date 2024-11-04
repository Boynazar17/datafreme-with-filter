# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WBH3mjky5sSVj-AD59dKUv2h__r6M1DC
"""

import pandas as pd
baza={
    "FISH":["Nodirova Aziza","Azizov Bekzod","Alijonov  Valijon","Azizova Lola","Anvarov ALiyor","Anvarova Laziza","Botirov Azamat","Malikova Malika","Asadullayev Temur","Qilechev Donyor" ],
    "Yosh":["12","13","15","13","14","11","16","17","17","16" ],
    "Jinsi":["qiz bola","o'g'il bola","o'g'il bola","qiz bola","o'g'il bola","qiz bola","o'g'il bola","qiz bola","o'g'il bola","o'g'il bola",],
    "Maktab raqami":["12","21","24","31","12","21","24","31","22","11" ]
}
df=pd.DataFrame(baza)
print(df)
df.to_excel("baza.xlsx")

filtr=df.loc[df["Jinsi"]=="qiz bola"]
print(filtr)

filtr=df.loc[df["Jinsi"]=="o'g'il bola"]
print(filtr)

filtr=df.loc[df["Yosh"]<"15"]
print(filtr)

filtr=df.loc[df["Yosh"]<"15"]
filtr=df.loc[df["Jinsi"]=="qiz bola"]

print(filtr)

filtr=df.loc[(df["Yosh"]<"15")&(df["Jinsi"]=="qiz bola")]

print(filtr)

filtr=df.loc[(df["Yosh"]<"15")&(df["Jinsi"]=="o'g'il bola")]

print(filtr)

filtr=df.loc[(df["Yosh"]>"15")&(df["Jinsi"]=="qiz bola")]

print(filtr)

filtr=df.loc[(df["Yosh"]>"15")&(df["Jinsi"]=="o'g'il bola")]

print(filtr)

filtr=df["Yosh"].min()

print(filtr)

filtr=df["Yosh"].max()

print(filtr)

