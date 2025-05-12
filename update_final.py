'''
UPDATE PROGRAM DISKON:
- Memisahkan fungsi ke dalam class
- Struktur berbasis class ProgramDiskon
- os.system('clear'/'cls'): Membersihkan terminal sebelum input baru (looping)

'''

import os

class ProgramDiskon:
    def __init__(self):
        self.total_awal = 0
        self.jenis = ""
        self.metode = ""
        self.diskon_pelanggan = 0.0
        self.diskon_belanja = 0.0
        self.potongan = 0
        self.total_bayar = 0.0

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def input_data(self):
        print("=== PROGRAM DISKON MEMBER/NON MEMBER ===")
        try:
            self.total_awal = float(input("Total belanja (Rp): "))
        except ValueError:
            print("Input tidak valid! Masukkan angka.")
            return False

        self.jenis = input("Jenis pelanggan (non/member/vip): ").lower()
        if self.jenis not in ["non", "member", "vip"]:
            print("Jenis pelanggan tidak dikenali!")
            return False

        self.metode = input("Metode bayar (tunai/transfer/qris): ").lower()
        if self.metode not in ["tunai", "transfer", "qris"]:
            print("Metode pembayaran tidak dikenali!")
            return False

        return True

    def hitung_diskon(self):
        # Diskon berdasarkan jenis pelanggan
        if self.jenis == "member":
            self.diskon_pelanggan = 0.10
        elif self.jenis == "vip":
            self.diskon_pelanggan = 0.20
        else:
            self.diskon_pelanggan = 0.0

        # Diskon berdasarkan total belanja
        if self.total_awal >= 1_000_000:
            self.diskon_belanja = 0.15
        elif self.total_awal >= 500_000:
            self.diskon_belanja = 0.10
        elif self.total_awal >= 100_000:
            self.diskon_belanja = 0.05
        else:
            self.diskon_belanja = 0.0

        # Potongan metode pembayaran
        self.potongan = 10_000 if self.metode == "transfer" else 0

        # Hitung total bayar
        total_diskon = self.total_awal * (self.diskon_pelanggan + self.diskon_belanja)
        self.total_bayar = self.total_awal - total_diskon - self.potongan

    def tampilkan_rincian(self):
        print("\n=== RINCIAN BELANJA ===")
        print(f"Diskon pelanggan ({self.diskon_pelanggan*100:.0f}%)\t: Rp{self.total_awal * self.diskon_pelanggan:,.0f}")
        print(f"Diskon belanja ({self.diskon_belanja*100:.0f}%)\t: Rp{self.total_awal * self.diskon_belanja:,.0f}")
        print(f"Potongan pembayaran\t: Rp{self.potongan:,.0f}")
        print(f"Total bayar        \t: Rp{self.total_bayar:,.0f}")
        print()

    def jalankan(self):
        while True:
            self.clear_screen()

            if not self.input_data():
                input("\nTekan ENTER untuk mencoba lagi...")
                continue

            self.hitung_diskon()
            self.tampilkan_rincian()

            ulang = input("Kembali ke menu utama? (YA/TIDAK): ").lower()
            if not ulang.startswith("y"):
                print("Terima kasih!")
                break


if __name__ == "__main__":
    app = ProgramDiskon()
    app.jalankan()
