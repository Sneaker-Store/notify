from os import times
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

rec_sms = db.Table('rec_sms',
    db.Column('notif_id', db.Integer, db.ForeignKey('notification.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)

rec_mail = db.Table('rec_mail',
    db.Column('notif_id', db.Integer, db.ForeignKey('notification.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)

class Notification(db.Model):
    __tablename__ = 'notification'
    """
    Notification
    """
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    subject = db.Column(db.String(200))
    message = db.Column(db.String(64000))
    mail_recipients = db.relationship('User', secondary=rec_mail, lazy='subquery')
    sms_recipients = db.relationship('User', secondary=rec_sms, lazy='subquery')
    timestamp = db.Column(db.String(120), nullable=True)
    status = db.Column(db.String(120))
    hash_repr = db.Column(db.String(200))

    def __repr__(self):
        return '<Notification %r>' % self.subject

    def __init__(self, sender, subject, message, mail_recipients, sms_recipients, timestamp, status, hash_repr):
        self.sender = sender
        self.subject = subject
        self.message = message
        self.mail_recipients = mail_recipients
        self.sms_recipients = sms_recipients
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
    notif_sent = db.relationship('Notification', backref='sent_by', lazy=True)

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