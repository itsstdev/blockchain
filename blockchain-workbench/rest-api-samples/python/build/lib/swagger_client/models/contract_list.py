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

from swagger_client.models.contract import Contract  # noqa: F401,E501


class ContractList(object):
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
        'contracts': 'list[Contract]'
    }

    attribute_map = {
        'next_link': 'nextLink',
        'contracts': 'contracts'
    }

    def __init__(self, next_link=None, contracts=None):  # noqa: E501
        """ContractList - a model defined in Swagger"""  # noqa: E501

        self._next_link = None
        self._contracts = None
        self.discriminator = None

        if next_link is not None:
            self.next_link = next_link
        if contracts is not None:
            self.contracts = contracts

    @property
    def next_link(self):
        """Gets the next_link of this ContractList.  # noqa: E501


        :return: The next_link of this ContractList.  # noqa: E501
        :rtype: str
        """
        return self._next_link

    @next_link.setter
    def next_link(self, next_link):
        """Sets the next_link of this ContractList.


        :param next_link: The next_link of this ContractList.  # noqa: E501
        :type: str
        """

        self._next_link = next_link

    @property
    def contracts(self):
        """Gets the contracts of this ContractList.  # noqa: E501


        :return: The contracts of this ContractList.  # noqa: E501
        :rtype: list[Contract]
        """
        return self._contracts

    @contracts.setter
    def contracts(self, contracts):
        """Sets the contracts of this ContractList.


        :param contracts: The contracts of this ContractList.  # noqa: E501
        :type: list[Contract]
        """

        self._contracts = contracts

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
            if isinstance(other, ContractList)
            else False
        )

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
