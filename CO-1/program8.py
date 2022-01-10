# Get a string from an input string where all occurrences of first character replaced with ‘$’, except first character.[eg: onion -> oni$n]

main_string = input("Type a string : ")
char = main_string[0]
main_string = main_string.replace(char,'$')
print(char+main_string[1:])

