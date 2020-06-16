import subprocess

with open("sitenames.txt", 'r') as f:
    for l in f:
        varURL = l.rstrip()
        print()
        print("varURL is: ",l)
        print('----------------------------------------')

        nslresult = subprocess.run(['nslookup', varURL], capture_output=True, universal_newlines=True)
        print()
        print("nslresult is:")
        print()
        print(nslresult.stdout)
        print('----------------------------------------')

        nslout = nslresult.stdout.split( )
        print("The first 9 items in the result (split by spaces) are:")
        print()
        print (nslout[0])
        print (nslout[1])
        print (nslout[2])
        print (nslout[3])
        print (nslout[4])
        print (nslout[5])
        print (nslout[6])
        print (nslout[7])
        print (nslout[8])
        print (nslout[9])
        print('----------------------------------------')

        ip = nslout[9]
        pingresult = subprocess.run(['ping', '-c', '1', ip], capture_output=True, universal_newlines=True)
        print(pingresult.stdout)
        print('----------------------------------------')

        if str.isdigit(ip[0]) == True:
            first_char = int(ip[0])
        else:
            first_char = ip[0]

        print("The first character in the ip variable is:",ip[0])
        switcher={
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
        print(switcher.get(first_char),"The first character in that variable is not a number.")
        print('----------------------------------------')

f.close()
