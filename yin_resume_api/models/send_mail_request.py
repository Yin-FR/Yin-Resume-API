from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from yin_resume_api.models.base_model import Model
from yin_resume_api.models.send_mail_request_receiver import SendMailRequestReceiver
from yin_resume_api import util

from yin_resume_api.models.send_mail_request_receiver import SendMailRequestReceiver  # noqa: E501

class SendMailRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, receiver=None):  # noqa: E501
        """SendMailRequest - a model defined in OpenAPI

        :param receiver: The receiver of this SendMailRequest.  # noqa: E501
        :type receiver: SendMailRequestReceiver
        """
        self.openapi_types = {
            'receiver': SendMailRequestReceiver
        }

        self.attribute_map = {
            'receiver': 'receiver'
        }

        self._receiver = receiver

    @classmethod
    def from_dict(cls, dikt) -> 'SendMailRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The send_mail_request of this SendMailRequest.  # noqa: E501
        :rtype: SendMailRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def receiver(self) -> SendMailRequestReceiver:
        """Gets the receiver of this SendMailRequest.


        :return: The receiver of this SendMailRequest.
        :rtype: SendMailRequestReceiver
        """
        return self._receiver

    @receiver.setter
    def receiver(self, receiver: SendMailRequestReceiver):
        """Sets the receiver of this SendMailRequest.


        :param receiver: The receiver of this SendMailRequest.
        :type receiver: SendMailRequestReceiver
        """

        self._receiver = receiver