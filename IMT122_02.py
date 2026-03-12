import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# 1. Definimos los componentes físicos del mundo real
R = 10000      # 10 kOhms
C = 100e-9     # 100 nF

# Calculamos la frecuencia de corte teórica para el gráfico
fc = 1 / (2 * np.pi * R * C)
print(f"Frecuencia de corte teórica: {fc:.2f} Hz")

# 2. Construimos la Función de Transferencia H(s) = 1 / (RC*s + 1)
numerador = [1]
denominador = [R * C, 1]
filtro_rc = signal.TransferFunction(numerador, denominador)

# 3. Calculamos el Diagrama de Bode
# scipy nos devuelve 'w' en radianes/segundo. Lo pasamos a Hz.
w, magnitud, fase = signal.bode(filtro_rc)
frecuencia_hz = w / (2 * np.pi)

# 4. Graficamos la Magnitud
plt.figure(figsize=(10, 5))
plt.semilogx(frecuencia_hz, magnitud, color='#1f77b4', linewidth=2.5)

# Marcadores visuales para los -3dB y la fc
plt.axvline(x=fc, color='red', linestyle='--', label=f'Frecuencia de Corte ({fc:.1f} Hz)')
plt.axhline(y=-3, color='green', linestyle=':', label='Caída de -3 dB')

# Estética de la gráfica
plt.title('Respuesta en Frecuencia: Filtro Pasa-Bajos RC')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud (dB)')
plt.grid(True, which="both", ls="--", alpha=0.7)
plt.legend()
plt.show()