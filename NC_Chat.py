import os
from colorama import Fore
import time


class CHAT:
    PINK='\033[35m'
    HOST='localhost'
    
    def Label():
        os.system('clear')
        os.system('figlet H Chat | lolcat')
        print(Fore.RED+'\t'*4+'¥__1.0v__¥\n\n')
        time.sleep(1)
        
        
    def Choice():
        print(Fore.YELLOW)
        print('[1]Create Host')
        print('[2]Join Host\n\n')
        
        choice=int(input(Fore.GREEN+'Enter Choice>>>   '+Fore.RED))
        
        if choice==1:
            CHAT.CHost()
        
        elif choice==2:
            CHAT.JHost()
            
        else:
             print('.....Invalied.....')
             exit(0)
      
    
        
    def JHost():
         print(CHAT.PINK)
         Host=input('~Enter connect wifi ip~  '+Fore.RED)
         Port=int(input(CHAT.PINK+'~Enter Target Device Port~  '+Fore.RED))
         print(Fore.GREEN+'\n<<<START Chating.....>>>\n'+Fore.RED)
         time.sleep(1)
         
         os.system(f'nc {CHAT.HOST} {Port}')
   
             
    def CHost():
         
         Port=int(input(CHAT.PINK+'\n~Enter 4 Number Port~  '+Fore.RED))
         print(Fore.GREEN+'\n<<<START Chating..... >>>\n'+Fore.RED)
         time.sleep(1)
         
         os.system(f'nc -l -p {Port}') 
         
         
CHAT.Label()
CHAT.Choice()
