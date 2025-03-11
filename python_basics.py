# Descrição: Código básico para relembrar sintaxe do Python

# 1. Variáveis e Tipos de Dados
nome = "João"  # String
idade = 25      # Inteiro
altura = 1.75   # Float
ativo = True    # Booleano

# Exibindo valores
print(f"Nome: {nome}, Idade: {idade}, Altura: {altura}, Ativo: {ativo}")

# 2. Entrada e Saída de Dados
nome_usuario = input("Digite seu nome: ")  # Captura entrada do usuário
print("Olá,", nome_usuario)  # Exibe mensagem formatada

# 3. Estruturas Condicionais
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você é maior de idade.")
elif idade >= 16:
    print("Você pode votar, mas não dirigir.")
else:
    print("Você é menor de idade.")

# 4. Laços de Repetição
# While
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1  # Incremento

# For com range
for i in range(5):  # De 0 a 4
    print("Número:", i)

# 5. Listas e Dicionários
frutas = ["maçã", "banana", "laranja"]  # Lista
print(frutas[1])  # Acessa "banana"
frutas.append("uva")  # Adiciona "uva"

pessoa = {"nome": "Ana", "idade": 30, "cidade": "São Paulo"}  # Dicionário
print(pessoa["nome"])  # Acessa "Ana"

# 6. Funções
def saudacao(nome):
    print("Olá,", nome)

saudacao("Carlos")

def soma(a, b):
    return a + b

resultado = soma(3, 5)
print("Soma:", resultado)

# 7. Manipulação de Arquivos
# Escrever em um arquivo
with open("arquivo.txt", "w") as arquivo:
    arquivo.write("Olá, mundo!")

# Ler de um arquivo
with open("arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo do arquivo:", conteudo)

# 8. Tratamento de Erros
try:
    x = int(input("Digite um número: "))
    print(10 / x)
except ZeroDivisionError:
    print("Não pode dividir por zero!")
except ValueError:
    print("Entrada inválida! Digite um número.")
