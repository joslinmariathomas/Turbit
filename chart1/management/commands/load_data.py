
import pymongo
import pandas as pd

from django.conf import settings
from django.core.management.base import BaseCommand
from chart1.models import Turbit
import pandas as pd

class Command(BaseCommand):
    help = 'Load data from Turbit file'

    def handle(self, *args, **kwargs):
        
        client=pymongo.MongoClient("mongodb://username:password@localhost:27017")
        
        db=client["Turbine"]
        t1_db=db["Turbine1"]
       
        Wind_Rotor=t1_db.find({},{'Dat/Zeit':1, 'Wind': 1, 'Leistung': 1, '_id': 0})
        
        for row in Wind_Rotor:
            #convert ISO date  to date 
            dt=dt=row['Dat/Zeit'].date()
            Turbit.objects.get_or_create(dt=dt,wind=row['Wind'],power=row['Leistung'])
        
            