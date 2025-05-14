import subprocess
import platform
import psutil #se der erro, executar o pip com sudo
import re

def calcular_saude(atributos):
    saude = 100

    realocados = int(atributos.get("Reallocated_Sector_Ct", 0))
    if realocados > 0:
        saude -= min(30, realocados)  
    pendentes = int(atributos.get("Current_Pending_Sector", 0))
    if pendentes > 0:
        saude -= min(20, pendentes) 

    erros = int(atributos.get("Raw_Read_Error_Rate", 0))
    if erros > 0:
        saude -= min(15, erros // 100)  

    # Temperatura (ideal <= 50°C)
    temperatura = int(atributos.get("Temperature_Celsius", 35))
    if temperatura > 60:
        saude -= 20
    elif temperatura > 50:
        saude -= 10

    return max(0, min(saude, 100))  # limitar entre 0 e 100

def extrair_atributos(smart_output):
    atributos = {}
    for linha in smart_output.splitlines():
        match = re.match(r"\s*(\d+)\s+([\w\-]+)\s+\S+\s+\d+\s+\d+\s+\d+\s+\S+\s+\S+\s+-\s+(\d+)", linha)
        if match:
            id_atributo, nome, valor = match.groups()
            atributos[nome] = valor
    return atributos

def verificar_disco(disco):
    print(f"\n🔍 Analisando disco: {disco}")
    try:
        comando = ["smartctl", "-A", disco]
        resultado = subprocess.run(comando, capture_output=True, text=True)

        if resultado.returncode != 0:
            print(f"  [!] Falha ao acessar {disco}. Precisa de permissões elevadas?")
            print(f"  {resultado.stderr.strip()}")
            return

        atributos = extrair_atributos(resultado.stdout)
        saude = calcular_saude(atributos)

        print(f"  ✅ Estimativa de saúde: {saude}%")
        if saude > 90:
            print("  🟢 Estado: Excelente")
        elif saude > 70:
            print("  🟡 Estado: Bom com observações")
        elif saude > 50:
            print("  🟠 Estado: Alerta - considere backup")
        else:
            print("  🔴 Estado: Crítico - risco de falha iminente!")

        # Temperatura
        temp = atributos.get("Temperature_Celsius")
        if temp:
            print(f"  🌡️ Temperatura: {temp}°C")

        # Setores realocados
        realocados = atributos.get("Reallocated_Sector_Ct", "0")
        print(f"  🧱 Setores realocados: {realocados}")

        # Setores pendentes
        pendentes = atributos.get("Current_Pending_Sector", "0")
        print(f"  ⌛ Setores pendentes: {pendentes}")

    except Exception as e:
        print(f"Erro ao verificar {disco}: {e}")

def listar_discos():
    sistema = platform.system()
    discos_encontrados = []

    if sistema == "Windows":
        for i in range(10):  # Tenta detectar até 10 discos
            discos_encontrados.append(f"\\\\.\\PhysicalDrive{i}")
    else:
        for disco in psutil.disk_partitions(all=False):
            if "/dev" in disco.device and "loop" not in disco.device:
                base = disco.device.split()[0].split("p")[0]
                if base not in discos_encontrados:
                    discos_encontrados.append(base)

    return list(set(discos_encontrados))

if __name__ == "__main__":
    print("🔧 Verificando saúde dos discos...\n")
    discos = listar_discos()
    if not discos:
        print("Nenhum disco detectado.")
    else:
        for disco in discos:
            verificar_disco(disco)
