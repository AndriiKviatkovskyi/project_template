from app.io.input import read_input, read_file_python, read_file_pandas
from app.io.output import print_output, write_file


def main():

    print("Test 1:\n")
    text_from_console = read_input()
    print_output(text_from_console)
    write_file(text_from_console, "data/writeTest1.txt")

    print("\nTest 2:\n")
    text_from_file = read_file_python("data/readTest2.txt")
    print_output(text_from_file)
    write_file(text_from_file, "data/writeTest2.txt")

    print("\nTest 3:\n")
    text_from_file_pandas = read_file_pandas("data/readTest3.txt")
    print_output(text_from_file_pandas)
    write_file(text_from_file_pandas, "data/writeTest3.txt")


if __name__ == "__main__":
    main()
