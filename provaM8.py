import re

# Cria um dicionário de intenções
intencoes = {
    re.compile(r"\bcomo\b.*\batualizar\b.*\bmeu\b.*\bcartão\b.*\bde\b.*\bcrédito\b"): "atualizar pagamento",
    re.compile(r"\bpreciso\b.*\bmudar\b.*\bforma\b.*\bpagamento\b"): "atualizar pagamento",
    re.compile(r"\bquero\b.*\batualizar\b.*\bminhas\b.*\binformações\b.*\bpagamento\b"): "atualizar pagamento",
    re.compile(r"\bmétodo\b.*\bde\b.*\bpagamento\b.*\bdesatualizado\b"): "atualizar pagamento",
    re.compile(r"\bonde\b.*\bvejo\b.*\bstatus\b.*\bpedido\b"): "acompanhar pedido",
    re.compile(r"\bcomo\b.*\bfaço\b.*\bpara\b.*\brastrear\b.*\bpedido\b"): "acompanhar pedido",
    re.compile(r"\bquero\b.*\bsaber\b.*\bonde\b.*\bestá\b.*\bmeu\b.*\bpedido\b"): "acompanhar pedido",
    re.compile(r"\bstatus\b.*\bde\b.*\bentrega\b"): "acompanhar pedido",
}

# Cria um dicionário de ações
acoes = {
    "atualizar pagamento": "Para atualizar suas informações de pagamento, entre em contato com o nosso atendimento ao cliente.",
    "acompanhar pedido": "Para acompanhar o status do seu pedido, entre em contato com o nosso atendimento ao cliente.",
}

# Escreva uma função que recebe o comando do usuário
def get_comando():
    comando = input("Digite seu comando: ")
    return comando

# Utilize uma entrada de loop infinito que permite ao usuário digitar comandos repetidamente
while True:
    # Recebe o comando do usuário
    comando = get_comando()

    # Procura a intenção do usuário no dicionário de intenções
    for expressao_regular, intencao in intencoes.items():
        if expressao_regular.search(comando):
            # Encontramos a intenção do usuário
            # Exibe a resposta correspondente no dicionário de ações
            print(acoes[intencao])
            break

    # Se não encontramos a intenção do usuário, exibimos uma mensagem de erro
    else:
        print("Não entendi sua intenção.")
