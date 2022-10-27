# This is a sample Python script.
import os.path
import robot.robot as robot

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def questions():
    while True:
        name = input('Hello I am Robosun. What are you name?\n')
        if name != '':
            break
    if os.path.exists(robot.csv_file_name):
        recommend = robot.recommend_restaurant_info()
        for item in recommend:
            print('My recommend restaurant is ' + item['NAME'])
            while True:
                like = input('Do you like this restaurant?[Yes/No]\n')
                lower_like = like.lower()
                if lower_like == 'yes' or lower_like == 'no':
                    break
            if lower_like == 'yes':
                break

    while True:
        restaurant = input(name + '.' + ' Which restaurant do you like?\n')
        if restaurant != '':
            break

    cap_rest = restaurant.capitalize()
    print(name + '.' + 'Thank you\n' + 'Have a nice day! Good bye!')

    if os.path.exists(robot.csv_file_name):
        count_dic_list = robot.read_from_csv(cap_rest)
        robot.write_to_csv(count_dic_list)
    else:
        count_list = [{'NAME': cap_rest, 'COUNT': 1}]
        robot.write_to_csv(count_list)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    questions()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
