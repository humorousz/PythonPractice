import os
import os.path

file_path = "/Users/zhangzhiquan/Github/PythonPractice/file.txt"
dir_path = "/Users/zhangzhiquan/Github/PythonPractice/dir.txt"
root_path = "./ks-features/ft-live/live/src/main/java/com/yxcorp/gifshow/live"
normal_symbol = '├── '
end_symbol = '└── '
file_filter_list = []
dir_filter_list = []


def get_file_list(file_path):
    file = open(file_path)
    return file.readlines()


def get_filter_files():
    global file_filter_list
    global dir_filter_list
    file_filter_list = get_file_list(file_path)
    dir_filter_list = get_file_list(dir_path)


def get_symbol(file_list, index):
    if index == len(file_list) - 1:
        return end_symbol
    else:
        return normal_symbol


def legal_file(full_node, node):
    if os.path.isdir(full_node):
        return full_node in dir_filter_list
    else:
        return node in file_filter_list


def dfs_show_dir(path, depth):
    if depth == 0:
        print("root:[" + path + "]")
    file_list = os.listdir(path)
    # 先过滤不合法
    for node in file_list[:]:
        full_node = path + '/' + node
        if not legal_file(full_node, node):
            file_list.remove(node)
    # 开始遍历
    for index, node in enumerate(file_list):
        full_node = path + '/' + node
        if os.path.isdir(full_node):
            print("| " * depth + normal_symbol + node)
            dfs_show_dir(full_node, depth + 1)
        else:
            print("| " * depth + get_symbol(file_list, index) + node)


if __name__ == '__main__':
    os.chdir('/Users/zhangzhiquan/KS/kwai-android')
    get_filter_files()
    dfs_show_dir(root_path, 0)
