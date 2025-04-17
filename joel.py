Scoping refers to the visibility and accessibility of variables in different parts of your code while the call stacks is a data structure that tracks functions calls during program execution. 


def outer_function():
    x = "outer x"
    print("Entering outer_function()")
    print("x in outer_function:", x)

    def middle_function():
        x = "middle x"
        print("  Entering middle_function()")
        print("  x in middle_function:", x)

        def inner_function():
            x = "inner x"
            print("    Entering inner_function()")
            print("    x in inner_function:", x)
            print("    Leaving inner_function()")

        inner_function()
        print("  Leaving middle_function()")

    middle_function()
    print("Leaving outer_function()")

outer_function()
