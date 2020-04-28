#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
 
headers={'accept': 'application/json', 'content-type': 'application/json'}

response = json.loads(requests.get('https://raw.githubusercontent.com/kaz-ogiwara/covid19/master/data/data.json', headers=headers).text)
 
print(json.dumps(response))
