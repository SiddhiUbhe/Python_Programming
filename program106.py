# Write a program to accept age from the user and check whether the person is eligible to vote. (Age should be 18 or above.)

def VoteAge(Age):
    if Age >= 18:
        return ("eligible")
    else:
        return ("Not eligible")
    

def main():
    Input = int(input("Enter your age :"))
    result = VoteAge(Input)
    print("You Are :",result)

if __name__ == "__main__":
    main()