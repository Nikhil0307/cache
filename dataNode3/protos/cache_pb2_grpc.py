# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from dataNode3.protos import cache_pb2 as dataNode3_dot_protos_dot_cache__pb2


class getModelFromDataNodeStub(object):
    """calls data nodes and gets model
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getModel = channel.unary_unary(
                '/cache.getModelFromDataNode/getModel',
                request_serializer=dataNode3_dot_protos_dot_cache__pb2.modelInfo.SerializeToString,
                response_deserializer=dataNode3_dot_protos_dot_cache__pb2.model.FromString,
                )
        self.putModel = channel.unary_unary(
                '/cache.getModelFromDataNode/putModel',
                request_serializer=dataNode3_dot_protos_dot_cache__pb2.wholeModel.SerializeToString,
                response_deserializer=dataNode3_dot_protos_dot_cache__pb2.model.FromString,
                )
        self.putObjectWithTime = channel.unary_unary(
                '/cache.getModelFromDataNode/putObjectWithTime',
                request_serializer=dataNode3_dot_protos_dot_cache__pb2.ObjectWithTime.SerializeToString,
                response_deserializer=dataNode3_dot_protos_dot_cache__pb2.text.FromString,
                )
        self.putObject = channel.unary_unary(
                '/cache.getModelFromDataNode/putObject',
                request_serializer=dataNode3_dot_protos_dot_cache__pb2.object.SerializeToString,
                response_deserializer=dataNode3_dot_protos_dot_cache__pb2.text.FromString,
                )
        self.putModelWithTime = channel.unary_unary(
                '/cache.getModelFromDataNode/putModelWithTime',
                request_serializer=dataNode3_dot_protos_dot_cache__pb2.ModelInfoWithTime.SerializeToString,
                response_deserializer=dataNode3_dot_protos_dot_cache__pb2.model.FromString,
                )


class getModelFromDataNodeServicer(object):
    """calls data nodes and gets model
    """

    def getModel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def putModel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def putObjectWithTime(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def putObject(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def putModelWithTime(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_getModelFromDataNodeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getModel': grpc.unary_unary_rpc_method_handler(
                    servicer.getModel,
                    request_deserializer=dataNode3_dot_protos_dot_cache__pb2.modelInfo.FromString,
                    response_serializer=dataNode3_dot_protos_dot_cache__pb2.model.SerializeToString,
            ),
            'putModel': grpc.unary_unary_rpc_method_handler(
                    servicer.putModel,
                    request_deserializer=dataNode3_dot_protos_dot_cache__pb2.wholeModel.FromString,
                    response_serializer=dataNode3_dot_protos_dot_cache__pb2.model.SerializeToString,
            ),
            'putObjectWithTime': grpc.unary_unary_rpc_method_handler(
                    servicer.putObjectWithTime,
                    request_deserializer=dataNode3_dot_protos_dot_cache__pb2.ObjectWithTime.FromString,
                    response_serializer=dataNode3_dot_protos_dot_cache__pb2.text.SerializeToString,
            ),
            'putObject': grpc.unary_unary_rpc_method_handler(
                    servicer.putObject,
                    request_deserializer=dataNode3_dot_protos_dot_cache__pb2.object.FromString,
                    response_serializer=dataNode3_dot_protos_dot_cache__pb2.text.SerializeToString,
            ),
            'putModelWithTime': grpc.unary_unary_rpc_method_handler(
                    servicer.putModelWithTime,
                    request_deserializer=dataNode3_dot_protos_dot_cache__pb2.ModelInfoWithTime.FromString,
                    response_serializer=dataNode3_dot_protos_dot_cache__pb2.model.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cache.getModelFromDataNode', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class getModelFromDataNode(object):
    """calls data nodes and gets model
    """

    @staticmethod
    def getModel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cache.getModelFromDataNode/getModel',
            dataNode3_dot_protos_dot_cache__pb2.modelInfo.SerializeToString,
            dataNode3_dot_protos_dot_cache__pb2.model.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def putModel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cache.getModelFromDataNode/putModel',
            dataNode3_dot_protos_dot_cache__pb2.wholeModel.SerializeToString,
            dataNode3_dot_protos_dot_cache__pb2.model.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def putObjectWithTime(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cache.getModelFromDataNode/putObjectWithTime',
            dataNode3_dot_protos_dot_cache__pb2.ObjectWithTime.SerializeToString,
            dataNode3_dot_protos_dot_cache__pb2.text.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def putObject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cache.getModelFromDataNode/putObject',
            dataNode3_dot_protos_dot_cache__pb2.object.SerializeToString,
            dataNode3_dot_protos_dot_cache__pb2.text.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def putModelWithTime(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cache.getModelFromDataNode/putModelWithTime',
            dataNode3_dot_protos_dot_cache__pb2.ModelInfoWithTime.SerializeToString,
            dataNode3_dot_protos_dot_cache__pb2.model.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class extrasStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.inValidate = channel.unary_unary(
                '/cache.extras/inValidate',
                request_serializer=dataNode3_dot_protos_dot_cache__pb2.modelInfo.SerializeToString,
                response_deserializer=dataNode3_dot_protos_dot_cache__pb2.text.FromString,
                )
        self.get_object_created_time = channel.unary_unary(
                '/cache.extras/get_object_created_time',
                request_serializer=dataNode3_dot_protos_dot_cache__pb2.modelInfo.SerializeToString,
                response_deserializer=dataNode3_dot_protos_dot_cache__pb2.text.FromString,
                )


class extrasServicer(object):
    """Missing associated documentation comment in .proto file."""

    def inValidate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_object_created_time(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_extrasServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'inValidate': grpc.unary_unary_rpc_method_handler(
                    servicer.inValidate,
                    request_deserializer=dataNode3_dot_protos_dot_cache__pb2.modelInfo.FromString,
                    response_serializer=dataNode3_dot_protos_dot_cache__pb2.text.SerializeToString,
            ),
            'get_object_created_time': grpc.unary_unary_rpc_method_handler(
                    servicer.get_object_created_time,
                    request_deserializer=dataNode3_dot_protos_dot_cache__pb2.modelInfo.FromString,
                    response_serializer=dataNode3_dot_protos_dot_cache__pb2.text.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cache.extras', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class extras(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def inValidate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cache.extras/inValidate',
            dataNode3_dot_protos_dot_cache__pb2.modelInfo.SerializeToString,
            dataNode3_dot_protos_dot_cache__pb2.text.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_object_created_time(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cache.extras/get_object_created_time',
            dataNode3_dot_protos_dot_cache__pb2.modelInfo.SerializeToString,
            dataNode3_dot_protos_dot_cache__pb2.text.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class ttlInspectorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.inspect = channel.unary_unary(
                '/cache.ttlInspector/inspect',
                request_serializer=dataNode3_dot_protos_dot_cache__pb2.segments.SerializeToString,
                response_deserializer=dataNode3_dot_protos_dot_cache__pb2.modelMeta.FromString,
                )
        self.serverStartUp = channel.unary_unary(
                '/cache.ttlInspector/serverStartUp',
                request_serializer=dataNode3_dot_protos_dot_cache__pb2.serverSpecs.SerializeToString,
                response_deserializer=dataNode3_dot_protos_dot_cache__pb2.boolean.FromString,
                )
        self.serverShutDown = channel.unary_unary(
                '/cache.ttlInspector/serverShutDown',
                request_serializer=dataNode3_dot_protos_dot_cache__pb2.serverSpecs.SerializeToString,
                response_deserializer=dataNode3_dot_protos_dot_cache__pb2.boolean.FromString,
                )


class ttlInspectorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def inspect(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def serverStartUp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def serverShutDown(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ttlInspectorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'inspect': grpc.unary_unary_rpc_method_handler(
                    servicer.inspect,
                    request_deserializer=dataNode3_dot_protos_dot_cache__pb2.segments.FromString,
                    response_serializer=dataNode3_dot_protos_dot_cache__pb2.modelMeta.SerializeToString,
            ),
            'serverStartUp': grpc.unary_unary_rpc_method_handler(
                    servicer.serverStartUp,
                    request_deserializer=dataNode3_dot_protos_dot_cache__pb2.serverSpecs.FromString,
                    response_serializer=dataNode3_dot_protos_dot_cache__pb2.boolean.SerializeToString,
            ),
            'serverShutDown': grpc.unary_unary_rpc_method_handler(
                    servicer.serverShutDown,
                    request_deserializer=dataNode3_dot_protos_dot_cache__pb2.serverSpecs.FromString,
                    response_serializer=dataNode3_dot_protos_dot_cache__pb2.boolean.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cache.ttlInspector', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ttlInspector(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def inspect(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cache.ttlInspector/inspect',
            dataNode3_dot_protos_dot_cache__pb2.segments.SerializeToString,
            dataNode3_dot_protos_dot_cache__pb2.modelMeta.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def serverStartUp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cache.ttlInspector/serverStartUp',
            dataNode3_dot_protos_dot_cache__pb2.serverSpecs.SerializeToString,
            dataNode3_dot_protos_dot_cache__pb2.boolean.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def serverShutDown(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cache.ttlInspector/serverShutDown',
            dataNode3_dot_protos_dot_cache__pb2.serverSpecs.SerializeToString,
            dataNode3_dot_protos_dot_cache__pb2.boolean.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class updateMetaStub(object):
    """calls master and returns meta
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.updateDataNodeMeta = channel.unary_unary(
                '/cache.updateMeta/updateDataNodeMeta',
                request_serializer=dataNode3_dot_protos_dot_cache__pb2.DataNodeSize.SerializeToString,
                response_deserializer=dataNode3_dot_protos_dot_cache__pb2.text.FromString,
                )
        self.updateEvictedModelMeta = channel.unary_unary(
                '/cache.updateMeta/updateEvictedModelMeta',
                request_serializer=dataNode3_dot_protos_dot_cache__pb2.modelMeta.SerializeToString,
                response_deserializer=dataNode3_dot_protos_dot_cache__pb2.text.FromString,
                )


class updateMetaServicer(object):
    """calls master and returns meta
    """

    def updateDataNodeMeta(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateEvictedModelMeta(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_updateMetaServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'updateDataNodeMeta': grpc.unary_unary_rpc_method_handler(
                    servicer.updateDataNodeMeta,
                    request_deserializer=dataNode3_dot_protos_dot_cache__pb2.DataNodeSize.FromString,
                    response_serializer=dataNode3_dot_protos_dot_cache__pb2.text.SerializeToString,
            ),
            'updateEvictedModelMeta': grpc.unary_unary_rpc_method_handler(
                    servicer.updateEvictedModelMeta,
                    request_deserializer=dataNode3_dot_protos_dot_cache__pb2.modelMeta.FromString,
                    response_serializer=dataNode3_dot_protos_dot_cache__pb2.text.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cache.updateMeta', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class updateMeta(object):
    """calls master and returns meta
    """

    @staticmethod
    def updateDataNodeMeta(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cache.updateMeta/updateDataNodeMeta',
            dataNode3_dot_protos_dot_cache__pb2.DataNodeSize.SerializeToString,
            dataNode3_dot_protos_dot_cache__pb2.text.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateEvictedModelMeta(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cache.updateMeta/updateEvictedModelMeta',
            dataNode3_dot_protos_dot_cache__pb2.modelMeta.SerializeToString,
            dataNode3_dot_protos_dot_cache__pb2.text.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
