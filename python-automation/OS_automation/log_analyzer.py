def analyze_logs(files_path):
    count={"INFO":0, "WARNING":0, "ERROR":0}
    with open(files_path,"r")as file:
        for line in file:
            if "INFO" in line:
                count ["INFO"] +=1
            elif "WARNING" in line:
                count ["WARNING"] +=1
            elif "ERROR" in line:
                count ["ERROR"] +=1
    return count

if __name__== "__main__":
    result=analyze_logs("sample.txt")
    print(result)
