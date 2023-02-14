import datetime

from pympler import asizeof


class Node(object):
    def __init__(self, key, val, segment, time):
        self.key = key
        self.val = val
        self.segment = segment
        self.time = time
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self):
        self.head = None
        self.tail = None
        self.nodeDict = {}
        self.timeStore = {}

    """
        --> Adds the object as the head of the linkedlist 
        --> Also adds the key, reference of the node as key value pair to the nodeDict
        --> If time-to-live is set key along with the time is stored in time store as key value pair for eviction
    """

    def add(self, segment, key, value, time=None):
        new = Node(key, value, segment, time)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new
        if segment not in self.nodeDict:
            self.nodeDict[segment] = {key: new}
        else:
            self.nodeDict[segment] = {**self.nodeDict[segment], key: new}
        if time is not None:
            if segment not in self.timeStore:
                self.timeStore[segment] = {key: time}
            else:
                self.timeStore[segment] = {**self.timeStore[segment], key: time}

    """
        --> get(key, segment) returns the object if the object is present else returns None
    """

    def get(self, key, segment):
        if segment in self.nodeDict:
            seg = self.nodeDict.get(segment)
            if key in seg:
                node = seg.get(key)
                if self.tail is self.head:
                    return node.val
                try:
                    if self.tail is node:
                        self.tail = self.tail.prev
                        self.tail.next.prev = None
                        self.tail.next = None
                    elif self.head is node:
                        return node.val
                    else:
                        node.prev.next = node.next
                        node.next.prev = node.prev
                        node.next = self.head
                        self.head.prev = node
                        self.head = node
                except Exception as e:
                    print(e)
                return node.val
            else:
                return
        else:
            return

    """
        --> eviction is done from the tail of the DLL until the specified 
            space (space after configured percentage of storage is cleared)
        --> Nodes which have time-to-live are not evicted                 
    """

    def evict(self, store, storage, AverageSpaceAfterAll):
        name_ = []
        segment_ = []
        boo = False
        curr = self.tail
        while store >= AverageSpaceAfterAll:
            segment = self.tail.segment
            key = self.tail.key
            temp = self.nodeDict[segment]
            if curr.time is not None:
                print("in time node")
                if curr is self.head:
                    break
                curr = curr.prev
                if curr.time is None:
                    size = round(asizeof.asizeof(temp.get(key).val) * 0.000001)
                    if curr is self.head:
                        curr.next.prev = None
                        self.head = curr.next
                        curr.next = None
                        key = curr.key
                        temp.pop(key)
                        curr = self.head
                    else:
                        curr.prev.next = curr.next
                        curr.next.prev = curr.prev
                        curr.next = None
                        curr.prev = None
                        key = curr.key
                        temp.pop(key)
                    if temp is not None:
                        self.nodeDict[segment] = temp
                        name_.append(key)
                        segment_.append(segment)
                        store -= size
                        storage -= size
                        boo = True
                    else:
                        del self.nodeDict[segment]
                        name_.append(key)
                        segment_.append(segment)
                        store -= round(asizeof.asizeof(curr.val) * 0.000001)
                        storage -= storage
                        boo = True
            else:
                print("in no time node")
                size = round(asizeof.asizeof(temp.get(key).val) * 0.000001)
                temp.pop(key)
                if temp is not None:
                    self.nodeDict[segment] = temp
                else:
                    del self.nodeDict[segment]
                if self.head is self.tail:
                    self.head = None
                    self.tail = None
                elif curr is self.tail:
                    self.tail = self.tail.prev
                    self.tail.next.prev = None
                    self.tail.next = None
                elif curr is self.head:
                    self.head.next = None
                    self.head = curr.next
                    self.head.prev = None
                else:
                    curr.next.prev = curr.prev
                    curr.prev.next = curr.next
                    curr.prev = None
                    curr.next = None
                name_.append(key)
                segment_.append(segment)
                store -= size
                storage -= size
                boo = True
        return name_, segment_, store, storage, boo

    """
        --> removeModel(key, segment) removes the particular object from cache
    """

    def removeModel(self, key, segment):
        if segment in self.nodeDict:
            seg = self.nodeDict.get(segment)
            if key in seg:
                node = seg.get(key)
                if self.tail is self.head:
                    self.head = None
                    self.tail = None
                elif self.tail is node:
                    self.tail = node.prev
                    self.tail.next.prev = None
                    self.tail.next = None
                elif self.head is node:
                    self.head = self.head.next
                    self.head.prev.next = None
                    self.head.prev = None
                else:
                    node.next.prev = node.prev
                    node.prev.next = node.next
                    node.next = None
                    node.prev = None
                    del seg[key]
                    self.nodeDict[segment] = seg
                return round(asizeof.asizeof(node.val) * 0.000001)
            return -1
        return -1

    def evictTimeExceededModels(self, segment):
        name_ = []
        segment_ = []
        size = 0
        if segment in self.timeStore:
            temp = list(self.timeStore[segment].keys())
            currentTime = datetime.datetime.now()
            dic = self.timeStore[segment]
            for key in temp:
                if dic[key] <= currentTime:
                    name_.append(key)
                    segment_.append(segment)
                    objects = self.nodeDict[segment]
                    size += round(asizeof.asizeof(objects.get(key).val) * 0.000001)
                    objects.pop(key)
                    dic.pop(key)
                    if dic is not None:
                        self.timeStore[segment] = dic
                    else:
                        del self.timeStore[segment]
                    if objects is not None:
                        self.nodeDict[segment] = objects
                    else:
                        del self.nodeDict[segment]
        return name_, segment_, size
