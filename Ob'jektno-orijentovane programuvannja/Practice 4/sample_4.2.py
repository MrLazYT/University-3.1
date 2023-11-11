def fun2(fun):
    print("Running my_function from fun2")
    fun()

def my_function():
    print("Hello From My Function!")

fun2(my_function)