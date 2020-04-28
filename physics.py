train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

def f_to_c (f_temp):
    c_temp = (f_temp-32) * 5/9
    return c_temp

def c_to_f(c_temp):
  f_temp = c_temp*(9/5) + 32
  return f_temp
  
def get_force(mass, acceleration):
  return mass*acceleration


def get_energy(mass, c=3*10**8):
  return mass*c

def get_work(mass, acceleration, distance):
  f = get_force(mass, acceleration)
  return f*distance

  
f_in_celsius = f_to_c(100)
c0_in_fahrenheit = c_to_f(0)
train_mass = 1000000
train_acceleration = 100
train_force = get_force(train_mass, train_acceleration)
distance = 100
train_work = get_work(train_mass, train_acceleration, distance)


print("The GE train supplies " + str(train_force) + " Newtons of force")
mass = 10
c = 3*10**8
bomb_mass = get_energy(mass, c)

print(bomb_mass)


  
