import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# criar um script chamado corpo_email e com uma variável corpo_email com o html
# from corpo_email import corpo_email


fromaddr = "criandorobosempython@gmail.com"
toaddr = "criandorobosempython@gmail.com, gabrielcasemiro68@gmail.com"

# Instância do MIMEMultipart
msg = MIMEMultipart()


msg['From'] = fromaddr

msg['To'] = toaddr

msg['Subject'] = "Video Aulas Grátis!!"


part1 = MIMEText(corpo_email, "html")

msg.attach(part1)

# Servidor SMTP
server = smtplib.SMTP('smtp.gmail.com', 587)

# Segurança
server.starttls()

server.login(fromaddr, 'robos123')

# Converte para String
text = msg.as_string()

server.sendmail(fromaddr, toaddr, text)

server.quit()
