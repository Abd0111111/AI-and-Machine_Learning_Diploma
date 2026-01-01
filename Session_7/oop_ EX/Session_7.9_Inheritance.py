'''
في كلاس flyer، قيمة wing_size بتتضاعف مرتين.

في كلاس swimmer، بيحتفظ بـ fin_size وبيتحكم في إمكانية السباحة.

في كلاس duck اللي يرث من الاثنين، بنستدعي الكونستركتور بتاع كل كلاس أب يدويًا.

في get_info() بننفذ دوال fly و swim مباشرة.
'''
class flyer :
    def __init__(self,is_flyer,wing_size):
        self.wing_size = wing_size *2
        self.is_flyer = is_flyer
    def fly (self):
       if (self.is_flyer ==True):
        print(f"yes is can fly by wing size {self.wing_size}")
       else:
        print(f"no is cant fly")

class swimmer:
    def __init__(self,is_swimming,fin_size):
        self.fin_size = fin_size
        self.is_swimming = is_swimming
    def swim (self):
        if self.is_swimming ==True:
         print(f"yes is can swim by fin_size {self.fin_size}")
        else:
            print(f"no is can swim ")
class duck(flyer,swimmer) :
    def __init__(self,is_flyer,wing_size,is_swimming,fin_size):
        flyer.__init__(self,is_flyer,wing_size)
        swimmer.__init__(self,is_swimming,fin_size)
    def get_info(self):
        self.fly()
        self.swim()

duck1 = duck(True,20,True,20)
duck1.get_info()


