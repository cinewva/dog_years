# Each year for a human is like 7.18 years for a dog
DOG_YRS_MULTIPLIER = 7.18  

def main():
    DOG_YRS_MULTIPLIER = 7.18
    calendar_years = float(input("Enter an age in calendar years: "))
    print("That's "+ str(round((calendar_years*DOG_YRS_MULTIPLIER),2)) + " in dog years!")


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()