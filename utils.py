def get_number(prompt, cast_type=int, min_val=None, max_val=None):
    while True:
        try:
            value = cast_type(input(prompt))
            
            if min_val is not None and value < min_val:
                print(f"Value must be >= {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Value must be <= {max_val}")
                continue
            return value
        except ValueError:
            print("Provided value is not a number")

def get_non_empty_string(prompt):
    while True:
        value = input(prompt)
        if value.strip():
            return value
        print("Provided value cannot be empty")

