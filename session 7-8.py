import random
import time
import numpy as np

N = 10**7
a = []
# list of 10 million numbers
for _ in range(N):
  a.append(random.randint(1, N))

start = time.perf_counter()
a.sort()
end = time.perf_counter()
print(f"classic took {end-start}")

a = np.random.randint(1, N, N)
start = time.perf_counter()
a.sort()
end = time.perf_counter()
print(f"NumPy took {end-start}")
import numpy as np
l = [1, 2, 3, 4, 5, 6, 7, 8] # pure python list
a = np.array(l) # a is a ndarray
print(a, type(a))
print(l, type(l))
print(a+2)
print(a/2)
print(a+a)
print(a**2)

a = np.array([[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10]])
print(a)
print (type(a))
print(f"{a.ndim}, {a.size}, {a.shape}, {a.dtype}\n")

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]], dtype=np.int16)
print(a)
print(f"{a.ndim}, {a.size}, {a.shape}, {a.dtype}")

a0 = np.zeros((4,10), dtype=int)
a1 = np.ones((2, 3, 4))
print(a0)
print(a1)
a11 = np.ones((2, 3, 4), dtype=np.int16)
print(a11)


import numpy as np

# --- basic arrays ---
a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])

print(f"a1={a1}, a2={a2}")
print(f"a1+a2={a1+a2}, a1*a2={a1*a2}")

# --- 2D example ---
a1 = np.array([[1, 2, 3], [4, 5, 6]])
print(a1 + a2)

print("\n\n")

# --- 3D example (fixed broadcasting) ---
a1 = np.ones((2, 3, 4))
a2 = np.array([4, 5, 6, 7])  # must match last dimension (4)

print(a1 + a2)
print(a1 * a2)

print("\n\n")

# --- other operations ---
print(10 / a1)
print(a1 * 2.5)
print(a1 > 3)

a = np.array(
    [[1, 2, 3, 4, 5],
     [6, 7, 8, 9, 10]]
     )
print(a)
print(a[0][1]) # row and column
print(a[1, 2]) # same thing

a = np.random.randint(10, 100, size=(3, 4, 5))
print(f"a={a}\n")
print(f"a[1] = \n {a[1]}\n")
print(f"a[1, 2] = \n{a[1, 2]}\n")
print(a[1, 1, 4])

import numpy as np
import matplotlib.pyplot as plt


dat = np.genfromtxt('data.csv', delimiter=',') # loads the data we downloaded before
dat = np.where(dat<1000, dat, np.nan)
# dat = np.where(dat<1000, dat, 0)

dat = dat[::-1, :]
lon = np.arange(-180.0, 180.1, 0.5)
lat = np.arange(-90.0, 90.1, 0.5)
date = '2021-08-29 to 2021-09-05'
source = 'https://neo.sci.gsfc.nasa.gov/view.php?datasetId=MOD_LSTD_E&date=2021-09-01'

fig, ax = plt.subplots(constrained_layout=True, figsize=(14, 8))
ax.set_facecolor('0.6')
pc = ax.pcolormesh(lon, lat, dat, shading='auto', cmap='inferno')
ax.set_aspect(1.3)
ax.set_xlabel('Longitude $[^o E]$')
ax.set_ylabel('Latitude $[^o N]$')
fig.colorbar(pc, shrink=0.6, extend='both', label='land temperature $[^oC]$');
ax.set_title(f'source: {source}', loc='left', fontsize='x-small');

# Import seaborn
import seaborn as sns

# Apply the default theme
sns.set_theme()

# Load an example dataset
tips = sns.load_dataset("tips")

# Create a visualization
sns.relplot(
    data=tips,
    x="total_bill", y="tip", col="time",
    hue="smoker", style="sex", size="size",
)


import matplotlib.pylab as plt
import numpy as np

x = np.linspace(0, 150, 20) # first usage
y = x**2
y2 = x**3/100 # we can use numpy arithmetic

plt.rcParams.update({'font.size': 16})
plt.figure(figsize = (10, 10))

plt.title("$X^2$ vs $X^3$/100")
plt.plot(x, y)
plt.plot(x, y2)
plt.show()

