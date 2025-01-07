import numpy as np
temperature = np.random.randint(15, 40, 30)
mean_of_temp = np.mean(temperature)
min_of_temp = np.min(temperature)
max_of_temp = np.max(temperature)

def convert_to_F(temp):
    print(f"{temp} C degree")
    F = temp * (9/5) +32
    print(f"{F} F degree")

sorted_temp = np.sort(temperature)

print(f"Mean Temperature: {mean_of_temp}")
print(f"Minimum Temperature: {min_of_temp}")
print(f"Maximum Temperature: {max_of_temp}")
print(f"Sorted Temperature: {sorted_temp}")

convert_to_F(max_of_temp)
