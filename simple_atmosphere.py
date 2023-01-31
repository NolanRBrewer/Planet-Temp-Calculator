# modules
import sys

'''
Purpose:
Calculation should be simple:
Given the solar constant of earth
    1367 watts per meter squared at one AU orbit 
Determine solar constant of various planets given orbital radius only.
From the solar constant and albedo combined with the Stefan-Boltzmann constant 
a temperature calculation can be made for a body with a simple atmosphere
'''


def rules():
    rule_1 = "For solar constants input 'solar\ constant' the planets name then orbital radius in AU (astronomical units)"
    rule_2 = "For a simple atmosphere input 'simple\ atmosphere' the orbital radius in AU and the percentage of light reflected by planet"
    return (f"Inputs:\n {rule_1}\n {rule_2} ")


def solar_constant(orbital_radius: float) -> float:
    e_constant = 1367  # watts per meter sqaured
    planet_constant = e_constant // (orbital_radius**2)
    return planet_constant


def simple_atmosphere(p_constant: float, albedo: float) -> float:
    # Stefan-Boltzmans constant
    sb_constant = 5.67*10 ** -8
    atmo_temp = (2*p_constant * (1 - albedo)) / (4 * sb_constant)
    return atmo_temp ** 0.25


if sys.argv[1] == "rules":
    print(rules())
elif sys.argv[1] == "solar constant":
    p_constant = solar_constant(float(sys.argv[3]))
    print(
        f"The solar constant of {sys.argv[2]} is : {p_constant} watts per meter squared.")
elif sys.argv[1] == "simple atmosphere":
    albedo = float(sys.argv[3]) / 100
    p_constant = solar_constant(float(sys.argv[2]))
    print(
        f"The simple atmosphere temperature of this planet is: {simple_atmosphere(p_constant, albedo)} degrees Kelvin")

else:
    print("Enter valid command: 'rules', 'solar\ constant', or ' simple\ atmosphere'. ")
