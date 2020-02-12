#!/usr/bin/env python
#_*_encoding:utf-8 _*_
import pymongo

conn = pymongo.MongoClient('127.0.0.1',27017)
db = conn.test
collection = db.spid
collection.insert({'name':"shengzhaoku",'xingbie':'man'})
print('=====插入完成，显示如下====')
doc = collection.find()
# for d in doc.keys():
#     print('key:%s-->value:' % (d.get(d)))
# print(doc)