import subprocess

with open("sitenames.txt", 'r') as INPUTFILE:
    for LINE in INPUTFILE:
        URL = LINE.rstrip()
        print()
        print("URL is: ",LINE)
        print('----------------------------------------')

        NSLRESULT = subprocess.run(['nslookup', URL], capture_output=True, universal_newlines=True)
        print()
        print("NSLRESULT is:")
        print()
        print(NSLRESULT.stdout)
        print('----------------------------------------')

        NSLOUT = NSLRESULT.stdout.split( )
        print("The first 9 items in the result (split by spaces) are:")
        print()
        print (NSLOUT[0])
        print (NSLOUT[1])
        print (NSLOUT[2])
        print (NSLOUT[3])
        print (NSLOUT[4])
        print (NSLOUT[5])
        print (NSLOUT[6])
        print (NSLOUT[7])
        print (NSLOUT[8])
        print (NSLOUT[9])
        print('----------------------------------------')

        IPADDR = NSLOUT[9]
        PINGRESULT = subprocess.run(['ping', '-c', '1', IPADDR], capture_output=True, universal_newlines=True)
        print(PINGRESULT.stdout)
        print('----------------------------------------')

        if str.isdigit(IPADDR[0]) == True:
            FIRST_CHAR = int(IPADDR[0])
        else:
            FIRST_CHAR = IPADDR[0]

        print("The first character in the ip variable is:",IPADDR[0])
        SELECTION={
            1: 'The first character in the IP address is a 1.',
            2: 'The first character in the IP address is a 2.',
            3: 'The first character in the IP address is a 3.',
            4: 'The first character in the IP address is a 4.',
            5: 'The first character in the IP address is a 5.',
            6: 'The first character in the IP address is a 6.',
            7: 'The first character in the IP address is a 7.',
            8: 'The first character in the IP address is a 8.',
            9: 'The first character in the IP address is a 9.'
        }
        OBSERVATION = SELECTION.get(FIRST_CHAR,"The first character in that variable is not a number.")
        print(OBSERVATION)
        print('----------------------------------------')

        OUTPUTFILE = open("outputfile.txt", "a")
        TO_WRITE = URL + "," + IPADDR + "," + OBSERVATION + "\n"
        OUTPUTFILE.write(TO_WRITE)
        OUTPUTFILE.close()

INPUTFILE.close()
