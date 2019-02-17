#Given a string of even length and print the output as string contains last half added with first half of the given string

Input_str = "vamsikrishna"
i = len(Input_str)//2
if len(Input_str)%2==0:
    print(Input_str[i:]+Input_str[:i])
