# Documentação do Script de Limpeza de Dados em Planilha Excel

Este script foi desenvolvido para limpar e padronizar os códigos presentes em uma planilha Excel. Ele utiliza a biblioteca `pandas` do Python para manipulação de dados tabulares.

## Requisitos
- Python 3.x
- Biblioteca pandas

## Funcionamento do Script

1. **Importação da Biblioteca Pandas**
   - O script começa importando a biblioteca `pandas` sob o alias `pd`, que é amplamente utilizada para manipulação de dados em Python.

2. **Carregamento da Planilha Excel**
   - Utiliza a função `pd.read_excel()` para carregar a planilha Excel especificada no arquivo 'base.xlsx' e armazená-la em um DataFrame chamado `planilha`.

3. **Função de Limpeza de Código**
   - Define a função `limpar_codigo(codigo)` que recebe um código como entrada.
   - Remove espaços em branco à direita e à esquerda usando o método `.strip()`.
   - Verifica se o código é uma string e se consiste em um número usando `isdigit()`.
   - Se for um número, mantém os zeros à esquerda usando `zfill(len(codigo))`.
   - Retorna o código original se não for uma string.
   - Esta função será aplicada à coluna 'Código' da planilha.


4. **Aplicação da Função de Limpeza**
   - Utiliza o método `apply()` do DataFrame para aplicar a função `limpar_codigo()` à coluna 'Código' da planilha.

5. **Salvamento da Planilha Atualizada**
   - Finalmente, salva a planilha atualizada no arquivo 'base_atualizada.xlsx' utilizando o método `to_excel()` do DataFrame, com o parâmetro `index=False` para não incluir índices no arquivo.

## Como Usar
- Certifique-se de ter o Python instalado em seu ambiente.
- Instale a biblioteca pandas se ainda não a tiver instalado: `pip install pandas`.
- Coloque sua planilha Excel com os dados a serem limpos na mesma pasta que o script ou especifique o caminho correto para o arquivo Excel.
- Execute o script.

## Exemplo de Uso
python nome_do_script.py


Isso limpará os códigos na coluna 'Código' da planilha 'base.xlsx' e salvará a versão atualizada como 'base_atualizada.xlsx'.

Este documento fornece uma visão geral do funcionamento e uso do script de limpeza de dados em planilha Excel. Se houver dúvidas adicionais, consulte a documentação da biblioteca pandas ou entre em contato com o desenvolvedor.

