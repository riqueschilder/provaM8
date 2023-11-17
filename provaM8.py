import re

#icionário de intenções
intencoes = {
    re.compile("como atualizar meu cartão de crédito"): "atualizar pagamento",
    re.compile("preciso mudar a forma de pagamento"): "atualizar pagamento",
    re.compile("quero atualizar minhas informações de pagamento"): "atualizar pagamento",
    re.compile("método de pagamento desatualizado"): "atualizar pagamento",
    re.compile("onde vejo o status do meu pedido"): "acompanhar pedido",
    re.compile("como faço para rastrear meu pedido"): "acompanhar pedido",
    re.compile("quero saber onde está meu pedido"): "acompanhar pedido",
    re.compile("status de entrega"): "acompanhar pedido",
}

#dicionário de ações
acoes = {
    "atualizar pagamento": "Para atualizar suas informações de pagamento, entre em contato com o nosso atendimento ao cliente.",
    "acompanhar pedido": "Para acompanhar o status do seu pedido, entre em contato com o nosso atendimento ao cliente.",
}

# comando do usuário
def get_comando():
    comando = input("Digite seu comando: ")
    return comando

# loop
while True:
    # Recebe o comando do usuário
    comando = get_comando()

    # Procura a intenção do usuário no dicionário de intenções
    for expressao_regular, intencao in intencoes.items():
        if expressao_regular.match(comando):
            # Encontramos a intenção do usuário
            # Exibe a resposta correspondente no dicionário de ações
            print(acoes[intencao])
            break

    # mensagem de erro
    else:
        print("Não entendi sua intenção.")
