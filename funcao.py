from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

#caminho para os arquivo anexo
os.chdir(r'C:\Hix_x\Área de Trabalho\ProjetosGit')


    
def enviar_email_2(assunto, mensagem, arquivo, para,de,senha):  
        msg = MIMEMultipart()
        msg['Subject'] = assunto
        msg['From'] = de
        msg['To'] = para

        # inicio do email
        msg.preamble = 'Multipart massage.\n'
        msg.attach(MIMEText(mensagem))

        # adicionando anexo
        pdfname = arquivo
        binary_pdf = open(pdfname, 'rb')
        payload = MIMEBase('application', 'octate-stream', Name=pdfname)
        payload.set_payload((binary_pdf).read())
        encoders.encode_base64(payload)
        payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
        msg.attach(payload)

        # montando email no SMTP server
        smtp = SMTP('smtp.gmail.com', 587)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(de, senha)
        
        # enviar email
        smtp.sendmail(msg['From'], msg['To'], msg.as_string())

# teste da função para envio de e-mail com anexo 
  
if __name__ == "__main__":
    remetente_ = '##' #email de remetente
    senha = '##' #senha de 16 digito google
    lista_emails = [  
        '##'
        ] #lista de email para envio
    assunto_email = '##' #assunto email
    corpo = 'Olá, tudo bem ?\nTeste de envio de e-mail!!'


    for emails in lista_emails:
        enviar_email_2(assunto_email, corpo, 'Arquivo.pdf', emails, remetente_, senha)
        
        