while True:
    try:
        iData = int(input("Enter the number Buddy:\n"))
        print(100/iData)
        break
    except ValueError:
        print("Enter proper data \n")
    except ZeroDivisionError:
        print("Don't enter 0\n")
    except :
        print("Ufff")
        break
    finally:
        print("Bye Bye\n")
