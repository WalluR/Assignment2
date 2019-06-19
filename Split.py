





def splitter_function(path):
    p_length = ""
    delimiter = "-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-"
    Final_list = []
    first_271 = ""
    break_index = 0
    with open(path + '/interface.txt', 'r') as file:




        interface_used = file.read().replace('\n', '')
        interface_used = interface_used.replace('Â', '')
        first_271 = interface_used[:len(delimiter)]
        old_interface_used = interface_used
        interface_used = interface_used.replace('¦', ' ')
        interface_used = interface_used.replace(' ', '')







        if first_271 == delimiter:
            i = 0
            interface_used = interface_used.replace('¦', ' ')
            while i < len(interface_used):
                if interface_used[i] != interface_used[i + 2]:
                    interface_used = interface_used.split()
                    break_index = i
                    break
                i += 1
            return(i,'One-Way')

        else:
            Result_as = old_interface_used.index(delimiter)
            return(Result_as,'Two-way')
















