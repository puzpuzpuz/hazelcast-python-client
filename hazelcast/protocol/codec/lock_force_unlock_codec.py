from hazelcast.serialization.bits import *
from hazelcast.protocol.client_message import ClientMessage
from hazelcast.protocol.codec.lock_message_type import *

REQUEST_TYPE = LOCK_FORCEUNLOCK
RESPONSE_TYPE = 100
RETRYABLE = True


def calculate_size(name, reference_id):
    """ Calculates the request payload size"""
    data_size = 0
    data_size += calculate_size_str(name)
    data_size += LONG_SIZE_IN_BYTES
    return data_size


def encode_request(name, reference_id):
    """ Encode request into client_message"""
    client_message = ClientMessage(payload_size=calculate_size(name, reference_id))
    client_message.set_message_type(REQUEST_TYPE)
    client_message.set_retryable(RETRYABLE)
    client_message.append_str(name)
    client_message.append_long(reference_id)
    client_message.update_frame_length()
    return client_message


# Empty decode_response(client_message), this message has no parameters to decode
