import pandas as pd
import matplotlib.pyplot as plt

# Data penjualan dari beberapa tabel
data1 = pd.DataFrame({
    'Tanggal': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06'],
    'Produk': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Laptop', 'Mouse'],
    'Jumlah': [2, 5, 3, 1, 1, 2],
    'Harga': [15000, 300, 700, 5000, 15000, 300]
})

data2 = pd.DataFrame({
    'Tanggal': ['2023-02-01', '2023-02-02', '2023-02-03', '2023-02-04', '2023-02-05', '2023-02-06'],
    'Produk': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Laptop', 'Mouse'],
    'Jumlah': [3, 7, 2, 2, 2, 3],
    'Harga': [15000, 300, 700, 5000, 15000, 300]
})

data3 = pd.DataFrame({
    'Tanggal': ['2023-03-01', '2023-03-02', '2023-03-03', '2023-03-04', '2023-03-05', '2023-03-06'],
    'Produk': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Laptop', 'Mouse'],
    'Jumlah': [1, 8, 4, 1, 2, 1],
    'Harga': [15000, 300, 700, 5000, 15000, 300]
})

# Gabungkan semua tabel menjadi satu DataFrame
data = pd.concat([data1, data2, data3])

# Ubah kolom `Tanggal` menjadi tipe data datetime
data['Tanggal'] = pd.to_datetime(data['Tanggal'])

# Tambahkan kolom `Total_Penjualan`
data['Total_Penjualan'] = data['Jumlah'] * data['Harga']

# Hitung total pendapatan bulanan
data['Bulan'] = data['Tanggal'].dt.to_period('M')
pendapatan_bulanan = data.groupby('Bulan')['Total_Penjualan'].sum()

# Visualisasi Scatterplot
plt.figure(figsize=(10, 6))
plt.scatter(data['Harga'], data['Jumlah'], alpha=0.5)
plt.title('Scatterplot Harga vs Jumlah')
plt.xlabel('Harga')
plt.ylabel('Jumlah Terjual')
plt.grid(True)
plt.show()

# Visualisasi Histogram Harga
plt.figure(figsize=(10, 6))
plt.hist(data['Harga'], bins=20, alpha=0.7, color='blue')
plt.title('Histogram Harga Produk')
plt.xlabel('Harga')
plt.ylabel('Frekuensi')
plt.grid(True)
plt.show()

# Visualisasi Histogram Jumlah Terjual
plt.figure(figsize=(10, 6))
plt.hist(data['Jumlah'], bins=20, alpha=0.7, color='green')
plt.title('Histogram Jumlah Produk Terjual')
plt.xlabel('Jumlah')
plt.ylabel('Frekuensi')
plt.grid(True)
plt.show()

# Visualisasi Grafik Batang Total Penjualan Bulanan
plt.figure(figsize=(10, 6))
pendapatan_bulanan.plot(kind='bar', color='orange')
plt.title('Total Penjualan Bulanan')
plt.xlabel('Bulan')
plt.ylabel('Total Pendapatan')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()
