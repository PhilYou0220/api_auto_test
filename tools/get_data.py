from tools.read_json import ReadJson


class GetData(object):
    def get_data(self, casepath):
        data = ReadJson(casepath).read_json()
        test_data = []
        real_test_data = []  # 承载[()]格式
        for i in data.items():
            test_data.append(i[1])
        test_data = tuple(test_data)
        real_test_data.append(test_data)
        return real_test_data  # [('https://ticketapi.shomes.cn/-/select-option/area', {}, 'youfei', '1')]

    def more_get_data(self, casepath):
        data = ReadJson(casepath).read_json()  # {A:{"a":b,"c":"d"},"B":{"a":b,"c":"d"}}
        test_data = []
        real_test_data = []  # 承载[()]格式
        for i in data.values():  # {"a":b,"c":"d"}
            for j in i.items():  # ("a":b),("c":"d")
                test_data.append(j[1])  # j[1] -> b
            test_data = tuple(test_data)
            real_test_data.append(test_data)
            test_data = []  # 清空 承接下一用例的值
        return real_test_data  # [('https://ticketapi.shomes.cn/-/select-option/area', '', 'youfei', '1'), ('https://ticketapi.shomes.cn/-/select-option/area', '', '13608031977', 'youfei123')]


# 调试函数
# casepath = "video_check/vc_area.json"
# a = GetData().more_get_data(casepath)
# print(a)
