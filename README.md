# Descrição do Projeto

Este projeto em Python foi desenvolvido para realizar a inutilização de numerações de Notas Fiscais Eletrônicas (NFe) modelo 55 na Receita Federal de forma automatizada e contínua. O programa utiliza a biblioteca `PyNFe` para se comunicar com os servidores da SEFAZ e inutilizar intervalos de numerações de NFe, especificando CNPJ, série, ano, e justificativa.

## Funcionalidades Principais

- **Inutilização de Numeração:** O programa realiza a inutilização de blocos de números de NFe em um loop contínuo, até que o valor máximo especificado seja atingido.
  
- **Intervalo Aleatório entre Requisições:** A função `sleep_random` foi implementada para adicionar um intervalo de espera aleatório entre as inutilizações, variando de 4 a 13 segundos. Essa técnica foi adotada para evitar a detecção de bot pela Receita Federal, simulando um comportamento humano.

- **Configuração Flexível:** O intervalo de numeração para cada inutilização (`range`) está configurado atualmente para 500, mas testes mostraram que é possível aumentar esse valor para até 585 sem problemas. 

- **Manutenção de Sequência:** A cada iteração, o programa ajusta automaticamente os números inicial e final para a próxima inutilização, garantindo a continuidade do processo.

## Considerações Importantes

- **Verificação na Última Inutilização:** O loop principal do programa (`while numero_final < 4734920`) contém uma potencial questão na última execução, onde o intervalo de 500 pode ultrapassar o valor de `4734920`. Isso pode fazer com que a última inutilização falhe, necessitando uma verificação manual para ajustar o intervalo final.

## Exemplo de Uso

Ao executar o script, ele se conectará aos servidores da SEFAZ, enviará as requisições de inutilização conforme configurado, e aguardará uma resposta. Em caso de sucesso, o script continuará para o próximo bloco de números, pausando por um intervalo aleatório antes de proceder.

## Requisitos

- Python 3.x
- Biblioteca `PyNFe`
- Certificado digital (arquivo `.pfx`) e senha

## Instruções de Uso

1. Clone o repositório.
2. Configure o caminho do certificado digital e a senha no script.
3. Ajuste os parâmetros de inutilização conforme necessário.
4. Execute o script para iniciar o processo de inutilização.
Obs: Em produção.