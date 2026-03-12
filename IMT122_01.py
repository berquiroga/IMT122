import numpy as np
import matplotlib.pyplot as plt

# 1. Configuración del Tiempo (Simularemos 3 segundos)
t = np.linspace(0, 3, 1000)

# 2. Señal de Entrada (El Corazón)
# Frecuencia de 1Hz y Amplitud Pico de 10mV (0.01V)
amplitud_in = 0.01
frecuencia = 1
v_in = amplitud_in * np.sin(2 * np.pi * frecuencia * t)

# 3. Parámetros del Hardware (Bloques MECA)
ganancia = 100
v_ref = 2.5  # Nuestra Tierra Virtual / Offset

# 4. El Procesamiento (Lo que hace el AD620 + Sumador)
v_out = (v_in * ganancia) + v_ref

# 5. El Osciloscopio Virtual (Visualización)
plt.figure(figsize=(10, 5))

# Dibujamos la entrada (pequeña, en el origen)
plt.plot(t, v_in, label="Entrada (Sensor): ±10mV", color="blue")

# Dibujamos la salida (grande, montada en 2.5V)
plt.plot(t, v_out, label="Salida (Hacia Arduino): 1.5V a 3.5V", color="red", linewidth=2)

# Dibujamos la referencia para que vean el "piso"
plt.axhline(y=2.5, color='green', linestyle='--', label="Tierra Virtual (2.5V)")
plt.axhline(y=0, color='black', linewidth=0.8) # Línea de 0V real

plt.title("Simulación Matemática del Pre-Amplificador (AD620 + Offset)")
plt.xlabel("Tiempo (segundos)")
plt.ylabel("Voltaje (Voltios)")
plt.legend(loc="upper right")
plt.grid(True, linestyle=':', alpha=0.7)

plt.tight_layout()
plt.show()check_circle