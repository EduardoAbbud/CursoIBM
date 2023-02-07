def fizzbuzz(VarA):
    div3 = VarA % 3
    div5 = VarA % 5

    if div3 == 0 and div5 != 0:
        return "Fizz"
    else:
        if div3 != 0 and div5 == 0:
            return "Buzz"
        else:
            if div3 == 0 and div5 == 0:
                return "FizzBuzz"
            else:
                return VarA
