print("Asal Sayı tespit ediciye hoşgeldiniz.")

while True:
    try:
        number = int(input("Sayı girişi yapınız:"))
    except:
        print("Yalnızca sayı girilmelidir!!")
        continue
    else:
        print("Sayı girişi yapıldı.")
        break


if number == 0:
    print("Asal sayı değildir.")

if number == 1:
    print("Asal sayı değildir.")

for a in range(number,-1):
    if a < 0:
        print("Negatif sayılarda asallık aranmaz!!")
        break

if number > 1:
    for i in range(2,number):
        if (number % i) == 0:
            print("Asal Sayı değildir.")
            break
    else:
        print("Asal sayıdır.")