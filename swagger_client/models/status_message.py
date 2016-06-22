# coding: utf-8

"""
    Betfair: Exchange Streaming API

    API to receive streamed updates. This is an ssl socket connection of CRLF delimited json messages (see RequestMessage & ResponseMessage)

    OpenAPI spec version: 1.0.1423
    Contact: bdp@betfair.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    
        http://www.apache.org/licenses/LICENSE-2.0
    
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class StatusMessage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        StatusMessage - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'op': 'str',
            'id': 'int',
            'error_message': 'str',
            'error_code': 'str',
            'connection_id': 'str',
            'connection_closed': 'bool',
            'status_code': 'str'
        }

        self.attribute_map = {
            'op': 'op',
            'id': 'id',
            'error_message': 'errorMessage',
            'error_code': 'errorCode',
            'connection_id': 'connectionId',
            'connection_closed': 'connectionClosed',
            'status_code': 'statusCode'
        }

        self._op = None
        self._id = None
        self._error_message = None
        self._error_code = None
        self._connection_id = None
        self._connection_closed = None
        self._status_code = None

    @property
    def op(self):
        """
        Gets the op of this StatusMessage.
        The operation type

        :return: The op of this StatusMessage.
        :rtype: str
        """
        return self._op

    @op.setter
    def op(self, op):
        """
        Sets the op of this StatusMessage.
        The operation type

        :param op: The op of this StatusMessage.
        :type: str
        """
        
        self._op = op

    @property
    def id(self):
        """
        Gets the id of this StatusMessage.
        Client generated unique id to link request with response (like json rpc)

        :return: The id of this StatusMessage.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this StatusMessage.
        Client generated unique id to link request with response (like json rpc)

        :param id: The id of this StatusMessage.
        :type: int
        """
        
        self._id = id

    @property
    def error_message(self):
        """
        Gets the error_message of this StatusMessage.
        Additional message in case of a failure

        :return: The error_message of this StatusMessage.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this StatusMessage.
        Additional message in case of a failure

        :param error_message: The error_message of this StatusMessage.
        :type: str
        """
        
        self._error_message = error_message

    @property
    def error_code(self):
        """
        Gets the error_code of this StatusMessage.
        The type of error in case of a failure

        :return: The error_code of this StatusMessage.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """
        Sets the error_code of this StatusMessage.
        The type of error in case of a failure

        :param error_code: The error_code of this StatusMessage.
        :type: str
        """
        allowed_values = ["NO_APP_KEY", "INVALID_APP_KEY", "NO_SESSION", "INVALID_SESSION_INFORMATION", "NOT_AUTHORIZED", "INVALID_INPUT", "INVALID_CLOCK", "UNEXPECTED_ERROR", "TIMEOUT", "SUBSCRIPTION_LIMIT_EXCEEDED", "INVALID_REQUEST", "CONNECTION_FAILED", "MAX_CONNECTION_LIMIT_EXCEEDED"]
        if error_code not in allowed_values:
            raise ValueError(
                "Invalid value for `error_code`, must be one of {0}"
                .format(allowed_values)
            )

        self._error_code = error_code

    @property
    def connection_id(self):
        """
        Gets the connection_id of this StatusMessage.
        The connection id

        :return: The connection_id of this StatusMessage.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """
        Sets the connection_id of this StatusMessage.
        The connection id

        :param connection_id: The connection_id of this StatusMessage.
        :type: str
        """
        
        self._connection_id = connection_id

    @property
    def connection_closed(self):
        """
        Gets the connection_closed of this StatusMessage.
        Is the connection now closed

        :return: The connection_closed of this StatusMessage.
        :rtype: bool
        """
        return self._connection_closed

    @connection_closed.setter
    def connection_closed(self, connection_closed):
        """
        Sets the connection_closed of this StatusMessage.
        Is the connection now closed

        :param connection_closed: The connection_closed of this StatusMessage.
        :type: bool
        """
        
        self._connection_closed = connection_closed

    @property
    def status_code(self):
        """
        Gets the status_code of this StatusMessage.
        The status of the last request

        :return: The status_code of this StatusMessage.
        :rtype: str
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """
        Sets the status_code of this StatusMessage.
        The status of the last request

        :param status_code: The status_code of this StatusMessage.
        :type: str
        """
        allowed_values = ["SUCCESS", "FAILURE"]
        if status_code not in allowed_values:
            raise ValueError(
                "Invalid value for `status_code`, must be one of {0}"
                .format(allowed_values)
            )

        self._status_code = status_code

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

