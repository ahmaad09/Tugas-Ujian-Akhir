import time
import sys

def animate_text(text, delay=0.1):
 
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(delay)
  print()

def sing_song():
  """
  Menampilkan lirik lagu "Sekuat Hatimu" dengan animasi teks.
  """
  lyrics = [
    ("Peluk hati kecil yang penuh dendam ini", 0.1),
    ("Ajariku menghapus sebuh rasa benci", 0.1),
    ("Biarkan kasih lembutmu sentuh hatiku", 0.1),
    ("Ubah aku jadi buah hati yang dulu", 0.1),
    ("Peluklah lelah jiwaku, Mama", 0.1),
    ("Yang terluka dipecundangi dunia", 0.1),
    ("Hanya kasihmu yang mampu", 0.1),
    ("Yang tak sekuat hatimu", 0.1)
  ]
  delays = [0.3, 0.5, 0.5, 0.6, 0.8, 1.0, 2.0, 0.5]

  for i in range(len(lyrics)):
    lyric, speed = lyrics[i]
    time.sleep(delays[i])
    animate_text(lyric, speed)

if __name__ == "__main__":
  sing_song()
