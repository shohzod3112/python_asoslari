"""
28/01/2021

Dasturlash asoslari

#30-DARS. VORISLIK VA POLIMORFIZM

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""


class Shaxs:
    """Shaxslar haqida ma'lumot"""

    def __init__(self, ism, familiya, passport, tyil):
        """Shaxsning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil

    def get_name(self):
        return self.ism
    
    def get_fam(self):
        return self.familiya
    
    def get_passport(self):
        return self.passport

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info

    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil


class Talaba(Shaxs):
    """Talaba klassi"""

    def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
        self.fanlar=[]

    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam

    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich

    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info
    
    def fanga_yozil(self, nomi):
        self.fanlar.append(nomi)
    
    def get_list_of_science(self):
        return [i.get_name() for i in self.fanlar]
    
    def remove_fan(self, nomi):
        self.fanlar.remove(nomi)


class Manzil:
    """Manzil saqlash uchun klass"""

    def __init__(self, uy, kocha, tuman, viloyat):
        """Manzil xususiyatlari"""
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat

    def get_manzil(self):
        """Manzilni ko'rish"""
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
        manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
        return manzil
    
    def get_info(self):
        return f"Adress: {self.viloyat} viloyati, {self.tuman} tumani, {self.kocha} ko'chasi, {self.uy}-uy"
    

talaba1_manzil = Manzil(12, "Olmazor", "Bog'bon", "Samarqand")
professor1_manzil = Manzil(2, "Yashnobod", "iltifot", "Toshkent")

magistr_manzil = Manzil(1, "Rakat", "Mirobod", "Toshkent")
user1_manzil = Manzil(12, "Yashnar", "Mirishkor", "Qashqadaryo")
talaba1 = Talaba("Valijon", "Aliyev", "FA112299", 2000, "0000012", talaba1_manzil)


class Fan:
    """Fanlar ro'yxatini saqlash uchun"""
    
    def __init__(self, nomi):
        self.nomi = nomi
        
    def get_name(self):
        return self.nomi
    
matematika = Fan("Oliy Matematika")
fizika = Fan("fizika")
kimyo = Fan("kimyo")

talaba1.fanga_yozil(matematika)
talaba1.fanga_yozil(fizika)
        
        

class Professor(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, manzil, maqomi, himoya_yili):
        super().__init__(ism, familiya, passport, tyil)
        self.manzil = manzil
        self.maqomi = maqomi
        self.himoya_yili = himoya_yili
        
    def get_maqom(self):
        return self.maqomi
    
    def get_himoya(self):
        return self.himoya_yili
    
    def get_info(self):
        return (f"{self.ism}, maqomlari: {self.maqomi}, himoya qilgan yili: {self.himoya_yili}")

class Foydalanuvchi(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
        super().__init__(ism, familiya, passport, tyil)
        
        self.idraqam = idraqam
        self.manzil = manzil
        
        def get_idraqam(self):
            """Foydalanuvchining ID raqami"""
            return self.idraqam
        
        def get_info1(self):
            """Foydalanuvchi haqida ma'lumot"""
            return f"{self.ism} {self.familiya}. Manzil: {Shaxs.manzil.get_manzil()}. ID raqami: {self.idraqam}"

professor1 = Professor("Shoh", "Ro'ziyev", "AA1232132", 1992, professor1_manzil, "Akademik", 2002)


class Magistr(Talaba):
    def __init__(self, ism, familiya, passport, tyil, idraqam, manzil, talim_turi, shartnoma_turi):
        super().__init__(ism, familiya, passport, tyil, idraqam, manzil) 
        self.talim_turi = talim_turi
        self.shartnoma_turi = shartnoma_turi
    
    def get_talim_turi(self):
        return self.talim_turi
    
    def get_shartnoma_turi(self):
        return self.shartnoma_turi
    
    def get_info(self):
        return (f"{self.ism}, talim turi: {self.talim_turi}, shartnoma turi: {self.shartnoma_turi}")
    
magistr1 = Magistr("Munisaxon", "Dilmurodova", "AA1232322", 2019, 11, magistr_manzil, "Sirtqi", "Byudjet")
  
user1 = Foydalanuvchi("Hasan", "Husanov", "AA1232252", 2002, 454, user1_manzil)

class Admin(Foydalanuvchi):
    def __init__(self, ism, familiya, passport, tyil, idraqam, manzil, user):
        super().__init__(ism, familiya, passport, tyil, idraqam, manzil)
        self.user = user
        
    def ban_user(self):
        return (f"{self.ism} ismli {self.user} user bloklandi")
     
banuser = Admin("Asad", "Fasad", "AA343434", 2000, 55, user1_manzil, "oddiy")

# banuser.get_info() kiritilganda pastdagi javob chiqyapti. get_info metodi
# Admin clasida yoq shuni uchun ota class metodidan foydalanilyapti.
# Out[20]: 'Asad Fasad. Passport:AA343434, 2000-yilda tug`ilgan'