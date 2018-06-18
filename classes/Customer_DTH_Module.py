class Customer_DTH:
    def __init__(self):
        self.__account_id=None
        self.__dth_balance=None
        self.__due_date=None
        self.__phone_no=None
        self.__op_id=None

    def get_account_id(self):
        return self.__account_id


    def get_dth_balance(self):
        return self.__dth_balance


    def get_due_date(self):
        return self.__due_date


    def get_phone_no(self):
        return self.__phone_no


    def get_op_id(self):
        return self.__op_id


    def set_account_id(self, value):
        self.__account_id = value


    def set_dth_balance(self, value):
        self.__dth_balance = value


    def set_due_date(self, value):
        self.__due_date = value


    def set_phone_no(self, value):
        self.__phone_no = value


    def set_op_id(self, value):
        self.__op_id = value


