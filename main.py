busy = [
{'start' : '10:30',
'stop' : '10:50'
},
{'start' : '18:40',
'stop' : '18:50'
},
{'start' : '14:40',
'stop' : '15:50'
},
{'start' : '16:40',
'stop' : '17:20'
},
{'start' : '20:05',
'stop' : '20:20'
}
]

def get_time_diff(start: str, stop: str) -> int:
    """Получение интервала времени в минутах: get_time_diff('13:01', '14:02') -> 61"""
    minutes_start = int(start[:2])*60 + int(start[3:])
    minutes_stop = int(stop[:2])*60 + int(stop[3:])
    return minutes_stop - minutes_start


def shift_half_hour(time: str) -> str:
    """Сдвиг на полчаса вперед ('10:04' -> '10:34')"""
    minutes = int(time[:2])*60 + int(time[3:]) + 30
    return f"{minutes//60}".zfill(2) + ":" + f"{minutes%60}".zfill(2)


def append_windows_by_interval(start_time: str, stop_time: str,
                               windows: list[dict[str, str]]) -> None:
    """Присоединение к списку windows свободных окон по 30 минут
    в заданном интервале (от start_time до stop_time)"""
    interval = get_time_diff(start_time, stop_time)
    if(interval >= 30):
        for _ in range(0, interval//30):
            stop_time = shift_half_hour(start_time)
            windows.append({'start': start_time, 'stop': stop_time})
            start_time = stop_time


def get_available_windows(appt_start: str, appt_stop: str, 
                          busy: list[dict[str, str]]) -> list[dict[str, str]]:
    """Получение списка свободных окон windows от начала приема до конца приема доктора 
    (от appt_start до appt_stop) с учетом списка занятых окон busy"""

    windows = []
    # сортировка списка занятых окон busy по возрастанию
    busy = sorted(busy, key=lambda x: x['start'])

    # цикл по занятым окнам
    for i in range(0, len(busy) - 1):
        
        # отрезок от начала приема (appt_start = '09:00') до начала первого занятого окна
        if i == 0:
            start_time = appt_start
            stop_time = busy[i]['start']
            append_windows_by_interval(start_time, stop_time, windows)

        # отрезки от конца i-ого занятого окна до начала i+1-ого занятного окна
        start_time  = busy[i]['stop']
        stop_time = busy[i+1]['start']
        append_windows_by_interval(start_time, stop_time, windows)

        # отрезок от конца последнего занятого окна до конца приема (appt_stop = '21:00')
        if i == len(busy) - 2:
            start_time = busy[i+1]['stop']
            stop_time = appt_stop
            append_windows_by_interval(start_time, stop_time, windows)
    
    return windows


if __name__ == '__main__':
    windows = get_available_windows('09:00', '21:00', busy)
    for window in windows: print(window)