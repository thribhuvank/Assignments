"""
Q1. Write a program to determine how much discount a customer can get based on the below conditions:
A customer gets the following discounts based on the respective criteria:
    1. 15 % on first purchase at the store.
    2. 10 % if he/she has a membership card
    3. 5% if senior citizen
    4. 10 % on coupons
Note:
    1. Only 2 discounts can be clubbed together, any 2 that give the highest discount
    2. New customers cannot redeem coupons or get membership card discount 
Sample output:
Eg 1: Customer is senior citizen and has a membership card
Output: 15%
Eg 2: Customer is senior citizen and has both coupon and membership card
Output: 20% 

"""

# Taking inputs from user
first_purchase = input("is it customers first purchase at the store (Yes/No) : ")
membership_card = input("is customers has a membership card  (Yes/No) : ")
senior_citizen = input("is customer is senior citizen (Yes/No) : ")
coupon_available = input("is customers has a coupon (Yes/No) : ")

# declaring discuounts
max_discount = 0
first_purchase_discount = 15
membership_card_discount = 10
senior_citizen_discount = 5
coupon_available_discount = 10

# calculating discounts based on customer inputs
if first_purchase == 'Yes':
    if membership_card == 'Yes':
        max_discount = max_discount + first_purchase_discount + membership_card_discount
    elif coupon_available == 'Yes':
        max_discount = max_discount + first_purchase_discount + coupon_available_discount
    elif senior_citizen == 'Yes':
        max_discount = max_discount + first_purchase_discount + senior_citizen_discount
    else:
        max_discount = max_discount + first_purchase_discount
    
elif membership_card == 'Yes':
    if senior_citizen == 'Yes':
        if coupon_available == 'Yes':
            max_discount = max_discount + membership_card_discount + coupon_available_discount
        else:
            max_discount = max_discount + membership_card_discount + senior_citizen_discount
    
    elif coupon_available == 'Yes':
        max_discount = max_discount + membership_card_discount + coupon_available_discount
    
    else:
        max_discount = max_discount + membership_card_discount

elif senior_citizen == 'Yes':
    if coupon_available == 'Yes':
        max_discount = max_discount + senior_citizen_discount + coupon_available_discount
    else:
        max_discount = max_discount + senior_citizen_discount

elif coupon_available == 'Yes':
    max_discount = max_discount + coupon_available_discount

else:
    print("Please provide valid inputs")


# printing maximum discount given for customer
print(str(max_discount) + '%')