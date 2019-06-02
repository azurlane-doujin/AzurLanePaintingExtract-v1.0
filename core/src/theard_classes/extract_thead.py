import os
import re
import shutil
import threading

from core.src.frame_classse.design_frame import MainFrame
from core.src.static_classes.image_deal import ImageWork
from core.src.static_classes.static_data import GlobalData
from core.src.struct_classes.extect_struct import PerInfo, PerWorkList


class RestoreThread(threading.Thread):

    def __init__(self, id_thread, name, able: PerWorkList, unable: PerWorkList, parent: MainFrame, setting,
                 names, save_path):
        threading.Thread.__init__(self)

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
                        save_path = f"{self.save_path}\\Lily化"

                    else:
                        save_path = f"{self.save_path}\\其他"

                elif self.setting[data.sk_output_group] == data.feg_by_name:
                    val = re.match(r'^(.+)(_[hg\d])$', now_info.name)
                    if val is not None:
                        val = val.group(1)
                        if now_info.has_cn and self.setting[data.sk_use_cn_name]:
                            value = self.names[val]
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
