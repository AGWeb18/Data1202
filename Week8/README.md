#    Week 8 - Functions - For Loops - Visualizations

### Built-in Python Functions

Python comes with a set of built-in functions that are always available. Here are some examples:

```python
# print function
print("Hello world!")

# len function
my_list = [1, 2, 3, 4, 5]
#===========================
print(len(my_list))  # Outputs: 5

# type function
print(type(my_list))  # Outputs: <class 'list'>

# str, int, float functions
print(int("123"))  # Outputs: 123
print(float("123.45"))  # Outputs: 123.45
print(str(123))  # Outputs: "123"

# max, min functions
print(max(my_list))  # Outputs: 5
print(min(my_list))  # Outputs: 1

# sum function
print(sum(my_list))  # Outputs: 15

# sorted function
print(sorted(my_list, reverse=True))  # Outputs: [5, 4, 3, 2, 1]

###############################


# Create your own function 
def my_function(arg1, arg2):
    # Your code here
    result = arg1 + arg2
    return result

# Call the function
print(my_function(5, 3))  # Outputs: 8


```