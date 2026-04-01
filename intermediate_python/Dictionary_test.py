
world = {
    "Bangladesh": 180,
    "china": 1400,
    "india": 1410,
    "pakistan": 200
}

print(world["Bangladesh"])

for country, population in world.items():
    if population == 1400:
        print(country)

        # Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ind_ger = countries.index('germany')

# Use ind_ger to print out capital of Germany
print(capitals[ind_ger])


# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# From string in countries and capitals, create dictionary europe
europe = {'spain':'madrid','france':'paris','germany':'berlin','norway':'oslo' }

# Print europe
print(europe)

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print out the keys in europe
print(europe.keys())


# Print out value that belongs to key 'norway'
print(europe['norway'])