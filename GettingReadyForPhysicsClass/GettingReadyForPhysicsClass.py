# Program that calculates various conversions

train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

# Converts Fahrenheit to Celsius
def f_to_c(temp_f):
  temp_c = (temp_f - 32) * 5/9
  return temp_c

f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

# Converts Celsius to Fahrenheit
def c_to_f(temp_c):
  temp_f = temp_c * (9/5) + 32
  return temp_f
  
c0_in_farenheit = c_to_f(0)
print(c0_in_farenheit)

# Calulates newtons of force
def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

# Calculates number of Joules
def get_energy(mass, c=3*10**8):
  return mass * c**2

bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

# Calculates Joules and distance
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration) * distance
  return force

train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")