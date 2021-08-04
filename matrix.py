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
        if self.rows == other.rows and self.columns == other.columns: # Check if same size
            values = []
            for i in range(len(self.values)):
                values.append(self.values[i] - other.values[i]) # Appending the subtracted values to a list
            values = tuple(values) # Making the list a tuple
            return Matrix(self.rows, self.columns, values) # and then returning a new matrix
        else:
            raise Exception("UnequalRowsAndColumns") # The exception for mismatched sizes

    def __mul__(self, scalar):
        """
        Multiply a matrix by a scalar.
        """
        values = []
        if isinstance(scalar, int):
            for value in self.values:
                values.append(value * scalar)
            tuple(values)
            return Matrix(self.rows, self.columns, values)
        else:
            raise Exception("MultByNonInt")

    def __matmul__(self, other):
        """
        Multiply a matrix by another matrix.
        """
        if self.columns == other.rows: # Check if they can be multiplied
            values = []
            for i in range(other.columns):
                for x in range(self.rows): # For each row and column pair
                    row = self.get_row(self, x)
                    column = self.get_col(other, i) # Get the current row and column
                    for z in range(self.columns): # For each value in the row and column
                        values.append(row[z] * column[z]) # Calculate the value and append it to values
            vals = self.chunk_it(values, self.rows * other.columns) # Split the values in to sets of 3
            _values = []
            for _list in vals:
                value = 0
                for val in _list:
                    value += val # Add the values in each list together
                _values.append(value) # Append the final value
            _values = _values[0::2] + _values[1::2] # Reorganize the values to the right order
            return Matrix(self.rows, other.columns, tuple(_values))
        else:
            raise Exception("UnequalRowsAndColumns")

    def get_col(self, matrix, col_num):
        """
        Get a column at position x.
        """
        column = matrix.values[col_num::matrix.columns]
        return column

    def get_row(self, matrix, row_num):
        """
        Get a row at position x.
        """
        values = matrix.values
        rows = self.chunk_it(values, matrix.rows)
        return rows[row_num]

    def chunk_it(self, seq, num):
        """
        This function was made by Max Shawabkeh, on Jan 25 '10 at 3:27,
        on the question:

        https://stackoverflow.com/questions/2130016/splitting-a-list-into-n-parts-of-approximately-equal-length

        """
        avg = len(seq) / float(num)
        out = []
        last = 0.0

        while last < len(seq):
            out.append(seq[int(last):int(last + avg)])
            last += avg

        return out
