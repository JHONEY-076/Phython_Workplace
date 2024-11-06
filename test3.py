def hamburger(y, z, x):
    print(z, "and", x, "like", y)
    return z

def main():
    x = "Python"
    y = "tyler"
    z = "tv"
    rugby = "hamburger"
    Python = "donnie"

    hamburger(x, y, z)
    hamburger(z, x, y)
    hamburger("rugby", z, Python)
    y = hamburger(y, rugby, "x")
    hamburger(y, y, "Python")

main()