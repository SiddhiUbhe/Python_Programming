import threading

def EvenNum():

    print("Inside EvenNum : ",threading.get_ident())

    for i in range(1,11):

        if(i % 2 == 0):

            print(i)

def OddNum():

    print("Inside OddNum : ",threading.get_ident())

    for i in range(1,11):

        if(i % 2 != 0):

            print(i)

def main():

    t1 = threading.Thread(target = EvenNum)
    t1.start()

    t2 = threading.Thread(target = OddNum)
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()