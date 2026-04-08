primes = [2, 3, 5, 7, 11, 13]

rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
rainbow[0] = "ruby"

print(primes[0], rainbow[0])

primes.append(17)

print(primes)
print(len(primes))

men = ["Greg", "Jock", "Charlie"]
women = ["Danielle", "Myrlie"]
people = []

people.append(men)
people.append(women)

print(people)
print(len(people))
print(people[1][0])

a = [1, 2]
b = [3, 4]
c = a + b

print(c)
