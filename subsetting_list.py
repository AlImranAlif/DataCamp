fam=["alif",1.75,"samim",1.70,"abbu",1.68,"ammu",1.65,"dadi",1.50]
print(fam)
print(fam[1])
print(fam[2:4])

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
# Use slicing to create downstairs
downstairs = areas[:6]

# Use slicing to create upstairs
upstairs = areas[-4:]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)