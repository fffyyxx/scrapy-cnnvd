# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql


# 导入json本地
class IcnnvdPipeline(object):
    def __init__(self):
        self.w = open("icnvvd_position.json", "wb")

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        content = content.encode('utf-8')
        self.w.write(content)
        return item

    def close_spider(self,spider):
        self.w.close()


# 导入icnvvd数据库
class Icnnvd_Pipeline(object):

    def __init__(self):
        self.db = pymysql.connect(
            # host='192.168.5.12',
            host='127.0.0.1',
            user='root',
            # passwd='vm123',
            passwd='root',
            db='new_semf',
            port=3306,
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor)

    def process_item(self, item, spider):
        cursor = self.db.cursor()
        cursor.execute("insert into loophole_vuln(url,CNNVD,title,CVE,grade,loophole_type,threat_type,release_time,update_time,loophole_info,loophole_bulletin,reference_website)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (''.join(item['url']), ''.join(item['CNNVD']), ''.join(item['title']), ''.join(item['CVE']), ''.join(item['grade']), ''.join(item['loophole_type']), ''.join(item['threat_type']), ''.join(item['release_time']), ''.join(item['update_time']), ''.join(item['loophole_info']), ''.join(item['loophole_bulletin']), ''.join(item['reference_website'])))
        self.db.commit()
        return item


# # 和Mysql建立链接
# db = pymysql.connect(host='192.168.5.12',user='root',passwd='vm123',port=3306)
# cursor = db.cursor()
# cursor.execute("SELECT VERSION()")
# data = cursor.fetchone()  # fetchone获取单条数据
# print('database version:', data)

# cursor.execute('show databases')
# cursor.execute('use icnvvd')
# cursor.execute('show tables')
# list_mysql = cursor.fetchone()
# print(list_mysql)
# list_mysql = cursor.fetchall()
# print(list_mysql)

# item=dict(item)
# table = 'loophole'
# sql = 'INSERT INTO loophole(name,url,title,CVE,release_time,update_time,loophole_info)values(%s,%s,%s,%s,%s,%s,%s)'
# cursor.execute(sql,( item['name'],item['url'],item['title'],item['CVE'],item['release_time'] ,item['update_time'],item['loophole_info']))
# db.commit()
# db.close()
