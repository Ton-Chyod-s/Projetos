# Projetos

O código apresentado é um script em Python que realiza algumas operações com arquivos XML e planilhas XLSX.

Aqui está uma descrição do que o código faz:

Importa as bibliotecas necessárias: sleep para adicionar pausas no script, load_workbook do openpyxl para lidar com planilhas XLSX, PySimpleGUI para exibir pop-ups, xml.etree.ElementTree para manipular arquivos XML, random para gerar números aleatórios, shutil para operações de arquivo, e os para operações do sistema.

Verifica se os arquivos necessários, "coordenada.xlsx" e "roteiro.xlsx", estão presentes na pasta. Caso contrário, exibe uma mensagem de pop-up informando os arquivos ausentes.

Define uma função pasta que cria uma pasta se ela não existir, utilizando o caminho fornecido.

Cria várias pastas usando a função pasta, para organizar os arquivos que serão gerados posteriormente.

Inicia um loop de repetição que itera de 2 a 401 (400 vezes).

Dentro do loop, recupera os valores das células na planilha "coordenada.xlsx" e "roteiro.xlsx" para as variáveis correspondentes.

Verifica se as coordenadas são nulas. Se forem nulas, o loop é interrompido.

Verifica se o campo de CEP no arquivo "coordenada.xlsx" está vazio. Se estiver vazio, o valor de CEP é obtido de outra célula.

Recupera os valores das células nas planilhas "coordenada.xlsx" e "roteiro.xlsx" para outras variáveis correspondentes.

Executa uma sequência de condicionais para determinar o tipo de construção a ser criada: casa, casa com casas secundárias ou prédio.

Para o caso de construção de uma casa, o código lê um arquivo XML de modelo ("hp.xml"), substitui os valores relevantes e grava um novo arquivo XML. Em seguida, o arquivo XML é compactado em um arquivo zip usando a biblioteca shutil. O arquivo XML original é excluído.

Para o caso de construção de uma casa com casas secundárias, o código lê um arquivo XML de modelo ("hp2.xml") e itera sobre a quantidade de casas secundárias. Para cada casa secundária, o código realiza operações semelhantes às descritas no passo 11.

Para o caso de construção de um prédio, o código lê dois arquivos XML de modelo ("arquivo.xml" e "apartamento.xml"). Ele gera um número aleatório para o nome do arquivo ZIP, substitui os valores relevantes nos arquivos XML e grava os arquivos XML correspondentes. Em seguida, o código movimenta o último arquivo XML gerado para uma pasta específica e realiza outras operações para modificar o XML principal. Por fim, o XML principal é gravado em um arquivo e compactado em um arquivo ZIP. Os arquivos XML originais são excluídos.

Exibe uma mensagem de pop-up informando que a criação foi concluída.

Em resumo, o código realiza a leitura e manipulação de arquivos XML e planilhas XLSX, cria novos arquivos
