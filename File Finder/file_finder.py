import os

"""
[✅] Accept user input (file name and directory)
[✅] Traverse to given directory [find_path(file_name, directory)]
    [✅] compare the given file name while traversing
    [✅] case insensitive
[✅] Open File (open_file(name_of_file, directory))
    [✅] Check the search results
        [✅] if items > 1
            [✅] Provide choices what item to open
        [✅] if items == 1
            [✅] open the first index
        [✅] other wise prompt the user
    [✅] Helper function (helper(paths, choice=0))
        [✅] provide choice 
            [✅] open the item without giving the path
            [✅] give the path but don't open the the item
            [✅] do both

"""


def find_path(file_name, directory):
    path = []
    ext = []
    # traverse the directory given
    for dirpath, dirnames, filenames in os.walk(directory):
        # traverse all file name
        for f in filenames:
            # compare without case sensitivity
            if os.path.splitext(f)[0].lower() == file_name.lower():
                ext.append(os.path.splitext(f)[1])
                path.append(os.path.join(dirpath, f))
    return path, ext


def helper(paths, choice=0):
    try:
        c = int(input(
            '\033[92mDo you want to open the file or get the path? \n[0] to open  \
            \n[1] to get the path \n[2] to do both \nchoose: '))
        if c == 0:
            # open file
            os.startfile(paths[choice])
        elif c == 1:
            # return path
            print(f'\033[96mYou can find the file at: {paths[choice]}')
        elif c == 2:
            # open file and return path
            os.startfile(paths[choice])
            print(f'\033[96mYou can find the file at: {paths[choice]}')
    except FileNotFoundError:
        # opening file error
        print(f'\033[91mFile not found try to navigate here {paths[choice]}')


def open_file(name_of_file, directory):
    # result of the search
    paths, exts = find_path(name_of_file, directory)

    # check if items are found
    if len(paths) == 0:
        print('\033[91mItem does not exist')
        return

    # check the number of results
    if len(exts) > 1:
        print(f'\033[95mMultiple items matched : {len(exts)} items')
        for i, p in enumerate(paths):
            print(f'[{i}] {os.path.basename(p)}')
        choice = int(
            input('\033[92mWhich one do you want to open? \n choose: '))
        helper(paths, choice)

    else:
        helper(paths)


def main(name_of_file, directory):
    open_file(name_of_file, directory)


if __name__ == '__main__':
    # get use input
    print('\033[95mMake sure to enter the exact name of a file')
    name_of_file = input("\033[92mEnter the name of the file: ")
    directory = input("\033[92mEnter the directory you want to inspect: ")
    main(name_of_file, directory)
