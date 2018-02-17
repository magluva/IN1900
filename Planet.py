
class Planet:
    '''
    Planet class takes three positional parameters:
    name = Planet name (string)
    radius = Planet radius (float)
    mass = Planet mass (float)
    A Planet object has methods:
    Planet.density() = Calculates the density of object: returns float
    Planet.print_info() = Prints all known inf(o of object: prints strings
    Planet.set_population() = sets a planet population
    '''

    def __init__(self, name, radius, mass):
        self.name = name
        self.radius = radius
        self.mass = mass

    def density(self):
        from numpy import pi
        r = self.radius*10**3
        v = (4/3*pi)*(r**3)
        return self.mass/v

    def print_info(self):
        print("Name:{0:>12}\nRadius:{1:>11} km\nMass:{2:>16} kg"\
              .format(self.name, self.radius, self.mass))
        print("Density:{0:22} kg/m³".format(self.density()))

    def set_population(self, x):
        self.population = x


# Test function(): Test case - Earth
def test():
    import time
    print("TestCase: Name=Earth, Radius=6.378e3, Mass=5.997e24, population=7497486172\n")
    start = time.time()
    planet1 = Planet("Earth", 6.378e3, 5.997e24)
    planet1.print_info()
    planet1.set_population(7497486172)
    tol = 1E-14
    # PEP8: One statement pr. line. *Throws PEP8 out of the window, flips table*
    success = (
               planet1.name is "Earth" and
               planet1.radius is 6.378e3 and
               planet1.mass is 5.997e24 and
               abs(planet1.density()-5518.1295824185645)<tol and
               abs(planet1.population-7497486172)<tol
               )
    msg = "Test finished in {} seconds ... FAILED".format(time.time()-start)
    assert success, msg
    print("{} has a population of {}".format(planet1.name, planet1.population))
    print("\nTest finished in {} seconds ... ok".format(time.time()-start))

if __name__ == "__main__":
    test()
    #print(Planet.__doc__)

# Terminal Output:
'''
$ python Planet.py
TestCase: Name=Earth, Radius=6.378e3, Mass=5.997e24, population=7497486172

Name:       Earth
Radius:     6378.0 km
Mass:       5.997e+24 kg
Density:    5518.1295824185645 kg/m³
Earth has a population of 7497486172


Test finished in 0.07811570167541504 seconds ... ok
'''
