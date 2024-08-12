import streamlit as st
import pandas as pd
import psycopg2
import altair as alt

# PostgreSQL veritabanına bağlanma
def get_data_from_postgres():
    conn = psycopg2.connect(dbname="sys_info", user="kuzey", password="1234", host="localhost", port="5432")
    query = "SELECT * FROM system_info;"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Streamlit uygulaması
st.set_page_config(page_title="Sistem Bilgisi Panosu", layout="wide")  # Layout genişliği artırma

st.title('🔍 Sistem Bilgisi Panosu')
st.write('Bu panel, sisteminizin CPU, RAM ve disk kullanımını gösterir.')

# Veriyi çekme
data = get_data_from_postgres()

# Veriyi timestamp'e göre sıralama (en güncel olan en üstte)
data = data.sort_values(by='timestamp', ascending=False)

# Başlıkları ve grafikleri ortalayarak aynı boyutta tutma
st.write('### 📊 Son Sistem Verileri')
st.dataframe(data, use_container_width=True)  # Tablonun genişliğini ayarla ve yatay kaydırma çubuğu ekle

# CPU Kullanımı grafiği için altair kullanımı
st.write('### 📈 CPU Kullanımı Zaman İçinde')
cpu_chart = alt.Chart(data).mark_line().encode(
    x='timestamp:T',
    y=alt.Y('cpu_usage:Q', scale=alt.Scale(domain=[0, 100])),
    tooltip=['timestamp', 'cpu_usage']
).properties(
    width='container',
    height=400
).interactive()

st.altair_chart(cpu_chart, use_container_width=True)

# RAM Kullanımı grafiği için altair kullanımı
st.write('### 🧠 RAM Kullanımı Zaman İçinde')
ram_chart = alt.Chart(data).mark_bar().encode(
    x='timestamp:T',
    y=alt.Y('ram_usage:Q', scale=alt.Scale(domain=[0, 100])),
    tooltip=['timestamp', 'ram_usage']
).properties(
    width='container',
    height=400
).interactive()

st.altair_chart(ram_chart, use_container_width=True)

# Disk Kullanımı grafiği için altair kullanımı
st.write('### 💽 Disk Kullanımı Zaman İçinde')
disk_chart = alt.Chart(data).mark_bar().encode(
    x='timestamp:T',
    y=alt.Y('disk_usage:Q', scale=alt.Scale(domain=[0, 100])),
    tooltip=['timestamp', 'disk_usage']
).properties(
    width='container',
    height=400
).interactive()

st.altair_chart(disk_chart, use_container_width=True)
