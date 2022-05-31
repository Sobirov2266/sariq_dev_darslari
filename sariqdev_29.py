class Talaba:
    def __init__(self, ismi, familyasi, tyil):
        self.ismi = ismi
        self.familyasi = familyasi
        self.tyil = tyil
        self.bosqich = 1


    def get_name(self):
        return self.ismi

    def get_lastname(self):
        return self.familyasi

    def get_age(self, yil):
        return yil - self.tyil

    def set_bosqich(self, bosqich):
        self.bosqich = bosqich

    def get_info(self):
        return f"Talabaning ismi: {self.ismi}, Talabaning familyasi: {self.familyasi}, bosqichi: {self.bosqich}"

    def update_bosqich(self):
        self.bosqich += 1

    def get_fullname(self):
        return f"{self.ism} {self.familiya}"

    def tanishtir(self):
        return f"Men: {self.ismi} {self.familyasi} . {self.bosqich} talabasi bo'laman. {self.tyil} da tug'ilganman"

# talaba1 = Talaba('Aziz', 'Sidiqjonov', 2002)
# talaba2 = Talaba('Laziz', 'Asadov', 1998)
# talaba3 = Talaba('Hamid', 'Sobirov', 2022)

class Fan:
    """Fan classi"""
    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []

    def add_student(self, talaba):
        """Fanga talabalar qo'shish"""
        self.talabalar.append((talaba))
        self.talabalar_soni += 1

    def get_name(self):
        return self.nomi

    def get_student(self):
        """Talabalar haqida ma'lumot"""
        return [talaba.get_fullname()  for talaba in self.talabalar]

    def get_student_num(self):
        return self.talabalar_soni



matematika = Fan("Oliy Matematika")
talaba1 = Talaba("Alijon", "Valiyev", 2000)
talaba2 = Talaba("Hasan", "Alimov", 2001)
talaba3 = Talaba("Akrom", "Boriyev", 2001)
matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)

print(matematika.talabalar_soni)
print(matematika.talabalar)
mat_talabalar = matematika.get_students()
print(mat_talabalar)

