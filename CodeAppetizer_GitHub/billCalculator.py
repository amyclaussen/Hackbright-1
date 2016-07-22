# This is a comment and it not read by the interpreter
# These are useful for describing difficult code or adding reminders.
# TODO - Read this code and fix it.
# (Part 1): Fix any bugs and make it work!

bill = int(float(raw_input("How much was your bill?"))*100)

print "Bill", bill

tip = bill * .18

print "Tip", tip

total_bill = (bill + tip)/100

print "total bill",total_bill

print "The tip is %s and the total bill is %s." % (tip, total_bill)
