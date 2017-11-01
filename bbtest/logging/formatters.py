import logging


class MysqlFormatter(logging.Formatter):
    def format(self, record):
        record.args = (record.args[0] * 1000, record.args[1])
        record.msg = "(\033[0;31m%.4fms\033[0m) \033[0;34m%s\033[0m"
        if self.uses_server_time() and not hasattr(record, "server_time"):
            record.server_time = self.formatTime(record, "%d/%b/%Y %H:%M:%S")
        return super().format(record)

    def uses_server_time(self):
        return self._fmt.find('%(server_time)') >= 0
