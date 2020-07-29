from Inbuilt_list_methods_FDS_SE import *
class Student:
    def __init__(self,A,B,C):
        self.A=A
        self.B=B
        self.C=C
        #CRICKET
        while True:
            try:
                na = int(input("How many students play cricket?"))
                break
            except:
                print("Please provide a number!")
                continue
        for i in range(1,na+1):
            p = input(f"Enter the name of the {i} student who play cricket:").title()
            if (p in A):
                print("The name of the student is already there in the list")
            else:
                z=to_append_element_in_list(A,p)
        n_a=to_calculate_length_of_list(A)
        print(" \U0001F3CF"*9)
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        print(f"There are altogether {n_a} students in the second year computer engineering class who play cricket and their names are as given below...")
        for i in range(0,n_a):
            print(str(i+1)+"."+A[i])
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        print()

        #BADMINTON
        while True:
            try:
                nb= int(input("How many students play badminton?"))
                break
            except:
                print("Please provide a number!")
                continue
        for i in range(1,nb+1):
            p = input(f"Enter the name of the {i} student who play badminton:").title()
            if p in B:
                print("The name of the student is already there in the list")
            else:
                y=to_append_element_in_list(B,p)
        n_b=to_calculate_length_of_list(B)
        print(" \U0001F3F8 " * 9)
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        print(f"There are altogether {n_b} students in the second year computer engineering class who play badminton and their names are as given below...")
        for i in range(0,n_b):
            print(str(i+1)+"."+B[i])
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        print()

        #FOOTBALL
        while True:
            try:
                nc = int(input("How many students play football?"))
                break
            except:
                print("Please provide a number!")
                continue
        for i in range(1,nc+1):
            p = input(f"Enter the name of the {i} student who play football:").title()
            if p in C:
                print("The name of the student is already there in the list")
            else:
                x= to_append_element_in_list(C, p)
        n_c=to_calculate_length_of_list(C)
        print(" \U000026BD " * 9)
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        print(f"There are altogether {n_c} students in the second year computer engineering class who play football and their names are as given below...")
        for i in range(0,n_c):
            print(str(i+1)+"."+C[i])
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        print()

    #BOTH CRICKET AND BADMINTON
    def both_cri_bad(self,A,B):
        inter=to_calculate_intersection_between_two_sets(A,B) #inter is a list which containe the names of students who play both cricket and badminton
        length_of_inter=to_calculate_length_of_list(inter)
        print(("\U0001F3CF"+" and "+"\U0001F3F8")*9)
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        print(f"There are altogether {length_of_inter} students in the second year computer engineering class who play both cricket and badminton...")
        if (length_of_inter>0):
            print("Their names are as given below...")
            for i in range(0,length_of_inter):
                print(str(i+1)+"."+inter[i])
        else:
            print("There are no students in the college who play both cricket and badminton...")
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        print()

    #CRICKET OR BADMINTON BUT NOT BOTH
    def cri_or_bad_but_not_both(self,a,b):
        symmetric_difference_of_a_b=to_calculate_symmetric_difference(a,b)
        length_of_symmetric_diff=to_calculate_length_of_list(symmetric_difference_of_a_b)
        print(("\U0001F3CF" + " or " + "\U0001F3F8") * 9)
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        print(f"There are altogether {length_of_symmetric_diff} students in the second year computer engineering class who play cricket or badminton but not both")
        if (length_of_symmetric_diff>0):
            for i in range(0, length_of_symmetric_diff):
                print(str(i + 1) + "." + symmetric_difference_of_a_b[i])
        else:
            print("There are no students in the second in the second year computer engineering class who play either cricket or badminton but not both")
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        print()

    #WHO PLAY NEITHER CRICKET NOR BADMINTON
    def neither_cri_nor_bad(self,a,b,c):
        union_of_cri_bad=to_calculate_union(a,b)
        l_n=[]
        for i in c:
            if i in union_of_cri_bad:
                pass
            else:
                l_n.append(i)
        length_of_l_n=to_calculate_length_of_list(l_n)
        print(("neither \U0001F3CF" + " nor " + "\U0001F3F8") * 9)
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        print(f"There are altogether {length_of_l_n} students in the second year computer engineering class who play neither cricket nor badminton")
        if (length_of_l_n > 0):
            for i in range(0, length_of_l_n):
                print(str(i + 1) + "." + l_n[i])
        else:
            print("There are no students in the second in the second year computer engineering class who play either cricket or badminton but not both")
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        print()

    #WHO PLAY CRICKET AND FOOTBALL BUT NOT BADMINTON
    def cri_n_foot_but_not_bad(self,a,b,c):
        cri_foot=to_calculate_intersection_between_two_sets(a,b)
        for i in cri_foot:
            if i in c:
                cri_foot.remove(i)
            else:
                pass
        length_of_cri_foot=to_calculate_length_of_list(cri_foot)
        print(("\U0001F3CF and \U000026BD but not \U0001F3F8") * 9)
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        print(f"There are altogether {length_of_cri_foot} students in the second year computer engineering class who play cricket and football but not badminton")
        if (length_of_cri_foot > 0):
            for i in range(0, length_of_cri_foot):
                print(str(i + 1) + "." + cri_foot[i])
        else:
            print("There are no students in the second in the second year computer engineering class who play cricket and football but not badminton")
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        print()

A=[];B=[];C=[]
s=Student(A,B,C)
s.both_cri_bad(s.A,s.B)
s.cri_or_bad_but_not_both(s.A,s.B)
s.neither_cri_nor_bad(s.A,s.B,s.C)
s.cri_n_foot_but_not_bad(s.A,s.C,s.B)
