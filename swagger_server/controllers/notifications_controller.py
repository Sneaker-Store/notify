import connexion
import six
from flask import Flask
from flask_sqlalchemy import  SQLAlchemy

from swagger_server.models.notification import Notification  # noqa: E501
from swagger_server.models.notification_status import NotificationStatus  # noqa: E501
from swagger_server.models.response_id import ResponseID  # noqa: E501
from swagger_server import util
from swagger_server.models.db_model import db, Notification, User

def delete_notif(id):  # noqa: E501
    """Delete scheduled notification

     # noqa: E501

    :param id: The ID of the notification to be deleted
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def get_notif_id(id):  # noqa: E501
    """Get the status of a notification

     # noqa: E501
     

    :param id: The ID corresponding to a notification sent or scheduled
    :type id: str

    :rtype: NotificationStatus
    """
    print("notificação")
    r2 = NotificationStatus("abdc","abcew",1231323,"sent",19283791923,[],[])
    r3 = ResponseID("asdasd")
    usr =  User.query.get(1) 
    usr2 = User.query.get(2)
    print(usr)
    notif = Notification("user1","asdasd","asdasdasd",[usr,usr2],[usr,usr2],912381239,"waiting","notif-asdasdasd")
    db.session.add(notif)
    db.session.commit()
    return r3


def send_notif(data):  # noqa: E501
    """Notify one or multiple e-mail adresses and/or cellphone numbers

    This action can be done as soon as the server is available to send the notification or, if a timestamp is passed, the notification will be sent at the scheduled time # noqa: E501

    :param data: JSON body required to create an e-mail notification. Optional timestamp field for scheduling
    :type data: dict | bytes

    :rtype: ResponseID
    """
    if connexion.request.is_json:
        data = Notification.from_dict(connexion.request.get_json())  # noqa: E501


    response = ResponseID("abcd")
    return response
