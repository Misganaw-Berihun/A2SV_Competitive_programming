def count_substring(string, sub_string):
    start = 0;
    start = string.find(sub_string,start)
    count = 0
    while(start != -1):
        count += 1;
        start = string.find(sub_string,start + 1)
    return count


    
