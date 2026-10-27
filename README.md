# Python Basic – Contoh Kode Lab

Contoh kode untuk 17 lab di modul *Python Basic*. Setiap folder = satu lab.
Jalankan skrip **dari dalam folder lab-nya** (beberapa lab membaca berkas relatif), misalnya:

```bash
cd 06-composite-data-types
python3 composite-data.py
```

| No | Folder | Berkas | Topik |
|---|---|---|---|
| 01 | `01-hello-world` | `hello-world.py` | print() pertama |
| 02 | `02-numeric-data-types` | `numeric-data.py` | int, float, complex, bool |
| 03 | `03-string-data-types` | `string-data-type.py` | string, konkatenasi, input(), format() |
| 04 | `04-list-tuple-dictionary` | `collections-demo.py` | list, tuple, dictionary |
| 05 | `05-categorize-values` | `categorize-values.py` | list campuran + for loop |
| 06 | `06-composite-data-types` | `composite-data.py`, `car_fleet.csv` | csv, deepcopy, list of dict |
| 07 | `07-conditionals` | `conditionals.py` | if / elif / else |
| 08 | `08-loops` | `while-loop.py`, `for-loop.py` | while, for, random |
| 09 | `09-git` | `README.md` | GitHub (tanpa kode) |
| 10 | `10-analyze-with-python` | `preproinsulin-seq.txt`, `analyze-insulin.py` | membersihkan sekuens insulin (bonus regex) |
| 11 | `11-string-sequence-numeric-weight` | `string-insulin.py` | string, berat molekul |
| 12 | `12-lists-and-loops` | `net-charge.py` | net charge pH 0–14 |
| 13 | `13-caesar-cipher` | `caesar-cipher.py` | user-defined function |
| 14 | `14-file-handlers` | `calc_weight_json.py`, `jsonFileHandler.py`, `files/insulin.json` | modul, JSON, try/except |
| 15 | `15-system-administration` | `sys-admin.py`, `sys-admin-windows.py` | os.system, subprocess.run (Linux / Windows) |
| 16 | `16-debugger` | `debugger.py` | breakpoint & watch di VS Code |
| 17 | `17-debugging-caesar-cipher` | `debug-caesar-1..4.py`, `solusi/` | mencari bug dengan debugger |

Catatan:
- Lab 04 tidak memakai nama `collections.py` (seperti contoh di modul) agar tidak menutupi modul bawaan Python `collections`.
- Lab 15: `sys-admin.py` memakai perintah Linux (`ls`, `uname`, `ps`) untuk lingkungan lab/Linux/WSL; `sys-admin-windows.py` adalah padanannya untuk Windows (`dir`, `ver`, `tasklist`).
- Folder `17-debugging-caesar-cipher/solusi/` berisi kunci jawaban. Hapus atau sembunyikan folder ini sebelum dibagikan ke peserta.
