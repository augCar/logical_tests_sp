def print_secuence(length: int, secuence: list):
    """
    Custom print function.

    :param length: Length desired by the user (used to validate the last number in the sequence and print the appropriate line breaks).
    :param secuence: The raw Fibonacci secuence.
    """
    print(f"\nFibonacci series of length {length}: ---> ", end="")
    for value in secuence:
        print(f"{value} - ", end="") if value != secuence[-1] else print(f"{value} <---\n")

def calculate_fibonacci(length: int): # I know this is not recursive, I just wanted to make it different haha...
    """
    This is the core logic function. Calculates the Fibonacci sequence for the length desired by the user.

    :param length: Secuence length desired by the user.
    :return: A list with the desired Fibonacci secuence.
    """
    secuence = [0,1]
    if length == 0:
        secuence.pop()
        return secuence
    elif length == 1:
        return secuence
    while (len(secuence) < length):
        secuence.append((secuence[-1]) + (secuence[-2]))
    return secuence

#---------- Main section -------------------------------------------------------
def main():
    """
    This is the main function of the program. Its objective is to obtain from the user the desired length of the Fibonacci series, to then execute the calculation and printing functions.
    """
    secuence_length = int(input("\nPlease enter the length you want in your Fibonacci series: "))
    print_secuence(secuence_length, calculate_fibonacci(secuence_length))

if __name__ == "__main__":
    main()

# C:\Users\augus\Documents\repos\sp_logical_tests\venv\Scripts\Activate.ps1
