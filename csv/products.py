import pandas as pd
link = pd.read_csv("https://raw.githubusercontent.com/sh4rkd/scale/master/csv/productos.csv")
f = open("C:/Users/lilol/Desktop/scale/reports/csv/productos.txt","w")
for i in link["Link"]:
  try:
    if(i.find("/product")>0):
      f.write(i+"\n")
  except:
    continue
f.close()