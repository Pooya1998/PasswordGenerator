import string
import random
def passwordgen(size=8,chars=string.ascii_lowercase+string.ascii_uppercase+string.digits):
    return ''.join(random.choice(chars)for _ in range(size))

print(passwordgen(int(input('How Many Character You need?: '))))
