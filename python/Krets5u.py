import numpy as np
import matplotlib.pyplot as plt

# Parametere
Vpk = 20          # Peakverdi på inngangsspenning [V]
V_F = 0.7          # Spenningsfall per diode [V]
f = 50            # Frekvens [Hz]
R = 1000          # Lastmotstand [ohm]
C = 100e-6        # Kondensator [F]
dt = 0.00005      # Tidssteg [s]

# Kun 2 perioder av inngangssignalet
T = 1 / f
t_end = 2 * T
t = np.arange(0, t_end, dt)
t_ms = t * 1000   # konverterer til ms

# inngangsspenning
v1 = Vpk * np.sin(2 * np.pi * f * t)

# Fullbølgelikerettet signal med 2 diodefall
V_rettet = np.abs(v1) - 2 * V_F
V_rettet = np.maximum(V_rettet, 0)

# Utgangsspenning over kondensatoren
V_o = np.zeros_like(t)

for i in range(1, len(t)):
    if V_rettet[i] > V_o[i - 1]:
        V_o[i] = V_rettet[i]
    else:
        V_o[i] = V_o[i - 1] * np.exp(-dt / (R * C))


V_DC = np.mean(V_o[int(0.5 * len(t)):])  # Beregn DC-verdi etter stabilisering
print(f"Simulert DC-verdi av utgangsspenningen: {V_DC:.2f} V")

# Plot
plt.figure(figsize=(10, 5))
plt.plot(t_ms, v1, label="Inngangsspenning $V_{1}(t)$",color="green")
plt.plot(t_ms, V_rettet, label="Likerettet spenning", color="gray")
plt.plot(t_ms, V_o, label="Utgangsspenning med kondensator $V_o(t)$", color="red")
#plot transparant V_DC som en horisontal linje
plt.axhline(V_DC, color="blue", linestyle="--", label=f"DC-verdi (etter stabilisering) $V_{{DC}}$ = {V_DC:.2f} V", alpha=0.35)

#show peak-to-peak voltage of V_o after stabilization
V_o_peak_to_peak = np.max(V_o[int(0.5 * len(t)):]) - np.min(V_o[int(0.5 * len(t)):])
plt.axhline(V_DC + V_o_peak_to_peak / 2, color="purple", linestyle="--", label=f"Peak-to-peak spenning (etter stabilisering) $V_{{pp}}$ = {V_o_peak_to_peak:.2f} V", alpha=0)

plt.xlabel("Tid [ms]")
plt.ylabel("Spenning [V]")
plt.title("Fullbølgelikeretter med kondensator (100μF) over 2 perioder")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

