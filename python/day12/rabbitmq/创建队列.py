#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Liang Lian
# Python 3.5

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', type='direct')


# 随机创建队列
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
print(queue_name)


# 绑定
# serverities = ['error', 'info', 'warning']
# for serverity in serverities:
serverity = 'error'
channel.queue_bind(exchange='logs_fanout', queue=queue_name, routing_key=serverity)

print('[*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print('[x] %r' % body)

channel.basic_consume(callback, queue=queue_name, no_ack=True)

channel.start_consuming()
