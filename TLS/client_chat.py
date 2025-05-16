import socket, ssl, threading

HOST, PORT = '127.0.0.1', 8443

# Función para recibir mensajes en paralelo
def escuchar(ssock):
    while True:
        data = ssock.recv(4096)
        if not data or data == b'SERVIDOR_FIN':
            print("\n[*] El servidor cerró la conexión.")
            break
        print(f"\nServidor > {data.decode('utf-8')}\nTú > ", end='', flush=True)

# Prepara contexto TLS sin verificación (pruebas)
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# Conéctate y lanza el hilo lector
with socket.create_connection((HOST, PORT)) as sock:
    with context.wrap_socket(sock, server_hostname=HOST) as ssock:
        print("[+] Handshake TLS completado. Puedes chatear.\n")
        hilo = threading.Thread(target=escuchar, args=(ssock,), daemon=True)
        hilo.start()

        # Bucle de envío desde stdin
        while True:
            msg = input("Tú > ")
            if msg.lower() in ('exit', 'salir'):
                ssock.send(b'CLIENTE_FIN')
                break
            ssock.send(msg.encode('utf-8'))
