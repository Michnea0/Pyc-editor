#pyc_info_win.py

from tkinter import * 
from pyc_error_msg import err_msg
from pyc_info_msg import info_msg

def read_info_file():
          info_msg("read_info_file()","Se incearca citirea fisierului...")
       
          try:
                    with open("pyc_info.txt","r") as info_file:

                              info_msg("read_info_file()","Se adauga continutul...")
                              content = info_file.read()
                              win_panel.delete(1.0,END)
                              win_panel.config(state="normal")
                              win_panel.insert(END,content)
                              win_panel.config(state="disabled")
                              info_msg("read_info_file()","Continut adaugat")

          except Exception as e:
                  err_msg("read_info_file()","Fisierul pyc_info.txt nu a fost gasit")


def pyc_info_win():
          global win_panel

          info_msg("pyc_info_win","Se incarca GUI...")
          cmd_root = Tk()
          cmd_root.title("Pyc Info")
          cmd_root.geometry("600x500")
          
          m_frame = Frame(cmd_root)
          m_frame.pack(expand=True,fill=BOTH)

          m_frame.grid_columnconfigure(0,weight=1)
          m_frame.grid_columnconfigure(1,weight=1)
          m_frame.grid_columnconfigure(2,weight=1)
          m_frame.grid_columnconfigure(3,weight=1)
          m_frame.grid_columnconfigure(4,weight=1)
          m_frame.grid_columnconfigure(5)

          m_frame.grid_rowconfigure(0,weight=1)
          m_frame.grid_rowconfigure(1,weight=1)
          m_frame.grid_rowconfigure(2,weight=1)
          m_frame.grid_rowconfigure(3,weight=1)
          m_frame.grid_rowconfigure(4,weight=1)

          win_title = Label(m_frame,text="info",font=['sans-serif',12],pady=5,fg="grey")
          win_title.grid(column=0,row=0,columnspan=5,sticky="nsew")

          win_panel = Text(m_frame,padx=10,pady=10)
          win_panel.grid(column=0,row=1,columnspan=5,rowspan=4,sticky="nsew",padx=5,pady=5)

          scroll_y = Scrollbar(m_frame, orient=VERTICAL, command= win_panel.yview)
          scroll_y.grid(column=5,row=1,rowspan=5,sticky="nsew")
          win_panel.config(yscrollcommand= scroll_y.set)

          info_msg("pyc_info_win","Gui incarcat")
          info_msg("pyc_info_win","Se apeleaza read_info_file()")
          read_info_file()
          cmd_root.mainloop()
          info_msg("pyc_info_win","pyc_info_win se inchide")

if __name__ == "__main__":
      try :
            pyc_info_win()

      except Exception as e:
            err_msg("pyc_info_win",e)