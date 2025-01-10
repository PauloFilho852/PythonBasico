import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "paulofilho055@gmail.com"
toaddr = "criandorobosempython@gmail.com, gabrielcasemiro68@gmail.com, paulofilho055@gmail.con"

# Instância do MIMEMultipart
msg = MIMEMultipart()

msg['From'] = fromaddr

msg['To'] = toaddr

msg['Subject'] = "Venha conhecer nosso restaurante!!!"

body = """Inauguração do nosso restaurante essa noite, venha conhecer."""

msg.attach(MIMEText(body, 'plain'))

# Servidor SMTP
server = smtplib.SMTP('smtp.gmail.com', 587)

# Segurança
server.starttls()

server.login(fromaddr, '054497Eu*')

# Converte para String
text = msg.as_string()

server.sendmail(fromaddr, toaddr, text)

server.quit()
