import connexion
import six

from swagger_server.models.service import Service  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util

def delete_user(username):  # noqa: E501
    """Delete user

     # noqa: E501

    :param username: Username that needs to be deleted
    :type username: str

    :rtype: None
    """
    return 'do some magic!'


def get_user_by_mail(username):  # noqa: E501
    """Get user by username

     # noqa: E501

    :param username: 
    :type username: str

    :rtype: User
    """
    return 'do some magic!'


def get_user_services(username):  # noqa: E501
    """Get user&#39;s service preference

     # noqa: E501

    :param username: 
    :type username: str

    :rtype: Service
    """
    print("teste")
    return 'do some magic!'


def register(data):  # noqa: E501
    """Register operation

    This call should be used when you wish to register to our notification service # noqa: E501

    :param data: JSON body required to create an account
    :type data: dict | bytes

    :rtype: None
    """
    print("teste")
    if connexion.request.is_json:
        data = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'

def update_user(username, body):  # noqa: E501
    """Update user

     # noqa: E501

    :param username: Username that needs to be updated
    :type username: str
    :param body: Updated user object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
