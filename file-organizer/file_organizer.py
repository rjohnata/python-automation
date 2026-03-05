import os
import shutil
from datetime import datetime

# Caminho que será organizado (altere se quiser)
TARGET_FOLDER = os.path.expanduser("~/Downloads")

# Tipos de arquivos
FILE_TYPES = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
    "Documentos": [".pdf", ".docx", ".doc", ".txt"],
    "Planilhas": [".xlsx", ".xls", ".csv"],
    "Executaveis": [".exe", ".msi"],
    "Compactados": [".zip", ".rar"]
}

# Criar pasta de log
LOG_FOLDER = "logs"
os.makedirs(LOG_FOLDER, exist_ok=True)

log_file = os.path.join(LOG_FOLDER, f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")

def write_log(message):
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(message + "\n")

print("Iniciando organização automática...\n")

for filename in os.listdir(TARGET_FOLDER):
    file_path = os.path.join(TARGET_FOLDER, filename)

    if os.path.isfile(file_path):
        file_extension = os.path.splitext(filename)[1].lower()

        moved = False

        for folder, extensions in FILE_TYPES.items():
            if file_extension in extensions:
                folder_path = os.path.join(TARGET_FOLDER, folder)
                os.makedirs(folder_path, exist_ok=True)

                shutil.move(file_path, os.path.join(folder_path, filename))
                message = f"Movido: {filename} -> {folder}"
                print(message)
                write_log(message)

                moved = True
                break

        if not moved:
            outros_path = os.path.join(TARGET_FOLDER, "Outros")
            os.makedirs(outros_path, exist_ok=True)
            shutil.move(file_path, os.path.join(outros_path, filename))
            message = f"Movido: {filename} -> Outros"
            print(message)
            write_log(message)

print("\nOrganização concluída com sucesso!")

input("\nPressione Enter para sair...")
