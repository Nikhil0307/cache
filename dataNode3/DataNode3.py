from concurrent import futures
from datetime import datetime

import grpc
import psutil
import requests
from pympler import asizeof
import xml.etree.ElementTree as ET
from dataNode3 import LRU
from protos import cache_pb2, cache_pb2_grpc

flag = True
boo = False
IP = "12347"

perc = 0
maxSize = 0
store = 0
storage = 0
config = dict()


class DataNode3(cache_pb2_grpc.getModelFromDataNodeServicer, cache_pb2_grpc.updateMetaServicer,
                cache_pb2_grpc.extrasServicer):
    """
        returns model if cached or moves the call to putModel
    """

    def getModel(self, request, context):
        name = request.name
        segment = request.segment
        lru = config.get(segment).get(segment)
        model = lru.get(name, segment)
        response = cache_pb2.model(object=model)
        if response.object is bytes():
            return self.putModel(request, context)
        return response

    """
        --> get model from ZOS and cache
    """

    def putModel(self, request, context):
        try:
            global storage, flag, store, perc
            name = request.name
            segment = request.segment
            flag = True
            # # #
            lru = config.get(segment).get(segment)
            store = config.get(segment).get("store")
            limit = config.get(segment).get("limit")
            max_object_size = int(config.get(segment).get("max_object_size"))
            perc = int(config.get(segment).get("eviction_percentage"))
            # # #
            # get data from ZOS and place in given DN
            mod = requests.get('http://127.0.0.1:5000/getModel', params={'name': name, 'segment': segment})
            if mod.content is None:
                return cache_pb2.text(message="model not available")
            model = mod.content
            modelSize = round(asizeof.asizeof(model) * 0.000001)
            SegmentMaxSize = int(limit)
            if modelSize >= max_object_size:  # if model size is greater than the allowed size then it is not saved
                self.updateEvictedModel(name=name, segment=segment)
                return cache_pb2.model(object=model)
            self.store(modelSize, SegmentMaxSize, lru, segment, name, model)
            return cache_pb2.model(object=model)
        except Exception as e:
            print(e)

    """
        --> Caching objects without time to live
    """

    def putObject(self, request, context):
        global storage, flag, store, perc
        name = request.name
        segment = request.segment
        model = request.object
        flag = True
        # # #
        lru = config.get(segment).get(segment)
        store = config.get(segment).get("store")
        limit = config.get(segment).get("limit")
        max_object_size = int(config.get(segment).get("max_object_size"))
        perc = int(config.get(segment).get("eviction_percentage"))

        modelSize = round(asizeof.asizeof(model) * 0.000001)
        SegmentMaxSize = int(limit)
        if modelSize >= max_object_size:  # if model size is greater than the allowed size then it is not saved
            self.updateEvictedModel(name=name, segment=segment)
            return cache_pb2.model(object=model)

        self.store(modelSize, SegmentMaxSize, lru, segment, name, model)
        return cache_pb2.text(message="success")

    """
        --> Caching objects with time to live
    """

    def putObjectWithTime(self, request, context):
        global storage, flag, store, perc
        flag = True
        name = request.name
        segment = request.segment
        time = request.time
        model = request.object
        # # #
        lru = config.get(segment).get(segment)
        store = config.get(segment).get("store")
        limit = config.get(segment).get("limit")
        max_object_size = int(config.get(segment).get("max_object_size"))
        perc = int(config.get(segment).get("eviction_percentage"))
        # # #
        modelSize = round(asizeof.asizeof(model) * 0.000001)
        SegmentMaxSize = int(limit)
        if modelSize >= max_object_size:  # if model size is greater than the allowed size then it is not saved
            self.updateEvictedModel(name=name, segment=segment)
            return cache_pb2.text(message="couldn't cache as the model size is larger that the configured size")
        temp = store + modelSize
        if temp >= SegmentMaxSize:
            # cache eviction
            flag = self.evict(modelSize, lru, SegmentMaxSize)
            # call to master for updating the current storage size of the machine
        storage += modelSize
        store += modelSize
        if flag:
            config.get(segment)["store"] = store
            # adding to cache
            time = datetime.strptime(time, "%Y-%m-%d %H:%M:%S.%f")
            lru.add(segment, name, model, time)
        else:
            storage -= modelSize
            store -= modelSize
            config.get(segment)["store"] = store
            # update master about the evicted object
            self.updateEvictedModel(name=name, segment=segment)
        # updating master about the dataNode size
        with grpc.insecure_channel(
                'localhost:50051') as channel:  # this port need to change to masters running port
            stub = cache_pb2_grpc.updateMetaStub(channel)
            try:
                stub.updateDataNodeMeta(cache_pb2.DataNodeSize(size=str(storage), IP="localhost:" + IP))
            except Exception as e:
                print(e)
        return cache_pb2.text(message="successfully cached")

    """
        --> this method is called when the getModel() is called with a time 
        --> this gets the object from ZOS and caches the object for the given time
    """

    def putModelWithTime(self, request, context):
        global storage, flag, store, perc
        flag = True
        name = request.name
        segment = request.segment
        time = request.time
        mod = requests.get('http://127.0.0.1:5000/getModel', params={'name': name, 'segment': segment})
        model = mod.content
        # # #
        lru = config.get(segment).get(segment)
        store = config.get(segment).get("store")
        limit = config.get(segment).get("limit")
        max_object_size = int(config.get(segment).get("max_object_size"))
        perc = int(config.get(segment).get("eviction_percentage"))
        # # #
        modelSize = round(asizeof.asizeof(model) * 0.000001)
        SegmentMaxSize = int(limit)
        if modelSize >= max_object_size:  # if model size is greater than the allowed size then it is not saved
            self.updateEvictedModel(name=name, segment=segment)
            return cache_pb2.text(message="couldn't cache as the model size is larger that the configured size")
        temp = store + modelSize
        if temp >= SegmentMaxSize:
            # cache eviction
            flag = self.evict(modelSize, lru, SegmentMaxSize)
            # call to master for updating the current storage size of the machine
        storage += modelSize
        store += modelSize
        if flag:
            config.get(segment)["store"] = store
            # adding to cache
            time = datetime.strptime(time, "%Y-%m-%d %H:%M:%S.%f")
            lru.add(segment, name, model, time)
        else:
            storage -= modelSize
            store -= modelSize
            config.get(segment)["store"] = store
            # update master about the evicted object
            self.updateEvictedModel(name=name, segment=segment)
        # updating master about the dataNode size
        with grpc.insecure_channel(
                'localhost:50051') as channel:  # this port need to change to masters running port
            stub = cache_pb2_grpc.updateMetaStub(channel)
            try:
                stub.updateDataNodeMeta(cache_pb2.DataNodeSize(size=str(storage), IP="localhost:" + IP))
            except Exception as e:
                print(e)
        return cache_pb2.model(object=model)

    """
        --> Invalidate() gets key and evicts the object from cache
    """

    def inValidate(self, request, context):
        key = request.name
        segment = request.segment
        global storage
        lru = config.get(segment).get(segment)

        self.updateEvictedModel(key, segment)
        size = lru.removeModel(key, segment)
        storage = storage - int(size)
        size = int(size)
        config.get(segment)["store"] = store - size

        return cache_pb2.text(message="evicted")

    """
        --> evict() has the percentage to be evicted which is configured by the 
            user, this evicts objects in the doubly linked list from the tail.
    """

    def evict(self, modelSize, lru, SegmentMaxSize):
        with grpc.insecure_channel(
                'localhost:50051') as channel:  # this port need to change to masters running port
            stub = cache_pb2_grpc.updateMetaStub(channel)
            global boo, storage, store
            percentage = int((perc / 100) * store)
            spaceAvailableAfterEvic = percentage + (SegmentMaxSize - store)
            AverageSpaceAfterAll = SegmentMaxSize - spaceAvailableAfterEvic
            name_, segment_, store, storage, boo = lru.evict(store, storage, AverageSpaceAfterAll)
            stub.updateEvictedModelMeta(cache_pb2.modelMeta(name=name_, segment=segment_))
            if (store + modelSize) > SegmentMaxSize:
                boo = False
        return boo

    """
        --> Models after being evicted, a call to the master is made and master's
            meta get updated
    """

    def updateEvictedModel(self, name, segment):
        with grpc.insecure_channel(
                'localhost:50051') as channel:  # this port need to change to masters running port
            stub = cache_pb2_grpc.updateMetaStub(channel)
            name_ = [name]
            segment_ = [segment]
            stub.updateEvictedModelMeta(cache_pb2.modelMeta(name=name_, segment=segment_))

    def store(self, modelSize, SegmentMaxSize, lru, segment, name, model):
        global storage, store, flag
        temp = store + modelSize
        if temp >= SegmentMaxSize:
            # cache eviction
            flag = self.evict(modelSize, lru, SegmentMaxSize)
            # call to master for updating the current storage size of the machine
        storage += modelSize
        store += modelSize
        if flag:
            config.get(segment)["store"] = store
            # adding to cache
            lru.add(segment, name, model)
        else:
            storage -= modelSize
            store -= modelSize
            config.get(segment)["store"] = store
            # update master about the evicted object
            self.updateEvictedModel(name=name, segment=segment)
        # updating master about the dataNode size
        with grpc.insecure_channel(
                'localhost:50051') as channel:  # this port need to change to masters running port
            stub = cache_pb2_grpc.updateMetaStub(channel)
            try:
                stub.updateDataNodeMeta(cache_pb2.DataNodeSize(size=str(storage), IP="localhost:" + IP))
            except Exception as e:
                print(e)


class Inspect(cache_pb2_grpc.ttlInspectorServicer):
    def inspect(self, request, context):
        segmentList = request.segment
        global storage, store
        name_ = list()
        segment_ = list()
        try:
            for segment in segmentList:
                store = config.get(segment)["store"]
                lru = config.get(segment).get(segment)
                tempName, tempSegment, size = lru.evictTimeExceededModels(segment)
                for i, n in enumerate(tempSegment):
                    name_.append(tempName[i])
                    segment_.append(tempSegment[i])
                store -= size
                storage -= size
                config.get(segment)["store"] = store
        except Exception as e:
            print(e)
        # updating master about the dataNode size
        with grpc.insecure_channel(
                'localhost:50051') as channel:  # this port need to change to masters running port
            stub = cache_pb2_grpc.updateMetaStub(channel)
            try:
                stub.updateDataNodeMeta(cache_pb2.DataNodeSize(size=str(storage), IP="localhost:" + IP))
            except Exception as e:
                print(e)
        return cache_pb2.modelMeta(name=name_, segment=segment_)


def parseXML(path):
    tree = ET.parse(path)
    root = tree.getroot()
    global maxSize, config
    maxSize = int(root.get("size"))
    memory = psutil.virtual_memory()
    AvailableMemoryForCache = int(round(memory.available / 1048576) / 2)
    if maxSize >= AvailableMemoryForCache:
        maxSize = AvailableMemoryForCache
        NoOfSegments = len(list(root))
        memoryForSegments = round(AvailableMemoryForCache / NoOfSegments)
        for item in root:
            if int(item.get("max_cache_size")) < memoryForSegments:
                mem = item.get("max_cache_size")
            else:
                mem = memoryForSegments
            config[item.get("name")] = {"limit": mem,
                                        "eviction_percentage": item.get("eviction_percentage"),
                                        "max_object_size": item.get("max_obj_size"),
                                        item.get('name'): LRU.LRUCache(),
                                        "store": 0
                                        }
    else:
        for item in root:
            config[item.get("name")] = {"limit": item.get("max_cache_size"),
                                        "eviction_percentage": item.get("eviction_percentage"),
                                        "max_object_size": item.get("max_obj_size"),
                                        item.get('name'): LRU.LRUCache(),
                                        "store": 0
                                        }


def startup():
    size = 1024 ** 3
    with grpc.insecure_channel("localhost:50051", options=[
        ('grpc.max_send_message_length', size),
        ('grpc.max_receive_message_length', size),
    ]) as channel:
        stub = cache_pb2_grpc.ttlInspectorStub(channel)
        response = stub.serverStartUp(cache_pb2.serverSpecs(DN='localhost' + IP, storage=str(storage)))
        return response.bool


def terminate():
    size = 1024 ** 3
    with grpc.insecure_channel("localhost:50051", options=[
        ('grpc.max_send_message_length', size),
        ('grpc.max_receive_message_length', size),
    ]) as channel:
        stub = cache_pb2_grpc.ttlInspectorStub(channel)
        stub.serverShutDown(cache_pb2.serverSpecs(DN='localhost' + IP, storage=str(storage)))


def serve():
    size = 1024 ** 3
    # check = startup()
    # print(check)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4), options=[
        ('grpc.max_send_message_length', size),
        ('grpc.max_receive_message_length', size)])
    cache_pb2_grpc.add_getModelFromDataNodeServicer_to_server(DataNode3(), server)
    cache_pb2_grpc.add_updateMetaServicer_to_server(DataNode3(), server)
    cache_pb2_grpc.add_extrasServicer_to_server(DataNode3(), server)
    cache_pb2_grpc.add_ttlInspectorServicer_to_server(Inspect(), server)
    server.add_insecure_port('[::]:' + IP)
    server.start()
    print("DataNode 3 running")
    server.wait_for_termination()


if __name__ == '__main__':
    try:
        parseXML("./config/config.xml")
        serve()
    finally:
        terminate()
