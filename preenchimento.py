from odf import text, teletype
from odf.opendocument import load
import os

for i in range(2):
    def pasta(caminho):
        pasta = caminho
        #verificar se a pasta existe se não existir ele ira criar
        if not os.path.exists(pasta):
            os.makedirs(pasta)
            
    pasta(os.path.abspath(f'acm{i}'))                                
                                    
    # Carregar o arquivo existente
    doc = load(os.path.abspath('termo aditivo ACS p ACM.odt'))

    # Acessar o conteúdo do documento
    content = doc.text

    # Editar o conteúdo
    paragraphs = content.getElementsByType(text.P)
    paragraphs[0].childNodes[0].nodeValue = 'Este é um exemplo de edição de ODT usando Python.'

    # Salvar as alterações
    doc.save(os.path.abspath(f'acm{i}//termo aditivo ACS p ACM.odt'))