import requests
import json
import pymongo
import asyncio
import time


def query_ocds(ocds):
    url = "https://datosabiertos.compraspublicas.gob.ec/PLATAFORMA/api/record?ocid="
    response = requests.get(url + ocds)
    if response.status_code == 200:
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["compraspublicas"]
        mycol = mydb["proceso_ocds"]

        proceso_ocds = response.json()
        proceso_ocds['_id'] = ocds
        filter = {'_id': proceso_ocds['_id']}
        mycol.update_one(filter, {"$set": proceso_ocds}, upsert=True)
        time.sleep(3)
    else:
        print(">>>>>>>>>>> "+str(response.status_code))


def ocds_details():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["compraspublicas"]
    mycol = mydb["procesos"]

    rows = mycol.find({}, 'ocid')

    i = 1
    for row in rows:
        print(str(i) + " " + row['_id'])
        #asyncio.run(query_ocds(row['_id']))
        query_ocds(row['_id'])
        i = i + 1


if __name__ == '__main__':
    ocds_details()
