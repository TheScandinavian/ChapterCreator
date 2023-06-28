import os


def function_create_chapter_directory():
    # Define new directory
    directory = "Chapter Creator"

    # Define parent directory path
    parent_dir = "C:/"

    # Define path for new directory
    path = os.path.join(parent_dir, directory)

    # Create new directory in parent directory
    os.mkdir(path)
    print("Directory '% s' created" % directory)


def function_check_chapter_directory():
    path = "C:/Chapter Creator/"
    chapter_dir_exist = os.path.exists(path)
    if chapter_dir_exist is False:
        function_create_chapter_directory()


if __name__ == "__Chapter_Creator_Main__":
    function_create_chapter_directory()
    function_check_chapter_directory()
