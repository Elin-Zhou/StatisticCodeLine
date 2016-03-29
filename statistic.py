import os


class Statistic:
    def __init__(self, root_path, *expand_name):
        '''
        :param root_path: 根路径
        :param expand_name: 拓展名列表
        :return:
        '''
        self.root_path = str(root_path)
        self.expand_name = expand_name

    def resolve(self):
        comment_line, code_line, blank_line = self.__resolve_dir(self.root_path)
        print("\n\n\n---------------------------------------------------------------------\n\n\n")
        print(
                self.root_path + "   comment_line:%d  code_line:%d  blank_line:%d" % (
                    comment_line, code_line, blank_line))

    def __resolve_dir(self, path):
        path = str(path)
        # 注释
        comment = 0
        # 代码
        code = 0
        # 空行
        blank_line = 0
        if not os.path.isdir(path):
            pass
        else:
            files = os.listdir(path)
            for file in files:
                if file.startswith("."):
                    continue
                new_path = path + "/" + file
                if os.path.isdir(new_path):
                    comment, code, blank_line = map(lambda x, y: x + y, (comment, code, blank_line),
                                                    self.__resolve_dir(new_path))
                else:
                    comment, code, blank_line = map(lambda x, y: x + y, (comment, code, blank_line),
                                                    self.__resolve_file(new_path))
        return comment, code, blank_line

    def __resolve_file(self, path):
        path = str(path)
        # 注释
        comment_line = 0
        # 代码
        code_line = 0
        # 空行
        blank_line = 0

        if list(filter(lambda arg: path.endswith(str(arg)), self.expand_name)):
            try:
                java_file = open(path, "r")
                for line in java_file:
                    line = line.lstrip()
                    if len(line) == 0:
                        blank_line += 1
                    elif line.startswith("//") or line.startswith("/*") or line.startswith("*") or line.startswith("#"):
                        comment_line += 1
                    else:
                        code_line += 1
            except UnicodeDecodeError:
                java_file = open(path, "r", encoding="utf8")
                for line in java_file:
                    line = line.lstrip()
                    if len(line) == 0:
                        blank_line += 1
                    elif line.startswith("//") or line.startswith("/*") or line.startswith("*") or line.startswith("#"):
                        comment_line += 1
                    else:
                        code_line += 1
            print(path + "   comment_line:%d  code_line:%d  blank_line:%d" % (comment_line, code_line, blank_line))
        else:
            pass

        return comment_line, code_line, blank_line


if __name__ == "__main__":
    path = "/yumei/code_new/"

    statistic = Statistic(path, ".java", ".jsp")
    statistic.resolve()
