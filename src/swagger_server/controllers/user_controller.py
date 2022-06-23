import connexion
import sqlalchemy
import requests

from swagger_server.models.service import Service  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.models.db_model import User as User_db, engine

Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

def delete_user(username):  # noqa: E501
    """Delete user

     # noqa: E501

    :param username: Username that needs to be deleted
    :type username: str

    :rtype: None
    """
    usr = session.query(User_db).filter_by(username=username).delete()
    session.commit()
    return 'deleted user'


def get_user_by_mail(username):  # noqa: E501
    """Get user by username

     # noqa: E501

    :param username: 
    :type username: str

    :rtype: User
    """
    usr = session.query(User_db).filter_by(username=username).first()
    if usr != None:
        user_response = User(usr.username,usr.email,usr.phone,usr.sms,usr.mail)
    else:
        user_response = 400
    return user_response


def get_user_services(username):  # noqa: E501
    """Get user&#39;s service preference

     # noqa: E501

    :param username: 
    :type username: str

    :rtype: Service
    """
    usr = session.query(User_db).filter_by(username=username).first()
    print(usr)
    if usr != None:
        user_response = Service(usr.sms,usr.mail)
    else:
        user_response = 400
    return user_response


def register(data):  # noqa: E501
    """Register operation

    This call should be used when you wish to register to our notification service # noqa: E501

    :param data: JSON body required to create an account
    :type data: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        data = User.from_dict(connexion.request.get_json())  # noqa: E501
        usr = User_db(data.username,data.email,data.phone,data.sms,data.mail)
        exists = session.query(User_db).filter_by(username=data.username).first() is not None
        if exists:
            print("user already exists")
            return 400
        else:
            session.add(usr)
            session.commit()
        print("added user")
    return 200


def update_user(username, body):  # noqa: E501
    """Update user

     # noqa: E501

    :param username: Username that needs to be updated
    :type username: str
    :param body: Updated user object
    :type body: dict | bytes


    :rtype: None
    """
    print("this still has to be integrated with the authentication service")
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'