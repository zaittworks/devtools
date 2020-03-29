def calculate_age(birth_date):

    '''
        Function calculates age of individual

        birth_date must be a dictionary with the following keys:
        year: Year of birth
        month: Month of birth
        day: Day of birth

        ie {'month': '5', 'day': '6', 'year': '1978'}

        Function outputs a dictionary with the following outputs:
        test: just the string 'test text' to check if all is well
        birth_date_day = birth_date['day']
        birth_date_month = birth_date['month']
        birth_date_year = birth_date['year']
        current_day = current_day
        current_month = current_month
        current_year = current_year
        output_age = output_age
        
    '''

    # parse today aka current date into day, month and year
    from datetime import date

    current_day = date.today().day
    current_month = date.today().month
    current_year = date.today().year

    output_age = 0
    
    # if today's month is after birth month => birthday passed, individual got older this current year
    if int(current_month) > int(birth_date['month']):
        output_age = int(current_year) - int(birth_date['year'])

    # if month of birth is right now in current month => age depends on the day we got
    elif int(current_month) == int(birth_date['month']):

    # is day of birth today or already passed => individual got older this year otherwise age is still that of last year
        if int(current_day) >= int(birth_date['day']):
            output_age = int(current_year) - int(birth_date['year'])
        else:
            output_age = int(current_year) - int(birth_date['year']) - 1

    # if month of birth is still in the future => individual has not gotten older this year
    else:
        output_age = int(current_year) - int(birth_date['year']) - 1


    function_outputs = dict()
    function_outputs['test'] = 'test text'
    function_outputs['birth_date_day'] = birth_date['day']
    function_outputs['birth_date_month'] = birth_date['month']
    function_outputs['birth_date_year'] = birth_date['year']
    function_outputs['current_day'] = current_day
    function_outputs['current_month'] = current_month
    function_outputs['current_year'] = current_year
    function_outputs['output_age'] = output_age
    
    return function_outputs


my_birth_date = dict()
my_birth_date = {'month': '3', 'day': '22', 'year': '1988'}

my_age = calculate_age(my_birth_date)
print(my_age['output_age'])
