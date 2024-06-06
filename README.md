Untuk menambahkan cara menjalankan proyek Anda di file README GitHub, Anda dapat mengikuti langkah-langkah berikut:

1. **Unduh dataset**: Tambahkan bagian di README yang menjelaskan cara mengunduh dataset. Anda dapat menyertakan link ke Google Drive atau tempat penyimpanan lainnya, serta memberikan instruksi tentang cara mengunduh dan menempatkan dataset di dalam proyek.

    ```markdown
    ## Unduh Dataset

    Anda dapat mengunduh dataset untuk proyek ini dari tautan berikut:

    [Download Dataset](https://drive.google.com/file/d/1crLu-zsVLiWEdjsL9JporpKpiDo69wGk/view?usp=sharing)

    Setelah mengunduh dataset, letakkan file-file tersebut di dalam folder `data`.
    ```

2. **Membuat file .env**: Berikan instruksi kepada pengguna tentang bagaimana cara membuat file `.env` dan mengisi variabel lingkungan yang diperlukan untuk koneksi ke database PostgreSQL. Anda juga dapat memberikan contoh isi file `.env`.

    ```markdown
    ## Konfigurasi .env

    Untuk menjalankan proyek ini, Anda perlu membuat file `.env` di dalam folder `env` dan mengisi variabel lingkungan berikut:

    ```
    POSTGRES_USER=your_username
    POSTGRES_PASSWORD=your_password
    POSTGRES_HOST=your_host
    POSTGRES_PORT=your_port
    POSTGRES_DB=your_database
    ```

    Pastikan untuk mengganti `your_username`, `your_password`, `your_host`, `your_port`, dan `your_database` dengan informasi koneksi PostgreSQL Anda.
    ```

3. **Cara Menjalankan Proyek**: Berikan instruksi tentang cara menjalankan proyek setelah dataset dan file `.env` telah disiapkan. Anda dapat memberikan contoh perintah yang perlu dijalankan.

    ```markdown
    ## Cara Menjalankan Proyek

    1. Unduh dataset dan simpan di dalam folder `data`.
    2. Buat file `.env` di dalam folder `env` dan isi dengan informasi koneksi PostgreSQL seperti yang dijelaskan di atas.
    3. Jalankan perintah berikut untuk memulai proyek:

    ```bash
    python main.py
    ```
    ```

Dengan menambahkan panduan langkah demi langkah seperti di atas, pengguna proyek Anda akan lebih mudah memahami cara menjalankannya. Pastikan untuk memberikan instruksi yang jelas dan lengkap agar tidak ada kebingungan.
