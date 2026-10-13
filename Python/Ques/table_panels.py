planets = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']
gravity = [3.7, 8.8, 9.8, 3.7, 24.7, 10.4, 8.6, 11.1]

print(type(gravity))
print(planets)
print(len(planets))

print('_' * 39)
print('| {:<15} | {:<10} |'.format('planet name', 'gravity'))
print('_' * 39)

i = 0
while i < len(planets):
    print('| {:<15} | {:<10} |'.format(planets[i], gravity[i]))
    i += 1

print('_' * 39)