# Kunci Jawaban Lab 17 (untuk trainer)

| Berkas | Gejala | Penyebab | Perbaikan |
|---|---|---|---|
| `debug-caesar-1.py` | `TypeError: unsupported operand type(s) for +: 'int' and 'str'` | `input()` mengembalikan string, lalu dijumlahkan dengan int | `newPosition = position + int(cipherKey)` |
| `debug-caesar-2.py` | Hanya huruf kapital yang terenkripsi (`CYU Testart rocks!`) | Pesan tidak diubah ke huruf besar, padahal alfabet berisi huruf besar saja | `uppercaseMessage = message.upper()` |
| `debug-caesar-3.py` | Dekripsi malah menggeser lagi ke depan (`EAW VIWXEVX ...`) | `decryptMessage` mengirim `cipherKey`, bukan `decryptKey` | `return encryptMessage(message, decryptKey, alphabet)` |
| `debug-caesar-4.py` | Hasil dekripsi sama dengan hasil enkripsi | `print` menampilkan variabel yang salah | `print(f'Decrypted Message: {myDecryptedMessage}')` |

Versi yang sudah diperbaiki ada di folder ini: `debug-caesar-1-fixed.py` s.d. `debug-caesar-4-fixed.py`.
