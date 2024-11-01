import json
import requests
import time

url = 'https://services.nvd.nist.gov/rest/json/cves/2.0?cveId='
api_key = '<REDACTED>'
headers = {'apiKey': '0da88756-8091-4af7-97a5-2fd1c4cda8aa'}
headers1 = {'cveId': 'CVE-2019-1010218'}

with open('input.txt', 'r') as input_file:

    for line in input_file:
        time.sleep(.5)
        line = line.strip()
        full_url = url + line
        print(full_url)
        try:
            r = requests.get(full_url).json()
            print (line + " " + r["vulnerabilities"][0]["cve"]["metrics"]["cvssMetricV31"][0]["cvssData"]["baseSeverity"])
        except Exception as error:
            print (error)
