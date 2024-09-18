""" x = 99
quotient, remainder = divmod(x,2)
if remainder == 1:
    print("Odd")
else:
    print("Even") """
""" def bad(q):
    q = ("0%")
def okay(w):
    w = ("15%")
def good(e):
    e = ('20%')
def great(r):
    r = ("25%")
service = good
if service == bad:
    print("0%")
elif service == okay:
    print("15% Tip")
elif service == good:
    print("20% Tip")
elif service == great:
    print("25% Tip") """
def find_factors(n):
    factors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    return sorted(factors)

# Example usage
number = 12
print(find_factors(number))  # Output: [1, 2, 3, 4, 6, 12]