from main import get_time_diff, shift_half_hour, get_available_windows

def test_get_time_diff():
    assert get_time_diff('18:20', '18:40') == 20
    assert get_time_diff('11:02', '11:19') == 17
    assert get_time_diff('17:50', '18:40') == 50
    assert get_time_diff('13:01', '14:02') == 61
    assert get_time_diff('19:59', '20:12') == 13

def test_shift_half_hour():
    assert shift_half_hour('09:00') == '09:30'
    assert shift_half_hour('19:30') == '20:00'
    assert shift_half_hour('18:40') == '19:10'
    assert shift_half_hour('11:19') == '11:49'
    assert shift_half_hour('17:50') == '18:20'

def test_get_available_windows():
    assert get_available_windows('09:00', '21:00', 
        [
        {'start': '18:15', 'stop': '20:59'},
        {'start': '09:25', 'stop': '17:39'}
        ]) ==\
        [
        {'start': '17:39', 'stop': '18:09'}]
    
    assert get_available_windows('09:00', '21:00', 
        [
        {'start': '11:25', 'stop': '16:23'}, 
        {'start': '09:29', 'stop': '10:50'},
        {'start': '17:29', 'stop': '20:13'}]) ==\
        [
        {'start': '10:50', 'stop': '11:20'},
        {'start': '16:23', 'stop': '16:53'},
        {'start': '16:53', 'stop': '17:23'},
        {'start': '20:13', 'stop': '20:43'}]

    assert get_available_windows('10:00', '17:00', 
        [
        {'start': '12:35', 'stop': '14:39'},
        {'start': '10:35', 'stop': '12:09'}
        ]) ==\
        [
        {'start': '10:00', 'stop': '10:30'},
        {'start': '14:39', 'stop': '15:09'},
        {'start': '15:09', 'stop': '15:39'},
        {'start': '15:39', 'stop': '16:09'},
        {'start': '16:09', 'stop': '16:39'}]

    assert get_available_windows('09:00', '21:00', 
        [
        {'start' : '10:30', 'stop' : '10:50'},
        {'start' : '18:40', 'stop' : '18:50'},
        {'start' : '14:40', 'stop' : '15:50'},
        {'start' : '16:40', 'stop' : '17:20'},
        {'start' : '20:05', 'stop' : '20:20'}]) == \
        [
        {'start': '09:00', 'stop': '09:30'},
        {'start': '09:30', 'stop': '10:00'},
        {'start': '10:00', 'stop': '10:30'},
        {'start': '10:50', 'stop': '11:20'},
        {'start': '11:20', 'stop': '11:50'},
        {'start': '11:50', 'stop': '12:20'},
        {'start': '12:20', 'stop': '12:50'},
        {'start': '12:50', 'stop': '13:20'},
        {'start': '13:20', 'stop': '13:50'},
        {'start': '13:50', 'stop': '14:20'},
        {'start': '15:50', 'stop': '16:20'},
        {'start': '17:20', 'stop': '17:50'},
        {'start': '17:50', 'stop': '18:20'},
        {'start': '18:50', 'stop': '19:20'},
        {'start': '19:20', 'stop': '19:50'},
        {'start': '20:20', 'stop': '20:50'}]