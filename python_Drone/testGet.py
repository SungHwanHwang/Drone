# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 13:22:44 2019

@author: h5435
"""

import requests

URL ='http://localhost:8000/api/flysaying'
response = requests.get(URL)
response.status_code
response.text