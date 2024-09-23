import copy

end_loop = False


class Matrix():
    def __init__(self, contents):
        self.contents = contents
        self.n = len(self.contents)
        self.poss = []
        self.poss_list = []
        self.comb_minor_list = []
        self.matrix_list = []

    def print_det(self):
        print("")
        for i in self.contents:
            print(i)
        print("")

    def duplic(self):
        duplicate_matrix = []
        for i in self.contents:
            duplicate_matrix.append(i)
        return duplicate_matrix

    def minor_map(self, address):
        selected_matrix = copy.deepcopy(self.contents)
        for i in address:
            minor([0, i], selected_matrix)
        return selected_matrix

    def determinate(self):
        # poss = []
        for i in range(0, self.n - 1):
            self.poss.append(0)
        # poss_list = []
        while not end_loop:
            poss2 = self.poss.copy()
            self.poss_list.append(poss2)
            self.poss[self.n - 2] += 1
            index_fix(self.poss, self.n)

        # comb_minor_list = []
        for j in self.poss_list:
            self.comb_minor_list.append(self.minor_map(j)[0][0])

        # Level denotes where in the branches diagram you are rn
        # Level n means you're currently solving all the possible nxn determinents
        # Currently you are at level 1 since comb_minor_list contains all the 1x1 determinants

        level = 1
        self.matrix_list = copy.deepcopy(self.poss_list)
        while len(self.comb_minor_list) > 1:
            level += 1
            for i in self.matrix_list:
                i.pop()
            self.comb_minor_list = group(self.comb_minor_list, level)
            clear_repeats(self.matrix_list)
            for i in enumerate(self.matrix_list):
                self.comb_minor_list[i[0]] = compute(i[0] , self)
            print("list" , self.comb_minor_list)
        print("final list", self.comb_minor_list)
        return self.comb_minor_list[0]

# type
determ = Matrix([
    [2, 3, 2],
    [3, 7, 1],
    [5, 4, 2]
])


def minor(major, arr):
    row = major[0]
    column = major[1]
    del arr[row]
    for i in arr:
        del i[column]
    return arr


def splice(arr, section):
    temp_arr = []
    for i in range(section[0], section[1]):
        temp_arr.append(arr[i])
    return temp_arr


def group(arr, n):
    new = []
    index_count = 0
    while not index_count >= len(arr):
        grp = []
        for i in splice(arr, [index_count, index_count + n]):
            grp.append(i)
        new.append(grp)
        index_count += n
    return new


# Master algorithm
def compute(index_address, current_matrix):
    matrix = current_matrix.minor_map(current_matrix.matrix_list[index_address])
    minor_list = current_matrix.comb_minor_list[index_address]
    computation = 0
    p = enumerate(minor_list)
    for i in p:
        term = ((-1) ** i[0]) * (matrix[0][i[0]]) * (i[1])
        computation += term
    return computation


# This part's for the inital one by one determinant list
def index_fix(poss, n):
    base = 2
    index_count = n - 2
    while index_count > 0:
        if index_count == 0 and poss[0] > n - 1:
            break
        elif poss[index_count] > (base - 1):
            poss[index_count - 1] += int(poss[index_count] / base)
            poss[index_count] = poss[index_count] - base
        index_count -= 1
        base += 1
    if poss[0] > n - 1:
        poss[0] = n - 1
        global end_loop
        end_loop = True
    else:
        end_loop = False


def clear_repeats(arr):
    index_count_i = 0
    for i in arr:
        index_count_j = index_count_i + 1
        for j in arr[index_count_i + 1:]:
            if i == j and not index_count_i == index_count_j:
                # print("removing ", j)
                arr.remove(j)
            index_count_j += 1
        index_count_i += 1


def distinction_check(arr):
    distinction = True
    temp_arr = arr.copy()
    for i in temp_arr:
        temp_arr.remove(i)
        for j in temp_arr:
            if i == j:
                print(i, j)
                distinction = False
                break
    if distinction:
        return True
    else:
        return False


# Input your coefficients in this, row by row, as such:
# a1 b1 c1 d1..... D1   Where a,b,c... are coeff of x,y,z..... and D is the value of the eqn
# eg 2x+3y = 5 would be input as:  [2 , 3, 5]
coefficients_list = [
    [2,3,5,12],
    [3,6,4,10],
    [6,7,3,15]
]
main_contents = copy.deepcopy(coefficients_list)
for i in main_contents:
    i.pop()

RHS_values = []
for i in coefficients_list:
    RHS_values.append(i[-1])
print(RHS_values)

#index_count = 0
#for i in D_contents:
#    for j in enumerate(i):
#        i[j[0]] = [j[1] , RHS_values[index_count]]
#    index_count += 1

#print(D_contents)/
# Now the actual solving logic begins

D_main = Matrix(main_contents)
#D_value = D_main.determinate()

'''
print(main_contents)
ans_list = []
D = Matrix([[13, 3, 5], [14, 6, 4], [15, 7, 3]])
print(D.contents)
print(" d " , determ.determinate())
for i in range(0 , len(coefficients_list)):
    alteration = main_contents.copy()
    for j in alteration:
        j[i] = RHS_values[i]
    D = Matrix(alteration)



matrix_to_solve = []
'''


# input any nxn determinant
determ = Matrix([
    [1,4,23,2,3],
    [8,5,2,2,2],
    [10,6,4,7,4],
    [13,14,32,8,9],
    [2,1,1,3,4]
])

print("The det is " + str(determ.determinate()))