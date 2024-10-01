from pynfe.processamento.comunicacao import ComunicacaoSefaz
import time
import random

# Função que faz o programa "dormir" por um tempo aleatório entre 4 e 13 segundos
def sleep_random():
    fator_sleep = round(random.uniform(4, 13), 2)
    time.sleep(fator_sleep)

# Configuração do certificado digital e outras informações necessárias
certificado = 'C:\\pasta1\\pasta2\\1certificado.pfx'  # Caminho para o arquivo do certificado digital
senha_certificado = '123456'  # Senha do certificado digital
uf = 'mg'  # Unidade federativa (estado) onde o CNPJ está registrado
homologacao = False  # Define se o ambiente é de homologação (True) ou produção (False)

# Configuração do intervalo de números a serem inutilizados
range = 500  # Intervalo de números para inutilização em cada iteração
i = 1  # Contador de iterações

# Dados da inutilização
max_range = 4734920
cnpj = '00000000000000'  # CNPJ da empresa
numero_inicial = 1380  # Primeiro número da sequência a ser inutilizada
numero_final = numero_inicial + range  # Último número da sequência a ser inutilizada
justificativa = 'Quebra de sequência de numeração'  # Justificativa para a inutilização
ano = 2024  # Ano da inutilização
serie = '1'  # Série da NFe

# Loop para realizar inutilizações até que o número final seja atingido
while numero_final < max_range:

    #Condicional para não deixar o ultimo numero a ser inutilizado ultrapassar o valor maximo da inutilização 
    if numero_final > max_range:
        numero_final = max_range
    
    # Inicializa a comunicação com a SEFAZ usando as configurações fornecidas
    comunicacao = ComunicacaoSefaz(uf, certificado, senha_certificado, homologacao)

    # Envia a requisição de inutilização de numeração para a SEFAZ
    envio = comunicacao.inutilizacao(
        modelo='nfe',
        cnpj=cnpj,
        numero_inicial=numero_inicial,
        numero_final=numero_final,
        justificativa=justificativa,
        ano=ano,
        serie=serie
    )

    # Exibe a resposta da SEFAZ
    print('Resposta da SEFAZ:\n', envio.text)

    # Verifica se a inutilização foi homologada pela SEFAZ
    if 'Inutilizacao de Numero homologado' in envio.text:
        print(f"Inutilização realizada com sucesso: Inicial {numero_inicial} Final {numero_final} | {i}x")
        # Atualiza os números inicial e final para a próxima iteração
        numero_inicial = numero_final + 1
        numero_final = numero_inicial + range
        i = i + 1  # Incrementa o contador de iterações
        sleep_random()  # Suspende a execução por um tempo aleatório antes da próxima iteração
        print("\n")
    else:
        # Se houver erro, exibe uma mensagem e encerra o loop
        print(f"Erro na inutilização: conferir sequência {numero_inicial} a {numero_final}.")
        break