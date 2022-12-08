import subprocess

def inst(p_name):
    """
    Install package(s) inside a python script.
    Supported formats:
    inst("numpy")
    inst("numpy, requests, pandas")
    inst(["numpy", "requests", "pandas"])
    """

    try:
        if isinstance(p_name, str):  # if p_name is a string, install the package
            print(f'\033[35mInstalling {p_name}...')
            if "," in p_name:
                p_name = p_name.split(",")
                inst(p_name)
                return
            p = p_name.replace(" ", "")
            print(f'Checking status of {p} using pip...\033[0m')
            output = subprocess.run("pip3 show " + p, shell=True)
            if output.returncode != 0:
                subprocess.run("pip3 install " + p, shell=True)
            else:
                print(f'{p} is already installed, skipping installation.\n')

        if isinstance(p_name, list):  # if p_name is a list, install all packages in the list
            for p in p_name:
                inst(p)

    except Exception as e:
        print(f'\033[31mAn error {e} occurred while installing {p_name}.\033[0m')