#pyc_main.py

from tkinter import *  #gui pyc
from pyc_error_msg import err_msg
from pyc_info_msg import info_msg
from pyc_info_win import pyc_info_win
from pyc_read import read_input_content

#acestea vin mutate in pyc_aditional_actions.py
def hide_label():
      info_msg("hide_label()","Se ascunde label...")
      win_title.grid_forget()
      win_panel.grid(column=0,row=0,columnspan=5,rowspan=3,sticky="nsew",padx=5)

def show_label():
      info_msg("show_label()","Se afiseaza label...")
      win_title.grid(column=0,row=0,columnspan=5,sticky="nsew")
      win_panel.grid(column=0,row=1,columnspan=5,rowspan=3,sticky="nsew",padx=5)
      #pana aici

def read_input():
       
      try:
            content_inp = win_panel.get()
            win_panel.delete(0,END)

            read_input_content(content_inp)

      except Exception as e:
            err_msg("read_input",e)

def pyc_win():
          info_msg("pyc_win","Se incarca GUI...")
          global win_title
          global win_panel

          cmd_root = Tk()
          cmd_root.title("Pyc eidtor Atos")
          cmd_root.geometry("600x500")

          #add menu

          menu_bar = Menu(cmd_root)
          cmd_root.config(menu=menu_bar)

          menu_file = Menu(menu_bar,tearoff=0)
          menu_file.add_command(label="Create file")
          menu_file.add_command(label="Open file")
          menu_file.add_command(label="Save file")
          menu_file.add_command(label="Save as file")
          menu_file.add_command(label="Close this file")

          
          menu_bar.add_cascade(label="File",menu=menu_file)

          menu_project = Menu(menu_bar,tearoff=0)
          menu_project.add_command(label="Create new project")
          menu_project.add_command(label="Open project")
          menu_project.add_command(label="View porjects")
          menu_project.add_command(label="View files form current porject")
          
          menu_bar.add_cascade(label="Project",menu=menu_project)

          menu_snippets = Menu(menu_bar,tearoff=0)
          menu_snippets.add_command(label="View snippets")
          
          menu_bar.add_cascade(label="Snippets",menu=menu_snippets)

          menu_toSolve = Menu(menu_bar,tearoff=0)
          menu_toSolve.add_command(label="Create a problem")
          menu_toSolve.add_command(label="View to Solve")
          
          menu_bar.add_cascade(label="To solve",menu=menu_toSolve)

          menu_edit = Menu(menu_bar,tearoff=0)
          menu_edit.add_command(label="Undo")
          menu_edit.add_command(label="Redo")
          menu_edit.add_command(label="Find")
          menu_edit.add_command(label="Replace")
          
          menu_bar.add_cascade(label="Edit",menu=menu_edit)
          
          menu_view = Menu(menu_bar,tearoff=0)
          menu_view.add_command(label="hide label",command=hide_label)
          menu_view.add_command(label="show label",command=show_label)
          menu_view.add_command(label="Settings")
          menu_view.add_command(label="Log")

          
          menu_bar.add_cascade(label="View",menu=menu_view)

          menu_help = Menu(menu_bar,tearoff=0)
          menu_help.add_command(label="About pyc",command=pyc_info_win)
          menu_help.add_command(label="How to use")
          menu_help.add_command(label="README pyc")
          menu_help.add_command(label="Update list pyc")
          menu_help.add_command(label="Website pyc")
          
          menu_bar.add_cascade(label="Help",menu=menu_help)

          #elms

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

          win_title = Label(m_frame,text="Welcome",font=['sans-serif',12],pady=5,fg="grey")
          win_title.grid(column=0,row=0,columnspan=5,sticky="nsew")

          win_panel = Text(m_frame,padx=10,pady=10)
          win_panel.grid(column=0,row=1,columnspan=5,rowspan=4,sticky="nsew",padx=10,pady=10)

          scroll_y = Scrollbar(m_frame, orient=VERTICAL, command= win_panel.yview)
          scroll_y.grid(column=5,row=1,rowspan=4,sticky="nsew")
          win_panel.config(yscrollcommand= scroll_y.set)

          info_msg("pyc_win","Gui incarcat")
          cmd_root.mainloop()
          info_msg("pyc_win","pyc se inchide")

if __name__ == "__main__":
      try :
            pyc_win()

      except Exception as e:
            err_msg("pyc_win",e)