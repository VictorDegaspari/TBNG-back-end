import time
from datetime import date, datetime

from apps.core.models import *
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Q


def log(msg):
    from datetime import datetime
    now = datetime.now()
    now = now.strftime("%Y-%m-%d %H:%M:%S")
    print(now + " " + msg)


while True:
    try:
        today = date.today()
        print(today)

        # EMAIL CASO EXISTA PREMIOS EXPIRADOS
        premio_expirado = Premio.objects.filter(Q(ativo=True) & Q(
            vigencia__contains=today))
        premio_expirado.update(ativo=False)

        premio = Premio.objects.filter(ativo=False)
        if len(premio) != 0:
            premio_id = []
            for i in range(len(premio)):
                premio_id.append(premio[i].id)
            send_mail('Hey Felipe, existem prêmios expirados', 'Segue abaixo o id do(s) prêmio(s): \n' + str(
                premio_id), settings.EMAIL_HOST_USER, ['vdegaspari.vm@gmail.com'], fail_silently=False)

        # EMAIL CASO EXISTA CLIENTES EXPIRADOS
        cliente_expirado = Cliente.objects.filter(
            Q(ativo=True) & Q(vencimento__contains=today))
        cliente_expirado.update(ativo=False)

        cliente = Cliente.objects.filter(ativo=False)
        if len(cliente) != 0:
            cliente_id = []
            for i in range(len(cliente)):
                cliente_id.append(cliente[i].id)
            send_mail('Hey Felipe, existem clientes expirados', 'Segue abaixo os id do(s) cliente(s): \n' + str(
                cliente_id), settings.EMAIL_HOST_USER, ['vdegaspari.vm@gmail.com'], fail_silently=False)

        log("Finalizado o processo batch de atualização de premios")
    except Exception as e:
        print("Erro durante processamento batch")
        print(e)
    finally:
        log("Aguardando 12 horas até a próxima chamada...")
        MINUTE = 60
        time.sleep(720 * MINUTE)
