import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca dataset
url = "dashboard/day.csv"
df = pd.read_csv(url)

# Mengubah nama judul kolom
df.rename(columns={
    'dteday': 'dateday',
    'yr': 'year',
    'mnth': 'month',
    'weathersit': 'weather_cond',
    'cnt': 'count'
}, inplace=True)

df['month'] = df['month'].map({
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
    7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
})

# Mapping numeric values to season names
df['season'] = df['season'].map({
    1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'
})

# Mapping numeric values to weekday names
df['weekday'] = df['weekday'].map({
    0: 'Sun', 1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thu', 5: 'Fri', 6: 'Sat'
})

# Mapping numeric values to weather condition names
df['weather_cond'] = df['weather_cond'].map({
    1: 'Clear/Partly Cloudy',
    2: 'Misty/Cloudy',
    3: 'Light Snow/Rain',
    4: 'Severe Weather'
})

df['season'] = df.season.astype('category')
df['year'] =df.year.astype('category')
df['month'] = df.month.astype('category')
df['holiday'] = df.holiday.astype('category')
df['weekday'] = df.weekday.astype('category')
df['workingday'] = df.workingday.astype('category')
df['weather_cond'] = df.weather_cond.astype('category')


# Judul Aplikasi
st.title("Analisis Data Peminjaman Sepeda")

# Pilihan menu di sidebar
menu_options = [
    "Analisis Temporal",
    "Analisis Musiman",
    "Analisis Cuaca",
    "Pengaruh Hari Libur dan Hari Kerja",
]
selected_menu = st.sidebar.selectbox("Pilih Menu", menu_options) 

# 2. Analisis Temporal
if selected_menu == "Analisis Temporal":
    st.header("Analisis Temporal")
    # Konversi kolom 'dteday' menjadi tipe data datetime
    df['dateday'] = pd.to_datetime(df['dateday'])
    # Plot jumlah peminjaman sepeda harian (bar plot)
    fig_temporal = plt.figure(figsize=(12, 6))
    plt.bar(df['dateday'], df['count'], label='Jumlah Peminjaman Sepeda')
    plt.title('Jumlah Peminjaman Sepeda Harian')
    plt.xlabel('Tanggal')
    plt.ylabel('Jumlah Peminjaman')
    plt.legend()
    st.pyplot(fig_temporal)
    st.markdown("""
    Kesimpulanya trend peminjaman sepeda mengalami kenaikan pada bulan 7 tahun 
    2011 dan mengalami penurunan kembali pada awal tahun 2012, dan kembali naik dengan signifikan 
    pada bulan 4 tahun 2012, dan mulai mengalami penurunan kembali ketika mendekati bulan ke 10 
    pada tahun 2012, berdasarkan hal ini dapat dilihat bahwasanya faktor musim, dan perubahan cuaca 
    berpengaruh dalam kasus penyewaan sepeda.
    """)

# 3. Analisis Musiman
elif selected_menu == "Analisis Musiman":
    st.header("Analisis Musiman")
    # Plot jumlah peminjaman sepeda per musim (bar plot)
    fig_musiman = plt.figure(figsize=(10, 6))
    sns.barplot(x='season', y='count', data=df, ci=None)
    plt.title('Distribusi Peminjaman Sepeda per Musim')
    plt.xlabel('Musim')
    plt.ylabel('Jumlah Peminjaman')
    st.pyplot(fig_musiman)
    st.markdown("""Untuk jumlah peminjaman sepeda juga dipengaruhi oleh faktor musim, hal ini
    tercatat jumlah peminjaman sepeda terbanyak terjadi pada musim gugur, kemudian disusul 
    oleh musim panas dan dingin, dan untuk peminjaman paling sedikit terjadi pada musim semi""")

# 4. Analisis Cuaca
elif selected_menu == "Analisis Cuaca":
    st.header("Analisis Cuaca")
    # Plot jumlah peminjaman sepeda berdasarkan situasi cuaca (bar plot)
    fig_cuaca = plt.figure(figsize=(10, 6))
    sns.barplot(x='weather_cond', y='count', data=df, ci=None)
    plt.title('Distribusi Peminjaman Sepeda berdasarkan Situasi Cuaca')
    plt.xlabel('Situasi Cuaca')
    plt.ylabel('Jumlah Peminjaman')
    st.pyplot(fig_cuaca)
    st.markdown("""Jumlah peminjaman sepeda juga dipengaruhi oleh kondisi cuaca, berdasarkan plot 
    diagram pada pertanyaan ke 3 tingkat peminjaman tertinggi terjadi pada cuaca clear/parly cloudy 
    sedangkan untuk tingkat peminjaman terendah ada pada cuaca Light snow/rain""")

# 5. Pengaruh Hari Libur dan Hari Kerja
elif selected_menu == "Pengaruh Hari Libur dan Hari Kerja":
    st.header("Pengaruh Hari Libur dan Hari Kerja")
    # Plot jumlah peminjaman sepeda pada hari libur dan hari kerja (bar plot)
    fig_hari_libur_kerja = plt.figure(figsize=(10, 6))
    sns.barplot(x='holiday', y='count', data=df, ci=None)
    plt.title('Distribusi Peminjaman Sepeda pada Hari Libur dan Hari Kerja')
    plt.xlabel('Hari Libur (1: Ya, 0: Tidak)')
    plt.ylabel('Jumlah Peminjaman')
    st.pyplot(fig_hari_libur_kerja)
    st.markdown("""Kesimpulan yang cukup menarik antara tingkat peminjaman pada hari kerja dan hari libur 
    kerja. Dimana tingkat peminjaman pada hari kerja lebih tinggi dibandingkan pada hari libur. Hal ini dapat 
    dijelaskan dengan beberapa faktor, termasuk kebiasaan dan rutinitas masyarakat selama hari kerja.""")


