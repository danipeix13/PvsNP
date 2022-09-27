def find_parent(x):
        x = x//2 if x%2==0 else 3*x+1
        while not is_prime(x):
                x = x//2 if x%2==0 else 3*x+1
        return x

def is_prime(x):
        if x <= 3:
                return True
        if x % 2 == 0:
                return False
        for i in range(3, x//2, 2):
                if x % i == 0:
                        return False
        return True;
