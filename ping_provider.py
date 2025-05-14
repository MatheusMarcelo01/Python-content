import speedtest

def medir_velocidade():
    print("Iniciando teste de velocidade...\n")

    st = speedtest.Speedtest()

    # obter server de acordo com o ping
    best_server = st.get_best_server()

    print("Servidor selecionado:")
    print(f" - Host: {best_server['host']}")
    print(f" - Local: {best_server['name']}, {best_server['country']}")
    print(f" - Distância aproximada: {best_server['d']} km")
    print(f" - Latência (ping): {best_server['latency']:.2f} ms\n")

    print("Medindo velocidade de download...")
    download = st.download()

    print("Medindo velocidade de upload...")
    upload = st.upload()

    #ident. provedor
    client_info = st.get_config()['client']
    isp = client_info.get('isp', 'Desconhecido')
    ip = client_info.get('ip', 'IP não encontrado')

    print("\n=== RESULTADOS ===")
    print(f"Provedor (ISP): {isp}")
    print(f"Endereço IP: {ip}")
    print(f"Velocidade de Download: {download / 1_000_000:.2f} Mbps")
    print(f"Velocidade de Upload:   {upload / 1_000_000:.2f} Mbps")
    print(f"Ping (Latência):        {best_server['latency']:.2f} ms")

if __name__ == "__main__":
    medir_velocidade()
