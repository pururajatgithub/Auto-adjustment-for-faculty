import numpy as np 
import datetime
import calendar
import pandas as pd 

def tt():
    
    teacher1=([1,1,0,0,0,0,1,1],
            [0,1,0,1,1,0,1,1],
            [1,1,0,0,1,0,1,1],
            [1,1,0,0,1,0,1,1],
            [1,1,0,0,0,0,1,1],
            [0,0,0,0,0,0,0,0])
    teacher2=[]
    teacher2=([0,0,1,1,1,0,1,1],
            [0,0,0,1,1,0,0,1],
            [0,0,1,1,0,0,1,1],
            [0,0,1,1,0,1,0,0],
            [0,1,1,0,1,0,1,0],
            [0,0,0,0,0,0,0,0])
    teacher3=[]
    teacher3=([1,1,1,0,0,0,1,1],
              [1,0,0,0,0,0,1,1],
              [0,0,0,0,1,1,0,1],
              [1,1,0,0,1,1,1,0],
              [0,0,1,1,1,0,1,1],
              [0,0,0,0,0,0,0,0])
    teacher4=[]
    teacher4=([0,0,0,1,1,0,0,0],
              [0,1,1,0,0,0,0,0],
              [0,0,1,1,0,1,0,0],
              [0,0,1,0,1,0,1,0],
              [1,1,0,1,0,1,0,0],
              [0,0,0,0,0,0,0,0])
    days=5
    hours=8
    import datetime
    import calendar
    now = datetime.datetime.now().weekday()
    
    now+=1
    print(now)
    print("if teacher 1 is absent press: 1\nif teacher 2 is absent press: 2\nif teacher 3 is absent press : 3\nif teacher 4 is absent press : 4")
    ta=int(input())
    if ta==1: #if teacher 1 is absent
        if now==1:  #check if day is Monday
            print("day is monday")
            
            if teacher1[0][0]==1:#check if teacher 1 has class at 9am
                if teacher2[0][0]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher3[0][0]==0:
                    print("Teacher 3 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher4[0][0]==0:
                    print("Teacher 4 will  be substiute  the lecture from 9-10 am")
                    
                # elif teacher5[0][0]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 9-10 am") 
                    
                else:
                    print("No teacher is Free")

            if teacher1[0][1]==1:#check if teacher 1 has class at 10am
                if teacher2[0][1]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 10-11 am")
                elif teacher3[0][1]==0:
                    print("Teacher 3 will  be substiute  the lecture from 10-11 am")
                elif teacher4[0][1]==0:
                    print("Teacher 4 will  be substiute  the lecture from 10-11 am")
                # elif teacher5[0][1]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 10-11 am") 
                else:
                    print("No teacher is Free")
            if teacher1[0][2]==1:#check if teacher 1 has class at 11am
                if teacher2[0][2]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 11-12 pm")
                    
                elif teacher3[0][2]==0:
                    print("Teacher 3 will  be substiute  the lecture from 11-12 pm")
                elif teacher4[0][2]==0:
                    print("Teacher 4 will  be substiute  the lecture from 11-12 pm")
                # elif teacher5[0][2]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 11-12 pm") 
                else:
                    print("No teacher is Free")
            if teacher1[0][3]==1:#check if teacher 1 has class at 12am
                if teacher2[0][3]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 12-1 pm")
                    
                elif teacher3[0][3]==0:
                    print("Teacher 3 will  be substiute  the lecture from 12-1 pm")
                elif teacher4[0][3]==0:
                    print("Teacher 4 will  be substiute  the lecture from 12-1 pm")
                # elif teacher5[0][3]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 12-1 pm") 
                else:
                    print("No teacher is Free")
            if teacher1[0][4]==1:#check if teacher 1 has class at 1pm
                if teacher2[0][4]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 1-2 pm")
                    
                elif teacher3[0][4]==0:
                    print("Teacher 3 will  be substiute  the lecture from 1-2 pm")
                elif teacher4[0][4]==0:
                    print("Teacher 4 will  be substiute  the lecture from 1-2 pm")
                # elif teacher5[0][4]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 1-2 pm") 
                else:
                    print("No teacher is Free")
            if teacher1[0][5]==1:#check if teacher 1 has class at 2pm
                if teacher2[0][5]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 2-3 pm")
                    
                elif teacher3[0][5]==0:
                    print("Teacher 3 will  be substiute  the lecture from 2-3 pm")
                elif teacher4[0][5]==0:
                    print("Teacher 4 will  be substiute  the lecture from 2-3 pm")
                # elif teacher5[0][5]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 2-3 pm") 
                else:
                    print("No teacher is Free")
            if teacher1[0][6]==1:#check if teacher 1 has class at 3pm
                if teacher2[0][6]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 3-4 pm")
                    
                elif teacher3[0][6]==0:
                    print("Teacher 3 will  be substiute  the lecture from 3-4 pm")
                elif teacher4[0][6]==0:
                    print("Teacher 4 will  be substiute  the lecture from 3-4 pm")
                # elif teacher5[0][6]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 3-4 pm") 
                else:
                    print("No teacher is Free") 
            if teacher1[0][7]==1:#check if teacher 1 has class at 4pm
                if teacher2[0][7]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 4-5 pm")
                    
                elif teacher3[0][7]==0:
                    print("Teacher 3 will  be substiute  the lecture from 4-5 pm")
                elif teacher4[0][7]==0:
                    print("Teacher 4 will  be substiute  the lecture from 4-5 pm")
                # elif teacher5[0][7]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 4-5 pm") 
                else:
                    print("No teacher is Free")
        elif now==2:#check if day is Tuesday
            
            if teacher1[1][0]==1:#check if teacher 1 has class at 9am
                if teacher2[1][0]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher3[1][0]==0:
                    print("Teacher 3 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher4[1][0]==0:
                    print("Teacher 4 will  be substiute  the lecture from 9-10 am")
                    
                # elif teacher5[1][0]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 9-10 am") 
                    
                else:
                    print("No teacher is Free")

            if teacher1[1][1]==1:#check if teacher 1 has class at 10am
                if teacher2[1][1]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 10-11 am")
                elif teacher3[1][1]==0:
                    print("Teacher 3 will  be substiute  the lecture from 10-11 am")
                elif teacher4[1][1]==0:
                    print("Teacher 4 will  be substiute  the lecture from 10-11 am")
                # elif teacher5[1][1]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 10-11 am") 
                else:
                    print("No teacher is Free")
            if teacher1[1][2]==1:#check if teacher 1 has class at 11am
                if teacher2[1][2]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 11-12 pm")
                    
                elif teacher3[1][2]==0:
                    print("Teacher 3 will  be substiute  the lecture from 11-12 pm")
                elif teacher4[1][2]==0:
                    print("Teacher 4 will  be substiute  the lecture from 11-12 pm")
                # elif teacher5[1][2]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 11-12 pm") 
                else:
                    print("No teacher is Free")
            if teacher1[1][3]==1:#check if teacher 1 has class at 12am
                if teacher2[1][3]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 12-1 pm")
                    
                elif teacher3[1][3]==0:
                    print("Teacher 3 will  be substiute  the lecture from 12-1 pm")
                elif teacher4[1][3]==0:
                    print("Teacher 4 will  be substiute  the lecture from 12-1 pm")
                # elif teacher5[1][3]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 12-1 pm") 
                else:
                    print("No teacher is Free")
            if teacher1[1][4]==1:#check if teacher 1 has class at 1pm
                if teacher2[1][4]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 1-2 pm")
                    
                elif teacher3[1][4]==0:
                    print("Teacher 3 will  be substiute  the lecture from 1-2 pm")
                elif teacher4[1][4]==0:
                    print("Teacher 4 will  be substiute  the lecture from 1-2 pm")
                # elif teacher5[1][4]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 1-2 pm") 
                else:
                    print("No teacher is Free")
            if teacher1[1][5]==1:#check if teacher 1 has class at 2pm
                if teacher2[1][5]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 2-3 pm")
                    
                elif teacher3[1][5]==0:
                    print("Teacher 3 will  be substiute  the lecture from 2-3 pm")
                elif teacher4[1][5]==0:
                    print("Teacher 4 will  be substiute  the lecture from 2-3 pm")
                # elif teacher5[1][5]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 2-3 pm") 
                else:
                    print("No teacher is Free")
            if teacher1[1][6]==1:#check if teacher 1 has class at 3pm
                if teacher2[1][6]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 3-4 pm")
                    
                elif teacher3[1][6]==0:
                    print("Teacher 3 will  be substiute  the lecture from 3-4 pm")
                elif teacher4[1][6]==0:
                    print("Teacher 4 will  be substiute  the lecture from 3-4 pm")
                # elif teacher5[1][6]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 3-4 pm") 
                else:
                    print("No teacher is Free") 
            if teacher1[1][7]==1:#check if teacher 1 has class at 4pm
                if teacher2[1][7]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 4-5 pm")
                    
                elif teacher3[1][7]==0:
                    print("Teacher 3 will  be substiute  the lecture from 4-5 pm")
                elif teacher4[1][7]==0:
                    print("Teacher 4 will  be substiute  the lecture from 4-5 pm")
                # elif teacher5[1][7]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 4-5 pm") 
                else:
                    print("No teacher is Free")
        elif now==3:#check if day is Wednesday
            
            if teacher1[2][0]==1:#check if teacher 1 has class at 9am
                if teacher2[2][0]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher3[2][0]==0:
                    print("Teacher 3 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher4[2][0]==0:
                    print("Teacher 4 will  be substiute  the lecture from 9-10 am")
                    
                # elif teacher5[2][0]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 9-10 am") 
                    
                else:
                    print("No teacher is Free")

            if teacher1[2][1]==1:#check if teacher 1 has class at 10am
                if teacher2[2][1]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 10-11 am")
                elif teacher3[2][1]==0:
                    print("Teacher 3 will  be substiute  the lecture from 10-11 am")
                elif teacher4[2][1]==0:
                    print("Teacher 4 will  be substiute  the lecture from 10-11 am")
                # elif teacher5[2][1]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 10-11 am") 
                else:
                    print("No teacher is Free")
            if teacher1[2][2]==1:#check if teacher 1 has class at 11am
                if teacher2[2][2]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 11-12 pm")
                    
                elif teacher3[2][2]==0:
                    print("Teacher 3 will  be substiute  the lecture from 11-12 pm")
                elif teacher4[2][2]==0:
                    print("Teacher 4 will  be substiute  the lecture from 11-12 pm")
                # elif teacher5[2][2]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 11-12 pm") 
                else:
                    print("No teacher is Free")
            if teacher1[2][3]==1:#check if teacher 1 has class at 12am
                if teacher2[2][3]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 12-1 pm")
                    
                elif teacher3[2][3]==0:
                    print("Teacher 3 will  be substiute  the lecture from 12-1 pm")
                elif teacher4[2][3]==0:
                    print("Teacher 4 will  be substiute  the lecture from 12-1 pm")
                # elif teacher5[2][3]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 12-1 pm") 
                else:
                    print("No teacher is Free")
            if teacher1[2][4]==1:#check if teacher 1 has class at 1pm
                if teacher2[2][4]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 1-2 pm")
                    
                elif teacher3[2][4]==0:
                    print("Teacher 3 will  be substiute  the lecture from 1-2 pm")
                elif teacher4[2][4]==0:
                    print("Teacher 4 will  be substiute  the lecture from 1-2 pm")
                # elif teacher5[2][4]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 1-2 pm") 
                else:
                    print("No teacher is Free")
            if teacher1[2][5]==1:#check if teacher 1 has class at 2pm
                if teacher2[2][5]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 2-3 pm")
                    
                elif teacher3[2][5]==0:
                    print("Teacher 3 will  be substiute  the lecture from 2-3 pm")
                elif teacher4[2][5]==0:
                    print("Teacher 4 will  be substiute  the lecture from 2-3 pm")
                # elif teacher5[2][5]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 2-3 pm") 
                else:
                    print("No teacher is Free")
            if teacher1[2][6]==1:#check if teacher 1 has class at 3pm
                if teacher2[2][6]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 3-4 pm")
                    
                elif teacher3[2][6]==0:
                    print("Teacher 3 will  be substiute  the lecture from 3-4 pm")
                elif teacher4[2][6]==0:
                    print("Teacher 4 will  be substiute  the lecture from 3-4 pm")
                # elif teacher5[2][6]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 3-4 pm") 
                else:
                    print("No teacher is Free") 
            if teacher1[2][7]==1:#check if teacher 1 has class at 4pm
                if teacher2[2][7]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 4-5 pm")
                    
                elif teacher3[2][7]==0:
                    print("Teacher 3 will  be substiute  the lecture from 4-5 pm")
                elif teacher3[2][7]==0:
                    print("Teacher 4 will  be substiute  the lecture from 4-5 pm")
                # elif teacher5[2][7]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 4-5 pm") 
                else:
                    print("No teacher is Free")
        elif now==4:#check if day is Thursday
            
            if teacher1[3][0]==1:#check if teacher 1 has class at 9am
                if teacher2[3][0]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher3[3][0]==0:
                    print("Teacher 3 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher4[3][0]==0:
                    print("Teacher 4 will  be substiute  the lecture from 9-10 am")
                    
                # elif teacher5[4][0]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 9-10 am") 
                    
                else:
                    print("No teacher is Free")

            if teacher1[3][1]==1:#check if teacher 1 has class at 10am
                if teacher2[3][1]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 10-11 am")
                elif teacher3[3][1]==0:
                    print("Teacher 3 will  be substiute  the lecture from 10-11 am")
                elif teacher4[3][1]==0:
                    print("Teacher 4 will  be substiute  the lecture from 10-11 am")
                # elif teacher5[4][1]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 10-11 am") 
                else:
                    print("No teacher is Free")
            if teacher1[3][2]==1:#check if teacher 1 has class at 11am
                if teacher2[3][2]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 11-12 pm")
                    
                elif teacher3[3][2]==0:
                    print("Teacher 3 will  be substiute  the lecture from 11-12 pm")
                elif teacher4[3][2]==0:
                    print("Teacher 4 will  be substiute  the lecture from 11-12 pm")
                # elif teacher5[3][2]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 11-12 pm") 
                else:
                    print("No teacher is Free")
            if teacher1[3][3]==1:#check if teacher 1 has class at 12am
                if teacher2[3][3]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 12-1 pm")
                    
                elif teacher3[3][3]==0:
                    print("Teacher 3 will  be substiute  the lecture from 12-1 pm")
                elif teacher4[3][3]==0:
                    print("Teacher 4 will  be substiute  the lecture from 12-1 pm")
                # elif teacher5[4][3]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 12-1 pm") 
                else:
                    print("No teacher is Free")
            if teacher1[3][4]==1:#check if teacher 1 has class at 1pm
                if teacher2[4][4]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 1-2 pm")
                    
                elif teacher3[3][4]==0:
                    print("Teacher 3 will  be substiute  the lecture from 1-2 pm")
                elif teacher4[3][4]==0:
                    print("Teacher 4 will  be substiute  the lecture from 1-2 pm")
                # elif teacher5[3][4]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 1-2 pm") 
                else:
                    print("No teacher is Free")
            if teacher1[3][5]==1:#check if teacher 1 has class at 2pm
                if teacher2[3][5]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 2-3 pm")
                    
                elif teacher3[3][5]==0:
                    print("Teacher 3 will  be substiute  the lecture from 2-3 pm")
                elif teacher4[3][5]==0:
                    print("Teacher 4 will  be substiute  the lecture from 2-3 pm")
                # elif teacher5[4][5]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 2-3 pm") 
                else:
                    print("No teacher is Free")
            if teacher1[3][6]==1:#check if teacher 1 has class at 3pm
                if teacher2[3][6]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 3-4 pm")
                    
                elif teacher3[3][6]==0:
                    print("Teacher 3 will  be substiute  the lecture from 3-4 pm")
                elif teacher4[3][6]==0:
                    print("Teacher 4 will  be substiute  the lecture from 3-4 pm")
                # elif teacher5[4][6]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 3-4 pm") 
                else:
                    print("No teacher is Free") 
            if teacher1[4][7]==1:#check if teacher 1 has class at 4pm
                if teacher2[4][7]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 4-5 pm")
                    
                elif teacher3[4][7]==0:
                    print("Teacher 3 will  be substiute  the lecture from 4-5 pm")
                elif teacher3[4][7]==0:
                    print("Teacher 4 will  be substiute  the lecture from 4-5 pm")
                # elif teacher5[4][7]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 4-5 pm") 
                else:
                    print("No teacher is Free")
        elif now==5:#check if day is Friday
            
            if teacher1[4][0]==1:#check if teacher 1 has class at 9am
                if teacher2[4][0]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher3[4][0]==0:
                    print("Teacher 3 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher4[4][0]==0:
                    print("Teacher 4 will  be substiute  the lecture from 9-10 am")
                    
                # elif teacher5[4][0]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 9-10 am") 
                    
                else:
                    print("No teacher is Free")

            if teacher1[4][1]==1:#check if teacher 1 has class at 10am
                if teacher2[4][1]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 10-11 am")
                elif teacher3[4][1]==0:
                    print("Teacher 3 will  be substiute  the lecture from 10-11 am")
                elif teacher4[4][1]==0:
                    print("Teacher 4 will  be substiute  the lecture from 10-11 am")
                # elif teacher5[5][1]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 10-11 am") 
                else:
                    print("No teacher is Free")
            if teacher1[4][2]==1:#check if teacher 1 has class at 11am
                if teacher2[4][2]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 11-12 pm")
                    
                elif teacher3[4][2]==0:
                    print("Teacher 3 will  be substiute  the lecture from 11-12 pm")
                elif teacher4[4][2]==0:
                    print("Teacher 4 will  be substiute  the lecture from 11-12 pm")
                # elif teacher5[4][2]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 11-12 pm") 
                else:
                    print("No teacher is Free")
            if teacher1[4][3]==1:#check if teacher 1 has class at 12am
                if teacher2[4][3]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 12-1 pm")
                    
                elif teacher3[4][3]==0:
                    print("Teacher 3 will  be substiute  the lecture from 12-1 pm")
                elif teacher4[4][3]==0:
                    print("Teacher 4 will  be substiute  the lecture from 12-1 pm")
                # elif teacher5[5][3]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 12-1 pm") 
                else:
                    print("No teacher is Free")
            if teacher1[4][4]==1:#check if teacher 1 has class at 1pm
                if teacher2[4][4]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 1-2 pm")
                    
                elif teacher3[4][4]==0:
                    print("Teacher 3 will  be substiute  the lecture from 1-2 pm")
                elif teacher4[4][4]==0:
                    print("Teacher 4 will  be substiute  the lecture from 1-2 pm")
                # elif teacher5[4][4]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 1-2 pm") 
                else:
                    print("No teacher is Free")
            if teacher1[4][5]==1:#check if teacher 1 has class at 2pm
                if teacher2[4][5]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 2-3 pm")
                    
                elif teacher3[4][5]==0:
                    print("Teacher 3 will  be substiute  the lecture from 2-3 pm")
                elif teacher4[4][5]==0:
                    print("Teacher 4 will  be substiute  the lecture from 2-3 pm")
                # elif teacher5[4][5]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 2-3 pm") 
                else:
                    print("No teacher is Free")
            if teacher1[4][6]==1:#check if teacher 1 has class at 3pm
                if teacher2[4][6]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 3-4 pm")
                    
                elif teacher3[4][6]==0:
                    print("Teacher 3 will  be substiute  the lecture from 3-4 pm")
                elif teacher4[4][6]==0:
                    print("Teacher 4 will  be substiute  the lecture from 3-4 pm")
                # elif teacher5[5][6]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 3-4 pm") 
                else:
                    print("No teacher is Free") 
            if teacher1[4][7]==1:#check if teacher 1 has class at 4pm
                if teacher2[4][7]== 0:
                    print("Teacher 2 will  be substiute  the lecture from 4-5 pm")
                    
                elif teacher3[4][7]==0:
                    print("Teacher 3 will  be substiute  the lecture from 4-5 pm")
                elif teacher4[4][7]==0:
                    print("Teacher 4 will  be substiute  the lecture from 4-5 pm")
                # elif teacher5[4][7]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 4-5 pm") 
                else:
                    print("No teacher is Free")
        elif now==6:
            print("Not a lecture day")
    elif ta==2: #if teacher 2 is absent
        if now==1:  #check if day is Monday
            
            if teacher2[0][0]==1:#check if teacher 2 has class at 9am
                if teacher1[0][0]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher3[0][0]==0:
                    print("Teacher 3 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher4[0][0]==0:
                    print("Teacher 4 will  be substiute  the lecture from 9-10 am")
                    
                # elif teacher5[0][0]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 9-10 am") 
                    
                else:
                    print("No teacher is Free")

            if teacher2[0][1]==1:#check if teacher 2 has class at 10am
                if teacher1[0][1]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 10-11 am")
                elif teacher3[0][1]==0:
                    print("Teacher 3 will  be substiute  the lecture from 10-11 am")
                elif teacher4[0][1]==0:
                    print("Teacher 4 will  be substiute  the lecture from 10-11 am")
                # elif teacher5[0][1]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 10-11 am") 
                else:
                    print("No teacher is Free")
            if teacher2[0][2]==1:#check if teacher 2 has class at 11am
                if teacher1[0][2]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 11-12 pm")
                    
                elif teacher3[0][2]==0:
                    print("Teacher 3 will  be substiute  the lecture from 11-12 pm")
                elif teacher4[0][2]==0:
                    print("Teacher 4 will  be substiute  the lecture from 11-12 pm")
                # elif teacher5[0][2]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 11-12 pm") 
                else:
                    print("No teacher is Free")
            if teacher2[0][3]==1:#check if teacher 2 has class at 12am
                if teacher1[0][3]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 12-1 pm")
                    
                elif teacher3[0][3]==0:
                    print("Teacher 3 will  be substiute  the lecture from 12-1 pm")
                elif teacher4[0][3]==0:
                    print("Teacher 4 will  be substiute  the lecture from 12-1 pm")
                # elif teacher5[0][3]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 12-1 pm") 
                else:
                    print("No teacher is Free")
            if teacher2[0][4]==1:#check if teacher 2 has class at 1pm
                if teacher1[0][4]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 1-2 pm")
                    
                elif teacher3[0][4]==0:
                    print("Teacher 3 will  be substiute  the lecture from 1-2 pm")
                elif teacher4[0][4]==0:
                    print("Teacher 4 will  be substiute  the lecture from 1-2 pm")
                # elif teacher5[0][4]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 1-2 pm") 
                else:
                    print("No teacher is Free")
            if teacher2[0][5]==1:#check if teacher 2 has class at 2pm
                if teacher1[0][5]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 2-3 pm")
                    
                elif teacher3[0][5]==0:
                    print("Teacher 3 will  be substiute  the lecture from 2-3 pm")
                elif teacher4[0][5]==0:
                    print("Teacher 4 will  be substiute  the lecture from 2-3 pm")
                # elif teacher5[0][5]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 2-3 pm") 
                else:
                    print("No teacher is Free")
            if teacher2[0][6]==1:#check if teacher 2 has class at 3pm
                if teacher1[0][6]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 3-4 pm")
                    
                elif teacher3[0][6]==0:
                    print("Teacher 3 will  be substiute  the lecture from 3-4 pm")
                elif teacher4[0][6]==0:
                    print("Teacher 4 will  be substiute  the lecture from 3-4 pm")
                # elif teacher5[0][6]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 3-4 pm") 
                else:
                    print("No teacher is Free") 
            if teacher2[0][7]==1:#check if teacher 2 has class at 4pm
                if teacher1[0][7]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 4-5 pm")
                    
                elif teacher3[0][7]==0:
                    print("Teacher 3 will  be substiute  the lecture from 4-5 pm")
                elif teacher4[0][7]==0:
                    print("Teacher 4 will  be substiute  the lecture from 4-5 pm")
                # elif teacher5[0][7]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 4-5 pm") 
                else:
                    print("No teacher is Free")
        elif now==2:#check if day is Tuesday
            
            if teacher2[1][0]==1:#check if teacher 2 has class at 9am
                if teacher1[1][0]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher3[1][0]==0:
                    print("Teacher 3 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher4[1][0]==0:
                    print("Teacher 4 will  be substiute  the lecture from 9-10 am")
                    
                # elif teacher5[1][0]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 9-10 am") 
                    
                else:
                    print("No teacher is Free")

            if teacher2[1][1]==1:#check if teacher 2 has class at 10am
                if teacher1[1][1]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 10-11 am")
                elif teacher3[1][1]==0:
                    print("Teacher 3 will  be substiute  the lecture from 10-11 am")
                elif teacher4[1][1]==0:
                    print("Teacher 4 will  be substiute  the lecture from 10-11 am")
                # elif teacher5[1][1]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 10-11 am") 
                else:
                    print("No teacher is Free")
            if teacher2[1][2]==1:#check if teacher 2 has class at 11am
                if teacher1[1][2]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 11-12 pm")
                    
                elif teacher3[1][2]==0:
                    print("Teacher 3 will  be substiute  the lecture from 11-12 pm")
                elif teacher4[1][2]==0:
                    print("Teacher 4 will  be substiute  the lecture from 11-12 pm")
                # elif teacher5[1][2]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 11-12 pm") 
                else:
                    print("No teacher is Free")
            if teacher2[1][3]==1:#check if teacher 2 has class at 12am
                if teacher1[1][3]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 12-1 pm")
                    
                elif teacher3[1][3]==0:
                    print("Teacher 3 will  be substiute  the lecture from 12-1 pm")
                elif teacher4[1][3]==0:
                    print("Teacher 4 will  be substiute  the lecture from 12-1 pm")
                # elif teacher5[1][3]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 12-1 pm") 
                else:
                    print("No teacher is Free")
            if teacher2[1][4]==1:#check if teacher 2 has class at 1pm
                if teacher1[1][4]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 1-2 pm")
                    
                elif teacher3[1][4]==0:
                    print("Teacher 3 will  be substiute  the lecture from 1-2 pm")
                elif teacher4[1][4]==0:
                    print("Teacher 4 will  be substiute  the lecture from 1-2 pm")
                # elif teacher5[1][4]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 1-2 pm") 
                else:
                    print("No teacher is Free")
            if teacher2[1][5]==1:#check if teacher 2 has class at 2pm
                if teacher1[1][5]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 2-3 pm")
                    
                elif teacher3[1][5]==0:
                    print("Teacher 3 will  be substiute  the lecture from 2-3 pm")
                elif teacher4[1][5]==0:
                    print("Teacher 4 will  be substiute  the lecture from 2-3 pm")
                # elif teacher5[1][5]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 2-3 pm") 
                else:
                    print("No teacher is Free")
            if teacher2[1][6]==1:#check if teacher 2 has class at 3pm
                if teacher1[1][6]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 3-4 pm")
                    
                elif teacher3[1][6]==0:
                    print("Teacher 3 will  be substiute  the lecture from 3-4 pm")
                elif teacher4[1][6]==0:
                    print("Teacher 4 will  be substiute  the lecture from 3-4 pm")
                # elif teacher5[1][6]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 3-4 pm") 
                else:
                    print("No teacher is Free") 
            if teacher2[1][7]==1:#check if teacher 2 has class at 4pm
                if teacher1[1][7]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 4-5 pm")
                    
                elif teacher3[1][7]==0:
                    print("Teacher 3 will  be substiute  the lecture from 4-5 pm")
                elif teacher4[1][7]==0:
                    print("Teacher 4 will  be substiute  the lecture from 4-5 pm")
                # elif teacher5[1][7]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 4-5 pm") 
                else:
                    print("No teacher is Free")
        elif now==3:#check if day is Wednesday
            
            if teacher2[2][0]==1:#check if teacher 2 has class at 9am
                if teacher1[2][0]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher3[2][0]==0:
                    print("Teacher 3 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher4[2][0]==0:
                    print("Teacher 4 will  be substiute  the lecture from 9-10 am")
                    
                # elif teacher5[2][0]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 9-10 am") 
                    
                else:
                    print("No teacher is Free")

            if teacher2[2][1]==1:#check if teacher 2 has class at 10am
                if teacher1[2][1]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 10-11 am")
                elif teacher3[2][1]==0:
                    print("Teacher 3 will  be substiute  the lecture from 10-11 am")
                elif teacher4[2][1]==0:
                    print("Teacher 4 will  be substiute  the lecture from 10-11 am")
                # elif teacher5[2][1]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 10-11 am") 
                else:
                    print("No teacher is Free")
            if teacher2[2][2]==1:#check if teacher 2 has class at 11am
                if teacher1[2][2]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 11-12 pm")
                    
                elif teacher3[2][2]==0:
                    print("Teacher 3 will  be substiute  the lecture from 11-12 pm")
                elif teacher4[2][2]==0:
                    print("Teacher 4 will  be substiute  the lecture from 11-12 pm")
                # elif teacher5[2][2]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 11-12 pm") 
                else:
                    print("No teacher is Free")
            if teacher2[2][3]==1:#check if teacher 2 has class at 12am
                if teacher1[2][3]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 12-1 pm")
                    
                elif teacher3[2][3]==0:
                    print("Teacher 3 will  be substiute  the lecture from 12-1 pm")
                elif teacher4[2][3]==0:
                    print("Teacher 4 will  be substiute  the lecture from 12-1 pm")
                # elif teacher5[2][3]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 12-1 pm") 
                else:
                    print("No teacher is Free")
            if teacher2[2][4]==1:#check if teacher 2 has class at 1pm
                if teacher1[2][4]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 1-2 pm")
                    
                elif teacher3[2][4]==0:
                    print("Teacher 3 will  be substiute  the lecture from 1-2 pm")
                elif teacher4[2][4]==0:
                    print("Teacher 4 will  be substiute  the lecture from 1-2 pm")
                # elif teacher5[2][4]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 1-2 pm") 
                else:
                    print("No teacher is Free")
            if teacher2[2][5]==1:#check if teacher 2 has class at 2pm
                if teacher1[2][5]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 2-3 pm")
                    
                elif teacher3[2][5]==0:
                    print("Teacher 3 will  be substiute  the lecture from 2-3 pm")
                elif teacher4[2][5]==0:
                    print("Teacher 4 will  be substiute  the lecture from 2-3 pm")
                # elif teacher5[2][5]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 2-3 pm") 
                else:
                    print("No teacher is Free")
            if teacher2[2][6]==1:#check if teacher 2 has class at 3pm
                if teacher1[2][6]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 3-4 pm")
                    
                elif teacher3[2][6]==0:
                    print("Teacher 3 will  be substiute  the lecture from 3-4 pm")
                elif teacher4[2][6]==0:
                    print("Teacher 4 will  be substiute  the lecture from 3-4 pm")
                # elif teacher5[2][6]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 3-4 pm") 
                else:
                    print("No teacher is Free") 
            if teacher2[2][7]==1:#check if teacher 2 has class at 4pm
                if teacher1[2][7]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 4-5 pm")
                    
                elif teacher3[2][7]==0:
                    print("Teacher 3 will  be substiute  the lecture from 4-5 pm")
                elif teacher4[2][7]==0:
                    print("Teacher 4 will  be substiute  the lecture from 4-5 pm")
                # elif teacher5[2][7]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 4-5 pm") 
                else:
                    print("No teacher is Free")
        elif now==4:#check if day is Thursday
            
            if teacher2[3][0]==1:#check if teacher 2 has class at 9am
                if teacher1[3][0]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher3[3][0]==0:
                    print("Teacher 3 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher4[3][0]==0:
                    print("Teacher 4 will  be substiute  the lecture from 9-10 am")
                    
                # elif teacher5[4][0]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 9-10 am") 
                    
                else:
                    print("No teacher is Free")

            if teacher2[3][1]==1:#check if teacher 2 has class at 10am
                if teacher1[3][1]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 10-11 am")
                elif teacher3[3][1]==0:
                    print("Teacher 3 will  be substiute  the lecture from 10-11 am")
                elif teacher4[3][1]==0:
                    print("Teacher 4 will  be substiute  the lecture from 10-11 am")
                # elif teacher5[4][1]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 10-11 am") 
                else:
                    print("No teacher is Free")
            if teacher2[3][2]==1:#check if teacher 2 has class at 11am
                if teacher1[3][2]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 11-12 pm")
                    
                elif teacher3[3][2]==0:
                    print("Teacher 3 will  be substiute  the lecture from 11-12 pm")
                elif teacher4[3][2]==0:
                    print("Teacher 4 will  be substiute  the lecture from 11-12 pm")
                # elif teacher5[3][2]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 11-12 pm") 
                else:
                    print("No teacher is Free")
            if teacher2[3][3]==1:#check if teacher 2 has class at 12am
                if teacher1[3][3]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 12-1 pm")
                    
                elif teacher3[3][3]==0:
                    print("Teacher 3 will  be substiute  the lecture from 12-1 pm")
                elif teacher4[3][3]==0:
                    print("Teacher 4 will  be substiute  the lecture from 12-1 pm")
                # elif teacher5[4][3]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 12-1 pm") 
                else:
                    print("No teacher is Free")
            if teacher2[3][4]==1:#check if teacher 2 has class at 1pm
                if teacher1[4][4]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 1-2 pm")
                    
                elif teacher3[3][4]==0:
                    print("Teacher 3 will  be substiute  the lecture from 1-2 pm")
                elif teacher4[3][4]==0:
                    print("Teacher 4 will  be substiute  the lecture from 1-2 pm")
                # elif teacher5[3][4]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 1-2 pm") 
                else:
                    print("No teacher is Free")
            if teacher2[3][5]==1:#check if teacher 2 has class at 2pm
                if teacher1[3][5]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 2-3 pm")
                    
                elif teacher3[3][5]==0:
                    print("Teacher 3 will  be substiute  the lecture from 2-3 pm")
                elif teacher4[3][5]==0:
                    print("Teacher 4 will  be substiute  the lecture from 2-3 pm")
                # elif teacher5[4][5]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 2-3 pm") 
                else:
                    print("No teacher is Free")
            if teacher2[3][6]==1:#check if teacher 2 has class at 3pm
                if teacher1[3][6]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 3-4 pm")
                    
                elif teacher3[3][6]==0:
                    print("Teacher 3 will  be substiute  the lecture from 3-4 pm")
                elif teacher4[3][6]==0:
                    print("Teacher 4 will  be substiute  the lecture from 3-4 pm")
                # elif teacher5[4][6]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 3-4 pm") 
                else:
                    print("No teacher is Free") 
            if teacher2[4][7]==1:#check if teacher 2 has class at 4pm
                if teacher1[4][7]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 4-5 pm")
                    
                elif teacher3[4][7]==0:
                    print("Teacher 3 will  be substiute  the lecture from 4-5 pm")
                elif teacher3[4][7]==0:
                    print("Teacher 4 will  be substiute  the lecture from 4-5 pm")
                # elif teacher5[4][7]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 4-5 pm") 
                else:
                    print("No teacher is Free")
        elif now==5:#check if day is Friday
            
            if teacher2[4][0]==1:#check if teacher 1 has class at 9am
                if teacher1[4][0]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher3[4][0]==0:
                    print("Teacher 3 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher4[4][0]==0:
                    print("Teacher 4 will  be substiute  the lecture from 9-10 am")
                    
                # elif teacher5[4][0]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 9-10 am") 
                    
                else:
                    print("No teacher is Free")

            if teacher2[4][1]==1:#check if teacher 2 has class at 10am
                if teacher1[4][1]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 10-11 am")
                elif teacher3[4][1]==0:
                    print("Teacher 3 will  be substiute  the lecture from 10-11 am")
                elif teacher4[4][1]==0:
                    print("Teacher 4 will  be substiute  the lecture from 10-11 am")
                # elif teacher5[5][1]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 10-11 am") 
                else:
                    print("No teacher is Free")
            if teacher2[4][2]==1:#check if teacher 2 has class at 11am
                if teacher1[4][2]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 11-12 pm")
                    
                elif teacher3[4][2]==0:
                    print("Teacher 3 will  be substiute  the lecture from 11-12 pm")
                elif teacher4[4][2]==0:
                    print("Teacher 4 will  be substiute  the lecture from 11-12 pm")
                # elif teacher5[4][2]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 11-12 pm") 
                else:
                    print("No teacher is Free")
            if teacher2[4][3]==1:#check if teacher 2 has class at 12am
                if teacher1[4][3]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 12-1 pm")
                    
                elif teacher3[4][3]==0:
                    print("Teacher 3 will  be substiute  the lecture from 12-1 pm")
                elif teacher4[4][3]==0:
                    print("Teacher 4 will  be substiute  the lecture from 12-1 pm")
                # elif teacher5[5][3]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 12-1 pm") 
                else:
                    print("No teacher is Free")
            if teacher2[4][4]==1:#check if teacher 1 has class at 1pm
                if teacher1[4][4]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 1-2 pm")
                    
                elif teacher3[4][4]==0:
                    print("Teacher 3 will  be substiute  the lecture from 1-2 pm")
                elif teacher4[4][4]==0:
                    print("Teacher 4 will  be substiute  the lecture from 1-2 pm")
                # elif teacher5[4][4]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 1-2 pm") 
                else:
                    print("No teacher is Free")
            if teacher2[4][5]==1:#check if teacher 1 has class at 2pm
                if teacher1[4][5]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 2-3 pm")
                    
                elif teacher3[4][5]==0:
                    print("Teacher 3 will  be substiute  the lecture from 2-3 pm")
                elif teacher4[4][5]==0:
                    print("Teacher 4 will  be substiute  the lecture from 2-3 pm")
                # elif teacher5[4][5]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 2-3 pm") 
                else:
                    print("No teacher is Free")
            if teacher2[4][6]==1:#check if teacher 1 has class at 3pm
                if teacher1[4][6]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 3-4 pm")
                    
                elif teacher3[4][6]==0:
                    print("Teacher 3 will  be substiute  the lecture from 3-4 pm")
                elif teacher4[4][6]==0:
                    print("Teacher 4 will  be substiute  the lecture from 3-4 pm")
                # elif teacher5[5][6]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 3-4 pm") 
                else:
                    print("No teacher is Free") 
            if teacher2[4][7]==1:#check if teacher 1 has class at 4pm
                if teacher1[4][7]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 4-5 pm")
                    
                elif teacher3[4][7]==0:
                    print("Teacher 3 will  be substiute  the lecture from 4-5 pm")
                elif teacher4[4][7]==0:
                    print("Teacher 4 will  be substiute  the lecture from 4-5 pm")
                # elif teacher5[4][7]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 4-5 pm") 
                else:
                    print("No teacher is Free")
        elif now==6:
            print("Not a lecture day")
    elif ta==3: #if teacher 3 is absent
        if now==1:  #check if day is Monday
            
            if teacher3[0][0]==1:#check if teacher 3 has class at 9am
                if teacher1[0][0]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher2[0][0]==0:
                    print("Teacher 2 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher4[0][0]==0:
                    print("Teacher 4 will  be substiute  the lecture from 9-10 am")
                    
                # elif teacher5[0][0]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 9-10 am") 
                    
                else:
                    print("No teacher is Free")

            if teacher3[0][1]==1:#check if teacher 3 has class at 10am
                if teacher1[0][1]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 10-11 am")
                elif teacher2[0][1]==0:
                    print("Teacher 2 will  be substiute  the lecture from 10-11 am")
                elif teacher4[0][1]==0:
                    print("Teacher 4 will  be substiute  the lecture from 10-11 am")
                # elif teacher5[0][1]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 10-11 am") 
                else:
                    print("No teacher is Free")
            if teacher3[0][2]==1:#check if teacher 3 has class at 11am
                if teacher1[0][2]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 11-12 pm")
                    
                elif teacher2[0][2]==0:
                    print("Teacher 2 will  be substiute  the lecture from 11-12 pm")
                elif teacher4[0][2]==0:
                    print("Teacher 4 will  be substiute  the lecture from 11-12 pm")
                # elif teacher5[0][2]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 11-12 pm") 
                else:
                    print("No teacher is Free")
            if teacher3[0][3]==1:#check if teacher 3 has class at 12am
                if teacher1[0][3]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 12-1 pm")
                    
                elif teacher2[0][3]==0:
                    print("Teacher 2 will  be substiute  the lecture from 12-1 pm")
                elif teacher4[0][3]==0:
                    print("Teacher 4 will  be substiute  the lecture from 12-1 pm")
                # elif teacher5[0][3]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 12-1 pm") 
                else:
                    print("No teacher is Free")
            if teacher3[0][4]==1:#check if teacher 3 has class at 1pm
                if teacher1[0][4]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 1-2 pm")
                    
                elif teacher2[0][4]==0:
                    print("Teacher 2 will  be substiute  the lecture from 1-2 pm")
                elif teacher4[0][4]==0:
                    print("Teacher 4 will  be substiute  the lecture from 1-2 pm")
                # elif teacher5[0][4]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 1-2 pm") 
                else:
                    print("No teacher is Free")
            if teacher3[0][5]==1:#check if teacher 3 has class at 2pm
                if teacher1[0][5]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 2-3 pm")
                    
                elif teacher2[0][5]==0:
                    print("Teacher 2 will  be substiute  the lecture from 2-3 pm")
                elif teacher4[0][5]==0:
                    print("Teacher 4 will  be substiute  the lecture from 2-3 pm")
                # elif teacher5[0][5]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 2-3 pm") 
                else:
                    print("No teacher is Free")
            if teacher3[0][6]==1:#check if teacher 2 has class at 3pm
                if teacher1[0][6]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 3-4 pm")
                    
                elif teacher2[0][6]==0:
                    print("Teacher 2 will  be substiute  the lecture from 3-4 pm")
                elif teacher4[0][6]==0:
                    print("Teacher 4 will  be substiute  the lecture from 3-4 pm")
                # elif teacher5[0][6]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 3-4 pm") 
                else:
                    print("No teacher is Free") 
            if teacher3[0][7]==1:#check if teacher 2 has class at 4pm
                if teacher1[0][7]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 4-5 pm")
                    
                elif teacher2[0][7]==0:
                    print("Teacher 2 will  be substiute  the lecture from 4-5 pm")
                elif teacher4[0][7]==0:
                    print("Teacher 4 will  be substiute  the lecture from 4-5 pm")
                # elif teacher5[0][7]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 4-5 pm") 
                else:
                    print("No teacher is Free")
        elif now==2:#check if day is Tuesday
            
            if teacher3[1][0]==1:#check if teacher 2 has class at 9am
                if teacher1[1][0]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher2[1][0]==0:
                    print("Teacher 2 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher4[1][0]==0:
                    print("Teacher 4 will  be substiute  the lecture from 9-10 am")
                    
                # elif teacher5[1][0]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 9-10 am") 
                    
                else:
                    print("No teacher is Free")

            if teacher3[1][1]==1:#check if teacher 2 has class at 10am
                if teacher1[1][1]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 10-11 am")
                elif teacher2[1][1]==0:
                    print("Teacher 2 will  be substiute  the lecture from 10-11 am")
                elif teacher4[1][1]==0:
                    print("Teacher 4 will  be substiute  the lecture from 10-11 am")
                # elif teacher5[1][1]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 10-11 am") 
                else:
                    print("No teacher is Free")
            if teacher3[1][2]==1:#check if teacher 2 has class at 11am
                if teacher1[1][2]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 11-12 pm")
                    
                elif teacher2[1][2]==0:
                    print("Teacher 2 will  be substiute  the lecture from 11-12 pm")
                elif teacher4[1][2]==0:
                    print("Teacher 4 will  be substiute  the lecture from 11-12 pm")
                # elif teacher5[1][2]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 11-12 pm") 
                else:
                    print("No teacher is Free")
            if teacher3[1][3]==1:#check if teacher 2 has class at 12am
                if teacher1[1][3]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 12-1 pm")
                    
                elif teacher2[1][3]==0:
                    print("Teacher 2 will  be substiute  the lecture from 12-1 pm")
                elif teacher4[1][3]==0:
                    print("Teacher 4 will  be substiute  the lecture from 12-1 pm")
                # elif teacher5[1][3]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 12-1 pm") 
                else:
                    print("No teacher is Free")
            if teacher3[1][4]==1:#check if teacher 2 has class at 1pm
                if teacher1[1][4]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 1-2 pm")
                    
                elif teacher2[1][4]==0:
                    print("Teacher 2 will  be substiute  the lecture from 1-2 pm")
                elif teacher4[1][4]==0:
                    print("Teacher 4 will  be substiute  the lecture from 1-2 pm")
                # elif teacher5[1][4]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 1-2 pm") 
                else:
                    print("No teacher is Free")
            if teacher3[1][5]==1:#check if teacher 2 has class at 2pm
                if teacher1[1][5]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 2-3 pm")
                    
                elif teacher2[1][5]==0:
                    print("Teacher 2 will  be substiute  the lecture from 2-3 pm")
                elif teacher4[1][5]==0:
                    print("Teacher 4 will  be substiute  the lecture from 2-3 pm")
                # elif teacher5[1][5]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 2-3 pm") 
                else:
                    print("No teacher is Free")
            if teacher3[1][6]==1:#check if teacher 2 has class at 3pm
                if teacher1[1][6]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 3-4 pm")
                    
                elif teacher2[1][6]==0:
                    print("Teacher 2 will  be substiute  the lecture from 3-4 pm")
                elif teacher4[1][6]==0:
                    print("Teacher 4 will  be substiute  the lecture from 3-4 pm")
                # elif teacher5[1][6]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 3-4 pm") 
                else:
                    print("No teacher is Free") 
            if teacher3[1][7]==1:#check if teacher 2 has class at 4pm
                if teacher1[1][7]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 4-5 pm")
                    
                elif teacher2[1][7]==0:
                    print("Teacher 2 will  be substiute  the lecture from 4-5 pm")
                elif teacher4[1][7]==0:
                    print("Teacher 4 will  be substiute  the lecture from 4-5 pm")
                # elif teacher5[1][7]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 4-5 pm") 
                else:
                    print("No teacher is Free")
        elif now==3:#check if day is Wednesday
            
            if teacher3[2][0]==1:#check if teacher 2 has class at 9am
                if teacher1[2][0]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher2[2][0]==0:
                    print("Teacher 2 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher4[2][0]==0:
                    print("Teacher 4 will  be substiute  the lecture from 9-10 am")
                    
                # elif teacher5[2][0]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 9-10 am") 
                    
                else:
                    print("No teacher is Free")

            if teacher3[2][1]==1:#check if teacher 2 has class at 10am
                if teacher1[2][1]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 10-11 am")
                elif teacher2[2][1]==0:
                    print("Teacher 2 will  be substiute  the lecture from 10-11 am")
                elif teacher4[2][1]==0:
                    print("Teacher 4 will  be substiute  the lecture from 10-11 am")
                # elif teacher5[2][1]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 10-11 am") 
                else:
                    print("No teacher is Free")
            if teacher3[2][2]==1:#check if teacher 2 has class at 11am
                if teacher1[2][2]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 11-12 pm")
                    
                elif teacher2[2][2]==0:
                    print("Teacher 2 will  be substiute  the lecture from 11-12 pm")
                elif teacher4[2][2]==0:
                    print("Teacher 4 will  be substiute  the lecture from 11-12 pm")
                # elif teacher5[2][2]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 11-12 pm") 
                else:
                    print("No teacher is Free")
            if teacher3[2][3]==1:#check if teacher 2 has class at 12am
                if teacher1[2][3]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 12-1 pm")
                    
                elif teacher2[2][3]==0:
                    print("Teacher 2 will  be substiute  the lecture from 12-1 pm")
                elif teacher4[2][3]==0:
                    print("Teacher 4 will  be substiute  the lecture from 12-1 pm")
                # elif teacher5[2][3]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 12-1 pm") 
                else:
                    print("No teacher is Free")
            if teacher3[2][4]==1:#check if teacher 2 has class at 1pm
                if teacher1[2][4]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 1-2 pm")
                    
                elif teacher2[2][4]==0:
                    print("Teacher 2 will  be substiute  the lecture from 1-2 pm")
                elif teacher4[2][4]==0:
                    print("Teacher 4 will  be substiute  the lecture from 1-2 pm")
                # elif teacher5[2][4]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 1-2 pm") 
                else:
                    print("No teacher is Free")
            if teacher3[2][5]==1:#check if teacher 2 has class at 2pm
                if teacher1[2][5]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 2-3 pm")
                    
                elif teacher2[2][5]==0:
                    print("Teacher 2 will  be substiute  the lecture from 2-3 pm")
                elif teacher4[2][5]==0:
                    print("Teacher 4 will  be substiute  the lecture from 2-3 pm")
                # elif teacher5[2][5]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 2-3 pm") 
                else:
                    print("No teacher is Free")
            if teacher3[2][6]==1:#check if teacher 2 has class at 3pm
                if teacher1[2][6]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 3-4 pm")
                    
                elif teacher2[2][6]==0:
                    print("Teacher 2 will  be substiute  the lecture from 3-4 pm")
                elif teacher4[2][6]==0:
                    print("Teacher 4 will  be substiute  the lecture from 3-4 pm")
                # elif teacher5[2][6]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 3-4 pm") 
                else:
                    print("No teacher is Free") 
            if teacher3[2][7]==1:#check if teacher 2 has class at 4pm
                if teacher1[2][7]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 4-5 pm")
                    
                elif teacher2[2][7]==0:
                    print("Teacher 2 will  be substiute  the lecture from 4-5 pm")
                elif teacher3[2][7]==0:
                    print("Teacher 4 will  be substiute  the lecture from 4-5 pm")
                # elif teacher5[2][7]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 4-5 pm") 
                else:
                    print("No teacher is Free")
        elif now==4:#check if day is Thursday
            
            if teacher3[3][0]==1:#check if teacher 2 has class at 9am
                if teacher1[3][0]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher2[3][0]==0:
                    print("Teacher 2 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher4[3][0]==0:
                    print("Teacher 4 will  be substiute  the lecture from 9-10 am")
                    
                # elif teacher5[4][0]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 9-10 am") 
                    
                else:
                    print("No teacher is Free")

            if teacher3[3][1]==1:#check if teacher 2 has class at 10am
                if teacher1[3][1]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 10-11 am")
                elif teacher2[3][1]==0:
                    print("Teacher 2 will  be substiute  the lecture from 10-11 am")
                elif teacher4[3][1]==0:
                    print("Teacher 4 will  be substiute  the lecture from 10-11 am")
                # elif teacher5[4][1]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 10-11 am") 
                else:
                    print("No teacher is Free")
            if teacher3[3][2]==1:#check if teacher 2 has class at 11am
                if teacher1[3][2]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 11-12 pm")
                    
                elif teacher2[3][2]==0:
                    print("Teacher 2 will  be substiute  the lecture from 11-12 pm")
                elif teacher4[3][2]==0:
                    print("Teacher 4 will  be substiute  the lecture from 11-12 pm")
                # elif teacher5[3][2]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 11-12 pm") 
                else:
                    print("No teacher is Free")
            if teacher3[3][3]==1:#check if teacher 2 has class at 12am
                if teacher1[3][3]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 12-1 pm")
                    
                elif teacher2[3][3]==0:
                    print("Teacher 2 will  be substiute  the lecture from 12-1 pm")
                elif teacher4[3][3]==0:
                    print("Teacher 4 will  be substiute  the lecture from 12-1 pm")
                # elif teacher5[4][3]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 12-1 pm") 
                else:
                    print("No teacher is Free")
            if teacher3[3][4]==1:#check if teacher 2 has class at 1pm
                if teacher1[4][4]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 1-2 pm")
                    
                elif teacher2[3][4]==0:
                    print("Teacher 2 will  be substiute  the lecture from 1-2 pm")
                elif teacher4[3][4]==0:
                    print("Teacher 4 will  be substiute  the lecture from 1-2 pm")
                # elif teacher5[3][4]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 1-2 pm") 
                else:
                    print("No teacher is Free")
            if teacher3[3][5]==1:#check if teacher 2 has class at 2pm
                if teacher1[3][5]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 2-3 pm")
                    
                elif teacher2[3][5]==0:
                    print("Teacher 2 will  be substiute  the lecture from 2-3 pm")
                elif teacher4[3][5]==0:
                    print("Teacher 4 will  be substiute  the lecture from 2-3 pm")
                # elif teacher5[4][5]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 2-3 pm") 
                else:
                    print("No teacher is Free")
            if teacher3[3][6]==1:#check if teacher 2 has class at 3pm
                if teacher1[3][6]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 3-4 pm")
                    
                elif teacher2[3][6]==0:
                    print("Teacher 2 will  be substiute  the lecture from 3-4 pm")
                elif teacher4[3][6]==0:
                    print("Teacher 4 will  be substiute  the lecture from 3-4 pm")
                # elif teacher5[4][6]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 3-4 pm") 
                else:
                    print("No teacher is Free") 
            if teacher3[4][7]==1:#check if teacher 2 has class at 4pm
                if teacher1[4][7]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 4-5 pm")
                    
                elif teacher2[4][7]==0:
                    print("Teacher 2 will  be substiute  the lecture from 4-5 pm")
                elif teacher4[4][7]==0:
                    print("Teacher 4 will  be substiute  the lecture from 4-5 pm")
                # elif teacher5[4][7]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 4-5 pm") 
                else:
                    print("No teacher is Free")
        elif now==5:#check if day is Friday
            
            if teacher3[4][0]==1:#check if teacher 1 has class at 9am
                if teacher1[4][0]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher2[4][0]==0:
                    print("Teacher 2 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher4[4][0]==0:
                    print("Teacher 4 will  be substiute  the lecture from 9-10 am")
                    
                # elif teacher5[4][0]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 9-10 am") 
                    
                else:
                    print("No teacher is Free")

            if teacher3[4][1]==1:#check if teacher 2 has class at 10am
                if teacher1[4][1]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 10-11 am")
                elif teacher2[4][1]==0:
                    print("Teacher 2 will  be substiute  the lecture from 10-11 am")
                elif teacher4[4][1]==0:
                    print("Teacher 4 will  be substiute  the lecture from 10-11 am")
                # elif teacher5[5][1]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 10-11 am") 
                else:
                    print("No teacher is Free")
            if teacher3[4][2]==1:#check if teacher 2 has class at 11am
                if teacher1[4][2]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 11-12 pm")
                    
                elif teacher2[4][2]==0:
                    print("Teacher 2 will  be substiute  the lecture from 11-12 pm")
                elif teacher4[4][2]==0:
                    print("Teacher 4 will  be substiute  the lecture from 11-12 pm")
                # elif teacher5[4][2]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 11-12 pm") 
                else:
                    print("No teacher is Free")
            if teacher3[4][3]==1:#check if teacher 2 has class at 12am
                if teacher1[4][3]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 12-1 pm")
                    
                elif teacher2[4][3]==0:
                    print("Teacher 2 will  be substiute  the lecture from 12-1 pm")
                elif teacher4[4][3]==0:
                    print("Teacher 4 will  be substiute  the lecture from 12-1 pm")
                # elif teacher5[5][3]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 12-1 pm") 
                else:
                    print("No teacher is Free")
            if teacher3[4][4]==1:#check if teacher 1 has class at 1pm
                if teacher1[4][4]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 1-2 pm")
                    
                elif teacher2[4][4]==0:
                    print("Teacher 2 will  be substiute  the lecture from 1-2 pm")
                elif teacher4[4][4]==0:
                    print("Teacher 4 will  be substiute  the lecture from 1-2 pm")
                # elif teacher5[4][4]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 1-2 pm") 
                else:
                    print("No teacher is Free")
            if teacher3[4][5]==1:#check if teacher 1 has class at 2pm
                if teacher1[4][5]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 2-3 pm")
                    
                elif teacher2[4][5]==0:
                    print("Teacher 2 will  be substiute  the lecture from 2-3 pm")
                elif teacher4[4][5]==0:
                    print("Teacher 4 will  be substiute  the lecture from 2-3 pm")
                # elif teacher5[4][5]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 2-3 pm") 
                else:
                    print("No teacher is Free")
            if teacher3[4][6]==1:#check if teacher 1 has class at 3pm
                if teacher1[4][6]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 3-4 pm")
                    
                elif teacher2[4][6]==0:
                    print("Teacher 2 will  be substiute  the lecture from 3-4 pm")
                elif teacher4[4][6]==0:
                    print("Teacher 4 will  be substiute  the lecture from 3-4 pm")
                # elif teacher5[5][6]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 3-4 pm") 
                else:
                    print("No teacher is Free") 
            if teacher3[4][7]==1:#check if teacher 1 has class at 4pm
                if teacher1[4][7]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 4-5 pm")
                    
                elif teacher2[4][7]==0:
                    print("Teacher 2 will  be substiute  the lecture from 4-5 pm")
                elif teacher4[4][7]==0:
                    print("Teacher 4 will  be substiute  the lecture from 4-5 pm")
                # elif teacher5[4][7]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 4-5 pm") 
                else:
                    print("No teacher is Free")
        elif now==6:
            print("Not a lecture day")
    elif ta==4: #if teacher 4 is absent
        if now==1:  #check if day is Monday
            
            if teacher4[0][0]==1:#check if teacher 3 has class at 9am
                if teacher1[0][0]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher2[0][0]==0:
                    print("Teacher 2 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher3[0][0]==0:
                    print("Teacher 3 will  be substiute  the lecture from 9-10 am")
                    
                # elif teacher5[0][0]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 9-10 am") 
                    
                else:
                    print("No teacher is Free")

            if teacher4[0][1]==1:#check if teacher 3 has class at 10am
                if teacher1[0][1]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 10-11 am")
                elif teacher2[0][1]==0:
                    print("Teacher 2 will  be substiute  the lecture from 10-11 am")
                elif teacher3[0][1]==0:
                    print("Teacher 3 will  be substiute  the lecture from 10-11 am")
                # elif teacher5[0][1]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 10-11 am") 
                else:
                    print("No teacher is Free")
            if teacher4[0][2]==1:#check if teacher 3 has class at 11am
                if teacher1[0][2]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 11-12 pm")
                    
                elif teacher2[0][2]==0:
                    print("Teacher 2 will  be substiute  the lecture from 11-12 pm")
                elif teacher3[0][2]==0:
                    print("Teacher 3 will  be substiute  the lecture from 11-12 pm")
                # elif teacher5[0][2]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 11-12 pm") 
                else:
                    print("No teacher is Free")
            if teacher4[0][3]==1:#check if teacher 3 has class at 12am
                if teacher1[0][3]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 12-1 pm")
                    
                elif teacher2[0][3]==0:
                    print("Teacher 2 will  be substiute  the lecture from 12-1 pm")
                elif teacher3[0][3]==0:
                    print("Teacher 3 will  be substiute  the lecture from 12-1 pm")
                # elif teacher5[0][3]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 12-1 pm") 
                else:
                    print("No teacher is Free")
            if teacher4[0][4]==1:#check if teacher 3 has class at 1pm
                if teacher1[0][4]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 1-2 pm")
                    
                elif teacher2[0][4]==0:
                    print("Teacher 2 will  be substiute  the lecture from 1-2 pm")
                elif teacher3[0][4]==0:
                    print("Teacher 4 will  be substiute  the lecture from 1-2 pm")
                # elif teacher5[0][4]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 1-2 pm") 
                else:
                    print("No teacher is Free")
            if teacher4[0][5]==1:#check if teacher 3 has class at 2pm
                if teacher1[0][5]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 2-3 pm")
                    
                elif teacher2[0][5]==0:
                    print("Teacher 2 will  be substiute  the lecture from 2-3 pm")
                elif teacher3[0][5]==0:
                    print("Teacher 3 will  be substiute  the lecture from 2-3 pm")
                # elif teacher5[0][5]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 2-3 pm") 
                else:
                    print("No teacher is Free")
            if teacher4[0][6]==1:#check if teacher 2 has class at 3pm
                if teacher1[0][6]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 3-4 pm")
                    
                elif teacher2[0][6]==0:
                    print("Teacher 2 will  be substiute  the lecture from 3-4 pm")
                elif teacher4[0][6]==0:
                    print("Teacher 3 will  be substiute  the lecture from 3-4 pm")
                # elif teacher5[0][6]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 3-4 pm") 
                else:
                    print("No teacher is Free") 
            if teacher4[0][7]==1:#check if teacher 2 has class at 4pm
                if teacher1[0][7]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 4-5 pm")
                    
                elif teacher2[0][7]==0:
                    print("Teacher 2 will  be substiute  the lecture from 4-5 pm")
                elif teacher3[0][7]==0:
                    print("Teacher 3 will  be substiute  the lecture from 4-5 pm")
                # elif teacher5[0][7]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 4-5 pm") 
                else:
                    print("No teacher is Free")
        elif now==2:#check if day is Tuesday
            
            if teacher4[1][0]==1:#check if teacher 2 has class at 9am
                if teacher1[1][0]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher2[1][0]==0:
                    print("Teacher 1 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher3[1][0]==0:
                    print("Teacher 3 will  be substiute  the lecture from 9-10 am")
                    
                # elif teacher5[1][0]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 9-10 am") 
                    
                else:
                    print("No teacher is Free")

            if teacher4[1][1]==1:#check if teacher 2 has class at 10am
                if teacher1[1][1]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 10-11 am")
                elif teacher2[1][1]==0:
                    print("Teacher 2 will  be substiute  the lecture from 10-11 am")
                elif teacher3[1][1]==0:
                    print("Teacher 3 will  be substiute  the lecture from 10-11 am")
                # elif teacher5[1][1]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 10-11 am") 
                else:
                    print("No teacher is Free")
            if teacher4[1][2]==1:#check if teacher 2 has class at 11am
                if teacher1[1][2]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 11-12 pm")
                    
                elif teacher2[1][2]==0:
                    print("Teacher 2 will  be substiute  the lecture from 11-12 pm")
                elif teacher3[1][2]==0:
                    print("Teacher 4 will  be substiute  the lecture from 11-12 pm")
                # elif teacher5[1][2]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 11-12 pm") 
                else:
                    print("No teacher is Free")
            if teacher4[1][3]==1:#check if teacher 2 has class at 12am
                if teacher1[1][3]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 12-1 pm")
                    
                elif teacher2[1][3]==0:
                    print("Teacher 2 will  be substiute  the lecture from 12-1 pm")
                elif teacher3[1][3]==0:
                    print("Teacher 3 will  be substiute  the lecture from 12-1 pm")
                # elif teacher5[1][3]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 12-1 pm") 
                else:
                    print("No teacher is Free")
            if teacher4[1][4]==1:#check if teacher 2 has class at 1pm
                if teacher1[1][4]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 1-2 pm")
                    
                elif teacher2[1][4]==0:
                    print("Teacher 2 will  be substiute  the lecture from 1-2 pm")
                elif teacher3[1][4]==0:
                    print("Teacher 3 will  be substiute  the lecture from 1-2 pm")
                # elif teacher5[1][4]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 1-2 pm") 
                else:
                    print("No teacher is Free")
            if teacher4[1][5]==1:#check if teacher 2 has class at 2pm
                if teacher1[1][5]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 2-3 pm")
                    
                elif teacher2[1][5]==0:
                    print("Teacher 2 will  be substiute  the lecture from 2-3 pm")
                elif teacher3[1][5]==0:
                    print("Teacher 3 will  be substiute  the lecture from 2-3 pm")
                # elif teacher5[1][5]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 2-3 pm") 
                else:
                    print("No teacher is Free")
            if teacher4[1][6]==1:#check if teacher 2 has class at 3pm
                if teacher1[1][6]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 3-4 pm")
                    
                elif teacher2[1][6]==0:
                    print("Teacher 2 will  be substiute  the lecture from 3-4 pm")
                elif teacher3[1][6]==0:
                    print("Teacher 3 will  be substiute  the lecture from 3-4 pm")
                # elif teacher5[1][6]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 3-4 pm") 
                else:
                    print("No teacher is Free") 
            if teacher4[1][7]==1:#check if teacher 2 has class at 4pm
                if teacher1[1][7]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 4-5 pm")
                    
                elif teacher2[1][7]==0:
                    print("Teacher 2 will  be substiute  the lecture from 4-5 pm")
                elif teacher3[1][7]==0:
                    print("Teacher 3 will  be substiute  the lecture from 4-5 pm")
                # elif teacher5[1][7]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 4-5 pm") 
                else:
                    print("No teacher is Free")
        elif now==3:#check if day is Wednesday
            
            if teacher4[2][0]==1:#check if teacher 2 has class at 9am
                if teacher1[2][0]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher2[2][0]==0:
                    print("Teacher 2 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher3[2][0]==0:
                    print("Teacher 3 will  be substiute  the lecture from 9-10 am")
                    
                # elif teacher5[2][0]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 9-10 am") 
                    
                else:
                    print("No teacher is Free")

            if teacher4[2][1]==1:#check if teacher 2 has class at 10am
                if teacher1[2][1]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 10-11 am")
                elif teacher2[2][1]==0:
                    print("Teacher 2 will  be substiute  the lecture from 10-11 am")
                elif teacher3[2][1]==0:
                    print("Teacher 3 will  be substiute  the lecture from 10-11 am")
                # elif teacher5[2][1]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 10-11 am") 
                else:
                    print("No teacher is Free")
            if teacher4[2][2]==1:#check if teacher 2 has class at 11am
                if teacher1[2][2]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 11-12 pm")
                    
                elif teacher2[2][2]==0:
                    print("Teacher 2 will  be substiute  the lecture from 11-12 pm")
                elif teacher3[2][2]==0:
                    print("Teacher 3 will  be substiute  the lecture from 11-12 pm")
                # elif teacher5[2][2]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 11-12 pm") 
                else:
                    print("No teacher is Free")
            if teacher4[2][3]==1:#check if teacher 2 has class at 12am
                if teacher1[2][3]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 12-1 pm")
                    
                elif teacher2[2][3]==0:
                    print("Teacher 2 will  be substiute  the lecture from 12-1 pm")
                elif teacher3[2][3]==0:
                    print("Teacher 3 will  be substiute  the lecture from 12-1 pm")
                # elif teacher5[2][3]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 12-1 pm") 
                else:
                    print("No teacher is Free")
            if teacher4[2][4]==1:#check if teacher 2 has class at 1pm
                if teacher1[2][4]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 1-2 pm")
                    
                elif teacher2[2][4]==0:
                    print("Teacher 2 will  be substiute  the lecture from 1-2 pm")
                elif teacher3[2][4]==0:
                    print("Teacher 3 will  be substiute  the lecture from 1-2 pm")
                # elif teacher5[2][4]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 1-2 pm") 
                else:
                    print("No teacher is Free")
            if teacher4[2][5]==1:#check if teacher 2 has class at 2pm
                if teacher1[2][5]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 2-3 pm")
                    
                elif teacher2[2][5]==0:
                    print("Teacher 2 will  be substiute  the lecture from 2-3 pm")
                elif teacher3[2][5]==0:
                    print("Teacher 3 will  be substiute  the lecture from 2-3 pm")
                # elif teacher5[2][5]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 2-3 pm") 
                else:
                    print("No teacher is Free")
            if teacher4[2][6]==1:#check if teacher 2 has class at 3pm
                if teacher1[2][6]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 3-4 pm")
                    
                elif teacher2[2][6]==0:
                    print("Teacher 2 will  be substiute  the lecture from 3-4 pm")
                elif teacher3[2][6]==0:
                    print("Teacher 3 will  be substiute  the lecture from 3-4 pm")
                # elif teacher5[2][6]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 3-4 pm") 
                else:
                    print("No teacher is Free") 
            if teacher4[2][7]==1:#check if teacher 2 has class at 4pm
                if teacher1[2][7]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 4-5 pm")
                    
                elif teacher2[2][7]==0:
                    print("Teacher 2 will  be substiute  the lecture from 4-5 pm")
                elif teacher3[2][7]==0:
                    print("Teacher 3 will  be substiute  the lecture from 4-5 pm")
                # elif teacher5[2][7]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 4-5 pm") 
                else:
                    print("No teacher is Free")
        elif now==4:#check if day is Thursday
            
            if teacher4[3][0]==1:#check if teacher 2 has class at 9am
                if teacher1[3][0]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher2[3][0]==0:
                    print("Teacher 2 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher3[3][0]==0:
                    print("Teacher 3 will  be substiute  the lecture from 9-10 am")
                    
                # elif teacher5[4][0]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 9-10 am") 
                    
                else:
                    print("No teacher is Free")

            if teacher4[3][1]==1:#check if teacher 2 has class at 10am
                if teacher1[3][1]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 10-11 am")
                elif teacher2[3][1]==0:
                    print("Teacher 2 will  be substiute  the lecture from 10-11 am")
                elif teacher3[3][1]==0:
                    print("Teacher 3 will  be substiute  the lecture from 10-11 am")
                # elif teacher5[4][1]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 10-11 am") 
                else:
                    print("No teacher is Free")
            if teacher4[3][2]==1:#check if teacher 2 has class at 11am
                if teacher1[3][2]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 11-12 pm")
                    
                elif teacher2[3][2]==0:
                    print("Teacher 2 will  be substiute  the lecture from 11-12 pm")
                elif teacher3[3][2]==0:
                    print("Teacher 3 will  be substiute  the lecture from 11-12 pm")
                # elif teacher5[3][2]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 11-12 pm") 
                else:
                    print("No teacher is Free")
            if teacher4[3][3]==1:#check if teacher 2 has class at 12am
                if teacher1[3][3]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 12-1 pm")
                    
                elif teacher2[3][3]==0:
                    print("Teacher 2 will  be substiute  the lecture from 12-1 pm")
                elif teacher3[3][3]==0:
                    print("Teacher 3 will  be substiute  the lecture from 12-1 pm")
                # elif teacher5[4][3]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 12-1 pm") 
                else:
                    print("No teacher is Free")
            if teacher4[3][4]==1:#check if teacher 2 has class at 1pm
                if teacher1[4][4]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 1-2 pm")
                    
                elif teacher2[3][4]==0:
                    print("Teacher 2 will  be substiute  the lecture from 1-2 pm")
                elif teacher3[3][4]==0:
                    print("Teacher 3 will  be substiute  the lecture from 1-2 pm")
                # elif teacher5[3][4]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 1-2 pm") 
                else:
                    print("No teacher is Free")
            if teacher4[3][5]==1:#check if teacher 2 has class at 2pm
                if teacher1[3][5]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 2-3 pm")
                    
                elif teacher2[3][5]==0:
                    print("Teacher 2 will  be substiute  the lecture from 2-3 pm")
                elif teacher3[3][5]==0:
                    print("Teacher 3 will  be substiute  the lecture from 2-3 pm")
                # elif teacher5[4][5]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 2-3 pm") 
                else:
                    print("No teacher is Free")
            if teacher4[3][6]==1:#check if teacher 2 has class at 3pm
                if teacher1[3][6]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 3-4 pm")
                    
                elif teacher2[3][6]==0:
                    print("Teacher 2 will  be substiute  the lecture from 3-4 pm")
                elif teacher3[3][6]==0:
                    print("Teacher 3 will  be substiute  the lecture from 3-4 pm")
                # elif teacher5[4][6]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 3-4 pm") 
                else:
                    print("No teacher is Free") 
            if teacher4[4][7]==1:#check if teacher 2 has class at 4pm
                if teacher1[4][7]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 4-5 pm")
                    
                elif teacher2[4][7]==0:
                    print("Teacher 2 will  be substiute  the lecture from 4-5 pm")
                elif teacher3[4][7]==0:
                    print("Teacher 3 will  be substiute  the lecture from 4-5 pm")
                # elif teacher5[4][7]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 4-5 pm") 
                else:
                    print("No teacher is Free")
        elif now==5:#check if day is Friday
            
            if teacher4[4][0]==1:#check if teacher 1 has class at 9am
                if teacher1[4][0]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher2[4][0]==0:
                    print("Teacher 2 will  be substiute  the lecture from 9-10 am")
                    
                elif teacher3[4][0]==0:
                    print("Teacher 3 will  be substiute  the lecture from 9-10 am")
                    
                # elif teacher5[4][0]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 9-10 am") 
                    
                else:
                    print("No teacher is Free")

            if teacher4[4][1]==1:#check if teacher 2 has class at 10am
                if teacher1[4][1]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 10-11 am")
                elif teacher2[4][1]==0:
                    print("Teacher 2 will  be substiute  the lecture from 10-11 am")
                elif teacher3[4][1]==0:
                    print("Teacher 3 will  be substiute  the lecture from 10-11 am")
                # elif teacher5[5][1]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 10-11 am") 
                else:
                    print("No teacher is Free")
            if teacher4[4][2]==1:#check if teacher 2 has class at 11am
                if teacher1[4][2]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 11-12 pm")
                    
                elif teacher2[4][2]==0:
                    print("Teacher 2 will  be substiute  the lecture from 11-12 pm")
                elif teacher3[4][2]==0:
                    print("Teacher 3 will  be substiute  the lecture from 11-12 pm")
                # elif teacher5[4][2]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 11-12 pm") 
                else:
                    print("No teacher is Free")
            if teacher4[4][3]==1:#check if teacher 2 has class at 12am
                if teacher1[4][3]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 12-1 pm")
                    
                elif teacher2[4][3]==0:
                    print("Teacher 2 will  be substiute  the lecture from 12-1 pm")
                elif teacher3[4][3]==0:
                    print("Teacher 3 will  be substiute  the lecture from 12-1 pm")
                # elif teacher5[5][3]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 12-1 pm") 
                else:
                    print("No teacher is Free")
            if teacher4[4][4]==1:#check if teacher 1 has class at 1pm
                if teacher1[4][4]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 1-2 pm")
                    
                elif teacher2[4][4]==0:
                    print("Teacher 2 will  be substiute  the lecture from 1-2 pm")
                elif teacher3[4][4]==0:
                    print("Teacher 3  will  be substiute  the lecture from 1-2 pm")
                # elif teacher5[4][4]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 1-2 pm") 
                else:
                    print("No teacher is Free")
            if teacher4[4][5]==1:#check if teacher 1 has class at 2pm
                if teacher1[4][5]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 2-3 pm")
                    
                elif teacher3[4][5]==0:
                    print("Teacher 3 will  be substiute  the lecture from 2-3 pm")
                elif teacher3[4][5]==0:
                    print("Teacher 3 will  be substiute  the lecture from 2-3 pm")
                # elif teacher5[4][5]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 2-3 pm") 
                else:
                    print("No teacher is Free")
            if teacher4[4][6]==1:#check if teacher 1 has class at 3pm
                if teacher1[4][6]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 3-4 pm")
                    
                elif teacher2[4][6]==0:
                    print("Teacher 2 will  be substiute  the lecture from 3-4 pm")
                elif teacher3[4][6]==0:
                    print("Teacher 3 will  be substiute  the lecture from 3-4 pm")
                # elif teacher5[5][6]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 3-4 pm") 
                else:
                    print("No teacher is Free") 
            if teacher4[4][7]==1:#check if teacher 1 has class at 4pm
                if teacher1[4][7]== 0:
                    print("Teacher 1 will  be substiute  the lecture from 4-5 pm")
                    
                elif teacher2[4][7]==0:
                    print("Teacher 2 will  be substiute  the lecture from 4-5 pm")
                elif teacher3[4][7]==0:
                    print("Teacher 3 will  be substiute  the lecture from 4-5 pm")
                # elif teacher5[4][7]==0:
                #     print("Teacher 5 will  be substiute  the lecture from 4-5 pm") 
                else:
                    print("No teacher is Free")
        elif now==6:
            print("Not a lecture day")



   
r=int(input("Press 1 to run program\nPress 0 to exit program\n"))
while r==1:
    tt()
    r=int(input("Press 1 to run program\nPress 0 to exit program\n"))

