from geo_etl import settings

class EtlService():

    def __init__(self):
        super().__init__()

    def run(self):
        file_path = settings.FILE_DIR
        teste = []
        t1 = {}
        with open(file_path + "data_points_20180101.txt") as fp:
            line = fp.readline()
            # print(line)
            cnt = 0
            while line:
                if cnt <= 3:
                    cnt += 1
                    info = line.find(':')
                    info_name = line[:info]
                    t1[info_name] = line[info:]

                else:
                    teste.append(t1)
                    cnt = 0
                    t1 = {}
                # print("Line {}: {}".format(cnt, line.strip()))
                line = fp.readline()
            return teste
        # f = open(file_path + "data_points_20180101.txt", "r")
        # print(f.read())

        # for i in f.readline():
        #     print(i)
