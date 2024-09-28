
# Simulador de Atividades Médicas com Realidade Virtual (VR)

## Descrição do Projeto

Este projeto é uma aplicação desenvolvida para simular atividades médicas usando técnicas de Realidade Virtual (VR) e Realidade Aumentada (AR). O projeto foi criado para auxiliar na formação de residentes médicos, permitindo a prática de procedimentos como suturas, cortes cirúrgicos e atividades de pinça em um ambiente controlado e supervisionado por tutores.

O simulador inclui um portal de controle, no qual tutores e residentes podem realizar login, gerenciar usuários, acompanhar o histórico de simulações e liberar usuários para novas atividades. As simulações são realizadas utilizando óculos de VR, proporcionando uma experiência imersiva e interativa para os usuários.

## Funcionalidades

1. **Portal de Controle**:
   - Fazer login.
   - Criar novo usuário.
   - Acompanhar histórico de simulações.
   - Liberar usuário para novas atividades.

2. **Simulação de Atividades Médicas**:
   - Simular atividades de treinamento com tutoriais.
   - Simular suturas e cortes cirúrgicos.
   - Praticar habilidades com simulação de perspectiva e atividades de pinça.

3. **Gestão de Usuários**:
   - Criação de novos usuários (residentes e tutores).
   - Armazenamento e acompanhamento das simulações realizadas por cada usuário.

## Estrutura de Dados Utilizada

O projeto utiliza matrizes e listas para armazenar os dados das simulações e das interações dos usuários. Cada simulação é representada por uma matriz, onde as linhas representam as etapas e as colunas representam as atividades executadas em cada etapa.

Exemplo de estrutura para armazenamento das atividades:

```python
simulacoes_usuarios = {
    "usuario_id_1": [
        ["login", "iniciar_simulacao", "simular_suturas", "finalizar_simulacao"],  # Simulação 1
        ["login", "iniciar_simulacao", "simular_cortes_cirurgicos", "finalizar_simulacao"],  # Simulação 2
    ],
    "usuario_id_2": [
        ["login", "iniciar_simulacao", "simular_perspectiva", "finalizar_simulacao"],  # Simulação 1
    ]
}
```

## Implementação

O código é implementado em Python e consiste nas seguintes funções principais:

1. **realizar_login(usuario)**:
   - Verifica se o usuário está cadastrado no sistema e realiza o login.

2. **criar_usuario(usuario_novo)**:
   - Adiciona um novo usuário ao sistema, caso ainda não exista.

3. **iniciar_simulacao(usuario, atividade)**:
   - Inicia uma nova simulação para o usuário com a atividade escolhida.

4. **adicionar_atividade(usuario, atividade)**:
   - Adiciona uma nova atividade à simulação em andamento.

5. **finalizar_simulacao(usuario)**:
   - Finaliza a simulação atual para o usuário.

6. **acompanhar_historico(usuario)**:
   - Exibe o histórico de simulações realizadas por um usuário.

7. **liberar_usuario(usuario)**:
   - Limpa o histórico de simulações do usuário, permitindo que ele inicie novas simulações.

## Estrutura do Repositório

- **simulador.py**: Contém as funções principais para simulação das atividades.
- **README.md**: Documentação do projeto.
- **requirements.txt**: Dependências do projeto (se necessário).
- **/docs**: Documentação adicional e arquivos auxiliares.

## Tecnologias Utilizadas

- **Python**: Linguagem principal para implementação das funções.
- **Matrizes e Listas**: Para armazenamento de dados das simulações.
- **GitHub**: Controle de versão e repositório.

## Autores

rm551973 - henrique parra 
rm97674 - guilherme barreto 
rm98939 - nicolas oliveira 
rm550667 - tony 
rm551460 - roberto oliveira
