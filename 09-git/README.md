# Lab 09 - Git

Lab ini tidak berisi kode Python. Langkah-langkahnya:

1. **Unduh berkas lab sebelumnya** – di VS Code, klik kanan folder di Explorer → *Download*, lalu ekstrak berkas zip-nya.
2. **Buat akun GitHub** di <https://github.com>.
3. **Baca panduan Hello World** di <https://docs.github.com/en/get-started/start-your-journey/hello-world>.
4. **Buat repository private** – klik *New*, beri nama `aws_restart`, pilih *Private*, centang *Add a README file*.
5. **Upload berkas** – klik *Add file → Upload files*, unggah semua berkas hasil ekstrak.
6. **Unduh repository** – klik *Code → Download ZIP*, simpan ke folder `aws_restart` lalu ekstrak untuk verifikasi.

## Alternatif lewat command line

```bash
git clone https://github.com/<username>/aws_restart.git
cd aws_restart
# salin berkas lab ke folder ini
git add .
git commit -m "Add Python lab files"
git push
```
