import os

normal_symbol = '├── '
end_symbol = '└── '
file_filter_list = ['PathTree.py', 'cal.py']
dir_filter_list = ['../filePath', 'Number']


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
    dfs_show_dir('..', 0)
