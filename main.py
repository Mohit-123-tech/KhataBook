import Khatabook
from colorama import Fore

with open(Khatabook.API["keyPath"], "r") as F:
    Key = F.read()
    F.close()

if Key == Khatabook.API["ActivationKey"]:
    while True:
        try:
            Code = int(input("Enter Code : "))
        except(Exception):
            print(Fore.RED,"Unknow Code",Fore.WHITE)
            exit()

        if Code == 1:
            Number = input("Enter Number : ")
            Name = input("Enter Name : ")
            Khatabook.DataBase.Createkhata(Name, Number)

        elif Code == 2:
            Number = input("Enter Number : ")
            Name = input("Enter Name : ")
            Amount = input("Enter Amount : ")
            Khatabook.DataBase.AddDataToKhata(Name, Number, Amount)

        elif Code == 3:
            Number = input("Enter Number : ")
            Name = input("Enter Name : ")
            print(Khatabook.DataBase.ShowData(Name, Number))

        elif Code == 4:
            Number = input("Enter Number : ")
            Name = input("Enter Name : ")
            Khatabook.DataBase.DeleteKhata(Name, Number)

        elif Code == 0:
            break

        else:
            print(Fore.RED,"Code Not Found",Fore.WHITE)

else :
    print(Fore.RED,"Activate Product",Fore.WHITE)
