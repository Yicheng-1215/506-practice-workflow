
import pandas as pd
import numpy as np

number_variable = 3
string_variable = "HHA 506"
list_variable = [1, 2, 3, 4, 5]
dictionary_variable = {
    "brand": "honda",
    "year": [10, 20, 30],
    "key3": {"nested_key": "nested_value"}
}

def analyze_data(a, b):
    if a > b:
        return f"{a} is greater than {b}"
    else:
        return f"{b} is less than or equal to {a}"
    
    
result = car_price(30000)
print(f'Car price is: {result}')
