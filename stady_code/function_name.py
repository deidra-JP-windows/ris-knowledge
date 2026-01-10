def foo():
    print("foo called")

def bar():
    print("bar called")

def main():
    mapping = {
        "a": "foo",
        "b": "bar"
    }
    for key, func_name in mapping.items():
        print(f"Calling function for key: {key}")
        func = locals().get(func_name)
        if callable(func):
            print(f"Executing {func_name}()")
            func()

if __name__ == '__main__':
    main()
