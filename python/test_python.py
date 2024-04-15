from python_functions import *



def test_files() -> None:
    """
    Tests the functions held in files.py
    """

    # fn_creator
    print(fn_creator('facebook', 'avian flu', 'egg laying'))
    print(fn_creator('facebook', 'avian flu', 'egg laying', prefix='0'))





def main() -> None:
    test_files()


if __name__ == "__main__":
    main()