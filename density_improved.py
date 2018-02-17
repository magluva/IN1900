
# Function using .join(): return dictionary
def read_densities(filename):
    densities = {}
    with open(filename, "r") as f:
        for line in f:
            words = line.split()
            # Assigns last word in line
            density = float(words[-1])
            # Assigns everything up to, but not including the last word in line
            substance = " ".join(words[0:-1])
            densities[substance] = density
    return densities

# Function using index: return dictionary
def alternative(filename):
    densities = {}
    with open(filename, "r") as f:
        for lines in f:
            # boolean list - True if digit
            a = [i.isdigit() for i in lines]
            for i, b in enumerate(a):
                if b:
                    index = i
                    break
            # Searches for digit (boolean) and assigns index to index-variable
            # Could have counted manually and found the index, but this code finds it for us
            substance = lines[:index:].strip()
            density = float(lines[index::].strip())
            densities[substance] = density
    return densities

# Test function
def test():
    func1 = read_densities("densities.dat")
    func2 = alternative("densities.dat")
    success = func1 == func2
    msg = "read_file() != alternative()"
    assert success, msg

def main():
    #Calling functions
    den = read_densities("densities.dat")
    alt = alternative("densities.dat")
    test()

if __name__ == "__main__":
    main()
