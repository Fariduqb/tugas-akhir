"""
"Diskon belanja pada Python"

FITUR: 
- Input Jenis Pelanggan

Non-member → 0%
Member → 10%
VIP → 20%

- Input Kode Voucher (opsional)

Logika Diskon Berdasarkan Jumlah Belanja

Total Belanja	    = Diskon Tambahan
< 100.000	0%
100.000 - 499.999	= 5%
500.000 - 999.999	= 10%
≥ 1.000.000	15%

potongan pembayaran:
Transfer bank Rp10.000
QRIS: tidak ada potongan
Tunai: tidak ada potongan

"""

def diskon_pelanggan(jenis):        # menghitung diskon berdasarkan jenis pelanggan
    jenis = jenis.lower()
    if jenis == "member":
        return 0.10
    elif jenis == "vip":
        return 0.20
    else:
        return 0.0


def diskon_belanja(total):          # menghitung diskon dari total belanja
    if total >= 1_000_000:
        return 0.15
    elif total >= 500_000:
        return 0.10
    elif total >= 100_000:
        return 0.05
    else:
        return 0.0


def potongan_pembayaran(metode):    # potongan dari metode pembayaran
    metode = metode.lower()
    if metode == "transfer":
        return 10_000
    elif metode == "qris":
        return 0
    else:
        return 0

# ====== MULAI PROGRAM ======
print("=== PROGRAM DISKON MEMBER/NON MEMBER ===")

# Input total belanja
try:
    total_belanja = float(input("Masukkan total belanja: Rp "))
except ValueError:
    print("Input tidak valid!")
    exit()

# Input jenis pelanggan
jenis_pelanggan = input("Masukkan jenis pelanggan (non-member/member/vip): ").lower()
if jenis_pelanggan not in ["non", "member", "vip"]:
    print("Jenis pelanggan tidak dikenali!")
    exit()


# Input metode pembayaran 
metode_bayar = input("Metode pembayaran (tunai/transfer/qris): ").lower() #lower() mengecilkan kalimat
if metode_bayar not in ["tunai", "transfer", "qris"]:
    print("Metode pembayaran tidak dikenali!")
    exit()


diskon1 = diskon_pelanggan(jenis_pelanggan)     # Hitung diskon
diskon2 = diskon_belanja(total_belanja)         # Hitung diskon
potongan = potongan_pembayaran(metode_bayar)

# Total diskon persentase
total_diskon_persen = diskon1 + diskon2         
total_diskon_rupiah = total_belanja * total_diskon_persen

# Hitung total yang harus dibayar
harga_setelah_diskon = total_belanja - total_diskon_rupiah - potongan


# Output hasil menggunakan :,.0f untuk nominal harga rupiah
print("\n=== RINCIAN DISKON ===")
print(f"Diskon jenis pelanggan ({diskon1*100:.0f}%)      : Rp{total_belanja * diskon1:,.0f}")
print(f"Diskon belanja ({diskon2*100:.0f}%)              : Rp{total_belanja * diskon2:,.0f}")
print(f"Potongan metode pembayaran             : Rp{potongan:,.0f}")
print(f"Total diskon                           : Rp{total_diskon_rupiah + potongan:,.0f}")
print(f"Total yang harus dibayar               : Rp{harga_setelah_diskon:,.0f}")


"""
tugas: 
- Perbaiki / bersihkan code nya agar fungsional programing
- OOP 
- Buat program tidak berhenti jika sudah selesai dan mulai dari awal lagi
"""