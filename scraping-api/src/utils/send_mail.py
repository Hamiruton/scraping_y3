import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

smtp_server = "smtp.gmail.com"
smtp_port = 587
username = "axelhamilton02@gmail.com"
# password = "qifenxaprwhffyer"
password = "xylujgwsrumanjuy"
dir_path = os.path.join(os.getcwd(), 'extraction-data')
subject = "Extraction scrap"

# body = "En fichier joint un fichier d'extraction"
# recipient = "Kevin.Tchehimouegnan@ycubeac.com"

def send_mail(recipients:list, body:str, filename_:str) -> bool:
  msg = MIMEMultipart()
  msg['From'] = username
  msg['To'] = ', '.join(recipients)
  msg['Subject'] = subject
  msg.attach(MIMEText(body, 'plain'))

  file_path = os.path.join(dir_path, filename_)
  with open(file_path, 'rb') as file:
    part = MIMEApplication(file.read(), Name=filename_)
    part.add_header('Content-Disposition', 'attachment', filename=filename_)
    msg.attach(part)

  try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
      server.starttls()
      server.login(username, password)
      server.sendmail(username, recipients, msg.as_string())
    return True
  except Exception as e:
    print("Error")
    print(e)
    return False