import json
import PyPDF2

def extractor(filename):
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
        print(text)
        # Itera pela lista de exames
        for a in range(len(exames)):
            # Localiza o nome do exame na string de texto
            start_index = text.find(exames[a][0][0])

            # Extrai uma substring a partir do índice de início do nome do exame
            # até o tamanho do nome do exame mais o número de caracteres especificado na lista de exames
            midstring = text[start_index :start_index+len(exames[a][0][0])+ exames[a][1]]

            # Divide a substring em uma lista de palavras
            midstring = midstring.split()
            print(midstring)
            try:
                substring = substring + exames[a][0][1] + midstring[-2] + ' '+ midstring[-1] + ';'
            except:
                substring = substring
        #converte a lista em uma lista de listas


        print(substring)  

extractor('document2.pdf')