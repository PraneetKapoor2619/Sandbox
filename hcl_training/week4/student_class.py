class student:
        """
                Class student
                Stores the name, GPA, clubs, active student/non-active student
        """

        def __init__(self, name):
                self.__name = name
                self.__GPA = float()
                self.__clubs = set()
                self.__status = True
                print("Student name: {:s} with active status has been instantiated.".format(self.__name))
        
        def get_name(self):
                return self.__name
        
        def get_GPA(self):
                return self.__GPA

        def get_clubs(self):
                return self.__clubs

        def get_status(self):
                return self.__status
        
        def get_all(self):
                return [self.get_name(), self.get_GPA(), self.get_clubs(), self.get_status()]

        def set_name(self, name):
                self.__name = name
        
        def set_GPA(self, GPA):
                self.__GPA = GPA

        def add_club(self, club):
                self.__clubs.add(club)

        def remove_club(self, club):
                self.__clubs.discard(club)
        
        def change_status(self):
                self.__status = not (self.__status)
                self.print_details()

        def print_details(self):
                print("\n" + "-"*50, "\nName: {:s}\nGPA: {:.1f}".format(self.__name, self.__GPA))
                print("Clubs: ", end = "")
                if (len(self.__clubs) == 0) : print("None", end = "")
                else :
                        for club in self.__clubs :
                                print(club, end = ", ")
                print("\nStatus: ", end = "")
                if (self.__status == True) :
                        print("Active")
                else :
                        print("Inactive")

marty = student("Marty McFly")
marty.set_GPA(3.8)
marty.change_status()
marty.add_club("Rock Band")
marty.add_club("Nuisance Creator")
marty.print_details()

record = marty.get_all()
record[0] = "Brad Pitt"
print(record)
marty.remove_club("Nuisance Creator")
marty.print_details()