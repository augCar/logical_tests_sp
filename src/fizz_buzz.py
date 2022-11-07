def fizz_buzz(user_range: int):
    """
    Logical function of the program.
    Prints numbers from one to the user's desired length on the screen, replacing multiples of 3 with Fizz, multiples of 5 with Buzz, and multiples of 3 and 5 with FizzBuzz.

    :param user_range: This parameter represents how long the user wants the printout to be.
    """
    print()
    [print("Fizz" * (x % 3 == 0) + "Buzz" * (x % 5 == 0) or x) for x in range (1, user_range + 1)] # I usually don't really like to use oneliners, but this problem it's more fun this way
    print()

#---------- Main section -------------------------------------------------------
if __name__ == "__main__":
    fizz_buzz(int(input("\nHow long do you want Fizz Buzz to be Fizz Buzzing? ")))
