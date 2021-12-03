# Part a
with open("input2a.txt") as f:
    lines = f.readlines()

def validate_password(line):
    a,b,c = line.split(" ")
    charMin, charMax = a.split("-")
    charMin=int(charMin)
    charMax=int(charMax)
    char = b[0]
    password = c.strip()
    valid = 1 if charMin <= password.count(char) <= charMax else 0
    return valid

n_valid_passwords = sum(map(validate_password, lines))
n_valid_passwords

# Part b
