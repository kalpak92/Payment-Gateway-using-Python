class customer_mobile:
    def __init__(self):
        self.__phone_no=None
        self.__conn_type=None
        self.__mob_balance=None
        self.__monthly_rental=None
        self.__op_id=None

    def get_phone_no(self):
        return self.__phone_no


    def get_conn_type(self):
        return self.__conn_type


    def get_mob_balance(self):
        return self.__mob_balance


    def get_monthly_rental(self):
        return self.__monthly_rental


    def get_op_id(self):
        return self.__op_id


    def set_phone_no(self, value):
        self.__phone_no = value


    def set_conn_type(self, value):
        self.__conn_type = value


    def set_mob_balance(self, value):
        self.__mob_balance = value


    def set_monthly_rental(self, value):
        self.__monthly_rental = value


    def set_op_id(self, value):
        self.__op_id = value
