import numpy as np
import matplotlib.pyplot as plt

class FiltroPasivoRC:
    # 1. El constructor de la clase
    def __init__(self, resistencia, capacitancia):
        self.R = resistencia
        self.C = capacitancia
        # Calculo de la frecuencia de corte de este filtro
        self.f_c = 1 / (2 * np.pi * self.R * self.C)

    # 2. Método (función) para mostrar los datos
    def mostrar_parametros(self):
        print("--- Parámetros del Filtro ---")
        print(f"Resistencia: {self.R} Ohms")
        print(f"Capacitancia: {self.C} Faradios")
        print(f"Frecuencia de Corte (f_c): {self.f_c} Hz")
        print("-----------------------------")

    # 3. Método (función) para graficar el diagrama de Bode}
    def graficar_bode(self, f_min=1, f_max=10000, puntos=1000):
        # Generar un vector de frecuencias (eje X logarítmico)
        frecuencia = np.logspace(start=np.log10(f_min),
                                 stop=np.log10(f_max),
                                 num=puntos)
        
        # Magnitud lineal
        omega = 2 * np.pi * frecuencia
        magnitud_lineal = 1 / np.sqrt(1 + (omega * self.R * self.C)**2)

        # Conversión a decibelios para el voltaje
        magnitud_db = 20 * np.log10(magnitud_lineal)

        # Cálculo de Fase (en grados)
        # np.arctan devuelve radianes, lo multiplicamos por 180/pi o usamos np.degrees
        fase_rad = -np.arctan(omega * self.R * self.C)
        fase_deg = np.degrees(fase_rad)

        # --- CREACIÓN DE LAS GRÁFICAS (BODE COMPLETO) ---
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
        
        # Gráfica Superior: Magnitud
        ax1.semilogx(frecuencia, magnitud_db, color='#1f77b4', linewidth=2)
        ax1.axvline(x=self.f_c, color='red', linestyle='--', label=f'fc = {self.f_c:.1f} Hz')
        ax1.axhline(y=-3, color='green', linestyle=':', label='-3 dB')
        ax1.set_title('Diagrama de Bode: Filtro Pasa-Bajos RC')
        ax1.set_ylabel('Magnitud (dB)')
        ax1.grid(True, which="both", ls="--", alpha=0.7)
        ax1.legend()

        # Gráfica Inferior: Fase
        ax2.semilogx(frecuencia, fase_deg, color='#ff7f0e', linewidth=2)
        ax2.axvline(x=self.f_c, color='red', linestyle='--')
        ax2.axhline(y=-45, color='purple', linestyle=':', label='-45° en fc')
        ax2.set_xlabel('Frecuencia (Hz)')
        ax2.set_ylabel('Fase (Grados)')
        ax2.grid(True, which="both", ls="--", alpha=0.7)
        ax2.legend()

        plt.tight_layout()
        plt.show()

# Instanciamos el filtro que diseñaron para el ESP32
mi_filtro_biomedico = FiltroPasivoRC(resistencia=10000, capacitancia=100e-9)

# Usamos sus métodos
mi_filtro_biomedico.mostrar_parametros()
mi_filtro_biomedico.graficar_bode()