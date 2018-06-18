class Vodafone_Mobile:
    def __init__(self):
        self.__rech_type=None
        self.__rech_amount=None
        self.__scheme=None
        self.__validity=None

    def get_rech_type(self):
        return self.__rech_type


    def get_rech_amount(self):
        return self.__rech_amount


    def get_scheme(self):
        return self.__scheme


    def get_validity(self):
        return self.__validity


    def set_rech_type(self, value):
        self.__rech_type = value


    def set_rech_amount(self, value):
        self.__rech_amount = value


    def set_scheme(self, value):
        self.__scheme = value


    def set_validity(self, value):
        self.__validity = value
