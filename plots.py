
import pandas as pd
import pymongo
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


client=pymongo.MongoClient("mongodb://username:password@localhost:27017")
db=client["Turbine"]



#Turbine1 WInd Rotor data
Wind_Power_t1=db["Turbine1"].find({},{'Wind': 1, 'Leistung': 1, '_id': 0})
Wind_Power_t1_df=pd.DataFrame(list(Wind_Power_t1))
#Turbine2 WInd Rotor data
Wind_Power_t2=db["Turbine2"].find({},{'Wind': 1, 'Leistung': 1, '_id': 0})
Wind_Power_t2_df=pd.DataFrame(list(Wind_Power_t2))

#Combined WInd Rotor data
Wind_Power_combined=db["combined"].find({},{'Wind': 1, 'Leistung': 1, '_id': 0})
Wind_Power_combined_df=pd.DataFrame(list(Wind_Power_combined))

gs = gridspec.GridSpec(2, 2)
fig = plt.figure()
ax1=fig.add_subplot(gs[0, 0])
ax2= fig.add_subplot(gs[0, 1])
ax3=fig.add_subplot(gs[1, :])

ax1.scatter(Wind_Power_t1_df['Wind'] , Wind_Power_t1_df['Leistung'] , c ="blue")
ax2.scatter(Wind_Power_t2_df['Wind'] , Wind_Power_t2_df['Leistung'] , c ="red")
ax3.scatter(Wind_Power_combined_df['Wind'] , Wind_Power_combined_df['Leistung'] , c ="green")
plt.xlabel("Wind speed (m/s)")
plt.ylabel("Power (kW)")
 
plt.show()
