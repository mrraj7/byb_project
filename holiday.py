# ==================================== Practical Task 1 ===================================
# This  program is to calculate a user’s total holiday cost, which includes the
# plane cost, hotel cost, and car-rental cost in sterling pounds.

# This function will take num_nights as an argument, and return a cost for the flight
def hotel_cost(num_nights):
    hotel_cost = 120 * num_nights
    return hotel_cost

# This function will take city_flight as an argument and return a cost for the flight 
def plane_cost(city_flight):
    if city == 1:
        cost = 250
    elif city == 2:
        cost = 300
    else:
        cost = 400
    return cost

# This function will take rental_days as an argument and return the total cost of the car rental 
def car_rental(rental_days):
    car_rental_cost = 100 * rental_days
    return car_rental_cost

# This function will take the three argument hotel_cost, plane_cost, car_rental 
# to calculate a total cost for the holiday
def holiday_cost():
    return

# This function displays the available city options and asks the user to input chose the city they will be flying to 
def city_options():
    while True:
        print("Which city you want to travel? Your options are :")
        print("1 - Bristol")
        print("2 - Birmingham")
        print("3 - Manchester")
        city_choice = int(input("Enter the option : "))
        if city_choice < 1 or city_choice > 3:
            print("Option not valid. Enter the valid option number ")
        else:
            break
    return city_choice

# Get the user input for the city they will be flying to
city = city_options()

# Get the user input for number of nights they will be staying in hotel
nights = int(input("Enter the number of nights for stay in hotel : "))

# Get the user input for number of days for which they will be hiring a car
car_rental_days = int(input("Enter the number of days you want to rent a car : "))

# Call the function plane_cost to get the flight ticket cost
flight_cost = plane_cost(city)

# Call the function hotel_cost to get the flight ticket cost
total_hotel_cost = hotel_cost(nights)

# Call the function car_rental to get the flight ticket cost
total_car_rental_cost = car_rental(car_rental_days)

# Calculate the total holiday cost
total_holiday_cost = flight_cost + total_hotel_cost + total_car_rental_cost

# Print the output of flight ticket cost, hotel stay cost, car rental cost and finally total holiday cost
print("===================================================")
print(f"Cost of return flight ticket : £ {flight_cost}")
print(f"Hotel stay cost for {nights} nights : £ {total_hotel_cost}")
print(f"Car rental cost for {car_rental_days} days : £ {total_car_rental_cost} ")
print("===================================================")
print(f"Total holiday cost : £ {total_holiday_cost} ")
print("===================================================")
