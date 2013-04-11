# -*- coding: utf-8 -*-

N = 5

class MyTask:
    # タスクの発生時刻と終了時刻を定義
    def __init__(self, s, t):
        self.start_time = s
        self.end_time   = t

def set_my_task_posibilities():
    # 発生しうるタスクの可能性を列挙する
    my_task_posibilities = []
    my_task_posibilities.append(MyTask(2,5))
    my_task_posibilities.append(MyTask(4,7))
    my_task_posibilities.append(MyTask(6,9))
    my_task_posibilities.append(MyTask(8,10))
    my_task_posibilities.append(MyTask(1,3))

    return my_task_posibilities

def solve(task_posibilites):

    task_list = []
    for idx in range(0,len(task_posibilites),1):
        task_list.append(MyTask(task_posibilites[idx].start_time, 
                                task_posibilites[idx].end_time))

    # タスクを終了時間の速いものをソートキーに並べ替える
    sorted_task_list = []
    for entry in sorted(task_list, key=lambda x:x.end_time):
        sorted_task_list.append(entry)

    ans = 0
    t   = 0

    # 最もタスクが終了する時間の速いものから配列に格納していく
    for idx in range(0, N):
        if (t < sorted_task_list[idx].start_time):
            ans += 1
            t = sorted_task_list[idx].end_time

    print ans


def __main__():
    my_task_posibilities = set_my_task_posibilities()

    solve(my_task_posibilities)

__main__()
