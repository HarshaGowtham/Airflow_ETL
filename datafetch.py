import requests
import json
import datetime as dt
import pandas as pd
import numpy as np
import os
import pdb

response = requests.get("https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/")  #get request to the API endpoint and retrieve the data
# pdb.set_trace()

data = response.json() #Extract the relevant data from the API response based on the API's response structure and parse it to python dictionary


date = dt.datetime.now()
date_string = str(date.date())

FILE_PATH="C:/Users/harsh/Desktop/work_space/My_projects/Airflow/test.json"


with open(FILE_PATH, "w") as outfile:

    outfile.write(json.dumps(data))


print(date_string)

