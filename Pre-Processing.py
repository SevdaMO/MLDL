import wfdb
import numpy as np
import matplotlib.pyplot as plt

# Datei einlesen
record = wfdb.rdrecord('/content/drive/MyDrive/zWtiCjFSxBFRmU3DklC4UMFKFHCOXJgS')

# Überprüfen, wie viele Kanäle der Record hat
print("Number of signals:", record.n_sig)
print("Signal names:", record.sig_name)

# Falls mehr als 1 Kanal vorhanden ist, den zweiten Kanal auswählen
if record.n_sig > 1:
    signal_data = np.array(record.p_signal[:, 1])  # Kanal 2 (Index 1)
else:
    print("Der Record enthält nur einen Kanal.")

# Form der Signal-Daten ausgeben
print("Signal Data Shape:", signal_data.shape)

# Signal-Daten plotten
plt.figure(figsize=(10, 4))
plt.plot(signal_data, color='blue')
plt.title("Signal Data for Channel 2")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()



