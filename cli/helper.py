def get_valid_input(input_type, valid_options = []):
    while(True):
        new_input = input(":: ")

        try:
            new_input = input_type(new_input)
        except:
            print("Input must be of type " + input_type.__name__)
            continue


        if(not valid_options or new_input in valid_options):
            return new_input
        elif valid_options and new_input not in valid_options:
            print("Input must one of the following options " + ", ".join(map(str, valid_options)))
            #continue
        else:
            print("Something went wrong, please try again")