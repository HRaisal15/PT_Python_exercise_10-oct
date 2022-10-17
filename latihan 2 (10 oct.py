awal = int(input("Dari Angka: "))
akhir = int(input("Sampai Angka: "))
for num in range(awal, akhir + 1):
    if num % 3 == 0:
        print(num)
        