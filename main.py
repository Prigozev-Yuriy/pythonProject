# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


    def get_vowels(String):
        return [each for each in String if each in "aeiou"]


    get_vowels("animal")  # [a, i, a]
    get_vowels("sky")  # []
    get_vowels("football")  # [o, o, a]


    def capitalize(String):
        return String.title()


    capitalize("shop")  # [Shop]
    capitalize("python programming")  # [Python Programming]
    capitalize("how are you!")  # [How Are You!]


    def merge(dic1, dic2):
        dic3 = dic1.copy()
        dic3.update(dic2)
        return dic3


    dic1 = {1: "hello", 2: "world"}
    dic2 = {3: "Python", 4: "Programming"}
    merge(dic1, dic2)  # {1: 'hello', 2: 'world', 3: 'Python', 4: 'Programming'}

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
