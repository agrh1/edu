from os import getlogin as gl
from tempfile import TemporaryFile
from psutil import virtual_memory as vm

class PercentError(Exception):
    pass

def is_persent(persent):
    if 0 <= persent <= 100:
        return True
    raise PercentError('Percent value must be between 0 and 100')


def is_int(val):
    try:
        int_val = int(val)
    except ValueError as v:
        print(v, 'wrong memory value, default value used')
        return False
    return True


def is_float(val):
    try:
        float_val = float(val)
    except ValueError as v:
        print(v, 'wrong memory value, default value used')
        return False
    return True


class PC_memory:
    def __init__(self, pc_id, user_name, memory_total, memory_used, memory_percent=None) -> None:
        # PID
        self.pc_id = pc_id
        # Username
        self.user_name = user_name
        # Total Mem
        self.memory_total = int(memory_total/1024**3) if is_int(memory_total) else 100
        # Used memory
        self.memory_used = int(memory_used/1024**3) if is_int(memory_used) else 0
        # Persent memory
        if memory_percent is None:
            self.memory_percent = round(self.memory_used/self.memory_total*100,1)
            is_persent(self.memory_percent)
        elif is_persent(memory_percent) and is_float(memory_percent):
            self.memory_percent = memory_percent
        
    def show_used_percent(self):
        return f"PC with id '{self.pc_id}' used {self.memory_percent} percent of memory"
    
    def is_enough_memory(self):
        '''
        False если памяти осталось меньше 10% (процент свободной памяти меньше 10) или меньше 1Гб
        '''
        if self.memory_percent > 90 or self.memory_total - self.memory_used < 1:
            return False
        return True


print(f"Нечисловая строка Total")
pc_mem1 = PC_memory(1, 'user1', 'test', 3*1024**3)
print(f" \
    {pc_mem1.pc_id} \
    \n{pc_mem1.user_name} \
    \n{pc_mem1.memory_total} \
    \n{pc_mem1.memory_used} \
    \n{pc_mem1.memory_percent}")
print(f"Нечисловая строка Used")
pc_mem2 = PC_memory(1, 'user1', 3*1024**3, 'test')
print(f" \
    {pc_mem2.pc_id} \
    \n{pc_mem2.user_name} \
    \n{pc_mem2.memory_total} \
    \n{pc_mem2.memory_used} \
    \n{pc_mem2.memory_percent}")
print(f"Большое количество используемой памяти")
# pc_mem3 = PC_memory(1, 'user1', 3*1024**3, 6*1024**3)
# print(f"Большое количество используемой памяти \
#     {pc_mem3.pc_id} \
#     \n{pc_mem3.user_name} \
#     \n{pc_mem3.memory_total} \
#     \n{pc_mem3.memory_used} \
#     \n{pc_mem3.memory_percent}")
print(f"Отрицательное значение памяти")
pc_mem4 = PC_memory(1, 'user1', -3*1024**3, 1*1024**3)
print(f" \
    {pc_mem4.pc_id} \
    \n{pc_mem4.user_name} \
    \n{pc_mem4.memory_total} \
    \n{pc_mem4.memory_used} \
    \n{pc_mem4.memory_percent}")
