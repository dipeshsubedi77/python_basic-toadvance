def main():
    message(5)
def message(times):
    if times > 0:
        print("this is a recursive funcrion")
        message(times - 1)
main()