# python_intermediario.py

# 1. List Comprehension (Criação rápida de listas)
numeros = [x for x in range(10)]  # Lista de 0 a 9
quadrados = [x**2 for x in numeros]  # Quadrados dos números
print("Lista de números:", numeros)
print("Lista de quadrados:", quadrados)

# 2. Funções com Argumentos Opcionais e Padrões
def saudacao(nome, mensagem="Olá"):
    print(f"{mensagem}, {nome}!")

saudacao("Carlos")  # Usa mensagem padrão
saudacao("Ana", "Bom dia")  # Mensagem personalizada

# 3. Funções Lambda (Funções anônimas curtas)
soma = lambda a, b: a + b
print("Soma de 3 + 5:", soma(3, 5))

# 4. Manipulação de Arquivos JSON
import json

dados = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

# Salvar em um arquivo JSON
with open("dados.json", "w") as arquivo:
    json.dump(dados, arquivo)

# Ler um arquivo JSON
with open("dados.json", "r") as arquivo:
    dados_lidos = json.load(arquivo)
    print("Dados lidos do JSON:", dados_lidos)

# 5. Uso de Decorators (Funções que modificam outras funções)
def meu_decorator(funcao):
    def wrapper():
        print("Executando antes da função principal...")
        funcao()
        print("Executando depois da função principal...")
    return wrapper

@meu_decorator
def minha_funcao():
    print("Essa é a função principal.")

minha_funcao()

# 6. Programação Orientada a Objetos (POO)
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

pessoa1 = Pessoa("Alice", 28)
pessoa1.apresentar()

# 7. Tratamento de Erros Avançado
try:
    with open("arquivo_inexistente.txt", "r") as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print("Arquivo não encontrado!")
except Exception as erro:
    print(f"Ocorreu um erro inesperado: {erro}")
finally:
    print("Bloco finally executado sempre.")

# 8. Uso de Threads para Paralelismo
import threading
import time

def tarefa():
    print("Iniciando tarefa...")
    time.sleep(2)
    print("Tarefa concluída!")

thread1 = threading.Thread(target=tarefa)
thread1.start()
thread1.join()

print("Código finalizado!")
