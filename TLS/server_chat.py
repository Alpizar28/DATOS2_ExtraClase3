import socket, ssl

HOST, PORT = '127.0.0.1', 8443

# Prepara socket TLS
bindsock = socket.socket()
bindsock.bind((HOST, PORT))
bindsock.listen(1)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('cert.pem', 'key.pem')

print(f"[*] Servidor escuchando en {HOST}:{PORT}")
newsock, addr = bindsock.accept()
conn = context.wrap_socket(newsock, server_side=True)
print(f"[+] Handshake TLS con {addr} completado. Puedes chatear.")

try:
    while True:
        # 1) Recibir mensaje del cliente
        data = conn.recv(4096)
        if not data:
            print("[*] Conexión cerrada por el cliente.")
            break
        print(f"Cliente dice: {data.decode('utf-8')}")

        # 2) Leer respuesta tuya desde stdin
        respuesta = input("Tú > ")
        if respuesta.lower() in ('exit', 'salir'):
            print("[*] Cerrando conexión.")
            conn.send(b'SERVIDOR_FIN')
            break
        conn.send(respuesta.encode('utf-8'))

finally:
    conn.close()
    bindsock.close()
