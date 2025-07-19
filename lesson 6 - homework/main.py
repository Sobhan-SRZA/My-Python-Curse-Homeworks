# برنامه اي بنويسيد که ماتريسي را از ورودي گرفتهو مجموع همه عناصر ماتريس را محاسبه کند.

rows = int(input("Tedad satr hara vared konid: "))

cols = int(input("Tedad soton hara vared konid: "))

matrix = []

total_matrix_sum = 0

for i in range(rows):

    row = input(f"Satre {i + 1} - Adad ra ba fasele vared konid: ").split()

    row = [int(x) for x in row]
    
    if len(row) != cols:
        print("Tedad soton ha dorost nist!")
        exit()

    matrix.append(row)
    total_matrix_sum += sum(row)

print("Matrixe vared shode: ")
for row in matrix:
    print(row)

print("Magmoe anasor: ", total_matrix_sum)
