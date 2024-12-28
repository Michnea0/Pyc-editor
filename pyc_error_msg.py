from colorama import Fore, Back

def err_msg(err_n,err_i):

      print (Fore.WHITE + Back.RED + f'[{str(err_n)}] : {str(err_i)}')
                          

if __name__ == "__main__" :
      try :

            err_msg("Autocaller","Totul merge bine")

      except Exception as e:

            print("[ INTERN ] : " + e)
