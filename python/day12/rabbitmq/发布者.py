#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Liang Lian
# Python 3.5

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))

channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', type='direct')

serverity = 'error'
message = '456'
channel.basic_publish(exchange='direct_logs', routing_key=serverity, body=message)

print('[x] Sent %r' % message)
connection.close()