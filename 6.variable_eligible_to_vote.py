# write a program that prints "are you eligible to vote or not"

voter_name = input("Please enter your name: ")
voter_age = input("Please enter your age: ")

if int(voter_age) >= 18:
    print("====================================================================================================")
    print("=                Dear", voter_name, "You are eligible to vote.                                     =")
    print("=                Congratulations! your vote has been submitted successfully.                       =")
    print("====================================================================================================")
else:
    print("====================================================================================================")
    print("=                Sorry Dear", voter_name, "sir you are not eligible to vote. You are below 18.     =")
    print("====================================================================================================")