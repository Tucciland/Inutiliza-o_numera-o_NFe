from pynfe.processamento.comunicacao import ComunicacaoSefaz
import time
import random

def sleep_random():
    fator_sleep = round(random.uniform(4, 13), 2)
    time.sleep(fator_sleep)

certificado = 'C:\\pasta1\\pasta2\\1certificado.pfx'
senha_certificado = '123456'
uf = 'mg'
homologacao = False

range = 500
i=1

cnpj = '00000000000000'
numero_inicial = 1380
numero_final = numero_inicial + range
justificativa = 'Quebra de sequência de numeração'
ano = 2024
serie = '1'

while numero_final < 4734920:
    comunicacao = ComunicacaoSefaz(uf, certificado, senha_certificado, homologacao)

    envio = comunicacao.inutilizacao(
        modelo='nfe',
        cnpj=cnpj,
        numero_inicial=numero_inicial,
        numero_final=numero_final,
        justificativa=justificativa,
        ano=ano,
        serie=serie
    )

    #print('Resposta da SEFAZ:\n', envio.text)

    if 'Inutilizacao de Numero homologado' in envio.text:
        print(f"Inutilização realizada com sucesso: Inicial {numero_inicial} Final {numero_final} | {i}x")
        numero_inicial = numero_final + 1
        numero_final = numero_inicial + range
        i=i+1
        sleep_random()
        print("\n")
    else:
        print(f"Erro na inutilização: conferir sequência {numero_inicial} a {numero_final}.")
        break