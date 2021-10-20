def get_grade(avg_marks):
    if avg_marks>= 90:
        return 'A'
    elif avg_marks<90 and avg_marks>=80:
        return 'B'
    else:
        avg_marks<80
        return 'C'


def get_avg(marks_list):
    n=len(marks_list)
    sum=0
    for i in range(0,n):
        sum= sum + marks_list[i]
    return sum/n
        


def main():
    no_of_students=int(input('enter the number of students: '))
    name_list=[]
    avg_list=[]
    for i in range(no_of_students):
        name= input('enter name of the candidate: ')
        marks_list=list(map(int,input('enter 6 subjects marks: ').split(' ')))
        name_list.append(name)
        avg_list.append(get_avg(marks_list))

    for i in range(no_of_students):
        print('----------------------------------------')
        print('Name: ',name_list[i])
        print('avg_marks: ', avg_list[i])
        print('Grade: ',get_grade(avg_list[i]))

if __name__=='__main__':
    main()
