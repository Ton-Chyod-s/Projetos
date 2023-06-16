# Projetos

O programa captura as coordenadas do mouse quando o botão esquerdo é pressionado e as salva em uma lista. Em seguida, o programa utiliza as coordenadas armazenadas para realizar ações específicas na tela.

Importação das bibliotecas necessárias:

from pynput import mouse: Importa a classe mouse do módulo pynput, que permite monitorar os eventos do mouse.
import keyboard: Importa o módulo keyboard, que permite verificar se uma tecla específica foi pressionada.
import pyautogui as pt: Importa o módulo pyautogui e o renomeia para pt, que fornece funções para controlar o mouse e o teclado.
from time import sleep: Importa a função sleep do módulo time, que pausa a execução do programa por um determinado período.
Inicialização da lista coordenadas:

Cria uma lista vazia para armazenar as coordenadas do mouse.
Definição da função on_click:

Esta função é chamada quando um evento de clique do mouse ocorre.
Ela recebe as coordenadas cx e cy do clique, o botão pressionado e um valor booleano pressed indicando se o botão foi pressionado ou solto.
Se o botão esquerdo do mouse for pressionado, as coordenadas (cx, cy) são adicionadas à lista coordenadas.
Criação do listener de mouse:

Utilizando o mouse.Listener do módulo pynput, é criado um listener que chama a função on_click sempre que um evento de clique do mouse ocorre.
Loop principal:

O programa entra em um loop infinito para capturar as coordenadas e realizar ações na tela.
Verifica se a tecla Esc foi pressionada utilizando a função keyboard.is_pressed('Esc').
Se a tecla Esc for pressionada, o loop principal é interrompido e o programa termina.
Caso contrário, o programa continua no loop principal.
Verificação das coordenadas:

Verifica se a lista coordenadas contém pelo menos 2 coordenadas capturadas.
Se houver pelo menos 2 coordenadas, as duas primeiras coordenadas são atribuídas às variáveis c1 e c2.
As coordenadas são desempacotadas nas variáveis x1, y1, x2 e y2 para facilitar o acesso.

Ações na tela (continuação):

Há um atraso adicional de 0.3 segundos após o segundo clique para simular uma pausa.
A função pt.rightClick() realiza um clique com o botão direito do mouse nas coordenadas (x2-25, y2-25), que estão ligeiramente deslocadas em relação ao segundo ponto capturado. Isso pode ser útil para executar uma ação específica em um elemento da tela.
Atualização da lista de coordenadas:

Após as ações na tela, as duas primeiras coordenadas são removidas da lista coordenadas, permitindo que o próximo par de coordenadas seja processado no próximo ciclo do loop.
Verificação de término:

O programa verifica se a tecla Esc foi pressionada novamente ou se a lista coordenadas está vazia.
Se qualquer uma dessas condições for verdadeira, o loop principal é interrompido e o programa termina.
O programa, portanto, captura as coordenadas do mouse quando o botão esquerdo é pressionado, realiza ações específicas na tela com base nessas coordenadas e continua a fazer isso até que a tecla Esc seja pressionada ou não haja mais coordenadas na lista.

