import json
import PyPDF2
import re

def extractor(filename):
    def extract_numbers(string):
        # Use a regex to find all the numbers in the string
        matches = re.findall(r'\b-?\d*\.?\d+(?:[,.]\d+)?\b', string)
        # Return the matches as a list of floats
        return [float(match.replace(',', '.')) for match in matches]
    # Abre o arquivo PDF em modo de leitura binária
    with open("exames.json", "r") as f:
        exames = json.load(f)

    with open(filename, 'rb') as file:
        # Cria um objeto PDF
        pdf = PyPDF2.PdfReader(file)
        text = ''

        # Itera pelas páginas do PDF
        for page_num in range(len(pdf.pages)):
            # Obtém a página
            page = pdf.pages[page_num]

            # Extrai o texto da página
            text = text + page.extract_text()

        substring = ''
        #print(text)
        # Itera pela lista de exames
        for a in range(len(exames)):
            # Localiza o nome do exame na string de texto
            start_index = text.find(exames[a][0][0])

            # Extrai uma substring a partir do índice de início do nome do exame
            # até o tamanho do nome do exame mais o número de caracteres especificado na lista de exames
            midstring = text[start_index :start_index+len(exames[a][0][0])+ exames[a][1]]

            result_index = midstring.find(exames[a][2])

            endstring = midstring[result_index+len(exames[a][2]) :result_index+len(exames[a][2])+ exames[a][3]]

            #print( endstring)

            g = extract_numbers(endstring)


            try:
                substring = substring + exames[a][0][1] + str(g[0]) + ' ' +exames[a][0][2] + ';'
            except:
                substring = substring
            #print(g)
        #converte a lista em uma lista de listas

        return(substring)  

#extractor('document2.pdf')