print("Welcome to the ski resort!")
print("")

#this gets the users budget and returns it to be used in other places.
def create_ski_day_budget():
    while True:
        user_budget = input("Please Enter your starting budget in dollars >> ")
        print("")
        try:
            user_budget = float(user_budget)
            return user_budget
            break
        except ValueError:
            print("")
            print("Your budget needs to be a number")
            print("")
    print()
    user_budget = float(user_budget)

#this gets if the user wants a full or half day ski pass and ask the user for there age, then calculates there left over budget accordingly.
def purchase_lift_ticket(budget):
    print("1. One-Day Ticket")
    print("")
    print("2. Half-Day Ticket")
    print("")

    while True:
        ticketType = input("What type of ticket do you want to purchase? >> ")
        print("")
        if ticketType in ["1", "2"]:
            break
        else:
            print("Your ticket type needs to be either full day or half day")
            print("")

    while True:
        age = input("What is your age? >> ")
        print("")
        try:
            age = int(age)
            break
        except ValueError:
            print("Your age needs to be a whole number")
            print("")
    age = int(age)
    if ticketType == "1":

        if age >= 0 and age <= 17:
            budget = budget - 31.5

        elif age >= 18 and age <= 65:
            budget = budget - 47.25

        elif age >= 66:
            budget = budget - 31.5

    else:

        if age >= 0 and age <= 17:
            budget = budget - 15.75

        elif age >= 18 and age <= 65:
            budget = budget - 21.125

        elif age >= 66:
            budget = budget - 15.75

    if budget >= 1:
        print("You where in budget. You still have $"+str(budget)+"!")
    else:
        print("You where not in budget. You went over the budget by $"+str(abs(budget)))

#These call the functions/runs them
user_Budget = create_ski_day_budget()
purchase_lift_ticket(user_Budget)