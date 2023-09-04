#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: v1.0
@author: jayzhen
@license: Apache Licence 
@software: PyCharm
@file: rabbitMQUtils
@time: 2018/3/1  11:12

pip install pika
"""

import pika

conn = pika.BlockingConnection(pika.ConnectionParameters("http://192.168.18.53:5672"))
channel = conn.channel()
channel.queue_declare(queue="testing")
channel.basic_publish(exchange="", routing_key="testing", body="hello jayzhen")
channel.close()