import numpy as np
import matplotlib.pyplot as plt

temperatures = np.array([
    [15, 20, 25],
    [16, 21, 24],
    [14, 19, 23],
    [15, 22, 26],
    [17, 20, 24],
    [16, 21, 25],
    [15, 19, 22]
])
average_temp_per_city = np.mean(temperatures,axis=0)
max_temp_per_day = np.max(temperatures,axis=1)
coldest_day_per_city = np.argmin(temperatures,axis=0)
noise = np.random.uniform(-0.5, 0.5,size=temperatures.shape)
temperatures_noisy = temperatures + noise
average_temp_overall = np.mean(temperatures_noisy,axis=0)

plt.plot(average_temp_overall,marker='o')
plt.title("Average Temperature of Each City Over the Week")
plt.xlabel("City")
plt.ylabel("Temperature (°C)")
plt.xticks(np.arange(3), labels=['City1', 'City2', 'City3'])
plt.show()
print("Average temperature per city (without noise):", average_temp_per_city)
print("Max temperature per day (without noise):", max_temp_per_day)
print("Coldest day per city:", coldest_day_per_city)
print("Average temperature overall (with noise):", average_temp_overall)

