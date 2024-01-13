from django.db import models
from cryptography.fernet import Fernet, InvalidToken
# Create your models here.



class new_key:
# Criação das funções de criptografia
    def generate_keys(name_key):
        name_key = name_key + ".key"
        generated_key = Fernet.generate_key()
        with open(name_key, 'wb') as new_key:
            new_key.write(generated_key)