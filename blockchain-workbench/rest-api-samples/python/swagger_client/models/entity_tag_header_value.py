# coding: utf-8

"""
    Azure Blockchain Workbench REST API

    The Azure Blockchain Workbench REST API is a Workbench extensibility point, which allows developers to create and manage blockchain applications, manage users and organizations within a consortium, integrate blockchain applications into services and platforms, perform transactions on a blockchain, and retrieve transactional and contract data from a blockchain.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.string_segment import StringSegment  # noqa: F401,E501


class EntityTagHeaderValue(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'tag': 'StringSegment',
        'is_weak': 'bool'
    }

    attribute_map = {
        'tag': 'tag',
        'is_weak': 'isWeak'
    }

    def __init__(self, tag=None, is_weak=None):  # noqa: E501
        """EntityTagHeaderValue - a model defined in Swagger"""  # noqa: E501

        self._tag = None
        self._is_weak = None
        self.discriminator = None

        if tag is not None:
            self.tag = tag
        if is_weak is not None:
            self.is_weak = is_weak

    @property
    def tag(self):
        """Gets the tag of this EntityTagHeaderValue.  # noqa: E501


        :return: The tag of this EntityTagHeaderValue.  # noqa: E501
        :rtype: StringSegment
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this EntityTagHeaderValue.


        :param tag: The tag of this EntityTagHeaderValue.  # noqa: E501
        :type: StringSegment
        """

        self._tag = tag

    @property
    def is_weak(self):
        """Gets the is_weak of this EntityTagHeaderValue.  # noqa: E501


        :return: The is_weak of this EntityTagHeaderValue.  # noqa: E501
        :rtype: bool
        """
        return self._is_weak

    @is_weak.setter
    def is_weak(self, is_weak):
        """Sets the is_weak of this EntityTagHeaderValue.


        :param is_weak: The is_weak of this EntityTagHeaderValue.  # noqa: E501
        :type: bool
        """

        self._is_weak = is_weak

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        return (
            self.__dict__ == other.__dict__
            if isinstance(other, EntityTagHeaderValue)
            else False
        )

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
