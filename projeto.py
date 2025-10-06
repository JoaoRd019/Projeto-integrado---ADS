# sistema de gestao de clientes
# classe paciente
class Paciente:
    def __init__(self, nome, idade, telefone):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
    
    def __repr__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"

# lista de pacientes
pacientes = []

# funcoes para cadastrar/ ver estatisticas/ buscar pacientes / listar pacientes
def cadastrar_pacientes():
    print("\n--Cadastro de Pacientes--")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    telefone = input("Telefone: ")
    pacientes.append(Paciente(nome, idade, telefone))

def ver_estatisticas():
    if pacientes:
        total_pacientes = len(pacientes)
        idade_total = sum(p.idade for p in pacientes)
        idade_media = idade_total / total_pacientes
        
        print("\n-- Estatísticas dos Pacientes --")
        print(f"Total de pacientes cadastrados: {total_pacientes}")
        print(f"Idade média dos pacientes: {idade_media:.2f} anos")
        
        # Ordenar por idade
        pacientes_ordenados = sorted(pacientes, key=lambda p: p.idade)
        
        print("\nLista de pacientes ordenada por idade:")
        for paciente in pacientes_ordenados:
            print(f"  - {paciente.nome}, {paciente.idade} anos, Tel: {paciente.telefone}")
    else:
        print("\nNenhum paciente cadastrado.")

def buscar_paciente():
    print("\n-- Buscar Paciente --")
    nome = input("Digite o nome do paciente: ")
    encontrado = False
    for paciente in pacientes:
        if paciente.nome == nome:
            print(f"Paciente {nome} está cadastrado")
            print(f"Idade: {paciente.idade}")
            print(f"Telefone: {paciente.telefone}")
            encontrado = True
    if not encontrado:
        print("Paciente não encontrado")

def listar_pacientes():
    print("\n--- Pacientes na lista ---")
    if not pacientes:
        print("Nenhum paciente cadastrado.")
    else:
        for paciente in pacientes:
            print(f"Nome: {paciente.nome} | Idade: {paciente.idade} | Telefone: {paciente.telefone}")

# menu simples de navegação
while True:
    print("\nSISTEMA CLÍNICA VIDA+ ")
    print("1. Cadastrar paciente")
    print("2. Ver estatísticas")
    print("3. Buscar paciente")
    print("4. Listar todos os pacientes")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_pacientes()
    elif opcao == "2":
        ver_estatisticas()
    elif opcao == "3":
        buscar_paciente()
    elif opcao == "4":
        listar_pacientes()
    elif opcao == "5":
        print("Programa encerrado")
        break