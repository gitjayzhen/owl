

import threading

# abc， def， ghi 输出 adg，beh, cfi


def str_to_list(s, result):
    tmp = [[x] for x in s]
    for i in range(len(tmp)):
        result[i].extend(tmp[i])

def main():
    result = [[],[],[]]
    v_1 = threading.Thread(target=str_to_list, args=("abc", result))
    v_2 = threading.Thread(target=str_to_list, args=("def", result))
    v_3 = threading.Thread(target=str_to_list, args=("ghi", result))
    for i in [v_1, v_2, v_3]:
        i.start()
        i.join()
    for n in result:
        print("".join(n))

if __name__ == "__main__":
    main()