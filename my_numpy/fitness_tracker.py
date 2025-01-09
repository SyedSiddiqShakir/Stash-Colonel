import numpy as np


def generate_data():
    np.random.seed(42)
    return np.random.randint(3000, 12000, size=(7, 7))

def calculate_daily_average(data):
    return np.mean(data)

def calculate_individual_total(data):
    return np.sum(data)
def most_stepped_day(data):
    individual_total = calculate_individual_total(data)
    individual_index = np.argmax(individual_total)
    return individual_index + 1, individual_total[individual_index]
def normalize_data(data):
    min_value = np.min(data)
    max_value = np.max(data)
    return (data - min_value) / (max_value - min_value)

def main():
    pass
