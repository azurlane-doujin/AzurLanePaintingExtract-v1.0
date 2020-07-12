import os
import queue
import re
import shutil
import threading
import time

from core.src.frame_classes.design_frame import MainFrame
from core.src.static_classes.image_deal import ImageWork
from core.src.static_classes.static_data import GlobalData
from core.src.structs_classes.extract_structs import PerInfo, PerWorkList


class RestoreThread(threading.Thread):

    def __init__(self, id_thread, name, able: PerWorkList, unable: PerWorkList, parent: MainFrame, setting,
                 names, save_path, ignore_case=False):
        threading.Thread.__init__(self)

        self.ignore_case = ignore_case
        self.names = names
        self.setting = setting
        self.format = parent

        self.able = able
        self.unable = unable

        self.threadID = id_thread

        self.name = name

        self.index = 0

        self.stop = False

        self.save_path = save_path

    def run(self):
        data = GlobalData()
        for self.index in range(len(self.able)):

            if self.stop:
                return
            try:
                if self.index < len(self.able) and not self.stop:
                    now_info: PerInfo = self.able[self.index]
                    self.format.m_staticText_info.SetLabel("当前第%d个！为：%s 类型-直接还原" % (self.index + 1, now_info.cn_name))

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

                    val = round(100 * (self.index / len(self.able)))
                    self.format.m_gauge_state.SetValue(val)
                    self.index += 1
            except KeyError as info:
                self.format.m_staticText_info.SetLabel(f"处理出错！，为{info}")
                raise
        if self.stop:
            return
        if self.setting[data.sk_export_all_while_copy]:

            num = 0
            if self.setting[data.sk_output_group] == data.feg_by_is_able:
                save_path = f'{self.save_path}\\拷贝'
            else:
                save_path = self.save_path

            os.makedirs(save_path, exist_ok=True)

            for name in self.unable:
                if self.stop:
                    return
                name: PerInfo = name
                name.add_save(save_path)
                num += 1
                shutil.copyfile(name.tex_path, name.save_path)

                self.format.m_gauge_state.SetValue(round(100 * (num / len(self.unable))))
                self.format.m_staticText_info.SetLabel(f"当前：{name.cn_name},仅拷贝")

        self.format.m_staticText_info.SetLabel(f"完成，共{len(self.able) + len(self.unable)}")
        self.format.start = False

        if self.stop:
            return

        self.format.m_gauge_state.SetValue(100)

        if self.setting[data.sk_open_output_dir]:
            os.system(r'start "%s"' % self.save_path)

        if self.setting[data.sk_finish_exit]:
            self.format.exit(None)

    def stop_(self, stop: bool):
        self.stop = stop

    def add_save_path(self, save_path: str):
        self.save_path = save_path

    def update_value(self, able, unable):
        self.able = able
        self.unable = unable


class WorkThread(threading.Thread):
    def __init__(self, name, work_queue, err_queue, locker, parent: MainFrame, setting,
                 names, save_path, size, ignore_case=False, ):
        super(WorkThread, self).__init__(name=name, )
        self.err_queue = err_queue
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

        while exit_flag:
            if self.work_queue.empty():
                exit_flag = False
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

                    val = round(100 * (count / self.size))
                    self.format.m_gauge_state.SetValue(val)

            except Exception as info:
                self.format.m_staticText_info.SetLabel(f"处理出错！，为{info},在{self.name}")
                self.locker.acquire()
                self.err_queue.put(info)
                self.locker.release()


class SideWorkThread(threading.Thread):
    def __init__(self, unable, setting, frame, save_path):
        super(SideWorkThread, self).__init__(name="Side work")
        self.setting = setting
        self.unable = unable
        self.format = frame
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
    def __init__(self, work_queue, err_queue, able_group, lock, frame, setting, size, threads):
        super(WatchDogThread, self).__init__(name="watch dog")
        self.threads = threads
        self.size = size
        self.setting = setting
        self.format = frame
        self.lock: threading.Lock = lock
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

        while not self.work_queue.empty():
            self.lock.acquire()
            self.work_queue.get()
            self.lock.release()

        while not self.err_queue.empty():
            self.lock.acquire()
            self.err_list.append(self.err_queue.get())
            self.lock.release()

        return self.err_list

    def exit_action(self):
        data = GlobalData()
        self.format.m_staticText_info.SetLabel(f"完成，共{self.size}")
        self.format.start = False

        self.format.m_gauge_state.SetValue(100)

        if self.setting[data.sk_finish_exit]:
            self.format.exit(None)

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

            t = not self.is_need and self.work_queue.empty()
            if t:
                self.stop()
                self.exit_action()

            time.sleep(0.1)
        while self.exit:
            data = list(map(lambda x: x.is_alive(), self.threads))
            if True in data:
                time.sleep(0.1)
            else:
                break
