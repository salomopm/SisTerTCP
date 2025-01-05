import socket
import time

HOST = '0.0.0.0'  # IP addres public server
PORT = 65432        # Port untuk listen
print(HOST)


# Membuat TCP Socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print('Server Side is listening...')

# Menunggu koneksi dari client
conn, addr = server_socket.accept()
print(f'Connected by {addr}')

# File yang ingin dikirim
filename = 'fileSize10KB.docx'  

start_time = time.time()

with open(filename, 'rb') as file:
    # rb -> membaca binary file dan mengirimkannya
    while chunk := file.read(1024):  
        conn.sendall(chunk)
        
end_time = time.time()
time_taken = end_time - start_time

print(f'File terkirim selama {time_taken:.2f} detik!')
conn.close()
server_socket.close()
