# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from dialogflow_v2.proto import (
    environment_pb2 as google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_environment__pb2,
)


class EnvironmentsStub(object):
    """Service for managing [Environments][google.cloud.dialogflow.v2.Environment].
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListEnvironments = channel.unary_unary(
            "/google.cloud.dialogflow.v2.Environments/ListEnvironments",
            request_serializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_environment__pb2.ListEnvironmentsRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_environment__pb2.ListEnvironmentsResponse.FromString,
        )


class EnvironmentsServicer(object):
    """Service for managing [Environments][google.cloud.dialogflow.v2.Environment].
    """

    def ListEnvironments(self, request, context):
        """Returns the list of all non-draft environments of the specified agent.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_EnvironmentsServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "ListEnvironments": grpc.unary_unary_rpc_method_handler(
            servicer.ListEnvironments,
            request_deserializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_environment__pb2.ListEnvironmentsRequest.FromString,
            response_serializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_environment__pb2.ListEnvironmentsResponse.SerializeToString,
        )
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "google.cloud.dialogflow.v2.Environments", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Environments(object):
    """Service for managing [Environments][google.cloud.dialogflow.v2.Environment].
    """

    @staticmethod
    def ListEnvironments(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.cloud.dialogflow.v2.Environments/ListEnvironments",
            google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_environment__pb2.ListEnvironmentsRequest.SerializeToString,
            google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_environment__pb2.ListEnvironmentsResponse.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
