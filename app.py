import streamlit as st
import pandas as pd
import psycopg2

# PostgreSQL veritabanına bağlanma
def get_data_from_postgres():
    conn = psycopg2.connect(dbname="sys_info", user="kuzey", password="1234", host="localhost", port="5432")
    query = "SELECT * FROM system_info;"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Streamlit uygulaması
st.set_page_config(page_title="Sistem Bilgisi Panosu", layout="wide")  # Layout genişliği artırma

st.title('🔍 Sistem Panosu')
st.write('Bu panel, sisteminizin CPU, RAM ve disk kullanımını gösterir.')

# Veriyi çekme
data = get_data_from_postgres()

# Veriyi timestamp'e göre sıralama (en güncel olan en üstte)
data = data.sort_values(by='timestamp', ascending=False)

# Başlıkları ve grafikleri ortalayarak aynı boyutta tutma
st.write('### 📊 Son Sistem Verileri')
st.dataframe(data, use_container_width=True)  # Tablonun genişliğini ayarla ve yatay kaydırma çubuğu ekle

st.write('### 📈 CPU Kullanımı Zaman İçinde')
st.line_chart(data[['timestamp', 'cpu_usage']].set_index('timestamp'), use_container_width=True)

st.write('### 🧠 RAM Kullanımı Zaman İçinde')
st.bar_chart(data[['timestamp', 'ram_usage']].set_index('timestamp'), use_container_width=True)

st.write('### 💽 Disk Kullanımı Zaman İçinde')
st.bar_chart(data[['timestamp', 'disk_usage']].set_index('timestamp'), use_container_width=True)
