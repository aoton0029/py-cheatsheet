import sys
import threading
import queue
import random
from time import sleep
from datetime import datetime

class ExcThread(threading.Thread):
    """実行するスレッドのクラス"""
    # コンストラクタ
    def __init__(self, bucket, name):
        threading.Thread.__init__(self)
        self.bucket = bucket
        self.name = name

    # スレッド実行
    def run(self):
        print(self.name + " start!")
        try:
            while True:
                random_num = random.randint(1, 10)
                date = datetime.now().strftime("%Y%m%d_%H%M%S")
                print(self.name + " :{}, {}".format(random_num, date))
                # 乱数が8より大きい場合はException
                if random_num > 8:
                    raise Exception(self.name + ' Exception!')
                sleep(1)
        except Exception:
            # Exceptionの情報をQueueに追加
            error_data = [self.name, sys.exc_info()]
            self.bucket.put(error_data)


def thread_mng():
    try:
        while True:
            # 無限ループは「Ctrl+C」で終了させる
            # キューからデータがなくなるまで取り出しを行う
            while not error_queue.empty():
                error_data = error_queue.get(block=False) # Queueのエラー内容を取得
                name = error_data[0]

                # 念のためスレッドの死活判定してエラーの表示＋スレッド作り直して始動
                if not thread_dict[name].isAlive():
                    printException(error_data[1])
                    thread_start(thread_dict, name, error_queue)
    except KeyboardInterrupt:
        # 「Ctrl+C」を検知
        printException(sys.exc_info())
        print("---- thread Exception Catch end ----")


# スレッドを開始する関数
def thread_start(thread_dict, name, error_queue):
    thread_dict[name] = ExcThread(error_queue, name)
    # メインスレッドが終了したら他のスレッドも終了させたいのでデーモンスレッドにしている
    thread_dict[name].setDaemon(True)
    thread_dict[name].start()


# エラーの内容を表示する関数
def printException(error_data):
    exc_type, exc_obj, exc_trace = error_data
    print(exc_type, exc_obj, exc_trace)


if __name__ == '__main__':
    print("---- thread Exception Catch start ----")
    thread_name_list = ["th-1", "th-2", "th-3", "th-4"] # スレッド名のリスト
    thread_dict = dict()
    error_queue = queue.Queue()

    # スレッド名の分だけスレッド開始
    for name in thread_name_list:
        thread_start(thread_dict, name, error_queue)
        
    