import subprocess

# Define the paths to your Python scripts
script1_path = 'D:/Aditya/College files/Year4Sem1/AD/AD-1/app1.py'
script2_path = 'D:/Aditya/College files/Year4Sem1/AD/AD-1/app2-1.py'

# Execute the first Python script
# subprocess.run(['python', script1_path])
choice = int(input("Enter the program you want to execute: "))

if(choice==1):
    print("Executing the program Image to Text")
    subprocess.run(['python', script1_path])
elif(choice==2):
    print("Executing the program Image to Table")
    subprocess.run(['python', script2_path])
else:
    print("Enter the valid choice")
# Execute the second Python script
# subprocess.run(['python', script2_path])
