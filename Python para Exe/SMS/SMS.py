
# %% [markdown]
# # Python para exe com códigos simples
# 
# ### Códigos que não interagem com outros arquivos ou ferramentas do computador
# 
# Usaremos a biblioteca pyinstaller
# 
# - Passo 1 - Instalar o pyinstaller
# 
# - Passo 2 - Executar o pyinstaller
# 
# pyinstaller -w nome_do_programa.py

# %%
from twilio.rest import Client

account_sid = 'AC241230583f6368a2ef9c7d6e7832be4c'
token = '58e9337a4d0464d438357ab846d51084'

client = Client(account_sid, token)

remetente = '+12292672666'
destino = '+5531998648054'

message = client.messages.create(
    to = destino,
    from_ = remetente,
    body = 'Salve'              )

print(message.sid)

# %% [markdown]
# ### Atenção no resultado
# 
# Repare que o programa final vai ficar extremamente pesado.
# 
# Isso porque o pyinstaller vai incluir todas as bibliotecas que temos instaladas no programa final, para garantir que ele vai funcionar.
# 
# Para evitar isso, precisaremos criar um ambiente virtual exclusivo para esse programa, vamos ver na prática como funciona na próxima aula

# %% [markdown]
# ### Observações Úteis
# 
# - Se o nome do seu arquivo .py tiver mais de uma palavra, na hora de testar, coloque o nome dele entre aspas duplas.<br>Ex:  python "Gabarito - SMS.py"
# - Se o seu antivírus verificar o pyinstaller, não precisa se preocupar, é normal e tá tudo certo
# - Provavelmente a 1ª vez que você rodar o seu programa, o antivírus vai verificar ele também
# - A pasta dist é o que pode ser distribuído. Você pode compactar ela em um zip e mandar para quem você quiser


