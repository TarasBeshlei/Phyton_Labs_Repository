import re




def NASA_search_in_log_file():
    count = 0
    file = open('access.webarchive')
    for line in file:
        if re.search('2[2-4]/Mar/2009:[0-2][0-9]:[0-5][0-9]:[0-5][0-9].*GET.*400', str(line)):
            count+=1
    print(count)
    file.close()


if __name__ == "__main__":
    NASA_search_in_log_file()