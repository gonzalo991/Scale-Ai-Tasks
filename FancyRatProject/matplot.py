import matplotlib.pyplot as plt

# Example data
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']
ventas = [10000, 12000, 9000, 11000, 15000, 13000]

# Creates the line graphic
plt.plot(meses, ventas)

# Customize
plt.title('Crecimiento de ventas por mes')
plt.xlabel('Meses')
plt.ylabel('Ventas')
plt.grid(True)

# Mostrar el gráfico
plt.show()