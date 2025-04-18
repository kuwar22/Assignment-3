# Assignment-3
Readme report- Ferry services total price calculator
###This python priject is minial CLI tool I created to calculate total price on extra services a ferry customer could request.
###The purpose was to practice
#Taking input from users.
###Using loops.
###Performing calculations.
###Validating input.
From other file task 1 I imported customer booking to handel customer booking not being utilize in this file but could be a subsystem of larger system.
###COMPLETE CODE WITH EXPLANANTION
from task 1 import customer booking
Importing customer booking function from file 1 python file.
I have included a reference to customer booking even through I dont use it in the code to sugest that this could be the part of larger ferry booking system.
#def ferry_service_total
Here we define the function ferry_service_total and set it to zero, it will hold the total cost for all the services items and cost.
###while true
This put user into infinite loop,so that they can add as many as services items as ther want.
A loop that will stop only when user type finish
###items= input 
Here i am asking the user an item name.
Item is the variable in which the input is stored.
###if item.lower()finish:break
If the user enters finish the loop breaks with break.
###cost=input
If the user did not enter finish, the programprompts them for the cos of that item.
The cost is taken as input in the form of a string and stored in the variable cost.
###if not cost indigit(): print continue
This verifies whether the cost consists only of digit so that the user did not enter something like 10 
If its not a number, it print and error and return to the loop.
###cost=floatcost
It teansform the cost to a float from a string and we do this to add it to the total.
###total price +=cost 
Adds the cost at present to the total running.
###print total price 
After the loop terminates when user write finish, the program show the cost for all items given.
###ferry_service_total
Once the file is run this line calls the function ferry_service_total so the program actually starts.
##How to use it
Run the python file.
You will be prompted to enter service item names and prices 
When you are finished type finish.
The total cost will then be shown on the screen.
###EXAMPLE
service item name:bike 
cost for item:$10 
service item name:snack
cost for item snack:$5
service item name:finish
total price:$15.0
##What I have learnt from this task 
Define and call functions in pythom.
Using a while loop and break to manage flow.
How to input validation with. isgigit to avoid errors.
###Step: from string to number with float()
Make a simple calculator based on user input.
##Ideas for later Development
Allow decimal values like 12.50 in input validation current limit is 12,500,00 which should be updated isdigit will only match whole number.
Use a dictionary to store item names and costs so that I can print a receipt.
In place of just checking add actual proper error handling using try/except isdigit.
Implement the customer_booking() function so this is a complete booking and payment system.


