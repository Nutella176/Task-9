#Set variables
air_mail = 0.36     #per Kilometer
freight_mail = 0.25 #per Kilometer
full_insurance = 50.00 
limited_insurance = 25.00
gift_yes = 15.00 
gift_no = 0.00
priority = 100.00 
standard = 20.00

#Get user to input product price and distance of delivery in kms
input_price = float(input("Please enter the price of the item you wish to purchase: "))
input_distance = float(input("Please enter the total distance of the delivery in kilometres:  "))

#Get user to choose between two options for each of the following and input answer: transport method, insurance, gift option and delivery speed
transport_method = input("Please choose between air mail or freight (air or freight): ")
insurance = input("Would you like full or limited insurance? (full or limited) ")
gift = input("Is it a gift? (yes or no) ")
delivery_speed = input("Please select either priority or standard delivery: (priority or standard): ")

#Set conditions
if transport_method == "air":
    transport_method_cost = air_mail
else:
    transport_method_cost = freight_mail
    
if insurance == "full":
    insurance_cost = full_insurance
else:
    insurance_cost = limited_insurance
    
if gift == "yes":
    gift_cost = gift_yes
else:
    gift_cost = gift_no
    
if delivery_speed == "priority":
    delivery_speed_cost = priority
else:
    delivery_speed_cost = standard

#Total cost calculation    
total_cost = (input_price + (input_distance * transport_method_cost) + insurance_cost + gift_cost + delivery_speed_cost)
    
print(f"The total cost for your parcel and postage is R{total_cost}")