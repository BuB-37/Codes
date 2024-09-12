print("TOTAL TRIP COST CALCULATION")
print("")
print("Your buget is 1600")
print("--------------------------------------------") 
# functions
def rental_car_cost (days) :
    cost_per_day = 60
    total_cost = days * cost_per_day
    if days >= 7:
        total_cost -= 50 # Discount for 7 or  more days
    elif days >= 3:
        total_cost -= 20 # Discount for 3 or more days
    return total_cost

def plane_ride_cost(hours) :
    cost_per_hour = 75
    total_plane_cost = hours * cost_per_hour
    if hours >= 3:
        total_plane_cost += 25 # over 3 hours means extra 25 dollars
    return total_plane_cost

def hotel_cost(hoteldays):
    hotel_per_day = 200
    total_hotel_cost = hoteldays * hotel_per_day
    package_input = int(input ("Enter '1' if you want premium package which cost 25 dollars extra or press '2' if you want deluxe package which cost extra 50 dollars : "))
    print("")
    if package_input == 1:
        total_hotel_cost += 25
    elif package_input == 2:
        total_hotel_cost += 50
    else:
        print("Enter valid input!")
    return total_hotel_cost

#input for functions
car_days = int(input( 'How many days are you renting the car : '))
print("")
plane_hours = int(input ("How many hours is your plane : "))
print("")
hotel_days = int(input ("How many days are you staying in the hotel : "))
print("")

# functions into variables
plane = plane_ride_cost(plane_hours)
hotel = hotel_cost(hotel_days)
car = rental_car_cost(car_days)

#function outputs
print ('Cost of hotel: ',hotel)
print ('Cost of car rental: ',car)
print ('Cost ofplane ride: ',plane)

#check if in buget
print("")
total_trip_cost = hotel + car + plane
left = 1600-total_trip_cost

if total_trip_cost < 1600:
    print("Trip cost is within buget!")
    print("You've saved : ",left,"Dollars")
else:
    print("Trip cost is not within buget!!")