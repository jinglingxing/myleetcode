class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = [(value, timestamp)]
        else:
            self.dic[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.dic:
            return ''

        value_time_list = self.dic[key]

        if not value_time_list:
            return ''

        left, right = 0, len(value_time_list) - 1

        while left < right:
            mid = (left + right + 1) // 2

            value, pre_time = value_time_list[mid]

            if pre_time > timestamp:
                right = mid - 1
            else:
                left = mid

        return value_time_list[left][0] if value_time_list[left][1] <= timestamp else ''