import connexion
import hashlib
import sqlalchemy
import requests

from swagger_server.models.notification import Notification as Notification_model  # noqa: E501
from swagger_server.models.notification_status import NotificationStatus as NotificationStatus_model  # noqa: E501
from swagger_server.models.response_id import ResponseID  # noqa: E501
from swagger_server import util
from swagger_server.models.db_model import Notification as Notification_db, User, engine, rec_mail,rec_sms

Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

def delete_notif(id):  # noqa: E501
    """Delete scheduled notification

     # noqa: E501

    :param id: The ID of the notification to be deleted
    :type id: str

    :rtype: None
    """

    #headers = {'token': request.headers['token'], 'email': request.headers['email']}
    #r = requests.get('http://localhost:5000/auth', headers=headers)
    #if r.status_code != 200:
    #    return make_response(
    #        "Not authenticated", r.status_code
    #    )

    hash_repr = id
    # Get the notification from the it's hash representation
    session.query(Notification_db).filter_by(hash_repr=hash_repr).delete()
    session.commit()
    return 'deleted notification'


def get_notif_id(id):  # noqa: E501
    """Get the status of a notification

     # noqa: E501

    :param id: The ID corresponding to a notification sent or scheduled
    :type id: str

    :rtype: NotificationStatus
    """
    list_mail_rec=[]
    list_sms_rec=[]
    hash_repr = id
    # Get the notification from the it's hash representation
    ndb = session.query(Notification_db).filter_by(hash_repr=hash_repr).first()

    #Query the association tables, to find wich user where notified
    list_mail = session.query(User).join(rec_mail).join(Notification_db).filter(rec_mail.c.notif_id == ndb.id).all()
    list_sms = session.query(User).join(rec_sms).join(Notification_db).filter(rec_sms.c.notif_id == ndb.id).all()
    for recipient in list_mail:
        list_mail_rec.append(recipient.email)
    for recipient in list_sms:
        list_sms_rec.append(recipient.phone)

    sender_email = session.query(User).get(ndb.sender).email
    notif_response = NotificationStatus_model(ndb.subject,sender_email,ndb.timestamp,ndb.status,ndb.sent_on,list_mail_rec,list_sms_rec)
    return notif_response


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
        usr_sender=  session.query(User).filter_by(username=data._from).first().id 
        subject = data.subject
        message = data.message
        timestamp = data.timestamp
        # Generate hash of the message + timestamp
        hash_repr = hashlib.sha1((message+str(timestamp)).encode("UTF-8")).hexdigest()[0:15]

        # Get users
        for recipients in data.recipients:
            usr = session.query(User).filter_by(username=recipients).first()
            # Depending on user wanting SMS and/or E-Mail notification
            if usr.sms == 'y':
                list_sms_rec.append(usr)
            if usr.mail == 'y':
                list_mail_rec.append(usr)

        notif = Notification_db(usr_sender,subject,message,list_mail_rec,list_sms_rec,timestamp,"not_sent",hash_repr)
        session.add(notif)
        session.commit()

    response = ResponseID(hash_repr)
    return response
