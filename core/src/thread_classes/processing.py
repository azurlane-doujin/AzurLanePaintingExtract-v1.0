import os
import re
import time
from multiprocessing import connection, Pool, Pipe

from core.src.static_classes.image_deal import ImageWork
from core.src.structs_classes.extract_structs import PerInfo


def worker(target, save, frame, data, count, size, pipe: connection.Connection):
    id=os.getpid()
    print(id,count)
    try:

        now_info: PerInfo = target
        frame.m_staticText_info.SetLabel("当前第%d个！为：%s 类型-直接还原" % (count, now_info.cn_name))

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

        val = round(100 * (count / size))
        frame.m_gauge_state.SetValue(val)
    except KeyError as info:
        frame.m_staticText_info.SetLabel(f"处理出错！，为{info}")
        print(info)
        pipe.send((info, id))

    time.sleep(0.5)


def apply_work(target_group, save_path, frame, data):
    pool = Pool()
    main_pipe, sub_pipe = Pipe()
    count = 1
    size = len(target_group)
    print(size)
    for target in target_group:
        print(count)
        print(target)
        pool.apply_async(worker,args=(target, save_path, frame, data, count, size, sub_pipe,))
        count += 1


    pool.close()
    pool.join()
