class Matrix():
    def __init__(self, rows, columns, values) -> None:
        """
        Initializer for the values of the matrix.

        rows: The number of horisontal rows.

        columns: The number of vertical columns.

        values: A tuple of numbers to go in the matrix, values must equal rows*columns.
        """
        self.rows = rows
        self.columns = columns
        if rows * columns == len(values): # Check if the user has used the right amount of values
            self.values = values
        else:
            raise Exception("InvalidLengthOfValues")

    def __repr__(self) -> str:
        """
        Basic representation of the matrix, which can be used to recreate the matrix exactly.
        """
        return f"Matrix({self.rows}, {self.columns}, {self.values})"

    def __str__(self) -> str:
        """
        End user representation of the matrix, organized in rows ands columns, like it should.
        """
        string = "" # Initialize the string to be returned.
        column = 0 # Variable to get the right value to print.
        for x in range(self.rows):
            for y in range(self.columns):
                string += str(self.values[column]) # Using the column variable append it the string.
                string += ' ' # Add some spacing bewtween numbers
                column += 1
            string += '\n'
        string = string[0:-2]
        return string

    def __add__(self, other):
        """
        Adds two matrices together, with an exception if they are differently sized.
        """
        if self.rows == other.rows and self.columns == other.columns: # Check if same size
            values = []
            for i in range(len(self.values)):
                values.append(self.values[i] + other.values[i]) # Appending the added values to a list
            values = tuple(values) # Making the list a tuple
            return Matrix(self.rows, self.columns, values) # and then returning a new matrix
        else:
            raise Exception("UnequalRowsAndColumns") # The exception for mismatched sizes

    def __sub__(self, other):
        """
        Subtract two matrices, with an exception if they are differently sized.
        """

