import math
import sys
"""
Purpose:
By taking the required inputs, return the blackbody temperature of those variables.
"""
"""
Necessary inputs:
Average temperature of the planet's home star
Albedo: this is the percentage of light not absorbed by the planet
Radius of the star: in Astronomical Units (Au)
Radius of the planet's orbit around home star: in Astronomical Units (Au)
Output:
Equilibrium Temperature of a planet. 
This is the temperature of a planet being only heated by the incident stellar energy. 
This does NOT account for the presence of an atmosphere or greenhouse effect.
"""


def rules():
    rule_1 = "Temperature of the star in Kelvin"
    rule_2 = "The percentage of light reflected by the planet"
    rule_3 = "Radius of the planet's orbit in AU (Astronomical Units)"
    rule_4 = "Radius of the star in AU (Astornomical Units)"
    return f" Inputs:\n {rule_1}\n {rule_2}\n {rule_3}\n {rule_4}"


def equilibrium_temperature(temp_stellar, albedo, orbital_radius, radius_stellar):
    # The temperature of a planet without atmosphere
    albedo = albedo / 100
    orbital_value = radius_stellar / (2 * orbital_radius)
    true_orbital_value = math.sqrt(orbital_value)

    equivalent_blackbody_temp = (temp_stellar *
                                 (1 - albedo)**.25 * true_orbital_value)
    return equivalent_blackbody_temp


# inputs only:
if sys.argv[1] == "rules":
    print(rules())
elif sys.argv[1] == "blackbody":
    # inputs for blackbody temperature
    temp_stellar = float(sys.argv[2])
    albedo = float(sys.argv[3])
    orbital_radius = float(sys.argv[4])
    radius_stellar = float(sys.argv[5])
    # Equilibrium temperature output
    temp_eq = (equilibrium_temperature
               (temp_stellar, albedo, orbital_radius, radius_stellar))
    # show result
    print(f"Equilibrium temperature this planet is : {temp_eq} K")
else:
    print("Please enter either: 'rules' or 'blackbody\ temp")
