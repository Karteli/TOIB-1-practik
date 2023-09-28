import getpass
import hashlib
parol = getpass.getpass(prompt="Напишите пароль: ")
parol = hashlib.sha256(parol.encode('utf-8')).hexdigest()
print('Hash parol = ',parol)

