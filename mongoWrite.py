import pymongo

class writeMongodbPipeline(object):

    def __init__(self):
        # 初始化mongo连接
        conn = pymongo.MongoClient('127.0.0.1',27017)
        #选择要连接的数据库
        db = conn['appinfo']
        #选择数据存放集合，或者称为表
        self.collection = db['appinfo']
    def process_item(self,item,spider):
        postItem = dict(item)
        self.collection.insert(postItem) #将数据插入数据库
        print('=============数据插入成功=============')
        return item  #可以省略不写
