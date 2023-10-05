def get_employees(path: str) -> list:
    """
    Функция создает список работников. Данные берутся из файла.
    Формируется список, каждый элемент которого имееет следующий вид:
    ФИО, департамент, команда, должность, оценка, зарплата
    :param path: строка, содержащая путь к файлу
    :return: возвращается список работников
    """
    file = open(path, 'r')
    employees = []
    for line in file:
        employees.append(line.split(';'))
    file.close()
    employees = employees[1:]
    for employee in employees:
        employee[4] = float(employee[4])
        employee[5] = int(employee[5])
    return employees


def get_summary() -> list:
    """
    Функция формирует отчет о департаментах. Для каждого департамента
    указывается его численность, минимальная, максимальная и средняя зарплаты
    :return: возвращается отчет, представленный в виде списка
    """
    employees = get_employees('Corp_Summary.csv')
    summary = {}
    for employee in employees:
        if employee[1] not in summary:
            summary[employee[1]] = [0, 10 ** 6, 0, 0]
        summary[employee[1]][0] += 1
        if employee[5] < summary[employee[1]][1]:
            summary[employee[1]][1] = employee[5]
        if employee[5] > summary[employee[1]][2]:
            summary[employee[1]][2] = employee[5]
        summary[employee[1]][3] += employee[5]
    for key in summary.keys():
        summary[key][3] = round(summary[key][3] / summary[key][0], 3)
    departments = sorted(list(summary.keys()))
    summary_list = []
    for department in departments:
        summary_list.append([department, *summary[department]])
    return summary_list


def print_hierarchy():
    """
    Функция печатает иерархию команд (департаменты и команды, которые
    в него входят)
    :return: функция ничего не возвращает
    """
    employees = get_employees('Corp_Summary.csv')
    hierarchy = {}
    for employee in employees:
        if employee[1] not in hierarchy:
            hierarchy[employee[1]] = set()
        hierarchy[employee[1]].add(employee[2])
    for key in hierarchy.keys():
        hierarchy[key] = sorted(list(hierarchy[key]))
    keys = sorted(list(hierarchy.keys()))
    print('\nИерархия команд:')
    for i in range(len(keys)):
        print(i + 1, '. ', keys[i], ': ', sep='')
        for j in range(len(hierarchy[keys[i]])):
            print('\t', j + 1, '. ', hierarchy[keys[i]][j], sep='')
    print()


def print_summary():
    """
    Функция запрашивает отчет и затем выводит его на экран
    :return: функция ничего не возвращает
    """
    summary = get_summary()
    for i in range(len(summary)):
        print(i + 1, '. ', summary[i][0], sep='')
        print('\tЧисленность: ', summary[i][1], '\n\tМин. зарплата: ',
              summary[i][2], '\n\tМакс. зарплата: ', summary[i][3],
              '\n\tСредняя зарплата: ', summary[i][4], sep='')
    print()


def save_summary():
    """
    Функция запрашивает отчет и сохраняет его в файл summary.csv
    :return: функция ничего не возвращает
    """
    titles = ['Департамент', 'Численность', 'Мин. зарплата', 'Макс. зарплата', 'Средняя зарплата']
    summary = get_summary()
    file = open('summary.csv', 'w')
    file.write(';'.join(titles) + '\n')
    for department in summary:
        file.write(';'.join(list(map(str, department))) + '\n')
    file.close()


def print_menu():
    """
    Функция реализует логику меню. Пользователь выбирает команду,
    которую он хочет выполнить
    :return: функция ничего не возвращает
    """
    print('0. Выйти из программы',
          '1. Вывести иерархию команд',
          '2. Вывести сводный отчет по департаментам',
          '3. Сохранить сводный отчет в виде csv-файла',
          sep='\n')
    print('Введите номер желаемой операции: ', end='')
    operation = input()
    while operation != '0':
        if operation != '1' and operation != '2' and operation != '3':
            print('Введен некорректный номер, повторите ввод: ', end='')
            operation = input()
            continue
        if operation == '1':
            print_hierarchy()
        if operation == '2':
            print_summary()
        if operation == '3':
            save_summary()
            print('Отчет записан в файл summary.csv\n')
        print('Введите номер желаемой операции: ', end='')
        operation = input()
    print('\nПрограмма закончена')


if __name__ == '__main__':
    print_menu()
