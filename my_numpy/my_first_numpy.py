import numpy 


array = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

array_sum = numpy.sum(array)
array_mean = numpy.mean(array)
array_std = numpy.std(array)

print(f"Original Array: {array}")
print(f"Sum: {array_sum}")
print(f"Mean: {array_mean}")
print(f"Standard Deviation: {array_std}")

squared_array = array ** 2
print(f"Squared Array: {squared_array}")
