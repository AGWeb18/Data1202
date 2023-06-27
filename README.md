# Data1202
This course walks through basics SQL and python data transformations


##  Week 7 - Transformations / Aggregations in Python

### Pre-Requisites 
Before starting, you should have a basic understanding of:

- Python syntax
- Basic data types in Python (strings, integers, floats, booleans)
- Control flow (if statements, for loops)
- Basic data structures (lists, dictionaries)
- Basic data manipulation techniques (indexing, slicing, filtering)


### Course content
- Finish off developing a "JOIN" in Python

# Join the two DataFrames on a common column
- Replace 'common_column' with the name of the column that the two tables have in common

```py
#   JOIN Syntax
df = pd.merge(df1, df2, on='common_column', how='left')
```


Then: 
- Understanding what functions are and why they're useful
- Using built-in Python functions - len(), str(), int()
- Defining your own functions based on the transformations. 
- Understanding function arguments and return values



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


#    Week 8 - Functions - For Loops - Visualizations

- Review of Functions

- For Loops vs Vectorization

- Visualization using Matplotlib in Python

