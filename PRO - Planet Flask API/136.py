from turtle import distance
import pandas as pd

df = pd.read_csv("archive_dataset_new.csv")
name = df["Star_name"].to_list()
mass = df["Mass"].to_list()
radius = df["Radius"].to_list()
distance = df["Distance"].to_list()


final_list = []

dict ={}
for i in range(0,len(name)):
    dict["name"]=name[i]
    dict["mass"]=mass[i]
    dict["radius"]=radius[i]
    dict["distance"]=distance[i]
    final_list.append(dict)
    dict ={}
print(final_list)



