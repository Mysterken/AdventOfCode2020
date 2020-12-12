data = open('input', 'r').read().split('\n\n')

# I failed this one...
# So the answer is incorrect

def checkrequired(string):
    def content(string, field, start, end):
        ct = (string[string.find(field)+start:string.find(field)+end])
        return ct

    string += ' '
    PASS = False

    if (string.find("byr:") != -1 and
        string.find("iyr:") != -1 and
        string.find("eyr:") != -1 and
        string.find("hgt:") != -1 and
        string.find("hcl:") != -1 and
        string.find("ecl:") != -1 and
        string.find("pid:") != -1):
        try:
            if 1920 <= int(content(string, 'byr:', 4, 8)) <= 2002:
                if 2010 <= int(content(string, 'iyr:', 4, 8)) <= 2020:
                    if 2020 <= int(content(string, 'eyr:', 4, 8)) <= 2030:
                        try :
                            if (150 <= int(content(string, 'hgt:', 4, 7)) <= 193 and
                                content(string, 'hgt:', 7, 9) == 'cm'):
                                PASS = True
                        except:
                            if (59 <= int(content(string, 'hgt:', 4, 6)) <= 76 and
                                content(string, 'hgt:', 6, 8) == 'in'):
                                PASS = True
                        if PASS:
                            if (content(string, 'hcl:', 4, 11).find('#') != -1 and
                                content(string, 'hcl:', 4, 11).find(' ') == -1):
                                    if (content(string, 'hcl:', 11, 12).find(' ') != -1 or
                                        content(string, 'hcl:', 12, 13).isalpha()):
                                        if (content(string, 'ecl:', 4, 7) == 'amb' or
                                            content(string, 'ecl:', 4, 7) == 'blu' or
                                            content(string, 'ecl:', 4, 7) == 'brn' or
                                            content(string, 'ecl:', 4, 7) == 'gry' or
                                            content(string, 'ecl:', 4, 7) == 'grn' or
                                            content(string, 'ecl:', 4, 7) == 'hzl' or
                                            content(string, 'ecl:', 4, 7) == 'oth'):
                                            if (content(string, 'ecl:', 7, 8) == ' ' or
                                                content(string, 'ecl:', 8, 9).isalpha()):
                                                if (int(content(string, 'pid:', 4, 13)) and
                                                    (content(string, 'pid:', 13, 14)) == ' '):
                                                    return True                                         
        except:
            pass
    return False

c = 0
for passport in data:
    if checkrequired(passport):
        c += 1
print(c)
