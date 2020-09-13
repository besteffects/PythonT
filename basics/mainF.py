from time import sleep

print("This is my file to demonstrate best practices")


def process_data(self):
    print('Beginning data processing...')
    modified_data = self + " that has been modified"
    sleep(3)
    print("Data processing finished")
    return modified_data


def read_data_from_web():
    print("Reading data from web")
    self = "Data from the web"
    return self


def write_data_to_database(self):
    print("Writing data to a database")
    print(self)


def main():
    self = read_data_from_web()
    modified_data = process_data(self)
    write_data_to_database(modified_data)


if __name__ == "__main__":
    main()
