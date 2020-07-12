import os
import queue
import re
import shutil
import threading
import time
from multiprocessing import connection

from core.src.frame_classes.main_frame import MainFrame
from core.src.static_classes.image_deal import ImageWork
from core.src.static_classes.static_data import GlobalData
from core.src.structs_classes.extract_structs import PerInfo


def worker(target, save, frame, data, count, pipe: connection.Connection):
    try:

        now_info: PerInfo = target
        frame.format.m_staticText_info.SetLabel("当前第%d个！为：%s 类型-直接还原" % (count, now_info.cn_name))

        now_info.is_save_as_cn = frame.setting[data.sk_use_cn_name]

        # 文件分类部分
        if frame.setting[data.sk_output_group] == data.feg_do_no_group:
            save_path = save

        elif frame.setting[data.sk_output_group] == data.feg_by_type:
            pattern_skin = data.fp_skin
            pattern_power = data.fp_build_up
            pattern_marry = data.fp_wedding
            pattern_young = data.fp_young
            pattern_self = data.fp_default_skin
            if pattern_skin.match(now_info.name) is not None:

                save_path = f"{save}\\皮肤"

            elif pattern_marry.match(now_info.name) is not None:
                save_path = f"{save}\\婚纱"

            elif pattern_power.match(now_info.name) is not None:
                save_path = f"{save}\\改造"

            elif pattern_self.match(now_info.name) is not None:
                save_path = f"{save}\\原皮"

            elif pattern_young.match(now_info.name) is not None:
                save_path = f"{save}\\幼女化"

            elif data.fp_u_skin.match(now_info.name) is not None:
                save_path = f"{save}\\μ兵装"

            else:
                save_path = f"{save}\\其他"

        elif frame.setting[data.sk_output_group] == data.feg_by_name:
            val = re.match(r'^(.+)(_[hg\d])$', now_info.name)
            if val is not None:
                val = val.group(1)
                if now_info.has_cn and frame.setting[data.sk_use_cn_name]:
                    if val.lower().startswith("hdn"):
                        val += '_1'
                    if frame.ignore_case:
                        val = val.lower()
                    value = frame.names.get(val)
                    if value != "":
                        val = value
            else:
                if now_info.has_cn and frame.setting[data.sk_use_cn_name]:
                    val = now_info.cn_name
                else:
                    val = now_info.name

            save_path = f"{save}\\{val}"

        elif frame.setting[data.sk_output_group] == data.feg_by_is_able:
            save_path = f"{save}\\{'还原'}"

        else:
            save_path = save

        os.makedirs(save_path, exist_ok=True)

        now_info.add_save(save_path)

        is_good, info = ImageWork.restore_tool(now_info)
        if not is_good:
            frame.format.m_staticText_info.SetLabel(info)

        val = round(100 * (frame.index / len(frame.able)))
        frame.format.m_gauge_state.SetValue(val)
        frame.index += 1
    except KeyError as info:
        frame.format.m_staticText_info.SetLabel(f"处理出错！，为{info}")
        pipe.send(info)


def lalal(l):
    print(l)

    time.sleep(0.5)


q = queue.Queue()


class WorkThread(threading.Thread):
    def __init__(self, name, work_queue, locker, parent: MainFrame, setting,
                 names, save_path, size, ignore_case=False, ):
        super(WorkThread, self).__init__(name=name, )
        self.size = size
        self.ignore_case = ignore_case
        self.save_path = save_path
        self.names = names
        self.setting = setting
        self.format = parent
        self.locker: threading.Lock = locker
        self.work_queue: queue.Queue = work_queue

    def run(self) -> None:
        data = GlobalData()
        exit_flag = True
        if self.work_queue.empty():
            exit_flag = False
        while exit_flag:
            try:
                # 拿东西
                if not self.work_queue.empty():
                    self.locker.acquire()
                    target, count = self.work_queue.get()
                    self.locker.release()

                    # 干活！
                    now_info: PerInfo = target
                    self.format.m_staticText_info.SetLabel("当前第%d个！为：%s 类型-直接还原" % (count + 1, now_info.cn_name))

                    now_info.is_save_as_cn = self.setting[data.sk_use_cn_name]

                    # 文件分类部分
                    if self.setting[data.sk_output_group] == data.feg_do_no_group:
                        save_path = self.save_path

                    elif self.setting[data.sk_output_group] == data.feg_by_type:
                        pattern_skin = data.fp_skin
                        pattern_power = data.fp_build_up
                        pattern_marry = data.fp_wedding
                        pattern_young = data.fp_young
                        pattern_self = data.fp_default_skin
                        if pattern_skin.match(now_info.name) is not None:

                            save_path = f"{self.save_path}\\皮肤"

                        elif pattern_marry.match(now_info.name) is not None:
                            save_path = f"{self.save_path}\\婚纱"

                        elif pattern_power.match(now_info.name) is not None:
                            save_path = f"{self.save_path}\\改造"

                        elif pattern_self.match(now_info.name) is not None:
                            save_path = f"{self.save_path}\\原皮"

                        elif pattern_young.match(now_info.name) is not None:
                            save_path = f"{self.save_path}\\幼女化"

                        elif data.fp_u_skin.match(now_info.name) is not None:
                            save_path = f"{self.save_path}\\μ兵装"

                        else:
                            save_path = f"{self.save_path}\\其他"

                    elif self.setting[data.sk_output_group] == data.feg_by_name:
                        val = re.match(r'^(.+)(_[hg\d])$', now_info.name)
                        if val is not None:
                            val = val.group(1)
                            if now_info.has_cn and self.setting[data.sk_use_cn_name]:
                                if val.lower().startswith("hdn"):
                                    val += '_1'
                                if self.ignore_case:
                                    val = val.lower()
                                value = self.names.get(val)
                                if value != "":
                                    val = value
                        else:
                            if now_info.has_cn and self.setting[data.sk_use_cn_name]:
                                val = now_info.cn_name
                            else:
                                val = now_info.name

                        save_path = f"{self.save_path}\\{val}"

                    elif self.setting[data.sk_output_group] == data.feg_by_is_able:
                        save_path = f"{self.save_path}\\{'还原'}"

                    else:
                        save_path = self.save_path

                    os.makedirs(save_path, exist_ok=True)

                    now_info.add_save(save_path)

                    is_good, info = ImageWork.restore_tool(now_info)
                    if not is_good:
                        self.format.m_staticText_info.SetLabel(info)

                    val = round(100 * (count / len(self.size)))
                    self.format.m_gauge_state.SetValue(val)

            except Exception as info:
                self.format.m_staticText_info.SetLabel(f"处理出错！，为{info},在{self.name}")


class SideWorkThread(threading.Thread):
    def __init__(self, unable, setting, format, save_path):
        super(SideWorkThread, self).__init__(name="Side work")
        self.setting = setting
        self.unable = unable
        self.format = format
        self.save_path = save_path

    def run(self) -> None:
        data = GlobalData()
        if self.setting[data.sk_export_all_while_copy]:

            num = 0
            if self.setting[data.sk_output_group] == data.feg_by_is_able:
                save_path = f'{self.save_path}\\拷贝'
            else:
                save_path = self.save_path

            os.makedirs(save_path, exist_ok=True)

            for name in self.unable:
                name: PerInfo = name
                name.add_save(save_path)
                num += 1
                shutil.copyfile(name.tex_path, name.save_path)

                self.format.m_gauge_state.SetValue(round(100 * (num / len(self.unable))))
                self.format.m_staticText_info.SetLabel(f"当前：{name.cn_name},仅拷贝")

        self.format.m_gauge_state.SetValue(100)


class WatchDogThread(threading.Thread):
    def __init__(self, work_queue, err_queue, able_group, unable_group, lock):
        super(WatchDogThread, self).__init__(name="watch dog")
        self.lock: threading.Lock = lock
        self.unable_group = unable_group
        self.able_group = able_group
        self.err_queue: queue.Queue = err_queue
        self.work_queue: queue.Queue = work_queue
        self.exit = False
        self.count = 0
        self.is_need = True

        self.err_list = []

        self.work_size = len(able_group)

    def stop(self):
        self.exit = True
        self.able_group.clear()
        self.unable_group.clear()
        while not self.work_queue.empty():
            self.lock.acquire()
            self.work_queue.get()
            self.lock.release()

        while not self.err_queue.empty():
            self.lock.acquire()
            self.err_list.append(self.err_queue.get())
            self.lock.release()

        return self.err_list

    def run(self) -> None:
        while not self.exit:
            if not self.work_queue.full() and self.is_need:
                self.lock.acquire()
                self.work_queue.put([self.able_group[self.count], self.count])
                self.lock.release()
                self.count += 1
                if not self.count < self.work_size:
                    self.is_need = False

            if not self.err_queue.empty():
                self.lock.acquire()
                self.err_list.append(self.err_queue.get())
                self.lock.release()

            time.sleep(0.1)


if __name__ == '__main__':
    pass
