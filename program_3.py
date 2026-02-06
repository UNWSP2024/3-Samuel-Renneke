#Shipping Charges
#Samuel Renneke, 2/6/2026

def weight_conversion(weight):
    # Calculate the shipping charge.
    if weight <= 2:
        shippingCost = weight * 1.5
    elif 2 < weight <= 6:
        shippingCost = weight * 3
    elif 6 < weight <= 10:
        shippingCost = weight * 4
    else:
        shippingCost = weight * 4.75
    return shippingCost


#### This piece of the code has been done for you,
#### you only need to worry about the actual shipping
#### charge logic in the weight_conversion function
if __name__ == '__main__':
    # Local variables
    weight = 0.0
    shippingCost = 0.0
    # Get package weight from the user.
    weight = float(input('Enter the weight of the package: '))
    # Display the shipping charge.
    shippingCost = weight_conversion(weight)
    print('Shipping charge: $', format(shippingCost, '.2f'))
