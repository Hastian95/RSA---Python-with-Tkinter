import random
def first_primes():
    my_prime_numbers = []
    numb = 0
    range_of_prime= 100 # How big numbers you are looking for #
    while numb < 2:
        prime = random.randrange (1,range_of_prime)
        starting = int(2)

        while (starting*starting) <= prime:
            score = prime % starting
            if score == int(0):
                prime = random.randrange(1,range_of_prime)
                starting = int(2)
            else:
                starting +=1

        if prime not in my_prime_numbers:
            my_prime_numbers.append(prime)
            numb += 1

        if len(my_prime_numbers) == 2:
            break
    return my_prime_numbers

def algorithm_RSA(my_prime_numbers):
    p = my_prime_numbers[0]
    q = my_prime_numbers[1]
    Theta = (p-1) * (q-1) #Euler formula
    n = p * q #Euler modulus
# Euklides Algorithm - GCD - greates common divisor - to find 'e'
    e = 7
# Edtended Euclidean algorithm - d * e mod Theta = 1 //
    u, w, d, z = 1, e, 0, Theta

    while w:
        if z != 0:
            if w < z:
                u, d = d, u
                w, z = z, w
            q = w//z
            u -= q*d
            w -= q*z
        else:
            return algorithm_RSA(first_primes())
    if z == 1:
        if d < 0: d += Theta
        return (e,n), (d,n)

        print(f"PUBLIC KEY: (e={e},n={n})")
        print(f"PRIVATE KEY: (d={d},n={n})")

        return publickeys, privatekeys

    else:
        return algorithm_RSA(first_primes())
def Encryption():
    print("Enter your text to encryption: ")
    t = input() #text_to_encrypt
    print("Enter e: ")
    e = int(input())
    print("Enter n: ")
    n = int(input())
    asci_decrypting = []
    text_decrypted = []
    for x in t:
        asci_decrypting.append(ord(x))
    for y in asci_decrypting:
        if 0<y<n:
            text_decrypted.append((y**e)%n)
        else:
            print("Tej wiadomości nie można zaszyfrować.")
    print(text_decrypted)
    return text_decrypted

def Decryption():
    print("Give me your decrypted message: ", end="\n")
    t=input()
    print("Enter d: ")
    d = int(input())   
    print("Enter n: ")
    n = int(input())
    final=''
    cleaning=t[1:-1]
    y=cleaning.split(', ')
    text_decrypted = []
    #Asci Part Up
    for c in y:
       if 0<int(c)<n:
           c_int=int(c)
           text_decrypted.append(chr(((c_int)**d)%n))
       else:
          print("Tej wiadomości nie można zaszyfrować.")
    for joining in text_decrypted:
        final+=joining
    print(final)
    return final

algorithm_RSA(first_primes())
Encryption()
Decryption()

#def User():
#    print("Please choose Decryption/D or Encryption/E?")
#    Answer = input()
#    if Answer=="D":
#        print()
#    elif Answer=="E":
#
#    else:
#        User()
#
#user()
