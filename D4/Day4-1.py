data = open('input', 'r').read().split('\n\n')

def checkrequired(string):
    if (string.find("byr:") != -1 and
        string.find("iyr:") != -1 and
        string.find("eyr:") != -1 and
        string.find("hgt:") != -1 and
        string.find("hcl:") != -1 and
        string.find("ecl:") != -1 and
        string.find("pid:") != -1):
        return True
    return False

c = 0
for passport in data:
    if checkrequired(passport):
        c += 1
print(c)
