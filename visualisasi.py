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

# Hitung total pendapatan
total_pendapatan = data['Total_Penjualan'].sum()

# Cari produk dengan penjualan tertinggi
produk_terlaris = data.groupby('Produk')['Jumlah'].sum().idxmax()

# Hitung total pendapatan bulanan
data['Bulan'] = data['Tanggal'].dt.to_period('M')
pendapatan_bulanan = data.groupby('Bulan')['Total_Penjualan'].sum()

# Buat grafik tren penjualan bulanan
plt.figure(figsize=(10, 6))
pendapatan_bulanan.plot(kind='line', marker='o')
plt.title('Tren Penjualan Bulanan')
plt.xlabel('Bulan')
plt.ylabel('Total Pendapatan')
plt.grid(True)
plt.show()

# Identifikasi bulan dengan pendapatan tertinggi dan rendah
bulan_tertinggi = pendapatan_bulanan.idxmax()
bulan_terendah = pendapatan_bulanan.idxmin()

# Saran untuk meningkatkan penjualan
saran = """
Untuk meningkatkan penjualan, berikut beberapa saran:
1. Fokus pada produk yang memiliki penjualan tertinggi, yaitu '{}'.
2. Lakukan promosi khusus pada bulan '{}', karena pendapatan pada bulan ini paling rendah.
3. Tingkatkan stok dan variasi produk pada bulan '{}', karena pendapatan pada bulan ini paling tinggi.
""".format(produk_terlaris, bulan_terendah, bulan_tertinggi)

print(saran)
