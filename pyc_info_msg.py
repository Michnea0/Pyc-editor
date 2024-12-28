from colorama import Fore, Back

info_msg_view = False

def info_msg(info_n,info_i):
        
          if info_msg_view == False:
                    pass 
          else:
                    print ( Fore.WHITE + Back.BLUE + f'[INFO][{str(info_n)}] : {str(info_i)}')                       
                

if __name__ == "__main__" :
          try :
                  
                    if info_msg_view == False:
                            print("[ INTERN ] : Info_msg_view este False ,trebuie sa fie True pentru a testa info_msg")
                          
                    else:
                              info_msg("Autocaller","Totul merge bine")
                          

          except Exception as e:

                    print("[ INTERN ] : " + e)
