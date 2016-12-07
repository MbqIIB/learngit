#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Liang Lian
# Python 3.5

import redis

class RedisHelper:

    def __init__(self):
        self.__conn = redis.Redis(host='127.0.0.1')

    def publish(self, msg, chan):
        self.__conn.publish(chan, msg)
        return True

    def subscribe(self, chan):
        pub = self.__conn.pubsub()
        pub.subscribe(chan)
        pub.parse_response()
        return pub
