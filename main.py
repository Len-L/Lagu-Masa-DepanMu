import time as qq
from threading import Thread, Lock
import sys

# Deklarasi Lock untuk menangani akses ke stdout
lock = Lock()

# Deklarasi warna untuk teks
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
RESET = '\033[0m'

# Fungsi untuk menampilkan teks secara animasi
def animate_text(text, delay=0.1, color_info=None):
    with lock:
        use_red = True  # Flag untuk mengganti warna
        for char in text:
            if color_info and char == color_info:  # Ganti warna untuk karakter tertentu
                color = f"{RED}{char}{RESET}" if use_red else f"{GREEN}{char}{RESET}"
                sys.stdout.write(color)
                use_red = not use_red
            else:
                sys.stdout.write(char)
            sys.stdout.flush()
            qq.sleep(delay)
        print()  # Pindah ke baris berikutnya setelah selesai

# Fungsi untuk menyanyikan lirik dengan delay dan kecepatan
def sing_lyric(lyric, delay, speed, color_char):
    qq.sleep(delay)  # Tunggu sesuai delay sebelum menampilkan lirik
    animate_text(lyric, speed, color_char)

# Fungsi utama untuk menjalankan lagu
def sing_song():
    lyrics = [
        ("\nA A A A A A A A A A Aku akan beritahu pada dunia", 0.08, 'A'),
        ("kau begitu indah", 0.08, None),
        ("yang pernah ku punya", 0.08, None),
        ("A A A A Aku akan selalu menemani dirimu", 0.08, 'A'),
        ("U U U U U U Ucap Terima kasih untuk dirimu", 0.09, 'U'),
        ("kita membuat memori sampai akhir hayat nanti", 0.08, None),
        ("cinta ku tak pernah mati jadi kau tak perlu worry", 0.07, None),
        ("genggam tanganku tak perlu ragu", 0.08, None),
        ("habiskan waktu hanya bersama dirimu", 0.08, None),
    ]
    
    delays = [0.3, 5.0, 6.8, 8.0, 11.3, 15.3, 18.6, 22.7, 26.0]  # Delay antar lirik
    
    threads = []  # Daftar untuk menyimpan thread
    for i in range(len(lyrics)):
        lyric, speed, color_char = lyrics[i]
        # Buat thread untuk setiap lirik
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed, color_char))
        threads.append(t)
        t.start()  # Mulai thread
    
    # Tunggu semua thread selesai
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()  # Jalankan fungsi utama untuk menyanyikan lagu
