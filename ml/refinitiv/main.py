import json
import refinitiv.data as rd

with open('refinitiv-data.config.json') as f:
    config = json.load(f)

rd_api_key = config['sessions']['platform']['rdp']['app-key']
rd_username = config['sessions']['platform']['rdp']['username']
rd_password = config['sessions']['platform']['rdp']['password']

print(rd_api_key)