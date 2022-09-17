#  will print some colorful name here
# go to https://pypi.org/project/termcolor/ for more help

from termcolor import colored

print(colored('Hasnat', 'green'), colored('Osman', 'blue'))
text = colored("Hasnat Osman", "blue", attrs=["reverse", "bold"])
print(text)

# text = colored("Hello, World!", "red", attrs=["reverse", "blink"])
# print(text)
# cprint("Hello, World!", "green", "on_red")
#
# print_red_on_cyan = lambda x: cprint(x, "red", "on_cyan")
# print_red_on_cyan("Hello, World!")
# print_red_on_cyan("Hello, Universe!")
#
# for i in range(10):
#     cprint(i, "magenta", end=" ")
#
# cprint("Attention!", "red", attrs=["bold"], file=sys.stderr)
