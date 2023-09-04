# -*- coding: utf-8 -*-

"""
@author: jayzhen
@license: Apache Licence 
@version: Python 3.8+
@file: rabbitmq_client.py
@time: 2023/9/4 19:25
pip install pika
"""

import pika

conn = pika.BlockingConnection(pika.ConnectionParameters("http://192.168.18.53:5672"))
channel = conn.channel()
channel.queue_declare(queue="testing")
channel.basic_publish(exchange="", routing_key="testing", body="hello jayzhen")
channel.close()