
import re
import csv


with open("rplidar_scan1ida.txt") as file:
    
    #Get just numbers from txt file
    clean = re.findall('\d*?\.\d', file.read())
    #print(clean)
    clean_chunck = []
    for i in range(0, len(clean), 2):
        chunk = clean[i:i+2]
        clean_chunck.append(chunk)
    

    print(clean_chunck)

    

    with open('rplidar_scan1ida_Out_osource.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerows(clean_chunck)
        print('saved')

    





