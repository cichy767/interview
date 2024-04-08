class MyContextManager:
    def __init__(self):
        print("Init!")

    def __enter__(self):
        print('enter!')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit!')


with MyContextManager() as cm:
    pass



