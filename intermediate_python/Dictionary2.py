world = {
    "Bangladesh": 180,
    "china": 1400,
    "india": 1410,
    "pakistan": 200
}

world["sealand"]=0.00027
print(world)
world["sealand"]=0.00028
print(world)
del(world["sealand"])
print(world)

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Add italy to europe
europe['italy']='rome'

# Print out italy in europe
print(europe)


# Add poland to europe
europe['poland']='warsaw'

# Print europe
print(europe)


# Dictionary of dictionaries
europe1 = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe1['france']['capital'])

# Create sub-dictionary data
data = {'capital': 'rome', 'population': 59.83}


# Add data to europe under key 'italy'
europe1['italy'] = data

# Print europe
print(europe1)