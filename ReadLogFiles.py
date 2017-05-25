with open("C:\\Users\\vamsi\\Desktop\\Application.log") as f:
    for rec in f:
        print(rec.strip("\n\r"))
