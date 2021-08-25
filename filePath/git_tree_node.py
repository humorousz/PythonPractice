import os
import os.path

# 获取过滤文件
from filePath.config_tree import end_symbol, normal_symbol, file_path, root_path, work_dir


def get_filter_files(path):
    return open(path).read().splitlines()


def get_filter_dirs(file_list):
    dir_list = []
    for file_name in file_list:
        full_path = os.path.dirname(file_name)
        if full_path not in dir_list:
            dir_list.append(full_path)
    return dir_list


def get_symbol(file_list, index):
    if index == len(file_list) - 1:
        return end_symbol
    else:
        return normal_symbol


def is_legal_dir(full_node, dir_filters):
    for dir_path in dir_filters:
        if dir_path.find(full_node) != -1:
            return True
    return False


def legal_file(full_node, file_filters, dir_filters):
    if os.path.isdir(full_node):
        return is_legal_dir(full_node, dir_filters)
    else:
        return full_node in file_filters


def get_legal_file_list(path, file_filters, dir_filters):
    file_list = os.listdir(path)
    for node in file_list[:]:
        full_node = path + '/' + node
        if not legal_file(full_node, file_filters, dir_filters):
            file_list.remove(node)
    return file_list


def print_node(file_list, full_node, node, index, depth):
    count = depth - 1
    while count >= 0:
        print("│    ", end='')
        count -= 1
    if os.path.isdir(full_node):
        print(normal_symbol + node)
    else:
        print(get_symbol(file_list, index) + node)


def dfs_show_dir(path, depth, file_filters, dir_filters):
    if depth == 0:
        print("root:[" + path + "]")
    file_list = get_legal_file_list(path, file_filters, dir_filters)
    file_list.sort()
    # 开始遍历
    for index, node in enumerate(file_list):
        full_node = path + '/' + node
        print_node(file_list, full_node, node, index, depth)
        if os.path.isdir(full_node):
            dfs_show_dir(full_node, depth + 1, file_filters, dir_filters)


def test_filters(it):
    for name in it:
        print(name)


# def test_case():
#     file_filter_list = get_filter_files(file_path)
#     test_filters(file_filter_list)
#     test_filters(get_filter_dirs(file_filter_list))


if __name__ == '__main__':
    os.chdir(work_dir)
    file_filter_list = get_filter_files(file_path)
    dfs_show_dir(root_path, 0, file_filter_list, get_filter_dirs(file_filter_list))
