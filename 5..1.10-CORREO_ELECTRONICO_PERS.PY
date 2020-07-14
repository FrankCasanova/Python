# APLICACIÓN DE CORREO ELECTRÓNICO PERSONALIZADO

import smtplib
servidor = smtplib.SMTP('smtp.gmail.com', 587)


contraseña = 'tdtjllmbsljcjloe'

remitente = 'frankcasanova.info@gmail.com'

texto = 'Estimado =S =A: '
texto += 'Por la presente le informamos de que nos debe usted la '
texto += 'cantidad de =E euros. Si no abona dicha cantidad antes '
texto += 'de 3 dias, su nombre pasara a nuestra lista de morosos'

seguir = 's'

while seguir == 's':
    # input('Dirección de correo del destinatario: ')
    destinatario = 'frankcasanova.info@yahoo.com'
    tratamiento = 'Senior'  # input('Tratamiento: ')
    apellido = 'Casanova'  # input('Apellido: ')
    euros = '2'  # input('Deuda (en euros): ')

    mensaje = 'From: {0}\nTo: {1}\n\n'.format(remitente, destinatario)

    personalizado = ''

    i = 0

    while i < len(texto):
        if texto[i] != '=':
            personalizado += texto[i]
        else:
            if texto[i + 1] == 'A':
                personalizado += apellido
                i += 1
            elif texto[i + 1] == 'E':
                personalizado += euros
                i += 1
            elif texto[i + 1] == 'S':
                personalizado += tratamiento
                i += 1
            else:
                personalizado += '='
        i += 1
    mensaje += personalizado

    servidor.starttls()
    servidor.login(remitente, contraseña)
    servidor.sendmail(remitente, destinatario, mensaje)

    print('Correo enviado.')

    seguir = input('Si desea enviar otro correo pulse << s >>: ')
