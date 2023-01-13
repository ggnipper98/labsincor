import json
import PyPDF2
import re
from parser.exames import *



def extractor(filename):
    # Define uma função para extrair números de uma string usando uma expressão regular
    def extract_numbers(string):
        # Usa uma regex para encontrar todos os números na string
        matches = re.findall(r'\b-?\d*\.?\d+(?:[,.]\d+)?\b', string)
        # Retorna os resultados como uma lista de floats
        return [float(match.replace(',', '.')) for match in matches]
    
    # Abre o arquivo PDF em modo de leitura binária
    with open(filename, 'rb') as file:
        # Cria um objeto PDF
        pdf = PyPDF2.PdfReader(file)
        # Inicializa uma string vazia para armazenar o texto de todas as páginas
        text = ''

        # Itera sobre as páginas do PDF
        for page_num in range(len(pdf.pages)):
            # Obtem a página atual
            page = pdf.pages[page_num]
            # Extrai o texto da página e adicione-o ao texto total
            text = text + page.extract_text()
        
        # Inicializa uma string vazia para armazenar os dados dos exames extraídos
        substring = ''

        #extrai a data e coloca na string

        matriz_data = [["Liberado em", ""], 16]
        data_index = text.find(matriz_data[0][0])
        data_text = text[data_index + len(matriz_data[0][0]) + 2:data_index+len(matriz_data[0][0])+ matriz[0][1]]
        try:
            substring = substring + data_text + ": "
        except:
            substring = substring
        # Itera sobre os exames nos dados dos exames
        for a in range(len(matriz)):
            # Encontra o índice do nome do exame no texto total
            start_index = text.find(matriz[a][0][0])
            # Extrai uma substring do texto, começando no índice do nome do exame
            # e terminando depois do tamanho do nome do exame mais o número de caracteres especificados nos dados do exame
            midstring = text[start_index :start_index+len(matriz[a][0][0])+ matriz[a][1]]
            # Encontra o índice do valor do exame na substring
            result_index = midstring.find(matriz[a][2])
            # Extrai o valor do exame da substring, começando do final da string de valor do exame e terminando depois do tamanho da string de valor do exame
# mais o número de caracteres especificados nos dados do exame
            endstring = midstring[result_index+len(matriz[a][2]) :result_index+len(matriz[a][2])+ matriz[a][3]]
            # Use a função extract_numbers para obter o valor do exame
            g = extract_numbers(endstring)
            # Adiciona o nome e o valor do exame à string de resultados, se um valor foi encontrado
            try:
                substring = substring + matriz[a][0][1] + str(g[0]) + ' ' +matriz[a][0][2] + ';'
            except:
                # Se ocorrer uma exceção (por exemplo, se nenhum valor foi encontrado), não faça nada
                substring = substring
        # Retorna a string de resultados
        return substring
