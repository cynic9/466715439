# 自定义去重
from scrapy.dupefilters import BaseDupeFilter
from scrapy.utils.request import request_fingerprint


class CuiyuDupeFilter(BaseDupeFilter):

    def __init__(self):
        self.visited_fd = set()

    @classmethod
    def from_settings(cls, settings):
        return cls()

    def request_seen(self, request):
        fd = request_fingerprint(request=request)
        if fd in self.visited_fd:
            return True
        self.visited_fd.add(fd)

    def open(self):  # can return deferred
        print('开始')

    def close(self, reason):  # can return a deferred
        print('结束')

    # def log(self, request, spider):  # log that a request has been filtered
    #     print('日志')