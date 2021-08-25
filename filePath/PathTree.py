import os
import os.path

file_path = "/Users/zhangzhiquan/Github/PythonPractice/file.txt"
root_path = "./ks-features/ft-live/live/src/main/java/com/yxcorp/gifshow/live"
normal_symbol = '├── '
end_symbol = '└── '


# 获取过滤文件
def get_filter_files(path):
    return open(path).readlines()


def get_filter_dirs(file_list):
    dir_set = set()
    for file_name in file_list:
        dir_set.add(os.path.dirname(file_name))
    return dir_set


def get_symbol(file_list, index):
    if index == len(file_list) - 1:
        return end_symbol
    else:
        return normal_symbol


def legal_file(full_node, node, file_filters, dir_filters):
    if os.path.isdir(full_node):
        return full_node in dir_filters
    else:
        return node in file_filters


def dfs_show_dir(path, depth, file_filters, dir_filters):
    if depth == 0:
        print("root:[" + path + "]")
    file_list = os.listdir(path)
    # 先过滤不合法
    for node in file_list[:]:
        full_node = path + '/' + node
        if not legal_file(full_node, node, file_filters, dir_filters):
            file_list.remove(node)
    # 开始遍历
    for index, node in enumerate(file_list):
        full_node = path + '/' + node
        if os.path.isdir(full_node):
            print("| " * depth + normal_symbol + node)
            dfs_show_dir(full_node, depth + 1)
        else:
            print("| " * depth + get_symbol(file_list, index) + node)


# def test_filters(it):
#     for name in it:
#         print(name)


# def test_case():
#     file_filter_list = get_filter_files(file_path)
#     test_filters(file_filter_list)
#     test_filters(get_filter_dirs(file_filter_list))


if __name__ == '__main__':
    os.chdir('/Users/zhangzhiquan/KS/kwai-android')
    file_filter_list = get_filter_files(file_path)
    dfs_show_dir(root_path, 0, file_filter_list, get_filter_dirs(file_filter_list))
