from os import times
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

tags_sms = db.Table('tags_sms',
    db.Column('notif_id', db.Integer, db.ForeignKey('notification.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)

tags_mail = db.Table('tags_mail',
    db.Column('notif_id', db.Integer, db.ForeignKey('notification.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)

class Notification(db.Model):
    __tablename__ = 'notification'
    """
    Notification
    """
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(50))
    subject = db.Column(db.String(200))
    message = db.Column(db.String(64000))
    sms_recipients = db.relationship('User', secondary=tags_sms, lazy='subquery',backref=db.backref('notification',lazy=True))
    mail_recipients = db.relationship('User', secondary=tags_mail, lazy='subquery',backref=db.backref('notification',lazy=True))
    timestamp = db.Column(db.String(120), nullable=True)
    status = db.Column(db.String(120))
    hash_repr = db.Column(db.String(200))

    def __repr__(self):
        return '<Notification %r>' % self.subject

    def __init__(self, sender, subject, message, sms_recipients, mail_recipients, timestamp, status, hash_repr):
        self.sender = sender
        self.subject = subject
        self.message = message
        self.sms_recipients = sms_recipients
        self.mail_recipients = mail_recipients
        self.timestamp = timestamp
        self.status = status
        self.hash_repr = hash_repr


class User(db.Model):
    __tablename__ = 'user'
    """
    User
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    fist_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    phone = db.Column(db.String(12))
    sms = db.Column(db.String(1))
    mail = db.Column(db.String(1))

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