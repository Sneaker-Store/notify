import connexion
import hashlib
import six

from swagger_server.models.notification import Notification as Notification_model  # noqa: E501
from swagger_server.models.notification_status import NotificationStatus as NotificationStatus_model  # noqa: E501
from swagger_server.models.response_id import ResponseID  # noqa: E501
from swagger_server import util
from swagger_server.models.db_model import Notification as Notification_db, User, db


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
    return 'do some magic!'


def send_notif(data):  # noqa: E501
    """Notify one or multiple e-mail adresses and/or cellphone numbers

    This action can be done as soon as the server is available to send the notification or, if a timestamp is passed, the notification will be sent at the scheduled time # noqa: E501

    :param data: JSON body required to create an e-mail notification. Optional timestamp field for scheduling
    :type data: dict | bytes

    :rtype: ResponseID
    """
    list_mail_rec = []
    list_sms_rec = []
    if connexion.request.is_json:
        data = Notification_model.from_dict(connexion.request.get_json())  # noqa: E501
        # get the username from its email of the user who send the notif
        usr_sender=  User.query.filter_by(username=data._from).first().id 
        subject = data.subject
        message = data.message
        timestamp = data.timestamp
        hash_repr = "mail-"+hashlib.sha1(message.encode("UTF-8")).hexdigest()[0:15]

        # Get users
        for recipients in data.recipients:
            usr = User.query.filter_by(username=recipients).first()
            # Depending on user wanting SMS and/or E-Mail notification
            if usr.sms == 'y':
                list_sms_rec.append(usr)
            if usr.mail == 'y':
                list_mail_rec.append(usr)

        notif = Notification_db(usr_sender,subject,message,list_mail_rec,list_sms_rec,timestamp,"not_sent",hash_repr)
        db.session.add(notif)
        db.session.commit()

    response = ResponseID(hash_repr)
    return response
