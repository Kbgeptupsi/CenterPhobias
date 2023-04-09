import bluetooth

# Busca dispositivos Bluetooth cercanos
devices = bluetooth.discover_devices()

# Imprime una lista de los dispositivos encontrados
for device in devices:
    print(device)

# Al parecer, el dispositivo que buscas está en la posición 0 de la lista de dispositivos encontrados
# Tambien puedes buscar el dispositivo por su nombre o dirección MAC (Bluetooth)


# Conecta al dispositivo deseado
address = "24:16:03:00:80:8D" # Reemplaza esto con la dirección Bluetooth de tu smartwatch
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((address, 1))
# Lee los datos enviados a través de la conexión Bluetooth
while True:
    data = sock.recv(1024)
    print("Conectado smarthwatch 7 Pro")
    print(data)
