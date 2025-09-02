import random

# Definindo as listas de caracteres
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Combinando todas as listas
all_characters = letters + numbers + symbols

# Pedindo ao usuário o tamanho da senha
try:
    password_length = int(input("Qual o tamanho da senha desejada? "))
except ValueError:
    print("Por favor, digite um número válido.")
    exit()

# Gerando a senha
password = []
for _ in range(password_length):
    password.append(random.choice(all_characters))

# Misturando a lista para garantir mais aleatoriedade
random.shuffle(password)

# Juntando os caracteres e imprimindo a senha final
final_password = "".join(password)
print(f"Sua nova senha é: {final_password}")
