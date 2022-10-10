awal = int(input("Dari angka: "))
akhir = int(input("sampai angka : "))
for num in range(awal, akhir + 1):
    if num % 3 == 0:
        print(num)