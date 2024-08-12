import psutil
import platform
import psycopg2
import time
from datetime import datetime

def get_system_info():
    info = {
        "os": platform.system(),
        "kernel": platform.release(),
        "cpu_usage": psutil.cpu_percent(interval=5),
        "ram_usage": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage('/mnt/c').percent,
        "timestamp": datetime.now()
    }
    return info

def create_table():
    conn = psycopg2.connect(dbname="sys_info", user="kuzey", password="1234", host="localhost", port="5432")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS system_info (
                        id SERIAL PRIMARY KEY,
                        os VARCHAR(50),
                        kernel VARCHAR(50),
                        cpu_usage REAL,
                        ram_usage REAL,
                        disk_usage REAL,
                        timestamp TIMESTAMP
                    )''')
    conn.commit()
    cursor.close()
    conn.close()

def insert_data(info):
    conn = psycopg2.connect(
        dbname="sys_info", user="kuzey", password="1234", host="localhost", port="5432"
    )
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO system_info (os, kernel, cpu_usage, ram_usage, disk_usage, timestamp) 
                      VALUES (%s, %s, %s, %s, %s, %s)''',
                   (info['os'], info['kernel'], info['cpu_usage'], info['ram_usage'], info['disk_usage'], info['timestamp']))
    conn.commit()
    cursor.close()
    conn.close()

def start_collecting(interval=55):
    create_table()
    while True:
        info = get_system_info()
        insert_data(info)
        print("Logged succesfully")
        time.sleep(interval)

if __name__ == "__main__":
    start_collecting()
