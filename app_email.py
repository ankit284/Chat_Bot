from flask import Flask, render_template
from flask_mail import Mail, Message

app=Flask(__name__)


def create_app():
    app = Flask(__name__)
    app.config.update(DEBUG=True,MAIL_SERVER='smtp.gmail.com',MAIL_PORT=465,MAIL_USE_SSL=True,MAIL_USERNAME='',MAIL_PASSWORD='')
    return app

def send_mail(msg_sub,msg_body,msg_list,mail_to,render_html=False):
# msg = Message('test subject', sender='botatservice@gmail.com', recipients='jpr.saurabh@gmail.com')
    app=create_app()
    with app.app_context():
        mail=Mail(app)
        try:
            msg = Message(msg_sub,
                sender="botatservice@gmail.com",
                recipients=[mail_to])
            msg.body = msg_body 
            if msg_list!=[] and render_html==True:
                msg.html=render_template('email.html',result=msg_list)        
            mail.send(msg)
            return 'Success'
        except Exception as e:
            return(str(e)) 

