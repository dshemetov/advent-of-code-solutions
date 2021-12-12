from advent_tools import Puzzle

def solve_a(s: str) -> int:
    passports = [str_to_passport_dict(" ".join(batch.split("\n"))) for batch in s.split("\n\n")]
    return sum(map(validate_passport_a, passports))

def str_to_passport_dict(s: str) -> dict:
    return dict(e.strip().split(":") for e in s.strip().split(" "))

def validate_passport_a(d: dict) -> bool:
    return {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}.issubset(set(d.keys()))

def solve_b(s: str) -> int:
    passports = [str_to_passport_dict(" ".join(batch.split("\n"))) for batch in s.split("\n\n")]
    return sum(map(validate_passport_b, passports))

def validate_passport_b(d: dict) -> bool:
    if not {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}.issubset(set(d.keys())):
        return False

    try:
        birth_check = 1920 <= int(d["byr"]) <= 2002
        issue_check = 2010 <= int(d["iyr"]) <= 2020
        expiration_check = 2020 <= int(d["eyr"]) <= 2030

        if d["hgt"][-2:] == "cm":
            height_check = 150 <= int(d["hgt"][:-2]) <= 193
        elif d["hgt"][-2:] == "in":
            height_check = 59 <= int(d["hgt"][:-2]) <= 76
        else:
            height_check = False
    except:
        return False

    hcl = d["hcl"]
    if not (hcl[0] == "#" and set(hcl[1:]).issubset(set("123456789abcdef")) and len(hcl[1:]) == 6):
        return False

    eye_color_check = d["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    pid = d["pid"]
    if not (pid.isdigit() and len(pid) == 9):
        return False

    return all([birth_check, issue_check, expiration_check, height_check, eye_color_check])


class Solution:
    @property
    def answer_a(self) -> int:
        return solve_a(Puzzle(4, 2020).input_data)

    @property
    def answer_b(self) -> int:
        return solve_b(Puzzle(4, 2020).input_data)
