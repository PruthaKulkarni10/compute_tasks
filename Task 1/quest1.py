# Input the number of rows and columns
num_columns, num_rows = map(int, input().split())

# Initialize a list to store the input values
data = []

# Input the data into a list of lists
for _ in range(num_rows):
    row = list(map(float, input().split()))
    data.append(row)

# Calculate the column-wise average
averages = [0] * num_columns

for j in range(num_columns):
    total = 0
    for i in range(num_rows):
        total += data[i][j]
    averages[j] = total / num_rows

# Print the column-wise averages
for average in averages:
    print("{:.1f}".format(average))
