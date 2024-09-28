# Definindo a estrutura inicial dos usuários e atividades
usuarios = ["residente1", "tutor1"]
atividades = [
    "login", "criar_usuario", "acompanhar_historico", "liberar_usuario",
    "simular_atividades", "simular_tutorial", "simular_suturas", 
    "simular_perspectiva", "simular_cortes_cirurgicos", "finalizar_simulacao"
]

# Armazenar simulações e resultados intermediários
simulacoes_usuarios = {}

# Função para realizar o login do usuário
def realizar_login(usuario):
    if usuario in usuarios:
        print(f"{usuario} fez login com sucesso.")
        return True
    else:
        print(f"Usuário {usuario} não encontrado.")
        return False

# Função para iniciar uma simulação e armazenar as etapas
def iniciar_simulacao(usuario, atividade):
    if usuario not in simulacoes_usuarios:
        simulacoes_usuarios[usuario] = []  # Inicializa uma lista de simulações para o usuário
    
    nova_simulacao = ["login", atividade]
    simulacoes_usuarios[usuario].append(nova_simulacao)
    print(f"Simulação iniciada para o usuário {usuario} com a atividade '{atividade}'.")

# Função para adicionar uma atividade a uma simulação existente
def adicionar_atividade(usuario, atividade):
    if usuario in simulacoes_usuarios and len(simulacoes_usuarios[usuario]) > 0:
        simulacoes_usuarios[usuario][-1].append(atividade)
        print(f"Atividade '{atividade}' adicionada à simulação do usuário {usuario}.")
    else:
        print(f"Não há simulação em andamento para o usuário {usuario}.")

# Função para finalizar uma simulação
def finalizar_simulacao(usuario):
    if usuario in simulacoes_usuarios and len(simulacoes_usuarios[usuario]) > 0:
        simulacoes_usuarios[usuario][-1].append("finalizar_simulacao")
        print(f"Simulação finalizada para o usuário {usuario}.")
    else:
        print(f"Não há simulação em andamento para o usuário {usuario}.")

# Função para criar um novo usuário
def criar_usuario(usuario_novo):
    if usuario_novo not in usuarios:
        usuarios.append(usuario_novo)
        print(f"Usuário '{usuario_novo}' criado com sucesso.")
    else:
        print(f"Usuário '{usuario_novo}' já existe.")

# Função para acompanhar o histórico de simulações de um usuário
def acompanhar_historico(usuario):
    if usuario in simulacoes_usuarios:
        print(f"Histórico de simulações para o usuário {usuario}:")
        for index, simulacao in enumerate(simulacoes_usuarios[usuario], start=1):
            print(f"  Simulação {index}: {simulacao}")
    else:
        print(f"Não há histórico para o usuário {usuario}.")

# Função para liberar um usuário para novas simulações
def liberar_usuario(usuario):
    if usuario in simulacoes_usuarios:
        simulacoes_usuarios[usuario].clear()
        print(f"Usuário {usuario} liberado para novas simulações.")
    else:
        print(f"Não há simulações registradas para o usuário {usuario}.")

# Exemplos de uso:
# Realizando login para um usuário
realizar_login("residente1")

# Criando um novo usuário
criar_usuario("residente2")

# Iniciando uma simulação para um usuário
iniciar_simulacao("residente1", "simular_tutorial")

# Adicionando uma atividade a uma simulação em andamento
adicionar_atividade("residente1", "simular_perspectiva")

# Finalizando uma simulação
finalizar_simulacao("residente1")

# Acompanhando o histórico de simulações para um usuário
acompanhar_historico("residente1")

# Liberando o usuário para novas simulações
liberar_usuario("residente1")

# Exibindo resultados de todas as simulações realizadas
print("\nSimulações realizadas:")
for usuario, simulacoes in simulacoes_usuarios.items():
    print(f"Usuário: {usuario}")
    for simulacao in simulacoes:
        print(f"  Simulação: {simulacao}")
