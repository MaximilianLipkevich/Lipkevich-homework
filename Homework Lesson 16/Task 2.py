class Mathematician:
    def square_nums(self, num_list):
        squared_list = []
        for num in num_list:
            squared_list.append(num*num)
        return squared_list

    def remove_positives(self, num_list):
        negatives_list = []
        for num in num_list:
            if num < 0:
                negatives_list.append(num)
        return negatives_list

    def filter_leaps(self, years_list):
        leap_years = []
        for year in years_list:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                leap_years.append(year)
        return leap_years

m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]

assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]

assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]