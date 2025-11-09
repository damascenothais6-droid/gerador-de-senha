import random
import string   


def password_generator(Len_pass=8):
    ascii_options= string.ascii_letters + string.digits + string.punctuation
    options = list(ascii_options)
    
    password_user=  ""
    
    for i in range(0,Len_pass):
        digit= random.choice(options)
        password_user = password_user + digit
        
    return password_user
    
choice_user = input("Digite o tamanho da senha que deseja gerar: ")
    
if choice_user.isdigit():
        choice_user = int(choice_user)
else:
    
        print("Por favor, digite um número válido.")
        exit()
        
response = password_generator(Len_pass = choice_user)
print(f"Senha gerada: \n {response}")
    