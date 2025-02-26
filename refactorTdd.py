
'''
def add(numbers: str) -> int:
    # Case 1: If the string is empty, return 0
    if numbers == "":
        return 0
    
    # Case 2: If the string contains one number, return that number
    if "," not in numbers:
        return int(numbers)
    
    # Case 3: If the string contains two numbers separated by comma, return their sum
    num_list = numbers.split(",")
    
    # Convert the list of strings to integers and return the sum
    return sum(int(num) for num in num_list)



def add(numbers: str) -> int:
    if numbers == "":
        return 0
    if "," not in numbers:
        return int(numbers)  # Single number, return it as an integer
    num_list = numbers.split(",")
    return sum(int(num.strip()) for num in num_list)  # Remove spaces around numbers before summing




def add(numbers: str) -> int:
    # Case 1: Handle the empty string case
    if numbers == "":
        return 0
    
    # Case 2: Handle custom delimiters
    if numbers.startswith("//"):
        delimiter_index = numbers.index("\n")
        delimiter = numbers[2:delimiter_index]  # Extract delimiter
        numbers = numbers[delimiter_index + 1:]  # Remove delimiter declaration

        # Replace the custom delimiter with a comma (for easier splitting)
        numbers = numbers.replace(delimiter, ",")
    
    # Case 3: Split the numbers by commas or newlines
    num_list = numbers.replace("\n", ",").split(",")
    
    # Case 4: Convert the list of strings to integers and return the sum
    return sum(int(num.strip()) for num in num_list if num.strip())


def add(numbers: str) -> int:
    # Case 1: Handle the empty string case
    if numbers == "":
        return 0
    
    # Case 2: Handle custom delimiters
    if numbers.startswith("//"):
        delimiter_index = numbers.index("\n")
        delimiter = numbers[2:delimiter_index]  # Extract delimiter
        numbers = numbers[delimiter_index + 1:]  # Remove delimiter declaration

        # Replace the custom delimiter with a comma (for easier splitting)
        numbers = numbers.replace(delimiter, ",")
    
    # Case 3: Replace newlines with commas to treat them as delimiters
    numbers = numbers.replace("\n", ",")
    
    # Case 4: Split the numbers by commas
    num_list = numbers.split(",")
    
    # Case 5: Convert the list of strings to integers and return the sum
    return sum(int(num.strip()) for num in num_list if num.strip())



import re

def add(numbers: str) -> int:
    # Case 1: Handle the empty string case
    if numbers == "":
        return 0
    
    # Case 2: Handle custom delimiters (optional)
    if numbers.startswith("//"):
        # Find where the delimiter declaration ends
        delimiter_index = numbers.index("\n")
        
        # Extract the custom delimiter
        delimiter_part = numbers[2:delimiter_index]
        
        # Handle multiple character delimiters, like "//[;]\n1;2"
        delimiter = delimiter_part.strip("[]")
        
        # Remove the delimiter line and the newline character
        numbers = numbers[delimiter_index + 1:]
        
        # Replace the custom delimiter with commas for easier processing
        numbers = numbers.replace(delimiter, ",")
    
    # Case 3: Replace newlines with commas to treat them as delimiters
    numbers = numbers.replace("\n", ",")
    
    # Case 4: Split the numbers by commas
    num_list = numbers.split(",")
    
    # Case 5: Convert the list of strings to integers and return the sum
    return sum(int(num.strip()) for num in num_list if num.strip())


# Refactored add Function:
# python
# Copy
import re

class NegativeNumberException(Exception):
    pass

def extract_delimiter(numbers: str) -> (str, str):
    """Extract delimiter and numbers from the input string."""
    if numbers.startswith("//"):
        # Custom delimiter line format: "//[delimiter]\n[numbers...]"
        delimiter_index = numbers.index("\n")
        delimiter_part = numbers[2:delimiter_index].strip("[]")
        numbers = numbers[delimiter_index + 1:]
        return delimiter_part, numbers
    # Default delimiter is comma and newline
    return ",", numbers

def handle_delimiters(numbers: str, delimiter: str) -> str:
    """Replace the delimiters (commas, newlines, or custom) with commas."""
    # Replace all delimiters (comma and newline) with a comma
    numbers = numbers.replace("\n", delimiter).replace(delimiter, ",")
    return numbers

def find_negatives(num_list: list) -> list:
    """Detect negative numbers and return them."""
    negatives = [num for num in num_list if num < 0]
    return negatives

def add(numbers: str) -> int:
    """Add the numbers in the string, supporting custom delimiters and negative number detection."""
    if numbers == "":
        return 0

    # Step 1: Extract custom delimiter (if any) and the numbers part
    delimiter, numbers = extract_delimiter(numbers)

    # Step 2: Handle the delimiters (comma, newline, or custom)
    numbers = handle_delimiters(numbers, delimiter)

    # Step 3: Split the numbers and convert them to integers
    num_list = [int(num.strip()) for num in numbers.split(",") if num.strip()]

    # Step 4: Check for negative numbers
    negatives = find_negatives(num_list)
    if negatives:
        raise NegativeNumberException(f"negatives not allowed: {', '.join(map(str, negatives))}")

    # Step 5: Return the sum of the numbers
    return sum(num_list)

######################################################################

class NegativeNumberException(Exception):
    pass

def extract_delimiter(numbers: str) -> (str, str): # type: ignore
    """Extract delimiter and numbers from the input string."""
    if numbers.startswith("//"):
        # Custom delimiter line format: "//[delimiter]\n[numbers...]"
        delimiter_index = numbers.index("\n")
        delimiter_part = numbers[2:delimiter_index].strip("[]")
        numbers = numbers[delimiter_index + 1:]
        return delimiter_part, numbers
    # Default delimiter is comma and newline
    return ",", numbers

def handle_delimiters(numbers: str, delimiter: str) -> str:
    """Replace the delimiters (commas, newlines, or custom) with commas."""
    # Replace all delimiters (comma and newline) with a comma
    numbers = numbers.replace("\n", delimiter).replace(delimiter, ",")
    return numbers

def find_negatives(num_list: list) -> list:
    """Detect negative numbers and return them."""
    negatives = [num for num in num_list if num < 0]
    return negatives

def add(numbers: str) -> int:
    """Add the numbers in the string, supporting custom delimiters, negative number detection, and ignoring numbers > 1000."""
    if numbers == "":
        return 0

    # Step 1: Extract custom delimiter (if any) and the numbers part
    delimiter, numbers = extract_delimiter(numbers)

    # Step 2: Handle the delimiters (comma, newline, or custom)
    numbers = handle_delimiters(numbers, delimiter)

    # Step 3: Split the numbers and convert them to integers
    num_list = [int(num.strip()) for num in numbers.split(",") if num.strip()]

    # Step 4: Check for negative numbers
    negatives = find_negatives(num_list)
    if negatives:
        raise NegativeNumberException(f"negatives not allowed: {', '.join(map(str, negatives))}")

    # Step 5: Filter out numbers greater than 1000
    num_list = [num for num in num_list if num <= 1000]

    # Step 6: Return the sum of the numbers
    return sum(num_list)

###############################
'''

import re

class NegativeNumberException(Exception):
    pass

def extract_delimiter(numbers: str) -> (str, str):
    """Extract delimiter and numbers from the input string."""
    if numbers.startswith("//"):
        # Custom delimiter line format: "//[delimiter]\n[numbers...]"
        delimiter_index = numbers.index("\n")
        delimiter_part = numbers[2:delimiter_index].strip("[]")
        numbers = numbers[delimiter_index + 1:]
        return delimiter_part, numbers
    # Default delimiter is comma and newline
    return ",", numbers

def handle_delimiters(numbers: str, delimiter: str) -> str:
    """Replace the delimiters (commas, newlines, or custom) with commas."""
    # Replace all delimiters (comma and newline) with a comma
    numbers = numbers.replace("\n", delimiter).replace(delimiter, ",")
    return numbers

def find_negatives(num_list: list) -> list:
    """Detect negative numbers and return them."""
    negatives = [num for num in num_list if num < 0]
    return negatives

def add(numbers: str) -> int:
    """Add the numbers in the string, supporting custom delimiters, negative number detection, and ignoring numbers > 1000."""
    if numbers == "":
        return 0

    # Step 1: Extract custom delimiter (if any) and the numbers part
    delimiter, numbers = extract_delimiter(numbers)

    # Step 2: Handle the delimiters (comma, newline, or custom)
    numbers = handle_delimiters(numbers, delimiter)

    # Step 3: Split the numbers and convert them to integers
    num_list = [int(num.strip()) for num in numbers.split(",") if num.strip()]

    # Step 4: Check for negative numbers
    negatives = find_negatives(num_list)
    if negatives:
        raise NegativeNumberException(f"negatives not allowed: {', '.join(map(str, negatives))}")

    # Step 5: Filter out numbers greater than 1000
    num_list = [num for num in num_list if num <= 1000]

    # Step 6: Return the sum of the numbers
    return sum(num_list)

import unittest

class TestStringCalculator(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(add(""), 0)  # Empty string should return 0

    def test_single_number(self):
        self.assertEqual(add("1"), 1)  # Single number should return that number

    def test_two_numbers(self):
        self.assertEqual(add("1,2"), 3)  # Sum of two numbers

    def test_no_comma(self):
        self.assertEqual(add("5"), 5)  # Single number should return that number

    def test_two_numbers_with_spaces(self):
        self.assertEqual(add(" 5, 7 "), 12)  # Handles spaces around numbers

    def test_numbers_with_commas_and_newlines(self):
        self.assertEqual(add("1,2\n3,4\n5"), 15)  # Numbers separated by both commas and newlines

    def test_extra_spaces(self):
        self.assertEqual(add(" 1, 2 , 3 "), 6)  # Handles spaces around numbers

    def test_custom_delimiter(self):
        self.assertEqual(add("//;\n1;2"), 3)  # Custom delimiter: ; separated numbers

    def test_custom_delimiter_with_mixed_input(self):
        self.assertEqual(add("//;\n1;2,3\n4"), 10)  # Mix of custom delimiter and commas/newlines


    def test_numbers_with_newline(self):
        self.assertEqual(add("1\n2\n3\n4"), 10)  # Numbers separated by newlines

    def test_numbers_with_commas_and_newlines(self):
        self.assertEqual(add("1,2\n3,4\n5"), 15)  # Numbers separated by both commas and newlines

    def test_extra_spaces(self):
        self.assertEqual(add(" 1, 2 , 3 "), 6)  # Handles spaces around numbers

    def test_custom_delimiter(self):
        self.assertEqual(add("//;\n1;2"), 3)  # Custom delimiter: ; separated numbers

    def test_custom_delimiter_with_mixed_input(self):
        self.assertEqual(add("//;\n1;2,3\n4"), 10)  # Mix of custom delimiter and commas/newlines

    def test_custom_delimiter_with_multiple_occurrences(self):
        self.assertEqual(add("//;\n1;2;3;4"), 10)
    
    def test_custom_delimiter_with_spaces(self):
        self.assertEqual(add("//;\n1 ; 2;3"), 6)  # Checks if it can handle spaces after delimiters
    
    def test_ignore_empty_elements(self):
        self.assertEqual(add("1,,2,,3"), 6)  # It should ignore the empty strings

    def test_ignore_spaces_between_numbers(self):
        self.assertEqual(add(" 1 , 2 , 3 "), 6)  # Should ignore spaces and calculate correctly
    
    def test_mixed_delimiters(self):
        self.assertEqual(add("//;\n1;2\n3"), 6)  # Newlines and semicolons as delimiters
    
    def test_custom_delimiter_with_square_brackets(self):
        self.assertEqual(add("//[;]\n1;2;3"), 6)  # Custom delimiter using square brackets

    def test_invalid_input_with_non_numbers(self):
        with self.assertRaises(ValueError):
            add("1,2,abc")  # This should raise an error

    def test_invalid_input_with_non_numbers(self):
        with self.assertRaises(ValueError):
            add("1,2,abc")  # This should raise an error
    
    def test_negative_numbers(self):
        with self.assertRaises(NegativeNumberException) as context:
            add("1,-2,3")
        self.assertEqual(str(context.exception), "negatives not allowed: -2")
        
        with self.assertRaises(NegativeNumberException) as context:
            add("-1,-2,-3")
        self.assertEqual(str(context.exception), "negatives not allowed: -1, -2, -3")

    def test_ignore_numbers_greater_than_1000(self):
        self.assertEqual(add("2,1001"), 2)  # 1001 is ignored
        self.assertEqual(add("1000,1001"), 1000)  # 1001 is ignored
        self.assertEqual(add("1001,2"), 2)  # 1001 is ignored
        self.assertEqual(add("//;\n1001;2;1001"), 2)  # 1001 is ignored

    def test_multi_character_custom_delimiter(self):
        self.assertEqual(add("//[***]\n1***2***3"), 6)  # Custom delimiter of length 3
        self.assertEqual(add("//[abc]\n1abc2abc3"), 6)  # Custom delimiter of length 3
        self.assertEqual(add("//[***]\n1***2***3***4"), 10)  # Custom delimiter of length 3

    # def test_multiple_custom_delimiters(self):
    #     self.assertEqual(add("//[*][%]\n1*2%3"), 6)  # Multiple custom delimiters of length 1
    #     self.assertEqual(add("//[***][abc]\n1***2abc3"), 6)  # Multiple custom delimiters of different lengths
    #     self.assertEqual(add("//[;;;][,,]\n1;;;2,,3"), 6)  # Multiple custom delimiters of different lengths

if __name__ == "__main__":
    unittest.main()