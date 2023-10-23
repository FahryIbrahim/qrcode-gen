# English
---
# QR Code Generator with Optional Logo and Color Customization

A simple script to generate QR codes based on user input. The generated QR code can optionally include a logo in the center or be customized with user-specified colors.

## Prerequisites

- Python 3
- `qrcode` module. Install using pip:

  ```bash
  pip install qrcode[pil]
  ```

## How to Use

1. Run the script:

   ```bash
   python <script_name>.py
   ```

2. You will be prompted to enter a URL. This is the data that will be encoded into the QR code.

3. Decide if you want to embed a logo into your QR code. If you choose yes, you will be prompted to provide the path to the logo image.

4. If you do not embed a logo, you can choose to customize the QR code's foreground and background colors. By default, the QR code will be generated in black and white.

5. The generated QR code will be saved as `qr.png` in the directory where the script is located.

## Code Overview

The script uses the `qrcode` library to generate the QR code. The flow of the program is as follows:

1. Create a QR code object with specified parameters.
2. Take the URL input from the user.
3. Check if the user wants to embed a logo. If yes, ask for the logo path.
4. If no logo is provided, check if the user wants to customize the QR code colors. If yes, ask for the foreground and background colors.
5. Save the generated QR code as `qr.png`.

---

Feel free to modify or add any additional information you think might be useful!

---

# Bahasa Indonesia

---

# Pembuat QR Code dengan Opsi Logo dan Kustomisasi Warna

Sebuah skrip sederhana untuk menghasilkan QR code berdasarkan masukan pengguna. QR code yang dihasilkan dapat memasukkan logo di tengahnya atau disesuaikan dengan warna yang ditentukan oleh pengguna.

## Persyaratan

- Python 3
- Modul `qrcode`. Instalasi dapat dilakukan dengan perintah pip berikut:

  ```bash
  pip install qrcode[pil]
  ```

## Cara Menggunakan

1. Jalankan skrip ini:

   ```bash
   python <nama_script>.py
   ```

2. Anda akan diminta untuk memasukkan URL. Ini adalah data yang akan dienkripsi ke dalam QR code.

3. Tentukan apakah Anda ingin memasukkan logo ke dalam QR code. Jika Anda memilih ya, Anda akan diminta untuk menyediakan jalur logo.

4. Jika Anda tidak memasukkan logo, Anda dapat memilih untuk menyesuaikan warna latar dan warna forground QR code. Secara default, QR code akan dihasilkan dalam warna hitam dan putih.

5. QR code yang dihasilkan akan disimpan sebagai `qr.png` dalam direktori di mana skrip ini berada.

## Gambaran Kode

Skrip ini menggunakan pustaka `qrcode` untuk menghasilkan QR code. Alur program adalah sebagai berikut:

1. Membuat objek QR code dengan parameter yang telah ditentukan.
2. Mengambil masukan URL dari pengguna.
3. Periksa apakah pengguna ingin memasukkan logo. Jika ya, minta jalur logo.
4. Jika tidak ada logo yang diberikan, periksa apakah pengguna ingin menyesuaikan warna QR code. Jika ya, minta warna latar dan forground.
5. Menyimpan QR code yang dihasilkan sebagai `qr.png`.

---

Anda dapat mengubah atau menambahkan informasi tambahan yang Anda anggap berguna!
