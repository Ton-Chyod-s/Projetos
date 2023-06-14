import os
from docx import Document

for i in range(2):
    def pasta(caminho):
        pasta = caminho
        #verificar se a pasta existe se não existir ele ira criar
        if not os.path.exists(pasta):
            os.makedirs(pasta)
            
    pasta(os.path.abspath(f'acm{i}'))                                
                                    
    # Carregar o arquivo existente
    doc = Document(os.path.abspath('termo aditivo ACS p ACM.docx'))

    # Acessar o conteúdo do documento
    paragraphs = doc.paragraphs

    # Editar o conteúdo
    paragraphs[3].text = 'Eu, (nome ou nome social), CPF ______________, carteira de identificação nº _________, emitida em _________, órgão emissor __________, aprovado e classificado em Processo Seletivo Simplificado, para os trabalhos do CENSO DEMOGRÁFICO 2022, para exercer a função de 	AGENTE CENSITÁRIO SUPERVISOR, sob a matrícula ___________.'

    # Salvar as alterações
    doc.save(os.path.abspath(f'acm{i}//termo aditivo ACS p ACM.docx'))