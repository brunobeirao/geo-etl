from geo_etl import settings

class EtlService():

    def __init__(self):
        super().__init__()

    def run(self):
        file_path = settings.FILE_DIR
        f = open(file_path + "data_points_20180101.txt", "r")
        print(f.read())
