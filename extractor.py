import json
import PyPDF2
import re
import pkg_resources

# Defina uma função para ler o arquivo de dados com os nomes e valores dos exames
def read_data_file():
    # Use pkg_resources para ler o arquivo de dados como uma string
    data_string = pkg_resources.resource_string(__name__, 'exames.json')
    # Carregue os dados JSON da string e retorne-os
    return json.loads(data_string.decode())

def extractor(filename):
    # Defina uma função para extrair números de uma string usando uma expressão regular
    def extract_numbers(string):
        # Use uma regex para encontrar todos os números na string
        matches = re.findall(r'\b-?\d*\.?\d+(?:[,.]\d+)?\b', string)
        # Retorne os resultados como uma lista de floats
        return [float(match.replace(',', '.')) for match in matches]
    
    # Leia os dados dos exames do arquivo JSON
    exames = read_data_file()
    # Abra o arquivo PDF em modo de leitura binária
    with open(filename, 'rb') as file:
        # Crie um objeto PDF
        pdf = PyPDF2.PdfReader(file)
        # Inicialize uma string vazia para armazenar o texto de todas as páginas
        text = ''

        # Itere sobre as páginas do PDF
        for page_num in range(len(pdf.pages)):
            # Obtenha a página atual
            page = pdf.pages[page_num]
            # Extraia o texto da página e adicione-o ao texto total
            text = text + page.extract_text()
        
        # Inicialize uma string vazia para armazenar os dados dos exames extraídos
        substring = ''
        
        # Itere sobre os exames nos dados dos exames
        for a in range(len(exames)):
            # Encontre o índice do nome do exame no texto total
            start_index = text.find(exames[a][0][0])
            # Extraia uma substring do texto, começando no índice do nome do exame
            # e terminando depois do tamanho do nome do exame mais o número de caracteres especificados nos dados do exame
            midstring = text[start_index :start_index+len(exames[a][0][0])+ exames[a][1]]
            # Encontre o índice do valor do exame na substring
            result_index = midstring.find(exames[a][2])
            # Extraia o valor do exame da substring, começando do final da string de valor do exame e terminando depois do tamanho da string de valor do exame
# mais o número de caracteres especificados nos dados do exame
            endstring = midstring[result_index+len(exames[a][2]) :result_index+len(exames[a][2])+ exames[a][3]]
            # Use a função extract_numbers para obter o valor do exame
            g = extract_numbers(endstring)
            # Adicione o nome e o valor do exame à string de resultados, se um valor foi encontrado
            try:
                substring = substring + exames[a][0][1] + str(g[0]) + ' ' +exames[a][0][2] + ';'
            except:
                # Se ocorrer uma exceção (por exemplo, se nenhum valor foi encontrado), não faça nada
                substring = substring
        # Retorne a string de resultados
        return substring
