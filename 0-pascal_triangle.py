def pascal_triangle(n):
    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return []

    triangle = []  # Initialization of the triangle as an empty list

    for i in range(n):
        # This creates a new row initialized with 1s
        row = [1] * (i + 1)

        # Calculations of the values for the inner elements of the row
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)  # This append the row to the triangle

    return triangle
