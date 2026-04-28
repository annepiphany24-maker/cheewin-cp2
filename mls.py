def initialize_library():

    try:
        file = open("MLS.txt", "x")
        file.close()
        print("File created successfully.")

    except FileExistsError:
        print("Library file already exists.")

    file = open("MLS.txt", "w")

    file.write("To Kill a Mockingbird\n")
    file.write("Behind the Blue Sky\n")
    file.write("Between the Rainbows\n")
    file.write("Learn Computer Programming\n")

    file.close()

    print("Initial books added successfully!")


initialize_library()