from core.src.static_classes.static_data import GlobalData

data = GlobalData()
a = {data.sk_clear_when_input: True, data.sk_finish_exit: True, data.sk_skip_exist: True, data.sk_open_output_dir: True,
     data.sk_use_cn_name: True, data.sk_make_new_dir: True,data.sk_export_all_while_copy:False, data.sk_input_filter_mesh: r'.+\.[Oo][Bb][Jj]',
     data.sk_input_filter_tex: r'.+\.[Pp][Nn][Gg]', data.sk_input_filter: 0, data.sk_output_group: 0}

print(a)
import json

with open("setting.json", 'w')as file:
    json.dump(a, file)
