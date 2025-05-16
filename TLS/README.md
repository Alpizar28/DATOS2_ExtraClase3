# TLS Chat - Ejemplos en Python

Este proyecto contiene un ejemplo de chat bidireccional seguro usando TLS (Python puro). A continuación encontrarás las instrucciones para configurar y ejecutar las aplicaciones servidor y cliente.

---


## Requisitos

* Python 3.7 o superior
* OpenSSL (para generar certificados)

---

## Generar certificados (si no los tienes)

En la raíz del proyecto (`TLS-TareaExtraclase#3/`), ejecuta:

```bash
openssl req -newkey rsa:2048 -nodes -keyout key.pem \
  -x509 -days 365 -out cert.pem \
  -subj "/CN=localhost"
```

Esto creará `cert.pem` y `key.pem`.

---

## Ejecución del chat TLS

1. **Copiar certificados a la carpeta `chat/`**

   ```bash
   cp cert.pem key.pem chat/
   ```

2. **Levantar el servidor TLS**

   ```bash
   cd chat
   python3 server_chat.py
   ```

   Verás en consola:

   ```
   [*] Servidor escuchando en 127.0.0.1:8443
   [*] Handshake TLS con ('127.0.0.1', XXXX) completado. Puedes chatear.
   ```

3. **Levantar el cliente TLS**

   En otra terminal (misma carpeta `chat/`):

   ```bash
   python3 client_chat.py
   ```

   Aparecerá el prompt para escribir mensajes:

   ```
   [+] Handshake TLS completado. Puedes chatear.
   Tú >
   ```

4. **Chatear**

   * Escribe tu mensaje tras `Tú > ` y presiona Enter.
   * Los mensajes del otro extremo aparecerán con el prefijo `Cliente dice:` (en servidor) o `Servidor >` (en cliente).
   * Para salir, escribe `exit` o `salir` y presiona Enter.

---

## Limpieza (opcional)

Si deseas eliminar archivos innecesarios:

```bash
# Borrar ejemplo básico
rm -r basic/
# Borrar cliente GUI si existiera
rm gui_client.py
```

---

## Control de versiones con Git (opcional)

Si usas Git, recuerda commitear los cambios:

```bash
git add .
git commit -m "Agregar ejemplo de chat TLS y README"
```

¡Listo! Ahora tienes un chat seguro sobre TLS en Python. Cualquier duda, abre un issue o contáctame.
