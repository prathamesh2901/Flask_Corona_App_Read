#!/usr/local/bin/python3
from rejson import Client, Path


class StateCache():


    def __init__(self, name):
        self.name = name

    def find_by_state(self):
        try:
            rj = Client(
                host='redis',
                port=6379,
                decode_responses=True)
            return rj.jsonget(self.name)
        except:
            return None


    def cache(self, obj):
        rj = Client(
            host='redis',
            port=6379,
            decode_responses=True)
        rj.jsonset(self.name, Path.rootPath(), obj)
