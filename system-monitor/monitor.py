import psutil
import time
from datetime import datetime
import os

LOG_FOLDER = "logs"
os.makedirs(LOG_FOLDER, exist_ok=True)

log_file = os.path.join(LOG_FOLDER, f"monitor_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")

def write_log(message):
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(message + "\n")

print("Iniciando monitoramento do sistema...\n")

cpu = psutil.cpu_percent(interval=1)
ram = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

info = f"""
Data/Hora: {datetime.now()}
Uso de CPU: {cpu}%
Uso de RAM: {ram}%
Uso de Disco: {disk}%
"""

print(info)
write_log(info)

print("Monitoramento concluído.")
input("Pressione Enter para sair...")
