# Lab 15 - System Administration
# Catatan: perintah ls, uname, dan ps adalah perintah Linux (lingkungan lab).

import os
import subprocess

# Exercise 1: os.system
os.system("ls")

# Exercise 2-4: subprocess.run dengan 1, 2, dan 3 argumen
subprocess.run(["ls"])
subprocess.run(["ls", "-l"])
subprocess.run(["ls", "-l", "README.md"])

# Exercise 5: informasi sistem
command = "uname"
commandArgument = "-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command, commandArgument])

# Exercise 6: informasi proses aktif
command = "ps"
commandArgument = "-x"
print(f'Gathering active process information with command: {command} '
      f'{commandArgument}')
subprocess.run([command, commandArgument])
