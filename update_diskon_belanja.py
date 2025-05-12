def hitung_diskon_pelanggan(jenis):
    if jenis == "member":
        return 0.10
    elif jenis == "vip":
        return 0.20
    return 0.0

def hitung_diskon_belanja(total):
    if total >= 1_000_000:
        return 0.15
    elif total >= 500_000:
        return 0.10
    elif total >= 100_000:
        return 0.05
    return 0.0

def potongan_metode_bayar(metode):
    if metode == "transfer":
        return 10_000
    return 0

def tampilkan_rincian(diskon_pelanggan, diskon_belanja, potongan, total_awal, total_bayar):
    print("\n=== RINCIAN ===")
    print(f"Diskon pelanggan ({diskon_pelanggan*100:.0f}%)\t: Rp{total_awal * diskon_pelanggan:,.0f}")
    print(f"Diskon belanja ({diskon_belanja*100:.0f}%)\t: Rp{total_awal * diskon_belanja:,.0f}")
    print(f"Potongan pembayaran\t: Rp{potongan:,.0f}")
    print(f"Total bayar        \t: Rp{total_bayar:,.0f}")
    print()

def program_diskon():
    ulang = 'ya'
    while ulang.lower().startswith("y"):
        print("\n=== PROGRAM DISKON MEMBER/NON MEMBER ===")
        try:
            total_awal = float(input("Total belanja (Rp): "))
        except ValueError:
            print("Input tidak valid!")
            continue

        jenis = input("Jenis pelanggan (non/member/vip): ").lower()
        if jenis not in ["non", "member", "vip"]:
            print("Jenis pelanggan tidak dikenali!")
            continue

        metode = input("Metode bayar (tunai/transfer/qris): ").lower()
        if metode not in ["tunai", "transfer", "qris"]:
            print("Metode pembayaran tidak dikenali!")
            continue

        diskon_pelanggan = hitung_diskon_pelanggan(jenis)
        diskon_belanja = hitung_diskon_belanja(total_awal)
        potongan = potongan_metode_bayar(metode)

        total_diskon = total_awal * (diskon_pelanggan + diskon_belanja)
        total_bayar = total_awal - total_diskon - potongan

        tampilkan_rincian(diskon_pelanggan, diskon_belanja, potongan, total_awal, total_bayar)

        ulang = input("Kembali ke menu utama? (YA/TIDAK): ")

    print("Terima kasih!")

if __name__ == "__main__":
    program_diskon()

"""
pisahkan untuk menjadi 1 fungsi
OOP nya kurang jelas
Looping kurang bersihkan terminal
"""