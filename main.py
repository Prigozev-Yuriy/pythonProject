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


    dic1 = {1: "hello", 2: "world"}q
    dic2 = {3: "Python", 4: "Programming"}
    merge(dic1, dic2)  # {1: 'hello', 2: 'world', 3: 'Python', 4: 'Programming'}

<<<<<<< HEAD
<<<<<<< HEAD


=======
>>>>>>> parent of 3829c82 (time commit)
=======
    import time

    start_time = time.time()


    def fun():
        a = 2
        b = 3
        c = a + b


    end_time = time.time()
    fun()
    timetaken = end_time - start_time
    print("Your program takes: ", timetaken)  # 0.0345

>>>>>>> parent of 126e379 (time/revers commit)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/




def check_duplicate(lst):
    return len(lst) != len(set(lst))
check_duplicate([1,2,3,4,5,4,6]) # True
check_duplicate([1,2,3]) # False
check_duplicate([1,2,3,4,9]) # False



def Filtering(lst):
    return list(filter(None,lst))
lst=[None,1,3,0,"",5,7]
Filtering(lst) #[1, 3, 5, 7]



