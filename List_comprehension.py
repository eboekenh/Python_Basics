# List comprehension exercise from dsmlbc bootcamp

# Loading car_crashes data set and applying some list comprehension methods

# Task 1: Convert the names of the numeric variables in the car_crashes data to uppercase letters and add NUM at the beginning.
# All variable names must be with capital letter

import seaborn as sns
df = sns.load_dataset ("car_crashes")
["NUM _" + col.upper () if df [col] .dtype! = "O" else col.upper () for col in df.columns]

# Task 2: Write "FLAG" AT the END of the variables that do NOT contain "no" in their name.


[col.upper () + "_ FLAG" if "no" not in col else col.upper () for col in df.columns]


# Task 3: Create a new df by selecting the names of the variables that are DIFFERENT from the variable names given below.
# og_list = ["abbrev", "no_previous"]
# First create a new list named new_cols using list comprehension according to the list above.
# Then create a new df by selecting these variables with df ["new_cols"] and name it as new_df.

# Task 3 Solution

og_list = ["abbrev", "no_previous"]
new_cols = [col for col in df.columns if col not in og_list]
new_df = df [new_cols]
new_df.head ()