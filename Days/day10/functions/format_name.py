def format_name(f_name, l_name):
    if f_name == '' or l_name == '':
        return "You didn't provide valid inputs."
    # print(f_name.title())
    # print(l_name.title())
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    # print(f"{formated_f_name} {formated_l_name}")
    return f"Result: {formated_f_name} {formated_l_name}"

formated_name = format_name("daniel", "DANIELS")
print(format_name)

output = len("Daniel")