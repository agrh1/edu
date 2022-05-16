'''
Напишите скрипт, который:

1. Принимает в качестве параметров требуемое количество записей и задержку (соответственно, он должен запускаться с терминала с указанием необходимых параметров).
2. Выводит в файл log_file.log указанное количество строчек лога с указанной задержкой между записью строк.
3. Структура строки лога - Трехбуквенное обозначение текущего месяца, число месяца, время в формате ЧЧ:ММ:СС, уровень записываемого лога, сообщение. Разделитель между всеми элементами лога - пробел. Месяц от даты также должен отделять пробел.
<месяц> <число> <часы>:<минуты>:<секунды> <уровень> <сообщение>
Содержание строки лога - сообщение с уровнем INFO, в котором вы передаете по одной переменной окружения в таком виде: <Имя переменной> -> <Содержание переменной>
Пример записи лога:
Jun 10 14:00:30 INFO NUMBER_OF_PROCESSORS -> 4
4. Запустите скрипт и запишите 10 строк лога с задержкой 2 секунды между записями.
'''

import argparse, logging, sys, os, time

# arg parser
parser = argparse.ArgumentParser(description="add args")
parser.add_argument('-num', help='number of lines', required=True, default=10, type=int)
parser.add_argument('-lat', help='latency', required=True, default=2, type=int)
args = parser.parse_args()

# logging
logging.basicConfig(
    filename='log_file.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%b %d %H:%M:%S',
)

i=0
for param in os.environ:
    
    if i < args.num:
        print(i, param)
        logging.info(f'{param} -> {os.environ.get(param)}')
        time.sleep(args.lat)
        i += 1
    else:
        break


with open('log_file.log', 'r') as f:
    logs = f.readlines()
    print("".join(logs[len(logs)-args.num:]))

