import sqlalchemy
from sqlalchemy import Table, Column, Integer, ForeignKey, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

engine = sqlalchemy.create_engine('mysql+pymysql://root:12345@127.0.0.1:3306/notifydb?charset=utf8mb4')
Base = declarative_base();

rec_sms = Table('rec_sms',
    Base.metadata,
    Column('notif_id', Integer, ForeignKey('notification.id'), primary_key=True),
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True)
)

rec_mail = Table('rec_mail',
    Base.metadata,
    Column('notif_id', Integer, ForeignKey('notification.id'), primary_key=True),
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True)
)

class Notification(Base):
    __tablename__ = 'notification'
    """
    Notification
    """
    id = Column(Integer, primary_key=True)
    sender = Column(Integer, ForeignKey('user.id'), nullable=False)
    subject = Column(String(200))
    message = Column(Text(64000))
    mail_recipients = relationship('User', secondary=rec_mail, lazy='subquery')
    sms_recipients = relationship('User', secondary=rec_sms, lazy='subquery')
    timestamp = Column(String(120), nullable=True)
    status = Column(String(120))
    hash_repr = Column(String(200))
    sent_on = Column(String(120), nullable=True)

    def __repr__(self):
        return '<Notification %r>' % self.id

    def __init__(self, sender, subject, message, mail_recipients, sms_recipients, timestamp, status, hash_repr):
        self.sender = sender
        self.subject = subject
        self.message = message
        self.mail_recipients = mail_recipients
        self.sms_recipients = sms_recipients
        self.timestamp = timestamp
        self.status = status
        self.hash_repr = hash_repr
        self.sent_on = "0"

class User(Base):
    __tablename__ = 'user'
    """
    User
    """
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(50))
    phone = Column(String(12))
    sms = Column(String(1))
    mail = Column(String(1))
    notif_sent = relationship('Notification', backref='sent_by', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def __init__(self, username, first_name, last_name, email, phone, sms, mail):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.sms = sms
        self.mail = mail

#Base.metadata.create_all(engine)