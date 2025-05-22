import os
import subprocess
import shlex
from tkinter import Tk, Label, Entry, Button, filedialog, ttk

def download_song():
    url = url_entry.get().strip()
    output_dir = output_dir_entry.get().strip()
    if not url or not output_dir:
        print("Por favor, preencha todos os campos.")
        return
    command = f"spotdl {url} --output {output_dir}"
    try:
        subprocess.run(shlex.split(command), check=True)
        print("Download concluído com sucesso!")
    except subprocess.CalledProcessError:
        print("Erro ao baixar a música.")

def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        output_dir_entry.delete(0, 'end') 
        output_dir_entry.insert(0, folder_selected)  

root = Tk()
root.title("Spotify Downloader")
root.geometry("500x250")

style = ttk.Style()
style.theme_use('clam')

Label(root, text="Link da Música:", font=('Arial', 12)).pack(pady=(10, 0))
url_entry = ttk.Entry(root, width=50)
url_entry.pack(pady=(0, 10))

Label(root, text="Pasta de Saída:", font=('Arial', 12)).pack(pady=(10, 0))
output_dir_entry = ttk.Entry(root, width=50)
output_dir_entry.pack(pady=(0, 10))

button_frame = ttk.Frame(root)
button_frame.pack(pady=(10, 10))

select_button = ttk.Button(button_frame, text="Selecionar Pasta", command=select_folder)
select_button.pack(side='left', padx=(0, 10))

download_button = ttk.Button(button_frame, text="Baixar Música", command=download_song)
download_button.pack(side='left')

root.mainloop()
