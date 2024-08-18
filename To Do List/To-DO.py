#Command Line Python based TO-DO List Application.
#Project for CodSoft Internship
#Naman Kalra


t=[]
def add():
    task=input("Please enter a Task:")
    t.append(task)
    print(f"Task '{task}' has been added to the list")
    print("\n")

def display():
    l=len(t)
    i=0
    j=1
    if t==[]:
        print("There are no task currently.")
    while i<l:
        print(f"Task {j}: {t[i]}")
        i+=1
        j+=1
    print("\n")
    
def remove():
    display()
    try:
        task=int(input("Select the # you want to delete:"))
        task-=1
        if task>=0 and task<len(t):
            t.pop(task)
            print("The task has been removed succesfully")
            print("\n")
        else:
            print(f"The Task {task} was not found.")
            print("\n")
    except:
        print("Invalid Input.")
        

if __name__=="__main__":
    print("Hiiii>>>\nWelcome to the To-Do List Application")
    print("What is your name?")
    name=input()
    print("\n")
    
    while True:
        print(f"What would you like to do??")
        print("---------------------------")
        print("1. Add a Task in the list")
        print("2. Delete a task from the list")
        print("3. Display the task from today")
        print("4. Exit the application")
        print("\n")
        x=int(input("Please select from 1-4:"))
        if x==1:
            add()
        elif x==2:
            print("\n")
            remove()
        elif x==3:
            print("\n")
            display()
        elif x==4:
            print("\n")
            print(f"Thank You for the time {name}... Have a Great Day!")
            break
        else:
            print("\n")
            print("Please choose from the above 1-4")