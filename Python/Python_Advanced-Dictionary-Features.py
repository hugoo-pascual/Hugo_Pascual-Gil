##planets = [['Jupiter', 1234], ['Mars', 0.15], ['Saturn', 764]]
##
##solar_system = {planet[0]: planet[1] for planet in planets}
##
##print(solar_system)



#Task 1

##planets = ['Jupiter', 1321, 'Mars', 0.15, 'Saturn', 764]


#One way
##solar_system1 = {}
##
##for i in range(0, len(planets), 2):
##    solar_system1[planets[i]] = planets[i + 1]
##    
##print(solar_system1)



#Another Way

##solar_system = {planets[i] : planets[i + 1] for i in range (0, len(planets), 2)}    # '=' => ':'
##print(solar_system)



#Task 2

solar_system = {1321 : 'Jupiter', 0.15 : 'Mars', 764 : 'Saturn'}


##solar_system_reverse = {solar_system[i] : solar_system[i - 1] for i in range (1, len(solar_system), 2)}
##print(solar_system_reverse)


planets = {value : key for key , value in solar_system.items()}
print(planets)

