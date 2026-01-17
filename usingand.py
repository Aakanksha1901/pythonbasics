#using and
# all conditions must be true for the whole expression to be true.

age = 20
has_id= True

if age >=18 and has_id:
    print("allowed to enter")
else:
    print("not allowed")


#using or
#at least one condition must be true

is_student = False
has_discount_card = True

if is_student or has_discount_card:
    print("You get a discount")
else:
    print("no discount.")


#using not
#reverse the boolean value

logged_in = False

if not logged_in:
    print("Please login first")


#combining multiple booleans

age = 25
has_ticket = True
is_vip = False

if(age>= 18 and has_ticket) or is_vip :
    print("can enter event")
else:
    print("cannot enter")
