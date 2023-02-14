# import xml.etree.ElementTree as ET
#
#
# def parseXML(path):
#     tree = ET.parse(path)
#     root = tree.getroot()
#     dict_ = dict()
#     for item in root:
#         dict_[item.get("name")] = {"limit": item.get("max_cache_size"),
#                                    "eviction_percentage": item.get("eviction_percentage"),
#                                    "max_object_size": item.get("max_obj_size")
#                                    }
#     print(dict_)
#
#
# if __name__ == "__main__":
#     parseXML("./config/config.xml")
import datetime

# import datetime
# st = "20:14:46"
# d = datetime.datetime.strptime(st, "%H:%M:%S").time()
# print(d, type(d))
# print(datetime.datetime.now().time().strftime("%H:%M:%S"))
# print((datetime.datetime.now()+datetime.timedelta(hours=8)).strftime("%H:%M:%S"), type(datetime.datetime.now().time()))

from datetime import datetime,timedelta

t = datetime.now()
dt = str(t)
new = datetime.strptime(dt, "%Y-%m-%d %H:%M:%S.%f")
newe = (datetime.now() + timedelta(hours=0.01)).strftime("%Y-%m-%d %H:%M:%S.%f")
print(dt, new)
print(newe)
print(t)