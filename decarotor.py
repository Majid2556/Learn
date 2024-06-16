#decarotor


def f_decorator(function):

    def kill():
        print("I kill the Evil")
        function()

    return kill()

@f_decorator
def func():
    print("This is func")
