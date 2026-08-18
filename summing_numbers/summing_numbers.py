def main():
    print("Summing Numbers: Rebuilding the sum(34,56,23,56,23)")
    print("================")
    sum = mysum(*[1,2,3,4])
    print(f"Sum: {sum}")

def mysum(*args):
    sum = 0
    try: 
        for i in args:
            sum += i
        return sum
    except TypeError as err:
        print(f"{err}")

if __name__ == "__main__":
    main()