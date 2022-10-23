from Class.Accounting import Accounting
from Class.Programming import Programming
from Class.Sale import Sale

def main():
    accounting = Accounting('Employee1', 500, 2)
    print(accounting.getData())

    print('\n---------------')

    programmer = Programming('Employee2', 100, 1, 'GameDev')
    print(programmer.getData())

    print('\n---------------')

    sale = Sale('Employee3', 300, 'Chiang Mai')
    print(sale.getData())
    
if __name__ == "__main__":
    main()
# end main