# Lab 15 - System Administration (versi Windows)
# Padanan perintah Linux -> Windows:
#   ls        -> dir      (perintah bawaan cmd, jadi dipanggil lewat "cmd /c")
#   ls -l     -> dir /q   (menampilkan pemilik berkas)
#   uname -a  -> ver      (perintah bawaan cmd)
#   ps -x     -> tasklist

import os
import subprocess

# Exercise 1: os.system
os.system("dir /b")

# Exercise 2-4: subprocess.run dengan 1, 2, dan 3 argumen
subprocess.run(["cmd", "/c", "dir", "/b"])
subprocess.run(["cmd", "/c", "dir", "/q"])
subprocess.run(["cmd", "/c", "dir", "/q", "README.md"])

# Exercise 5: informasi sistem
command = "ver"
# flush=True agar teks ini muncul sebelum output dari subprocess
print(f'Gathering system information with command: {command}', flush=True)
subprocess.run(["cmd", "/c", command])

# Exercise 6: informasi proses aktif
command = "tasklist"
commandArgument = "/fi"
commandFilter = "STATUS eq RUNNING"
print(f'Gathering active process information with command: {command} '
      f'{commandArgument} "{commandFilter}"', flush=True)
subprocess.run([command, commandArgument, commandFilter])
