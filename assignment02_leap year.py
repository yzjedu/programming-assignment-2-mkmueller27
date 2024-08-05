# Step 0: Intro comment here
# Name: Kristina Mueller
# Course: CS701/GB735, Dr. Yalew
# Date: August 5, 2024
# Programming Assignment: 2
# Program Inputs: Month (as a number in the range 1 through 12), Year
# Program Outputs: Number of days in the given month

def main():

# Step 1: Ask the user for the month and year
    month = str(input("Enter the month (MM): "))
    year = int(input("Enter the year (YYYY): "))

    leap_year = None
# Step 2: Determine if the year is a leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap_year = True
        print("leap Year")
    else:
        leap_year = False
        print("non-leap year")
   
    # Step 3: Determine the number of days in the month
    number_of_days = None
    if month == "01" or month == "03" or month =="05" or month =="07" or month =="08" or month =="10" or month =="12":
        number_of_days = 31
    elif month == "02" and leap_year == True:
        number_of_days = 29
    elif month == "02" and leap_year == False:
        number_of_days = 28
    else:
        number_of_days = 30
   
    # Step 4: Output the number of days in the month
    print("Number of Days: ", number_of_days)

   
pass

if __name__ == "__main__":
    main()