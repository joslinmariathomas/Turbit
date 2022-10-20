
import pandas as pd
import pymongo
import os


client=pymongo.MongoClient("mongodb://username:password@localhost:27017")
db=client["Turbine"]

#printing database names
dbs=client.list_database_names()

#function to load data to database
def load_csv(fname,doc_name,rewrite):
    data_path=os.path.join("data",fname+".csv")
    data=pd.read_csv(data_path,sep=";")
    
    data.columns = data.columns.str.strip()
    data=data.drop(axis=0,index=0)
    
    data["Dat/Zeit"] = pd.to_datetime(data["Dat/Zeit"])
    data['Wind'] = data['Wind'].str.replace(',', '.').astype(float)
    data['Leistung'] = data['Leistung'].str.replace(',', '.').astype(float)
    
    doc=db[doc_name]
    
    #converting data structure to mongodb json
    data1=data.to_dict(orient="records")
    
    #check if collection exists
    if rewrite=="Y":
        x = doc.delete_many({})
    x = doc.insert_many(data1)
    
    
#loading data to mongodb    
load_csv("Turbine1","Turbine1","Y")     
load_csv("Turbine2","Turbine2","Y")
load_csv("Turbine1","combined","Y")
load_csv("Turbine2","combined","N")
