INPUT_FILE = "./common_passwords.txt"
with open(input_file), "r", encoding="utf-8") as file:
    data =file.read()

lines = data.split("\n")
