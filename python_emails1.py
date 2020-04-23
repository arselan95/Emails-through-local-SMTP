import smtplib, ssl

smtp_server = 'smtp.gmail.com'
port = 465  # For SSL

sender = 'zgravity207@gmail.com'
password = input('Type your password and press enter: ')

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, password)
    print('login works')
    # TODO: Send email here