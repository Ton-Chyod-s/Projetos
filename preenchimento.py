import os
import ezodf

for i in range(2):
    def pasta(caminho):
        pasta = caminho
        #verificar se a pasta existe se não existir ele ira criar
        if not os.path.exists(pasta):
            os.makedirs(pasta)
            
    pasta(os.path.abspath(f'acm{i}'))                                
                                    
    # Carregar o arquivo existente
    doc = ezodf.opendoc(os.path.abspath('termo aditivo ACS p ACM.odt'))

    # Acessar o conteúdo do documento
    content = doc.body

    # Editar o conteúdo
    paragraphs = [p for p in content if isinstance(p, ezodf.Paragraph)]
    paragraphs[0].text = 'Este é um exemplo de edição de ODT usando Python.'

    # Salvar as alterações
    doc.save(os.path.abspath(f'acm{i}//termo aditivo ACS p ACM.odt', pretty=True))