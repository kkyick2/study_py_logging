from concurrent.futures import ThreadPoolExecutor, as_completed
from pprint import pprint
from datetime import datetime
import time
import logging
import json
from netmiko import ConnectHandler, NetMikoAuthenticationException, NetmikoTimeoutException


logging.getLogger("paramiko").setLevel(logging.WARNING)

logging.basicConfig(
    format="%(threadName)s %(name)s %(levelname)s: %(message)s", level=logging.INFO
)

def count_time(func):
    def inner(*args):
        start = time.time()
        result = func(*args)
        print(f"[{func.__name__}] running time: {round((time.time() - start), 6)}s")
        return result
    return inner


def send_show(device_dict, command):
    start_msg = "===> {} Connection: {}"
    received_msg = "<=== {} Received: {}"
    ip = device_dict["ip"]
    logging.info(start_msg.format(datetime.now().time(), ip))
    if ip == "192.168.100.1":
        time.sleep(5)

    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
        logging.info(received_msg.format(datetime.now().time(), ip))
    return {ip: result}


def send_command_to_devices(devices, command):
    data = {}
    with ThreadPoolExecutor(max_workers=4) as executor:
        future_list = []
        for device in devices:
            future = executor.submit(send_show, device, command)
            future_list.append(future)
            print("Future: {} for device {}".format(future, device["ip"]))
        for f in as_completed(future_list):
            try:
                result = f.result()
                print("Future done {}".format(f))
            except (NetMikoAuthenticationException, NetmikoTimeoutException) as e:
                print ('type is:', e.__class__.__name__)
                print(e)
            else:
                data.update(result)
    return data

@count_time
def main():
    start_time = datetime.now()
    with open("devices.json") as f:
        devices = json.load(f)
        
    pprint(send_command_to_devices(devices, "sh clock"))

if __name__ == "__main__":
    main()