 cars=100
space_in_a_car=4.0
drivers=30
passengers=90
cars_not_driven=cars-drivers
cars_driven=drivers
caporal_capacity=cars_driven*space_in_a_car
averange_passengers_per_car=passengers/cars_driven


print("There are ", cars,"cars availables.")
print("There are only",drivers,"drivers availables.")
print("There will be ", cars_not_driven,"empty cars today.")
print("We can tranport",caporal_capacity,"people today.")
print("We have ", passengers,"to caporal today.")
print("We need to put about",averange_passengers_per_car,"in each car.")
