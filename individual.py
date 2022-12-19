class Individual:
    _n = 0
    
    def __init__(self, genotype, name=None):
        self.__genotype = Individual.validate_genotype(genotype)
        self.__name = Individual.__genarate_name(name)


    def __genarate_name(name):
        if name is None:
            Individual._n += 1
            return "Indiv" + str(Individual._n)
        return name


    def validate_genotype(genotype):
        if genotype not in ["AA","Ai","BB","Bi","AB","ii"]:
            raise ValueError("Genotype invalid.")
        return genotype


    def __repr__(self):
        return "Individual(%s)" %(self.__genotype)


    def __str__(self):
        return self.__genotype


    @property
    def name(self):
        return self.__name


    @property
    def genotype(self):
        return self.__genotype


    @property
    def blood_type(self):
        if self.genotype == "AA" or self.genotype == "Ai":
            return "A"
        if self.genotype == "BB" or self.genotype == "Bi":
            return "B"
        if self.genotype == "AB":
            return "AB"
        if self.genotype == "ii":
            return "O"


    @property
    def agglutinogens(self):
        if self.blood_type == "AB":
            return "A,B"
        elif self.blood_type == "O":
            return "None"
        elif self.blood_type == "A":
            return "A"
        else:
            return "B"


    @property
    def agglutinins(self):
        if self.blood_type == "AB":
            return "None"
        elif self.blood_type == "O":
            return "A,B"
        elif self.blood_type == "A":
            return "B"
        else:
            return "A"


    def conversion(arg):
        if isinstance(arg, str):
            return Individual(arg)
        elif isinstance(arg, Individual):
            return arg
        else:
            raise TypeError("Argument of method is invalid.")


    def offsprings_genotypes(self, other):
        other = Individual.conversion(other)
        set_genotypes = []
        
        for i in self.genotype:
            for j in other.genotype:
                if (i == "A" and j == "B") or (i == "B" and j == "A"):
                    set_genotypes.append("AB")
                elif (i == "i" and j == "A") or (i == "A" and j == "i"):
                    set_genotypes.append("Ai")
                elif (i == "i" and j == "B") or (i == "B" and j == "i"):
                    set_genotypes.append("Bi")
                else:
                    set_genotypes.append(i + j)
        return set(set_genotypes)


    def offsprings_blood_types(self, other):
        other = Individual.conversion(other)
        set_blood_types = []
        
        for i in self.offsprings_genotypes(other):
            if i == "AB":
                set_blood_types.append("AB")
            elif i == "AA" or i == "Ai":
                set_blood_types.append("A")
            elif i == "BB" or i == "Bi":
                set_blood_types.append("B")
            else:
                set_blood_types.append("O")
        return set(set_blood_types)


    def blood_transfusion(self, donator, receptor):
        donator = Individual.conversion(donator)
        receptor = Individual.conversion(receptor)
        
        if donator.blood_type == "O" or receptor.blood_type == "AB":
            return True
        elif donator.blood_type == receptor.blood_type:
            return True
        else:
            return False


    def can_donate(self, other):
        return self.blood_transfusion(self, other)


    def can_receive(self, other):
        return self.blood_transfusion(other, self)

