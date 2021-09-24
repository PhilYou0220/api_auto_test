import json


class ReadJson(object):
    def __init__(self, filename):
        self.filepath = "../testcasedata/" + filename

    def read_json(self):
        with open(self.filepath, mode='r', encoding="utf8") as f:
            data = json.load(f)  # data为字典类型 单例{} 多例{A:{"a":b,"c":"d"},"B":{"a":b,"c":"d"}}
        return data


if __name__ == '__main__':
    print(ReadJson("video_check/vc_area.json").read_json())
