from django.core.mail import send_mail

def mail(receiver_mail,name):
    subject = "Data Submitted"
    from_email = "DATAFLOW"
    to_email = [receiver_mail]
    mail_message = """Dear {},\nYOU HAVE SUBMITTED YOUR DATA SUCCESSFULLY!!""".format(name)

    send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=mail_message, fail_silently=False)