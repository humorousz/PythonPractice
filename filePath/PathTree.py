import os

normal_symbol = '├──'
end_symbol = '└──'
file_filter_list = ['cal.pyc']
dir_filter_list = ['.git']


def get_symbol(file_list, index):
    if index == len(file_list) - 1:
        return end_symbol
    else:
        return normal_symbol


def legal_file(node):
    if os.path.isdir(node):
        return True
    else:
        return node in file_filter_list


def dfs_show_dir(path, depth):
    if depth == 0:
        print("root:[" + path + "]")
    fileList = os.listdir(path)
    for index, node in enumerate(fileList):
        next_node = path + '/' + node
        if legal_file(next_node):
            if os.path.isdir(next_node):
                print("| " * depth + get_symbol(fileList, index) + node)
                dfs_show_dir(next_node, depth + 1)
            else:
                print("| " * depth + get_symbol(fileList, index) + node)


if __name__ == '__main__':
    dfs_show_dir('..', 0)
