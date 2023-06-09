import smtplib
from email.message import EmailMessage
import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server_login_mail = "connect.community2022@gmail.com"
server_login_password = "sharda"
server.login(server_login_mail, server_login_password)


def say(text):
    engine.say(text)
    engine.runAndWait()


say("hello sir, how can i help you? myself email assistant")


def assistant_listener():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            info = listener.recognize_google(voice, language="en-in").lower()
            return info

    except:
        return "no"


def send_email(rec, subject, message):
    email = EmailMessage()
    email['From'] = server_login_mail
    email['To'] = rec
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


contact = {
    "harsh": "vajpayeeharsh2001@gmail.com",
    "youtube": "youtube@gmail.com"
}


def whattodo():
    listen_me = assistant_listener()
    if "assistant" in listen_me:
        if "write mail" in listen_me:
            print("To whom you want to send mail?")
            say("To whom you want to send mail?")
            try:
                user = assistant_listener()
                email = contact[user]
            except:
                say(user+" not found in your contacts!")
                return 0
            print("What you want to be subject?")
            say("What you want to be subject?")
            subject = assistant_listener()
            print("what should be the message?")
            say("what should be the message?")
            message = assistant_listener()
            send_email(email, subject, message)
            print("Email Send Successfully")
            say("Email Send Successfully")
            say('Do you want to send more email?')
            send_more = assistant_listener()
            if 'yes' in send_more:
                whattodo()

while True:
    whattodo()
