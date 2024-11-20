attempted=0
logged=False
dsaques=['1. A queue follows: A.LIFO B.FIFO C.Linear Tree D.Ordered array\n',
         '2. Which data structure is used for recursion: A.Stack B.Queue C.Binary Tree D.B Tree\n',
         '3. What is worst case time complexity of Quick Sort: A.O(n) B.O(n (log n)) C.O(n^2) D.None\n',
         '4. The data structure which implements BFT on graph: A.Stack B.Array C.Tree D.Queue\n',
         '5. Which is based on LIFO principle: A.Stack B.Queue C.Array D.Linked List\n']
with open('dsa.txt','a') as dsa:
    dsa.writelines(dsaques)
dbmsques=['1. Who created DBMS: A.Edgar Frank Codd B.Charles Benchman C.Charles Babbage D.Sharon Codd\n',
          '2. Which of the following is not a type of database: A.Heirarchical B.Network C.Relational D.Decentralised\n',
          '3. What is data of data called: A.Metadata B.Teradata C.Relations D.Hyper data\n',
          '4. What is tables known as in RDBMS: A.Records B.Keys C.Relations D.Fields\n',
          '5. Which of the following is not a language in DBMS: A.DDL B.DML C.TCL D.None\n']
with open('dbms.txt','w') as dbms:
    dbms.writelines(dbmsques)
pythonques=['1. Who invented Python: A.Guido Van Rossum B.Charles Babbage C.Sharon Codd D.Charles Bechman\n',
            '2. Is Python case sensitive: A.No B.Yes C.Machine dependent D.None\n',
            '3. Which is extension for Python file: A.py B.pl C.python D.p\n',
            '4. How a block of code is defined in Python: A.Indentation B.Brackets C.Key D.All of these\n',
            '5. Which keyword is used to define a function in Python: A.def B.function C.fun D.define\n']
with open('python.txt','a') as python:
        python.writelines(pythonques)
def register():
    enrollment=input("Enter your enrollment no.:")
    name=input("Enter your name:")
    college_name=input("Enter your college name:")
    password=input("Enter your password:")
    with open('user.txt','a') as file:
        file.write(f"{enrollment},{name},{college_name},{password} \n")
    with open('login.txt','a') as filedetails:
        filedetails.write(f"{enrollment},{password} \n")
def login():
    global logged
    enrollment=input("Enter enrollment no.:")
    password=input("Enter password:")
    with open('login.txt','r') as file:
        rep=file.readlines()
        data={}
        lst=[]
        for i in rep:
            i=i[0:-2:1]
            lst.append(i)
        for i in lst:
            data[i[0:12]]=i[13::]
        for i in data:
            if i==enrollment and data[i]==password:
                logged=True
        if logged==True:
            print("Logged in successfully")
        else:
            print("invalid details")
def attemptquiz():
    global logged
    global attempted
    dsacorrect=['B','A','C','D','A']
    dbmscorrect=['B','D','A','C','D']
    pythoncorrect=['A','B','A','A','A']
    login()
    if logged==True:
        choice=int(input("""Choose option:
              1.DBMS
              2.DSA
              3.Python"""))
        if choice==1:
            j=0
            with open('dbms.txt','r') as dbms:
                li=dbms.readlines()
                for i in li:
                    print(i)
                    ans=input("Enter your ans:")
                    if ans==dbmscorrect[j]:
                        attempted+=20
                    j+=1
        elif choice==2:
            j=0
            with open('dsa.txt','r') as dsa:
                li=dsa.readlines()
                for i in li:
                    print(i)
                    ans=input("Enter your ans:")
                    if ans==dsacorrect[j]:
                        attempted+=20
                    j+=1
        elif choice==3:
            j=0
            with open('python.txt','r') as python:
                li=python.readlines()
                for i in li:
                    print(i)
                    ans=input("Enter your ans:")
                    if ans==pythoncorrect[j]:
                        attempted+=20
                    j+=1
        else:
            print("Invalid choice")
def showresult():
    global attempted
    print(f"Marks out of 100:{attempted}")
def exit():
    exit()

op=int(input("""Enter choice:
1.Register
2.Login
3.Attemp Quiz
4.Show Result
5. Exit"""))
if op==1:
    register()
elif op==2:
    login()
elif op==3:
    attemptquiz()
elif op==4:
    showresult()
elif op==5:
    exit()
else:
    print("Invalid choice")
       
        
            
                
        
              
    
