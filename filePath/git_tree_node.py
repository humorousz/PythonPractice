# -*- coding: utf-8
from __future__ import print_function
import os
import os.path
import sys

normal_symbol = '├──'
end_symbol = '└──'
modify_count = 0


def get_filter_files(root_path, path):
    res_list = []
    for temp in open(path).read().splitlines():
        res_list.append(root_path + "/" + temp)
    return res_list


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
        global modify_count
        modify_count += 1
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


def print_git_tree_node(root_path, work_path, file):
    os.chdir(work_path)
    file_filter_list = get_filter_files(root_path, file)
    dfs_show_dir(work_path, 0, file_filter_list, get_filter_dirs(file_filter_list))


if __name__ == '__main__':
    work_dir = sys.argv[1]
    file_path = sys.argv[2]
    root_dir = os.getcwd()
    print_git_tree_node(root_dir, work_dir, file_path)
    print("total modify file count :" + str(modify_count))
