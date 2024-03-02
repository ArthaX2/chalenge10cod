input_angka = int(input("Masukkan jumlah angka : "))


fib_list = []
a, b = 1, 1


for _ in range(input_angka):
    fib_list.append(a)
    a, b = b, a + b


print("Deret Fibonacci:", fib_list)