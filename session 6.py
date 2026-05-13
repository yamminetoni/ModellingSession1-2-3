# I am now writing python code:
a = 90
b = -9
print(f"The result is {a+b}")
print(f"the square of a={a*a}")
# to run this code you just need to press the play button
first_n = 100
numbers = list(range(2, first_n))
for prime in numbers:
  for number in range(2*prime, first_n, prime):
    if number in numbers:
      numbers.remove(number)
print(len(numbers))

#@markdown What animals do you like?
animals = "Dogs" #@param {type:"string"}
#@markdown What is your name?
name = "Toni" #@param {type:"string"}

print(f"{"Toni"} {"Yammine"} likes {"dogs"}")

class Car:
  def __init__(self, brand, hp, automatic, color, date, seats):
    self.brand = brand
    self.hp = hp
    self.automatic = automatic
    self.color = color
    self.date = date
    self.seats = seats

  def __str__(self):
    transmission = "automatic" if self.automatic else "manual"
    print_date = self.date.split("-")[0]
    return f"{self.seats} seater {self.color} {print_date} {self.brand}, {transmission} {self.hp}HP"



car_brand = "bmw" # @param {type:"string"}
hp = 490 # @param {type:"slider", min:50, max:1200, step:5}
automatic = True # @param {type:"boolean"}
color = "green" # @param ["red", "blue", "green", "yellow", "black", "white"]
purchase_date = "2023-11-08" # @param {type:"date"}
seats = 5 # @param {"type":"slider","min":2,"max":7,"step":1}
my_car = Car(car_brand, hp, automatic, color, purchase_date, seats)

print(my_car)

max_number = 2616 #@param {type:"slider", min:500, max:5000, step:1}

numbers = list(range(2, max_number))
for prime in numbers:
  for number in range(2*prime, 1000, prime):
    if number in numbers:
      numbers.remove(number)
print(numbers)

#
name = "Toni"
sport = "football"
money = 19300
likes_dogs = True # @param {type:"boolean"}
birthday = "2007-08-31" # @param {type:"date"}

print(f"{name} was born on {birthday}, has {money}$ and likes {sport}")

# load an example dataset
from vega_datasets import data
cars = data.cars()

# plot the dataset, referencing dataframe column names
import altair as alt
interval = alt.selection_interval()

alt.Chart(cars).mark_point().encode(
  x='Horsepower',
  y='Miles_per_Gallon',
  color='Origin'
).interactive()

import matplotlib.pyplot as plt

import matplotlib.patches as mpatches
import matplotlib.path as mpath

fig, ax = plt.subplots()

Path = mpath.Path
path_data = [
    (Path.MOVETO, (1.58, -2.57)),
    (Path.CURVE4, (0.35, -1.1)),
    (Path.CURVE4, (-1.75, 2.0)),
    (Path.CURVE4, (0.375, 2.0)),
    (Path.LINETO, (0.85, 1.15)),
    (Path.CURVE4, (2.2, 3.2)),
    (Path.CURVE4, (3, 0.05)),
    (Path.CURVE4, (2.0, -0.5)),
    (Path.CLOSEPOLY, (1.58, -2.57)),
    ]
codes, verts = zip(*path_data)
path = mpath.Path(verts, codes)
patch = mpatches.PathPatch(path, facecolor='r', alpha=0.5)
ax.add_patch(patch)

# plot control points and connecting lines
x, y = zip(*path.vertices)
line, = ax.plot(x, y, 'bo-')

ax.grid()
ax.axis('equal')
plt.show()
