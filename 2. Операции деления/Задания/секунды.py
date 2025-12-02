seconds = int(input("Введите число секунд"))
hours = seconds // 3600
minutes = seconds % 3600 // 60
seconds %= 60
print(f"{hours}:{minutes}:{seconds}")

