# importamos las librerias necesarias
import bluetooth
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

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
    data = 100 # Sample rate (Hz)
    duration = 10 # Duration (seconds)
    t = np.arange(0, duration, 1/data)
    data = np.sin(2*np.pi*10*t) + np.sin(2*np.pi*20*t) + np.sin(2*np.pi*30*t)



    # Filter the data to extract the heart rate signal
    b, a = signal.butter(4, [1/15, 1/5], btype='band')
    filtered_data = signal.filtfilt(b, a, data)

    # Plot the heart rate signal in real time
    fig, ax = plt.subplots()
    line, = ax.plot(t, filtered_data)
    ax.set_ylim([-3, 3])

    for i in range(len(t)):
        line.set_ydata(filtered_data[:i])
        plt.pause(0.001)

    plt.show()