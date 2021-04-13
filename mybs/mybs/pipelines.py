# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import os

class MybsPipeline:
    def save_file(self,path, item):
        # 先将字典对象转化为可写入文本的字符串
        item = json.dumps(str(item), ensure_ascii=False)
        try:
            if not os.path.exists(path):
                with open(path, "w", encoding='utf-8') as f:
                    f.write(item + ",\n")
            else:
                with open(path, "a", encoding='utf-8') as f:
                    f.write(item + ",\n")
        except Exception as e:
            print("write error==>", e)

    def process_item(self, item, spider):
        path = "test1.json"
        self.save_file(path, item)
        return item
