import requests
import json
import os
from speech import speak, speakLimited

def get_wikiextract(searchparam):
    formatstring = "https://en.wikipedia.org/api/rest_v1/page/summary/"
    queryurl = formatstring + searchparam.replace(" ", "_")
    response = requests.get(queryurl)
    respjson = response.json()
    if (response.status_code == 200):
        print("Query Result Found.")
        print(respjson["extract"])
        return respjson["extract"]
    else:
        print("Sorry. Query Not Found on Wikipedia.")
        return "Sorry. Query Not Found on Wikipedia."

query = input("Enter Query: ")

speakLimited(get_wikiextract(query))