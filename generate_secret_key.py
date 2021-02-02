from django.core.management.utils import get_random_secret_key
secret_key = get_random_secret_key()
with open('.env', 'w+') as arq:
    dados = 'SECRET_KEY=%s'%secret_key
    arq.write(dados)