class LopHoc:
    # Khai báo thuộc tính ở chuẩn private
    __ten_lop = '10A1'
    # Khai báo phương thức ở chuẩn private
    def __getName(self):
        print(self.__ten_lop)

    #Khai báo phương thức ở dạng public để gọi thành phần private
    def get(self):
        self.__getName()



