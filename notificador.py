import smtplib

MY_EMAIL = "sersancal@gmail.com"
PASSW = "dclznljkebpowwcd"


def envio(message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        message = "Aqui te envio el tiempo de hoy"
        subject = f"EL TIEMPO DE HOY"
        message_with_subject = f"Subject:{subject}\n\n{message}"
        connection.starttls()
        connection.login(MY_EMAIL,PASSW)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=message_with_subject.encode('utf-8'))

