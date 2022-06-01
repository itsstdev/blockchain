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

from swagger_client.models.ledger import Ledger  # noqa: F401,E501


class LedgerList(object):
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
        'next_link': 'str',
        'ledgers': 'list[Ledger]'
    }

    attribute_map = {
        'next_link': 'nextLink',
        'ledgers': 'ledgers'
    }

    def __init__(self, next_link=None, ledgers=None):  # noqa: E501
        """LedgerList - a model defined in Swagger"""  # noqa: E501

        self._next_link = None
        self._ledgers = None
        self.discriminator = None

        if next_link is not None:
            self.next_link = next_link
        if ledgers is not None:
            self.ledgers = ledgers

    @property
    def next_link(self):
        """Gets the next_link of this LedgerList.  # noqa: E501


        :return: The next_link of this LedgerList.  # noqa: E501
        :rtype: str
        """
        return self._next_link

    @next_link.setter
    def next_link(self, next_link):
        """Sets the next_link of this LedgerList.


        :param next_link: The next_link of this LedgerList.  # noqa: E501
        :type: str
        """

        self._next_link = next_link

    @property
    def ledgers(self):
        """Gets the ledgers of this LedgerList.  # noqa: E501


        :return: The ledgers of this LedgerList.  # noqa: E501
        :rtype: list[Ledger]
        """
        return self._ledgers

    @ledgers.setter
    def ledgers(self, ledgers):
        """Sets the ledgers of this LedgerList.


        :param ledgers: The ledgers of this LedgerList.  # noqa: E501
        :type: list[Ledger]
        """

        self._ledgers = ledgers

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
            if isinstance(other, LedgerList)
            else False
        )

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
