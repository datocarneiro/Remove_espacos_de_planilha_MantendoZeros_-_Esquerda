import pandas as pd

# Carregar a planilha do Excel
planilha = pd.read_excel('base.xlsx')

# Função para remover espaços à direita e à esquerda e manter os zeros à esquerda nos números
def limpar_codigo(codigo):
    if isinstance(codigo, str):  # Verifica se é uma string
        codigo = codigo.strip()  # Remove espaços em branco no início e no fim
        if codigo.isdigit():  # Verifica se é um número
            return codigo.zfill(len(codigo))  # Mantém os zeros à esquerda
        else:
            return codigo
    else:
        return codigo  # Retorna o valor original se não for uma string

# Aplicar a função à coluna 'Código'
planilha['Código'] = planilha['Código'].apply(limpar_codigo)

# Salvar a planilha atualizada
planilha.to_excel('base_atualizada.xlsx', index=False)
