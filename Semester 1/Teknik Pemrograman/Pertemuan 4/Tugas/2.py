def main():
    result = "1"
    for i in range(2,40):
        result = result + "+"+ str(i)
        # cara alternative
        # print(i,end="+")
    print(result)
if __name__ == "__main__":
    main()