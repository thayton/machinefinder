#!/usr/bin/env python

import time
import json
import requests

class Scraper(object):
    def __init__(self):
        self.url = 'http://www.machinefinder.com/ww/en-US/mfinder/results'

        self.params = {
            'mw': 't',
            'lang_code': 'en-US'
        }

        self.payload = {
            "context": {
                "kind": "mf",
                "region": "na",
                "search_kind": "tractors"
            },
            "locked_criteria": {
                "pw_min": 200
            },
            "criteria": {
                "pw_min":200
            },
            'show_more_start': 0
        }

    def scrape(self):
        while True:
            r = requests.post(
                    url=self.url,
                    params=self.params,
                    data=json.dumps(self.payload),
                    headers={
                        'Content-Type': 'application/json;charset=UTF-8',
                    }
                )

            j = r.json()
            machines = j['results']['machines']

            for m in machines:
                print json.dumps(m, indent=2)

            if len(machines) < 25:
                break

            self.payload['show_more_start'] += len(machines)
            print self.payload['show_more_start']
            time.sleep(1)

if __name__ == '__main__':
    scraper = Scraper()
    scraper.scrape()
