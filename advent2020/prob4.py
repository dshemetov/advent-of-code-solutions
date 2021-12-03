# Part a
def parse_line(line):
    line = line.strip()
    entries = line.split(" ")
    fields_dict = dict(map(lambda e: e.strip().split(":"), entries))
    return fields_dict

def validate_passport(passport):
    required_fields = set(passport.keys())
    valid = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}.issubset(required_fields)
    return valid

with open("input4a.txt") as f:
    lines = f.readlines()

# Group lines into passports
ixs = [i for i in range(len(lines)) if lines[i] == "\n"]
unparsed_passports = [
    " ".join(lines[ixs[i] + 1 : ixs[i + 1]]) for i in range(len(ixs) - 1)
]
unparsed_passports += [" ".join(lines[: ixs[0]]), " ".join(lines[ixs[-1] + 1 :])]
passports = map(parse_line, unparsed_passports)
print(sum(map(validate_passport, passports)))


# Part b
def validate_passport(passport):
    required_fields = set(passport.keys())

    field_check = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}.issubset(required_fields)
    if not field_check:
        return False

    try:
        byr = passport["byr"]
        birth_check = 1920 <= int(byr) <= 2002

        iyr = passport["iyr"]
        issue_check = 2010 <= int(iyr) <= 2020

        eyr = passport["eyr"]
        expiration_check = 2020 <= int(eyr) <= 2030

        hgt = passport["hgt"]
        hgt_num = hgt[:-2]
        hgt_units = hgt[-2:]
        if hgt_units == "cm":
            height_check = 150 <= int(hgt_num) <= 193
        elif hgt_units == "in":
            height_check = 59 <= int(hgt_num) <= 76
        else:
            return False
    except:
        return False

    hcl = passport["hcl"]
    hcl_chars = {str(x) for x in range(10)}.union(list("abcdef"))
    if not (hcl[0] == "#" and set(hcl[1:]).issubset(hcl_chars) and len(hcl[1:]) == 6):
        return False

    ecl = passport["ecl"]
    eye_color_check = ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    pid = passport["pid"]
    if not (pid.isdigit() and len(pid) == 9):
        return False

    return birth_check and issue_check and expiration_check and height_check and eye_color_check

passports = map(parse_line, unparsed_passports)
sum(map(validate_passport, passports))
