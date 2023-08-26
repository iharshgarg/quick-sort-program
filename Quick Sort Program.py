#Quick Sort Program
def swapper(list,pointer,pivot):
    temp=list[pointer]
    list[pointer]=list[pivot-1]
    list[pivot-1]=list[pivot]
    list[pivot]=temp
def sorter(list,pointer,pivot):
    if pointer<pivot:
        old_pointer=pointer
        old_pivot=pivot
        while pointer!=pivot:
            if list[pointer]>=list[pivot]:
                swapper(list,pointer,pivot)
                pivot-=1
            else:
                pointer+=1
        sorter(list,old_pointer,pivot-1)
        sorter(list,pivot+1,old_pivot)
def quick(list):
    sorter(list,0,len(list)-1)
    return list
print('Hello, Welcome to my Quick Sort Program!')
def program():
    mylist=list(eval(input('Enter the list: ')))
    print('Your sorted list is:',quick(mylist))
    if input('Do you want to sort more?\n')=='yes':
        program()
    else:
        print('Thank you for using the program\nexiting...')
program()