class CreateBankAccount():

    def __init__(self, __id='', __name='', __balance=0):
        self.__id = __id
        self.__name = __name
        self.__balance = __balance
        
    def __dep(self, dep):   #存款
        self.__balance = self.__balance + int(dep)
    
    def __wit(self, wit):   #提款
        self.__balance = self.__balance + int(wit)

    def __tra(self, )

