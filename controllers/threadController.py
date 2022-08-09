import sys
from threading import Thread

class ThreadController():

    threads = []
    dameon = False

    def __init__(self):
        pass

    def add_thread(self, args = ()):
        self.threads.append(
            Thread(
                target=self.call_script,
                args=args
            )
        )

    def call_script(self, process):
        process.start()

    def start_threads(self):
        threads = self.threads
        dameonBool = self.dameon

        try:
            for t in threads:
                t.daemon = dameonBool
            for t in threads:
                t.start()
            for t in threads:
                t.join()
        except Exception as e:
            print("threading err:")
            print(e)