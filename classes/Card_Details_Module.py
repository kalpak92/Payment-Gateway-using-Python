class Card_Details:
    def __init__(self):
        self.__card_number=None
        self.__cust_name=None
        self.__expiry_date=None
        self.__cvv=None
        self.__card_type=None
        self.__status=None
        self.__balance=None
        self.__grid_code=None
        
        
    def get_card_number(self):
        return self.__card_number


    def get_cust_name(self):
        return self.__cust_name


    def get_expiry_date(self):
        return self.__expiry_date


    def get_cvv(self):
        return self.__cvv


    def get_card_type(self):
        return self.__card_type


    def get_status(self):
        return self.__status


    def get_balance(self):
        return self.__balance


    def get_grid_code(self):
        return self.__grid_code


    def set_card_number(self, value):
        self.__card_number = value


    def set_cust_name(self, value):
        self.__cust_name = value


    def set_expiry_date(self, value):
        self.__expiry_date = value


    def set_cvv(self, value):
        self.__cvv = value


    def set_card_type(self, value):
        self.__card_type = value


    def set_status(self, value):
        self.__status = value


    def set_balance(self, value):
        self.__balance = value


    def set_grid_code(self, value):
        self.__grid_code = value
