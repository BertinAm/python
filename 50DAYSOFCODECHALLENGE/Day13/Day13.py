# Day13: 50daysofcodechallenge
def your_vat():
    try:
        price = float(input("Enter the price \n"))
        VAT = float(input("Enter the percentage %"))
        while True:
            if len(str(price)) > 0 and price != 0 and VAT > 0:
                perc = (VAT / 100) * price
                return round(price + perc)
                break

            elif len(str(price)) < 0 or price == 0 or VAT <= 0:
                print("Invalid Input")
                price = int(input("Enter the price \n"))
                VAT = float(input("Enter the percentage %"))
                continue
    except ValueError:
        print("You entered something other than numbers")
        price = float(input("Enter the price \n"))
        VAT = float(input("Enter the percentage %"))
        perc = (VAT / 100) * price
        return round(price + perc)


print(your_vat())

