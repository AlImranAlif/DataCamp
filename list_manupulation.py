fam=["alif",1.75,"samim",1.70,"abbu",1.68,"ammu",1.65,"dadi",1.50]
fam[5]=1.66
print(fam)
fam[7:8]=[1.60]
print(fam)

add_fam=fam + ["dada",1.72]
print(add_fam)


del[add_fam[10]]
print(add_fam)


# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1]=10.50


# Change "living room" to "chill zone"
areas[4]="chill zone"

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse",24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage",15.45]
print(areas_2)