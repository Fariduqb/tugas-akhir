


import datetime

# Fungsi untuk menghitung diskon berdasarkan jenis pelanggan
def diskon_pelanggan(jenis):
    jenis = jenis.lower()
    if jenis == "member":
        return 0.10
    elif jenis == "vip":
        return 0.20
    else:
        return 0.0

# Fungsi untuk menghitung diskon dari total belanja
def diskon_belanja(total):
    if total >= 1_000_000:
        return 0.15
    elif total >= 500_000:
        return 0.10
    elif total >= 100_000:
        return 0.05
    else:
        return 0.0


def diskon_voucher(kode):
    today = datetime.datetime.now()
    kode = kode.upper()
    kode_valid = today.strftime("%b").upper() + str(today.day)
    if kode == kode_valid:
        return 0.05
    return 0.0

# Fungsi potongan dari metode pembayaran
def potongan_pembayaran(metode):
    metode = metode.lower()
    if metode == "transfer":
        return 10_000
    elif metode == "qris":
        return 5_000
    else:
        return 0

# ====== MULAI PROGRAM ======
print("=== PROGRAM DISKON SEDERHANA ===")

# Input total belanja
try:
    total_belanja = float(input("Masukkan total belanja: Rp "))
except ValueError:
    print("Input tidak valid!")
    exit()

# Input jenis pelanggan
jenis_pelanggan = input("Masukkan jenis pelanggan (non-member/member/vip): ").lower()
if jenis_pelanggan not in ["non-member", "member", "vip"]:
    print("Jenis pelanggan tidak dikenali!")
    exit()

# Input kode voucher
kode_voucher = input("Masukkan kode voucher (opsional): ")

# Input metode pembayaran
metode_bayar = input("Metode pembayaran (tunai/transfer/qris): ").lower()
if metode_bayar not in ["tunai", "transfer", "qris"]:
    print("Metode pembayaran tidak dikenali!")
    exit()

# Hitung diskon
diskon1 = diskon_pelanggan(jenis_pelanggan)
diskon2 = diskon_belanja(total_belanja)
diskon3 = diskon_voucher(kode_voucher)
potongan = potongan_pembayaran(metode_bayar)

# Total diskon persentase
total_diskon_persen = diskon1 + diskon2 + diskon3
total_diskon_rupiah = total_belanja * total_diskon_persen

# Hitung total yang harus dibayar
harga_setelah_diskon = total_belanja - total_diskon_rupiah - potongan


# Output hasil
print("\n=== RINCIAN DISKON ===")
print(f"Diskon jenis pelanggan ({diskon1*100:.0f}%) : Rp{total_belanja * diskon1:,.0f}")
print(f"Diskon belanja ({diskon2*100:.0f}%)           : Rp{total_belanja * diskon2:,.0f}")
if diskon3 > 0:
    print(f"Diskon voucher ({diskon3*100:.0f}%)         : Rp{total_belanja * diskon3:,.0f}")
else:
    print("Diskon voucher                             : Tidak berlaku")
print(f"Potongan metode pembayaran                 : Rp{potongan:,.0f}")
print(f"Total diskon                               : Rp{total_diskon_rupiah + potongan:,.0f}")
print(f"Total yang harus dibayar                   : Rp{harga_setelah_diskon:,.0f}")