#!/usr/bin/python3
if __name__ == "__main__":
    # Import functions from calculator_1.py
    from calculator_1 import add, sub, mul, div
    
    # Define variables a and b
    a = 10
    b = 5
    
    # Perform calculations and print results
    result_add = add(a, b)
    result_sub = sub(a, b)
    result_mul = mul(a, b)
    result_div = div(a, b)
    
    print(f"{a} + {b} = {result_add}")
    print(f"{a} - {b} = {result_sub}")
    print(f"{a} * {b} = {result_mul}")
    print(f"{a} / {b} = {result_div}")

