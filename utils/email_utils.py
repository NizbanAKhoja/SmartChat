import smtplib
from email.mime.text import MIMEText

def send_api_key(to_email, api_key):
    msg = MIMEText(f"Your API key is: {api_key}")
    msg['Subject'] = 'Your API Key'
    msg['From'] = 'nizbana89@gmail.com'
    msg['To'] = to_email

    # Sending email via Gmail SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('nizbana89@gmail.com', 'aadz njct lanx ixjm')  # Use your app password here
        server.sendmail('nizbana89@gmail.com', to_email, msg.as_string())
