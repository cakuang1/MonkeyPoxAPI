import asyncio
import json
import requests
import pprint




res = requests.get('https://www.cdc.gov/poxvirus/monkeypox/response/modules/MX-response-case-count-US.json?v=2022-08-01T05%3A00%3A00.000Z')




parsed = json.loads(res.text)
data = parsed['data']
def numcases(state):
    try:

        
    except ValueError:
        print(state + "is not a valid argument")




def totalcasestoday():

    for i in in 










