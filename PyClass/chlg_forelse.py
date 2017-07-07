"""
Create a program that takes an IP address and prints out the number of segments and their length.
Verify the validity of the IP given. Invalid IPs:
    .123.45.678.91
    123.456.789.
    123.456.1234567
    12.12t.12
    12.3.45.6.78
    '' - nothing
This is a loop exercise - spliting is cheating!
"""
def ipcheck(ipadd):
    counter = 0
    sec = {0:""}
    for i in ipadd:
        if i in "0123456789":
            sec[counter] += i
        elif i == ".":
            if counter == 0 and sec[counter] == "":
                print("ERROR!--Invalid IP!")
                return False
            counter += 1
            sec[counter] = ""
        else:
            print("ERROR!--Invalid IP!")
            return False
    print("IP {0} has {1} sections:".format(ipadd, str(len(sec.keys()))))
    for s in sec.keys():
        print("Section {0} has {1} characters".format(str(s), str(len(str(sec[s])))))
    return sec

ipadd = input("Enter IP:")
ipcheck(ipadd)
