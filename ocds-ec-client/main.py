# This is a sample Python script.
import requests
import json
import pymongo
import asyncio


async def query_page(page, url):
    paged_url = url + "&page=" + str(page)
    response = requests.get(paged_url)

    if response.status_code == 200:
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["compraspublicas"]
        mycol = mydb["procesos"]

        for proceso in response.json()['data']:
            proceso['_id'] = proceso['ocid']
            filter = {'_id': proceso['_id']}
            mycol.update_one(filter, {"$set": proceso}, upsert=True)
    else:
        print(">>>>>>>>>>> "+str(response.status_code))


def consume_ocds(name):
    url = "https://datosabiertos.compraspublicas.gob.ec/PLATAFORMA/api/search_ocds?year=2022&buyer=GUAYAQUIL"
    response = requests.get(url+"&page=1")

    print(response.status_code)

    if response.status_code == 200:
        total_pages = response.json()['pages']

        for p in range(1, total_pages + 1):
            print(p)
            asyncio.run(query_page(p, url))


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    consume_ocds()
