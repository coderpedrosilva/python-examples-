# Descrição: Exemplos avançados de Python para aprofundamento

# 1. Geradores (Generators) e Yield
# Geradores economizam memória pois produzem valores sob demanda

def gerador_numeros(limite):
    numero = 0
    while numero < limite:
        yield numero  # Mantém o estado da função
        numero += 1

meu_gerador = gerador_numeros(5)
for num in meu_gerador:
    print("Número gerado:", num)

# 2. Expressões Geradoras (Generator Expressions)
numeros_quadrados = (x**2 for x in range(5))
print("Quadrados gerados:", list(numeros_quadrados))

# 3. Metaprogramação com Metaclasses
class MinhaMeta(type):
    def __new__(cls, nome, bases, dct):
        print(f"Criando classe {nome}")
        return super().__new__(cls, nome, bases, dct)

class MinhaClasse(metaclass=MinhaMeta):
    def __init__(self, valor):
        self.valor = valor

obj = MinhaClasse(10)

# 4. Manipulação Avançada de JSON
import json
from json.decoder import JSONDecodeError

dados = '{"nome": "João", "idade": 30}'  # JSON em formato de string
try:
    dados_dict = json.loads(dados)
    print("JSON convertido:", dados_dict)
except JSONDecodeError as e:
    print("Erro ao decodificar JSON:", e)

# 5. Multiprocessamento para Paralelismo
import multiprocessing
import time

def tarefa_multiprocessos():
    print("Iniciando processo...")
    time.sleep(2)
    print("Processo finalizado!")

if __name__ == "__main__":
    processo = multiprocessing.Process(target=tarefa_multiprocessos)
    processo.start()
    processo.join()
    print("Execução paralela concluída!")

# 6. Uso de Asyncio para Programação Assíncrona
import asyncio

async def minha_tarefa():
    print("Iniciando tarefa assíncrona...")
    await asyncio.sleep(2)
    print("Tarefa assíncrona concluída!")

async def main():
    await asyncio.gather(minha_tarefa(), minha_tarefa())

asyncio.run(main())

# 7. Context Manager Personalizado
class MeuContexto:
    def __enter__(self):
        print("Entrando no contexto...")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Saindo do contexto...")

with MeuContexto():
    print("Executando dentro do bloco 'with'...")

# 8. Operações com Memória Compartilhada
from multiprocessing import Value

contador = Value('i', 0)  # Inteiro compartilhado entre processos

def incrementar():
    with contador.get_lock():  # Garante acesso exclusivo
        contador.value += 1

processos = [multiprocessing.Process(target=incrementar) for _ in range(5)]

for p in processos:
    p.start()
for p in processos:
    p.join()

print("Valor final do contador:", contador.value)
