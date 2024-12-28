from pyc_error_msg import err_msg


def read_input_content(content):
      pass
            


if __name__ == "__main__":
      try :
            read_input_content("Autocaller,all good")

      except Exception as e:
            err_msg("read_input_content",e)