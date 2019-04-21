#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 14:11:49 2019

@author: Azlan
"""


import http.client
import json
import time
import sys
import math
import csv
import pandas as pd
import numpy as np
'''
data_sf = pd.read_csv('SanFran_fixed.csv')
data_attr = pd.read_csv('FULL_attractions.tsv', sep='\t')

sf_id = sorted(data["id"].unique())   
data_filtered = pd.concat(data_attr[data_attr.id == sf_id[i]] for i in range(len(sf_id)))

data_filtered.to_csv("SF_attractions.csv",index=False)


data_attr = pd.read_csv("SF_attractions.csv")

with open('SF_attractions_simplified.csv', 'w', encoding='utf-8') as f:
    f.write('id,attractions_coordinates')

for i in range(len(data_attr)):
    attr = [pd.read_json(data_attr.attractions[i]).geometry[j]["coordinates"] for j in range(len(pd.read_json(data_attr.attractions[i])))]

    with open('SF_attractions_simplified.csv', 'a', encoding='utf-8') as f:
        f.write("\n%s,%s" % (json.dumps(str(data_attr.id[i])), json.dumps(str(attr))))
        
'''


'''
data_attr = pd.read_csv('SF_attractions.csv')
data = []
data_icon = []

for i in range(len(data_attr)):
    if (i%100==0):
        print(i)
    temp = pd.read_json(data_attr.attractions[i])
    for j in range(len(temp)):
        data.append([temp.properties[j]["name"],temp.properties[j]["category"],temp.geometry[j]["coordinates"],temp.properties[j]["openingHours"],])
        data_icon.append([temp.properties[j]["category"],temp.properties[j]["icon"]])
  
data_unique = pd.DataFrame(data).sort_values(by=[0]).drop_duplicates(subset = 0).reset_index(drop=True)
data_icon_unique = pd.DataFrame(data_icon).sort_values(by=[0]).drop_duplicates(subset = 0).reset_index(drop=True)

with open('attractions.tsv', 'w', encoding='utf-8') as f:
    f.write("id\tname\tcat\tcoordinates\thours\n")
    for i in range(len(data_unique)):
        f.write("%d\t%s\t%s\t%s\t%s\n" % (i,str(data_unique[0][i]),str(data_unique[1][i]),str(data_unique[2][i]),str(data_unique[3][i])))
          
    
with open('icons.tsv', 'w', encoding='utf-8') as f:
    f.write("id\tcat\turl\n")
    for i in range(len(data_icon_unique)):
        f.write("%d\t%s\t%s\n" % (i,str(data_icon_unique[0][i]),str(data_icon_unique[1][i])))


'''




'''
data_all = pd.read_csv('SF_attractions.csv')
data_attr = pd.read_csv('attractions.tsv', sep = "\t")
data_icon = pd.read_csv('icons.tsv', sep = "\t")
data = []
for i in range(len(data_all)):
    if (i%100==0):
        print(i)
    temp = pd.read_json(data_all.attractions[i])
    data.append([data_all.id[i],[[data_attr[data_attr.name==temp.properties[j]["name"]].id.values[0],temp.properties[j]["distance"]] for j in range(len(temp))]])



with open('SF_host_attr_simp.tsv', 'w', encoding='utf-8') as f:
    f.write("host_id\tattractions\n")
    for i in range(len(data)):
        f.write("%s\t%s\n" % (str(data[i][0]),str(data[i][1])))

'''

data_all = pd.read_csv('SF_host_attr_simp.tsv', sep = "\t")
data_attr = pd.read_csv('attractions.tsv', sep = "\t")
data_icon = pd.read_csv('icons.tsv', sep = "\t")

temp = pd.read_json(data_all.attractions[0])
print(data_all.host_id[0],[[data_attr[data_attr.id == temp[0][j]].name.values[0], data_attr[data_attr.id == temp[0][j]].coordinates.values[0],data_icon[data_icon.cat == data_attr[data_attr.id == temp[0][j]].cat.values[0]].url.values[0],temp[1][j]] for j in range(10)])


















