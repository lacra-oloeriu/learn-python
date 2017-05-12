def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")#This line print a text whit a number of cheese
    print(f"You have {boxes_of_crackers} boxes_of_crackers!")#that print a text whit the number of boxex of crackers
    print("Man that's enough for a party!")#this one print the text""
    print(" Get a blanket.\n")# print the txt


print("We can just give the function numbers direcrly:")#print the text
cheese_and_crackers(20, 30)#we give the function ...numbres


print("Or, we can use variavles from our script:")#print the text
amount_of_cheese = 10#the variables for fonction
amount_of_crackers = 50#variables for functions

cheese_and_crackers(amount_of_cheese, amount_of_crackers)#total variables cheese and crackers


print("We can even do math inside too:")#print the text
cheese_and_crackers(10+ 20, 5+6)#the function calculate the adition numbers and put the result


print("And we can combine the two, variables and math:")#text than explein the next
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)#function whit we combine math and variables than incrise the totol for cheese whit 100 and crackers whit 1000
