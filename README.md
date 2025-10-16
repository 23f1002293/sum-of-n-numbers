# Sum of N Numbers

## Summary

This is a minimal, user-friendly application to calculate the sum of a given quantity ('n') of numbers. The project provides two ways to use the calculator:

1.  A command-line interface (CLI) written in Python.
2.  An interactive web-based interface using HTML, CSS, and JavaScript.

## Setup

No special installation is required. You just need the necessary runtime environments.

### For the Command-Line Version

-   Ensure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/).

### For the Web Version

-   A modern web browser (like Chrome, Firefox, or Edge) is all you need.

## Usage

### Command-Line (main.py)

1.  Open your terminal or command prompt.
2.  Navigate to the directory where the files are saved.
3.  Run the script using the following command:
    ```bash
    python main.py
    ```
4.  The program will first ask you how many numbers you wish to sum.
5.  It will then prompt you to enter each number one by one.
6.  After all numbers are entered, it will display the list of numbers and their total sum.

### Web Interface (index.html)

1.  Locate the `index.html` file in your file explorer.
2.  Double-click the file to open it in your default web browser.
3.  In the input box, type the numbers you want to sum, separated by spaces or commas.
4.  Click the "Calculate Sum" button.
5.  The result will be displayed below the button.

## Code Explanation

### `main.py`

This Python script provides an interactive command-line experience.

-   `get_positive_integer(prompt)`: A helper function that safely prompts the user for a positive integer, handling non-numeric input and non-positive values.
-   `get_number(prompt)`: A helper function that safely prompts the user for any number (integer or float), handling non-numeric input.
-   `main()`: The main execution function that orchestrates the program flow. It first asks for the count of numbers, then iterates that many times to collect each number, and finally prints the result.
-   `if __name__ == "__main__":`: This standard Python construct ensures that the `main()` function is called only when the script is executed directly.

### `index.html`

This single HTML file contains the structure, styling, and logic for the web interface.

-   **HTML**: A simple structure with a `<form>`, an `<input>` field for the numbers, a `<button>` to submit, and a `<p>` tag to display the result.
-   **CSS**: Minimal CSS is included within a `<style>` tag to center the content and provide a clean, readable layout.
-   **JavaScript**: The core logic is contained within a `<script>` tag.
    -   It attaches an event listener to the form's `submit` event.
    -   `event.preventDefault()` is used to stop the default form submission behavior (which would cause a page reload).
    -   The input string is retrieved, split by spaces or commas, and cleaned of any empty entries.
    -   The resulting array of strings is converted to an array of numbers.
    -   Input is validated to ensure all parts are valid numbers. If not, an error is shown.
    -   The `reduce()` method is used to efficiently calculate the sum of the numbers.
    -   The final result is then displayed on the page.

## License

This project is licensed under the MIT License.
