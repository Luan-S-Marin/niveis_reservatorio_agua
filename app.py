#Este programa mostra os níveis de um reservatório de água
#Autor: Luan-S-Marin

import os 

os.system("cls")

#Importa a biblioteca colorama para definir e exibir caracteres com cores no terminal
from colorama import Fore, Style

#inicio do programa 
print("==== Nível do reservatório ====")

#Função para definir a cor da mensagem avisando o nível do reservatório
def definir_cor(nivel):
   if nivel == 1:
      return Fore.RED
   elif nivel == 2:
      return Fore.YELLOW
   elif nivel == 3:
      return Fore.GREEN
   elif nivel == 4:
         return Fore.CYAN
   elif nivel == 5:
         return Fore.BLUE

#Lista que armazena as mensagens 
mensagens = [
"Atenção - Reservatório está em nível muito baixo",
"Reservatório está em nível baixo",
"Reservatório está em nível medio",
"Reservatório está em nível alto",
"Atenção - Reservatório está em nível muito alto"]

#Exibe todas as mensagens da lista na tela com suas respectivas cores 
for i in range (len(mensagens)):
    print(definir_cor(i+1) + mensagens[i])


#Encerra a função de cores 
print(Style.RESET_ALL)
