import os
import re
import threading

from core.src.frame_classse.design_frame import MainFrame
from core.src.static_classes.image_deal import ImageWork
from core.src.struct_classes.extect_struct import PerInfo, PerWorkList


class RestoreThread(threading.Thread):

    def __init__(self, id_thread, name, able: PerWorkList, unable: PerWorkList, parent: MainFrame, setting,
                 full, names, save_path):
        threading.Thread.__init__(self)
        self.full = full
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

        for self.index in range(len(self.able)):

            if self.stop:
                break
            if self.index < len(self.able) and not self.stop:
                now_info: PerInfo = self.able[self.index]
                self.format.m_staticText_info.SetLabel("当前第%d个！为：%s 类型-直接还原" % (self.index + 1, now_info.cn_name))

                # now_info.set_ex_as_cn = self.setting["export_with_cn"]

                # if self.setting['div_use'] == 0:
                #     if self.setting["div_type"] == 1:

                #         save_path = f"{self.save_path}\\{now_info.cn_name}"
                #         os.makedirs(save_path, exist_ok=True)

                #     elif self.setting["div_type"] == 2:
                #         pattern_skin = re.compile(r'^[a-zA-Z0-9_]+_\d$')
                #         pattern_power = re.compile(r'^[a-zA-Z0-9_]+_[gG]$')
                #         pattern_marry = re.compile(r'^[a-zA-Z0-9_]+_[hH]$')
                #         pattern_self = re.compile(r'^[a-zA-Z0-9_]+$')
                #         if pattern_skin.match(now_info.name) is not None:

                #             save_path = f"{self.save_path}\\皮肤"

                #         elif pattern_marry.match(now_info.name) is not None:
                #             save_path = f"{self.save_path}\\婚纱"

                #         elif pattern_power.match(now_info.name) is not None:
                #             save_path = f"{self.save_path}\\改造"

                #         elif pattern_self.match(now_info.name) is not None:
                #             save_path = f"{self.save_path}\\原皮"
                #         else:
                #             save_path = f"{self.save_path}\\其他"

                #     else:
                #         save_path = self.save_path

                # elif self.setting['div_use'] == 1:
                #     list_work = self.setting['divide_list']
                #     paths = filter(lambda x: re.match(x['pattern'], now_info.name), list_work[1:])
                #     paths = list(map(lambda x: f"{self.save_path}\\{x['dir']}", paths))

                #     if not paths:
                #         save_path = f"{self.save_path}\\其他"
                #     else:
                #         save_path = paths[0]

                # else:
                save_path = self.save_path

                os.makedirs(save_path, exist_ok=True)

                now_info.add_save(save_path)

                is_good, info = ImageWork.restore_tool(now_info)
                if not is_good:
                    pass

                val = round(100 * (self.index / len(self.able)))
                self.format.m_gauge_state.SetValue(val)
                self.index += 1

        #   if self.setting["export_type"] == 1:
        #
        #       num = 0
        #       os.makedirs(f'{self.save_path}\\拷贝', exist_ok=True)
        #
        #       for name in self.unable:
        #           name: PerInfo = name
        #           name.add_save(f'{self.save_path}\\拷贝')
        #           num += 1
        #           shutil.copyfile(name.tex_path, name.save_path)
        #
        #           self.format.m_gauge_state.SetValue(round(100 * (num / len(self.unable))))
        #           self.format.m_staticText_info.SetLabel(f"当前：{name.cn_name},仅拷贝")

        self.format.m_staticText_info.SetLabel(f"完成，共{len(self.able) + len(self.unable)}")
        self.format.start = False

        self.format.m_gauge_state.SetValue(100)

    #  if self.full["open_dir"]:
    #      os.system(r'start "%s"' % self.save_path)
    #
    #  if self.full['finish_exit']:
    #      self.format.exit(True)
    #
    #  if self.format.any_error():
    #      self.format.m_notebook_info.SetSelection(2)

    def stop_(self, stop: bool):
        self.stop = stop

    def add_save_path(self, save_path: str):
        self.save_path = save_path

    def update_value(self, able, unable):
        self.able = able
        self.unable = unable
