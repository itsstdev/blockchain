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

from swagger_client.models.contract_action_parameter import ContractActionParameter  # noqa: F401,E501


class ContractAction(object):
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
        'id': 'int',
        'user_id': 'int',
        'provisioning_status': 'int',
        'timestamp': 'datetime',
        'parameters': 'list[ContractActionParameter]',
        'workflow_function_id': 'int',
        'transaction_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'user_id': 'userId',
        'provisioning_status': 'provisioningStatus',
        'timestamp': 'timestamp',
        'parameters': 'parameters',
        'workflow_function_id': 'workflowFunctionId',
        'transaction_id': 'transactionId'
    }

    def __init__(self, id=None, user_id=None, provisioning_status=None, timestamp=None, parameters=None, workflow_function_id=None, transaction_id=None):  # noqa: E501
        """ContractAction - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._user_id = None
        self._provisioning_status = None
        self._timestamp = None
        self._parameters = None
        self._workflow_function_id = None
        self._transaction_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if user_id is not None:
            self.user_id = user_id
        if provisioning_status is not None:
            self.provisioning_status = provisioning_status
        if timestamp is not None:
            self.timestamp = timestamp
        if parameters is not None:
            self.parameters = parameters
        if workflow_function_id is not None:
            self.workflow_function_id = workflow_function_id
        if transaction_id is not None:
            self.transaction_id = transaction_id

    @property
    def id(self):
        """Gets the id of this ContractAction.  # noqa: E501


        :return: The id of this ContractAction.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ContractAction.


        :param id: The id of this ContractAction.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def user_id(self):
        """Gets the user_id of this ContractAction.  # noqa: E501


        :return: The user_id of this ContractAction.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ContractAction.


        :param user_id: The user_id of this ContractAction.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def provisioning_status(self):
        """Gets the provisioning_status of this ContractAction.  # noqa: E501


        :return: The provisioning_status of this ContractAction.  # noqa: E501
        :rtype: int
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        """Sets the provisioning_status of this ContractAction.


        :param provisioning_status: The provisioning_status of this ContractAction.  # noqa: E501
        :type: int
        """

        self._provisioning_status = provisioning_status

    @property
    def timestamp(self):
        """Gets the timestamp of this ContractAction.  # noqa: E501


        :return: The timestamp of this ContractAction.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ContractAction.


        :param timestamp: The timestamp of this ContractAction.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def parameters(self):
        """Gets the parameters of this ContractAction.  # noqa: E501


        :return: The parameters of this ContractAction.  # noqa: E501
        :rtype: list[ContractActionParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this ContractAction.


        :param parameters: The parameters of this ContractAction.  # noqa: E501
        :type: list[ContractActionParameter]
        """

        self._parameters = parameters

    @property
    def workflow_function_id(self):
        """Gets the workflow_function_id of this ContractAction.  # noqa: E501


        :return: The workflow_function_id of this ContractAction.  # noqa: E501
        :rtype: int
        """
        return self._workflow_function_id

    @workflow_function_id.setter
    def workflow_function_id(self, workflow_function_id):
        """Sets the workflow_function_id of this ContractAction.


        :param workflow_function_id: The workflow_function_id of this ContractAction.  # noqa: E501
        :type: int
        """

        self._workflow_function_id = workflow_function_id

    @property
    def transaction_id(self):
        """Gets the transaction_id of this ContractAction.  # noqa: E501


        :return: The transaction_id of this ContractAction.  # noqa: E501
        :rtype: int
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this ContractAction.


        :param transaction_id: The transaction_id of this ContractAction.  # noqa: E501
        :type: int
        """

        self._transaction_id = transaction_id

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
            if isinstance(other, ContractAction)
            else False
        )

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
