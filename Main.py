import os
import sys
import time

from core.src.frame_classes.main_frame import MainFrame


class LogHolder(object):
    def __init__(self, work_path, stream=sys.stdout,name=""):
        self.stream = stream
        self.work_path = work_path
        self.t = time.localtime()
        self.file_name=os.path.join(path, f"core\\assets\\{name}.txt")
        self.is_last_n=True

    def write(self, message):
        if self.is_last_n:
            message=f"\n\t{time.asctime(self.t)}\n--------------\n{message}"
            self.is_last_n=False
        if message.endswith("\n"):
            message=f"{message}\n--------------\n"
            self.is_last_n=True
        self.stream.write(message)

        with open(self.file_name,'a')as file:
            file.write(message)

    def flush(self):
        pass


if __name__ == '__main__':
    path = os.path.split(os.path.realpath(sys.argv[0]))[0]
    sys.stderr = LogHolder(path, sys.stderr,"error_logs")
    sys.stdout = LogHolder(path, sys.stdout, "output_logs")
    MainFrame.run(path)
