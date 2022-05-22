'''
сбор данных машины, регистрация на сервере и ежеминутная передача данных
'''
from socket import gethostname
from time import sleep
import logging
import platform
import os
import psutil
import requests as rq

# logging
logging.basicConfig(
    filename='log_file.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%b %d %H:%M:%S',
)

# cooking client_info
def get_client_data() -> dict:
    '''
    собирает данные о клиенте
    '''
    hostname = gethostname() #hostname (ARmbp.local)
    try:
        desc = os.environ["DESC"]
    except KeyError:
        desc = "Empty desc"
    my_ip = rq.get('https://api.my-ip.io/ip').text

    return {"ip_address": my_ip, "description": desc, "name": hostname}


# cooking client_hw_info
def get_client_hw_data() -> dict:
    '''
    собирает данные о hw клиента
    '''
    load1, load5, load15 = os.getloadavg()
    partitions = psutil.disk_partitions()
    disks_info = []
    for partition in partitions:
        disk_info = {}
        disk_info['disk'] = {partition.device}
        disk_info['mountpoint'] = {partition.mountpoint}
        disk_info['file_system_type'] = {partition.fstype}
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            # this can be catched due to the disk that
            # isn't ready
            continue
        disk_info['total'] = {partition_usage.total}
        disk_info['used'] = {partition_usage.used}
        disk_info['free'] = {partition_usage.free}
        disks_info.append(disk_info)


    hwdict = {
        'host_information':
        {
            'sysname':platform.uname().system, 'hostname':platform.uname().node
            },
        'network': list(psutil.net_if_addrs().keys()),
        'disk': disks_info,
        'memory':
        {
            'memory_total': psutil.virtual_memory().total,
            'memory_used': psutil.virtual_memory().used,
            'memory_percent': psutil.virtual_memory().percent
            },
        'cpu':
        {
            'cpu_cores': psutil.cpu_count(logical=True),
            'cpu_physical_cores': psutil.cpu_count(logical=False),
            'cpu_freqency': f'{psutil.cpu_freq().max:.2f}'
            },
        'load_average':
        {
            '1 min': load1,
            '5 min': load5,
            '15 min': load15
            }
    }
    logging.info(hwdict)
    return hwdict

logging.info('Старт программы')
client_data = get_client_data()
logging.info('Данные о клиенте собраны')
client_hw_data = get_client_hw_data()
logging.info('Данные об оборудовании клиента собраны')

# connect to server and registered
IS_REGISTERED = False
ADD_SERVER_LINK = 'http://127.0.0.1:8000/api/servers/add'
ADD_SERVERDATA_LINK = 'http://127.0.0.1:8000/api/serverdata/add'
REGISTERED_SERVERS_LINK = 'http://127.0.0.1:8000/api/servers/status'
SERVER_ADMIN_LINK = 'http://127.0.0.1:8000/admin'
try:
    with rq.Session() as s:
        status_code = s.get(SERVER_ADMIN_LINK).status_code
        if status_code == 200:
            content = s.get(REGISTERED_SERVERS_LINK).json()
            for each in content:
                if each['ip_address'] == client_data['ip_address']:
                    logging.info('Сервер уже зарегистрирован')
                    IS_REGISTERED = True
        if not IS_REGISTERED:
            if s.post(ADD_SERVER_LINK, data=client_data).status_code == 201:
                logging.info('Успешная регистрация сервера')
                IS_REGISTERED = True
            else:
                IS_REGISTERED = False
                logging.error("Сервер не был зарегистрирован")
        while IS_REGISTERED:
            s.post(ADD_SERVERDATA_LINK, \
                data={'ip_address': str(client_data['ip_address']),'data': str(client_hw_data)})
            logging.info("Данные загружены")
            sleep(60)
except rq.exceptions.ConnectionError as ce:
    logging.error("ConnectionError Can't connect to server.")
except rq.exceptions.HTTPError as he:
    logging.error("HTTPError. Can't connect to server.")
except rq.exceptions.Timeout as t:
    logging.error('Timeout')
except rq.exceptions.TooManyRedirects as rmr:
    logging.error('TooManyRedirects')
except rq.exceptions.RequestException as re:
    logging.error('RequestException')
except TypeError as te:
    logging.error('TypeError via Session')
except KeyboardInterrupt as ki:
    logging.info('Завершение работы с клавиатуры')
