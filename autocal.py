from statistics import stdev
import time
from Connection import FloatModbusClient


fur_stb = None
mas_stb = None
ch_temp = None
fur_std = []
mas_std = []

host = "192.168.111.222"
port = 502


def std_check(ch_name, stb_time, std):
    if(ch_name == "furnace"):
        addr = 33280
    elif(ch_name == "master"):
        addr = 33288
    for i in range(60):
        ch = FloatModbusClient(host, port, unit_id=1, auto_open=True)
        ch_temp.append(ch.read_float(addr, 1))
        ch.close()
        time.sleep(stb_time/60)
    if(stdev(ch_temp) > std):
        std_check(ch_name, stb_time, std)
    return stdev(ch_temp)


def mas_temp_check(set_point, mas_temp_diff):
    ch = FloatModbusClient(host, port, unit_id=1, auto_open=True)
    ch_temp = ch.read_float(33288, 1)
    ch.close()
    if((ch_temp-set_point) > mas_temp_diff):
        mas_temp_check(set_point, mas_temp_diff)
    else:
        return


def main(sp_list, mas_stb_time, fur_stb_time, standard_mas_std, mas_temp_diff):
    for i in range(len(sp_list)):
        set_point = sp_list(i)
        ch = FloatModbusClient(host, port, unit_id=1, auto_open=True)
        ch.write_float(33796, [set_point])
        fur_stb = False
        mas_stb = False
        while True:
            ch_temp = ch.read_float(33280, 1)
            ch.close()
            if(ch_temp == set_point):
                fur_std.append(std_check("furnace", fur_stb_time, 1))
                fur_stb = True
                mas_temp_check(set_point, mas_temp_diff)
                mas_std.append(
                    std_check("master", mas_stb_time, standard_mas_std))
                mas_stb = True
                break
    if(fur_stb == True and mas_stb == True):
        return [fur_std, mas_std]
