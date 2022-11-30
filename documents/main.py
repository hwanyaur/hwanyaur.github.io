# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd

tutor_initial_csv = pd.read_csv('/Users/hwanyaur/Desktop/Tutor_Time_Submission_Form2021-10-27_21_30_25.csv')
student_initial_csv = pd.read_csv('/Users/hwanyaur/Desktop/Student_Time_Submission_Form2021-10-27_21_30_25.csv')
#test['Mon'].split('\n')#.splitlines()

# ----------------
def initial_table(test):
    """
    Creating initial table with times available on all days, name, email, and last update date.
    :param test: The table from the form that tutors fill out
    :return: fin_table with table in the form of 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
    'Friday', 'Saturday', 'Sunday' and tutor information as well as lists (name_list, email_list, last_updated_date)
    """
    dict = {}
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    time_slot = ['1', '2', '3', '4', '5']
    error = []
    for d in range(0, len(days)):
        dict[days[d]] = []
    name_list = []
    email_list = []
    last_updated_date = []
    language_list = []
    interest_list = []
    submission_date = []
    for i in range(0, len(test)):
        name_list.append(test["Your First + Last Name"][i])
        email_list.append(test["Your Email"][i])
        last_updated_date.append(test["Last Update Date"][i])
        language_list.append(test["Language"][i])
        interest_list.append(test["Interest"][i])
        submission_date.append(test["Submission Date"][i])
        Monday = []
        Tuesday = []
        Wednesday = []
        Thursday = []
        Friday = []
        Saturday = []
        Sunday = []
        for d in range(0, len(days)):
            for nn in range(1, 6):
                if test[f"{days[d]} Time {nn}"][i] != 'PM\nPM' and pd.isna(test[f"{days[d]} Time {nn}"][i]) == False:
                    if test[f"{days[d]} Time {nn}"][i][
                       22:23] == ':':  # test['Monday Time 2'][0] '08:00 PM - 09:00 PM (1:00)'
                        if d == 0:
                            Monday.append(test[f"{days[d]} Time {nn}"][i][:-7])
                        elif d == 1:
                            Tuesday.append(test[f"{days[d]} Time {nn}"][i][:-7])
                        elif d == 2:
                            Wednesday.append(test[f"{days[d]} Time {nn}"][i][:-7])
                        elif d == 3:
                            Thursday.append(test[f"{days[d]} Time {nn}"][i][:-7])
                        elif d == 4:
                            Friday.append(test[f"{days[d]} Time {nn}"][i][:-7])
                        elif d == 5:
                            Saturday.append(test[f"{days[d]} Time {nn}"][i][:-7])
                        elif d == 6:
                            Sunday.append(test[f"{days[d]} Time {nn}"][i][:-7])
                    else:
                        error.append(test["Your First + Last Name"][i])

        dict['Monday'].append(Monday)
        dict['Tuesday'].append(Tuesday)
        dict['Wednesday'].append(Wednesday)
        dict['Thursday'].append(Thursday)
        dict['Friday'].append(Friday)
        dict['Saturday'].append(Saturday)
        dict['Sunday'].append(Sunday)

    fin_table = pd.DataFrame(dict)
    fin_table.insert(0, 'Name', name_list)
    fin_table.insert(1, 'Email', email_list)
    fin_table.insert(2, 'Last Update Date', last_updated_date)
    fin_table.insert(3, 'Language', language_list)
    fin_table.insert(4, 'Interest', interest_list)
    fin_table.insert(5, 'Submission Date', submission_date)
    print('The time submission form contains error...')
    print(error)

    return fin_table, name_list, email_list, last_updated_date,language_list,interest_list, submission_date, error

def vectorize_table(fin_table, name_list, email_list, last_updated_date, language_list,interest_list, submission_date):
    """
    Creating vector for comparison
    :param fin_table: Table from initialization
    :return: the table with time in vector form
    """
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    dict_comparison = {}
    for d in range(0, len(days)):
        dict_comparison[days[d]] = []

    for i in range(0, len(fin_table)):
        for j in range(0, len(days)):
            temp_vector = []
            for k in range(0, len(fin_table[days[j]][i])):
                if fin_table[days[j]][i][k][6:8] == 'PM' and fin_table[days[j]][i][k][17:19] == 'PM':
                    if fin_table[days[j]][i][k][0:2] != '12':
                        start_hour = int(
                            fin_table[days[j]][i][k][0:2]) + 12  # fin_table[days[j]][i][k][0:2] #Start Time Hour
                    else:
                        start_hour = int(fin_table[days[j]][i][k][0:2])

                    if fin_table[days[j]][i][k][11:13] != '12':
                        end_hour = int(
                            fin_table[days[j]][i][k][11: 13]) + 12  # fin_table[days[j]][i][k][11: 13] #End Time Hour
                    else:
                        end_hour = int(fin_table[days[j]][i][k][11:13])

                elif fin_table[days[j]][i][k][6:8] == 'AM' and fin_table[days[j]][i][k][17:19] == 'AM':
                    start_hour = int(fin_table[days[j]][i][k][0:2])
                    end_hour = int(fin_table[days[j]][i][k][11: 13])
                elif fin_table[days[j]][i][k][6:8] == 'AM' and fin_table[days[j]][i][k][17:19] == 'PM':
                    start_hour = int(fin_table[days[j]][i][k][0:2])
                    if fin_table[days[j]][i][k][11:13] != '12':
                        end_hour = int(
                            fin_table[days[j]][i][k][11: 13]) + 12  # fin_table[days[j]][i][k][11: 13] #End Time Hour
                    else:
                        end_hour = int(fin_table[days[j]][i][k][11:13])

                start_minutes = int(fin_table[days[j]][i][k][3:5]) / 60  # Start Time Minutes
                end_minutes = int(fin_table[days[j]][i][k][14: 16]) / 60  # End Time Minutes
                start_time = start_hour + start_minutes
                end_time = end_hour + end_minutes
                temp_vector.append([start_time, end_time])
            if len(fin_table[days[j]][i]) == 0:
                dict_comparison[days[j]].append([0, 0])
            else:
                dict_comparison[days[j]].append(temp_vector)

    comparison_table = pd.DataFrame(dict_comparison)
    comparison_table.insert(0, 'Name', name_list)
    comparison_table.insert(1, 'Email', email_list)
    comparison_table.insert(2, 'Last Update Date', last_updated_date)
    comparison_table.insert(3, 'Language', language_list)
    comparison_table.insert(4, 'Interest', interest_list)
    comparison_table.insert(5, 'Submission Date', submission_date)
    return comparison_table

def comparison(tutor,student):
    '''
    :param tutor: the vectorized tutor table
    :param student: the vecotrized student table
    :return: the df with rating, student name, tutor name, student email, and tutor email
    '''
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    rating_list = []
    tutor_list = []
    student_list = []
    Monday = []
    Tuesday = []
    Wednesday = []
    Thursday = []
    Friday = []
    Saturday = []
    Sunday = []
    tutor_email = []
    student_email = []
    tutor_language = []
    student_language = []
    tutor_interst = []
    student_interest = []
    for j in range(0, len(student)):
        for l in range(0,len(tutor)):
            rating = 0
            for k in range(0, len(days)):
                temp_vector = []
                for m in range(0, len(tutor[days[k]][l])):
                    for n in range(0, len(student[days[k]][j])):
                        if student[days[k]][j]!=[0,0] and tutor[days[k]][l]!=[0,0]:
                            tutor_start = tutor[days[k]][l][m][0]
                            tutor_end = tutor[days[k]][l][m][1]
                            student_start = student[days[k]][j][n][0]
                            student_end = student[days[k]][j][n][1]
                            if (tutor_start == student_end) or (student_start < tutor_start and student_end < tutor_end) or (student_start > tutor_start and student_end > tutor_end) or ((tutor_start > student_end) and (student_end - tutor_start) < 1) or ((student_start > tutor_end) and (tutor_end - student_start) < 1):
                                rating += 0
                            else:
                                rating += 1

                                if tutor_start <= student_start:
                                    record_start_time = student_start
                                else:
                                    record_start_time = tutor_start

                                if tutor_end <= student_end:
                                    record_end_time = tutor_end
                                else:
                                    record_end_time = student_end
                                temp_vector.append([record_start_time, record_end_time])

                if k == 0:
                    Monday.append(temp_vector)
                elif k == 1:
                    Tuesday.append(temp_vector)
                elif k == 2:
                    Wednesday.append(temp_vector)
                elif k == 3:
                    Thursday.append(temp_vector)
                elif k == 4:
                    Friday.append(temp_vector)
                elif k == 5:
                    Saturday.append(temp_vector)
                elif k == 6:
                    Sunday.append(temp_vector)
            rating_list.append(rating)
            tutor_list.append(tutor['Name'][l])
            student_list.append(student['Name'][j])
            tutor_email.append(tutor['Email'][l])
            student_email.append(student['Email'][j])
            tutor_language.append(tutor['Language'][l])
            student_language.append(student['Language'][j])
            tutor_interst.append(tutor['Interest'][l])
            student_interest.append(student['Interest'][j])
    d = {'Student Name': student_list, 'Tutor Name': tutor_list, 'Tutor Language': tutor_language, 'Student Language': student_language,
        'Tutor Interest':tutor_interst,'Student Interest':student_interest,'Rating': rating_list,'Monday':Monday, 'Tuesday':Tuesday,
        'Wednesday':Wednesday, 'Thursday':Thursday, 'Friday':Friday, 'Saturday':Saturday, 'Sunday':Sunday,
        'Student Email':student_email, 'Tutor Email':tutor_email}
    df = pd.DataFrame(data=d)

    return df

def check(df,student_name_list):
    #Step 0: Make sure all students have pairing
    need_to_ask_for_availability = []
    for s in range(0,len(student_name_list)):
        student_df = df[df["Student Name"].isin([student_name_list[s]])]
        if sum(student_df['Rating']) == 0:
            need_to_ask_for_availability.append(student_name_list[s])
    return need_to_ask_for_availability

def unique(list):
    unique_list = []
    for x in list:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

def match(df):
    # Step 1: Make sure student with ELL needs match with tutor who speak that - first round of pairing
    # 1.1 select the language student
    language_students = df[df["Student Language"] != 'English']
    language_students = language_students[language_students["Student Language"] == language_students["Tutor Language"]]
    # Selecting necessary list
    language_need_student_list = unique(list(language_students['Student Name']))
    language_list = unique(list(language_students['Student Language']))
    ranking_total = []
    for ln in range(0, len(language_need_student_list)):
        language_student = language_students[language_students["Student Name"].isin([language_need_student_list[ln]])]
        total = sum(language_student['Rating'])
        unique_language = unique(list(language_student['Student Language']))
        total_vector = [total] * len(language_student)  # Adjusting vector length
        if len(ranking_total) == 0:
            ranking_total = total_vector
        else:
            ranking_total = ranking_total + total_vector

    language_students.insert(0, 'Ranking Total', ranking_total)
    language_students = language_students[language_students["Rating"] != 0]

    # Keep in mind this table only contains the population with language tutors
    # If no pairing is made in this step, it's fine

    # Initializing the vectors
    paired_tutor = []
    paired_student = []
    paired_language = []
    paired_tutor_email = []
    paired_student_email = []
    unpaired_student = []
    unpaired_student_lan = []
    Monday_time = []
    Tuesday_time = []
    Wednesday_time = []
    Thursday_time = []
    Friday_time = []
    Saturday_time = []
    Sunday_time = []
    tutor_interest_fin = []
    student_interest_fin = []

    #ELL Pairing Block
    for lan in range(0, len(language_list)):
        one_language_students = language_students[language_students["Student Language"].isin([language_list[lan]])]
        one_language_students['Order'] = one_language_students['Ranking Total'].rank(method='dense', ascending=True)
        one_language_students = one_language_students.sort_values(by=['Order'], ascending=True)
        unique_student_list = unique(list(one_language_students['Student Name']))
        print(f"The number of {language_list[lan]} Tutor: {len(unique(list(one_language_students['Tutor Name'])))}")
        print(f"The number of {language_list[lan]} Student: {len(unique_student_list)}")
        for ol in range(0, len(unique_student_list)):
            if len(one_language_students) != 0:
                new_unique_student_list = unique(list(one_language_students['Student Name']))
                if unique_student_list[ol] in new_unique_student_list:
                    to_be_paired = one_language_students[
                        one_language_students["Student Name"].isin([unique_student_list[ol]])]
                    to_be_paired['Order_Rating'] = to_be_paired['Rating'].rank(method='dense', ascending=False)
                    to_be_paired = to_be_paired.sort_values(by=['Order_Rating'], ascending=True)
                    to_be_paired = to_be_paired.reset_index(drop=True)
                    tutor_pair = to_be_paired['Tutor Name'][0]
                    Monday_time.append(to_be_paired['Monday'][0])
                    Tuesday_time.append(to_be_paired['Tuesday'][0])
                    Wednesday_time.append(to_be_paired['Wednesday'][0])
                    Thursday_time.append(to_be_paired['Thursday'][0])
                    Friday_time.append(to_be_paired['Friday'][0])
                    Saturday_time.append(to_be_paired['Saturday'][0])
                    Sunday_time.append(to_be_paired['Sunday'][0])
                    tutor_email_i = to_be_paired['Tutor Email'][0]
                    tutor_interest_i = to_be_paired['Tutor Interest'][0]
                    student_interest_i = to_be_paired['Student Interest'][0]
                    # Delete the paired information out of the complete table
                    new_one_language_students = one_language_students[
                        ~one_language_students["Student Name"].isin([unique_student_list[ol]])]
                    new_one_language_students = new_one_language_students[
                        ~new_one_language_students["Tutor Name"].isin([tutor_pair])]
                    # Use these two vectors to move the students/tutors from the entire population table
                    paired_tutor.append(tutor_pair)
                    paired_student.append(unique_student_list[ol])
                    # Additional vectors for final table
                    tutor_interest_fin.append(tutor_interest_i)
                    student_interest_fin.append(student_interest_i)
                    paired_language.append(language_list[lan])
                    paired_tutor_email.append(to_be_paired['Student Email'][0])
                    paired_student_email.append(tutor_email_i)
                    # Updating the table
                    one_language_students = new_one_language_students
                else:
                    unpaired_student.append(unique_student_list[ol])
                    unpaired_student_lan.append(language_list[lan])
            else:
                unpaired_student.append(unique_student_list[ol])
                unpaired_student_lan.append(language_list[lan])

    ELL_d = {'Student': paired_student, 'Tutor': paired_tutor, 'Language': paired_language,'Student Interest':student_interest_fin,
                'Tutor Interest': tutor_interest_fin,
             'Student Email': paired_student_email, 'Tutor Email': paired_tutor_email,
             'Monday': Monday_time, 'Tuesday': Tuesday_time, 'Wednesday': Thursday_time, 'Thursday': Wednesday_time,
             'Friday': Friday_time, 'Saturday': Saturday_time, 'Sunday': Sunday_time}

    ELL_df = pd.DataFrame(data=ELL_d)

    ELL_Unpaired = {'Student': unpaired_student, 'Language': unpaired_student_lan}
    ELL_Unpaired_df = pd.DataFrame(data=ELL_Unpaired)

    # Step 2: Remove those student from step 1 in both df and the student name list
    removed_df = df[~df["Student Name"].isin(paired_student)]
    removed_df = removed_df[~removed_df["Tutor Name"].isin(paired_tutor)]
    removed_df = removed_df[removed_df["Rating"] != 0]
    distinct_list_of_student = unique(list(removed_df["Student Name"]))
    removed_df2 = removed_df
    # Initializing vectors
    Monday_time = []
    Tuesday_time = []
    Wednesday_time = []
    Thursday_time = []
    Friday_time = []
    Saturday_time = []
    Sunday_time = []
    unpaired_student = []
    unpaired_student_lan = []
    paired_tutor = []
    paired_student = []
    paired_language = []
    paired_student_email = []
    paired_tutor_email = []
    tutor_interest_fin = []
    student_interest_fin = []

    ranking_total = []
    for ln in range(0, len(distinct_list_of_student)):
        removed_df_student = removed_df[removed_df["Student Name"].isin([distinct_list_of_student[ln]])]
        total = sum(removed_df_student['Rating'])
        total_vector = [total] * len(removed_df_student)  # Adjusting vector length
        if len(ranking_total) == 0:
            ranking_total = total_vector
        else:
            ranking_total = ranking_total + total_vector

    removed_df.insert(0, 'Ranking Total', ranking_total)

    # 1.Making sure all student has pairing, student with lower rankings will be ranked first
    for k in range(0, len(distinct_list_of_student)):
        removed_df['Order'] = removed_df['Ranking Total'].rank(method='dense', ascending=True)
        if len(removed_df) != 0:
            new_distinct_list_of_student = unique(list(removed_df["Student Name"]))
            if distinct_list_of_student[k] in new_distinct_list_of_student:
                # Selecting one student
                to_be_paired = removed_df[removed_df["Student Name"].isin([distinct_list_of_student[k]])]
                to_be_paired['Order_Rating'] = to_be_paired['Rating'].rank(method='dense', ascending=False)
                to_be_paired = to_be_paired.sort_values(by=['Order_Rating'], ascending=True)
                to_be_paired = to_be_paired.reset_index(drop=True)

                for r in range(0,len(to_be_paired)):
                    tutor_pair = to_be_paired['Tutor Name'][r]
                    tutor_email_i = to_be_paired['Tutor Email'][r]
                    tutor_interest_i = to_be_paired['Tutor Interest'][r]
                    student_interest_i = to_be_paired['Student Interest'][r]

                    # Delete the paired information out of the complete table
                    new_removed_df = removed_df[~removed_df["Student Name"].isin([distinct_list_of_student[k]])]
                    new_removed_df = new_removed_df.reset_index(drop=True)
                    # If repairing all the rating of the previous one, and still cannot ensure everyone is paired, keep the current pairing
                    check_reduction = []
                    for n in range(0,len(new_removed_df)):
                        if new_removed_df['Tutor Name'][n] == tutor_pair:
                            check_reduction.append(new_removed_df['Ranking Total'][n] - new_removed_df['Rating'][n])

                    if (0 not in check_reduction):
                        new_removed_df = new_removed_df[~new_removed_df["Tutor Name"].isin([tutor_pair])]
                        Monday_time.append(to_be_paired['Monday'][r])
                        Tuesday_time.append(to_be_paired['Tuesday'][r])
                        Wednesday_time.append(to_be_paired['Wednesday'][r])
                        Thursday_time.append(to_be_paired['Thursday'][r])
                        Friday_time.append(to_be_paired['Friday'][r])
                        Saturday_time.append(to_be_paired['Saturday'][r])
                        Sunday_time.append(to_be_paired['Sunday'][r])

                        # Use these two vectors to move the students/tutors from the entire population table
                        paired_tutor.append(tutor_pair)
                        paired_student.append(distinct_list_of_student[k])
                        # Additional vectors for final table
                        paired_language.append('English')
                        paired_tutor_email.append(to_be_paired['Student Email'][0])
                        paired_student_email.append(tutor_email_i)
                        tutor_interest_fin.append(tutor_interest_i)
                        student_interest_fin.append(student_interest_i)
                        # Updating the table
                        removed_df = new_removed_df
                    elif (0 in check_reduction) and r==(len(to_be_paired)-1):
                        tutor_pair = to_be_paired['Tutor Name'][0]
                        Monday_time.append(to_be_paired['Monday'][0])
                        Tuesday_time.append(to_be_paired['Tuesday'][0])
                        Wednesday_time.append(to_be_paired['Wednesday'][0])
                        Thursday_time.append(to_be_paired['Thursday'][0])
                        Friday_time.append(to_be_paired['Friday'][0])
                        Saturday_time.append(to_be_paired['Saturday'][0])
                        Sunday_time.append(to_be_paired['Sunday'][0])
                        tutor_email_i = to_be_paired['Tutor Email'][0]
                        new_removed_df = new_removed_df[~new_removed_df["Tutor Name"].isin([tutor_pair])]
                        # Use these two vectors to move the students/tutors from the entire population table
                        paired_tutor.append(tutor_pair)
                        paired_student.append(distinct_list_of_student[k])
                        # Additional vectors for final table
                        paired_language.append('English')
                        paired_tutor_email.append(to_be_paired['Student Email'][0])
                        paired_student_email.append(tutor_email_i)
                        tutor_interest_fin.append(tutor_interest_i)
                        student_interest_fin.append(student_interest_i)
                        # Updating the table
                        removed_df = new_removed_df
            else:
                unpaired_student.append(distinct_list_of_student[k])
                unpaired_student_lan.append('English')
        else:
            unpaired_student.append(distinct_list_of_student[k])
            unpaired_student_lan.append('English')

    Unpaired2 = {'Student': unpaired_student, 'Language': unpaired_student_lan}
    Unpaired_df2 = pd.DataFrame(data=Unpaired2)

    Paired_d = {'Student': paired_student, 'Tutor': paired_tutor, 'Language': paired_language, 'Student Interest':student_interest_fin,
                'Tutor Interest': tutor_interest_fin, 'Student Email': paired_student_email, 'Tutor Email': paired_tutor_email,
                'Monday': Monday_time, 'Tuesday': Tuesday_time, 'Wednesday': Thursday_time, 'Thursday': Wednesday_time,
                'Friday': Friday_time, 'Saturday': Saturday_time, 'Sunday': Sunday_time}

    Paired_df = pd.DataFrame(data=Paired_d)

    return language_list, language_students, distinct_list_of_student, removed_df2, ELL_df, ELL_Unpaired_df, Paired_df, Unpaired_df2

def other_option(language_list, language_students, distinct_list_of_student, removed_df2):
    STUDENT = []
    LANGUAGE = []
    other_option = []

    for lan in range(0, len(language_list)):
        one_language_students = language_students[language_students["Student Language"].isin([language_list[lan]])]
        one_language_students['Order'] = one_language_students['Ranking Total'].rank(method='dense', ascending=True)
        one_language_students = one_language_students.sort_values(by=['Order'], ascending=True)
        unique_student_list = unique(list(one_language_students['Student Name']))
        for ol in range(0, len(unique_student_list)):
            indiv_student = one_language_students[one_language_students["Student Name"].isin([unique_student_list[ol]])]
            indiv_student = indiv_student.reset_index(drop=True)
            indiv_option = []
            STUDENT.append(unique_student_list[ol])
            LANGUAGE.append(language_list[lan])
            for indiv in range(0, len(indiv_student)):
                indiv_option.append(indiv_student['Tutor Name'][indiv])
            other_option.append(indiv_option)

    for k in range(0, len(distinct_list_of_student)):
        removed_df2['Order'] = removed_df2['Ranking Total'].rank(method='dense', ascending=True)
        indiv_student = removed_df2[removed_df2["Student Name"].isin([distinct_list_of_student[k]])]
        indiv_student = indiv_student.reset_index(drop=True)
        indiv_option = []
        STUDENT.append(distinct_list_of_student[k])
        LANGUAGE.append('English')
        for indiv in range(0, len(indiv_student)):
            indiv_option.append(indiv_student['Tutor Name'][indiv])
        other_option.append(indiv_option)

    Other_option_d = {'Student': STUDENT, 'Language': LANGUAGE, 'Other Option': other_option}

    Other_option_df = pd.DataFrame(data=Other_option_d)

    return Other_option_df

def match_with_interest(df):
    # Step 1: Make sure student with ELL needs match with tutor who speak that - first round of pairing
    # 1.1 select the language student
    language_students = df[df["Student Language"] != 'English']
    language_students = language_students[language_students["Student Language"] == language_students["Tutor Language"]]
    # Selecting necessary list
    language_need_student_list = unique(list(language_students['Student Name']))
    language_list = unique(list(language_students['Student Language']))
    ranking_total = []
    for ln in range(0, len(language_need_student_list)):
        language_student = language_students[language_students["Student Name"].isin([language_need_student_list[ln]])]
        total = sum(language_student['Rating'])
        unique_language = unique(list(language_student['Student Language']))
        total_vector = [total] * len(language_student)  # Adjusting vector length
        if len(ranking_total) == 0:
            ranking_total = total_vector
        else:
            ranking_total = ranking_total + total_vector

    language_students.insert(0, 'Ranking Total', ranking_total)
    language_students = language_students[language_students["Rating"] != 0]

    # Keep in mind this table only contains the population with language tutors
    # If no pairing is made in this step, it's fine

    # Initializing the vectors
    paired_tutor = []
    paired_student = []
    paired_language = []
    paired_tutor_email = []
    paired_student_email = []
    unpaired_student = []
    unpaired_student_lan = []
    Monday_time = []
    Tuesday_time = []
    Wednesday_time = []
    Thursday_time = []
    Friday_time = []
    Saturday_time = []
    Sunday_time = []
    tutor_interest_fin = []
    student_interest_fin = []

    #ELL Pairing Block
    for lan in range(0, len(language_list)):
        one_language_students = language_students[language_students["Student Language"].isin([language_list[lan]])]
        one_language_students['Order'] = one_language_students['Ranking Total'].rank(method='dense', ascending=True)
        one_language_students = one_language_students.sort_values(by=['Order'], ascending=True)
        unique_student_list = unique(list(one_language_students['Student Name']))

        for ol in range(0, len(unique_student_list)):
            if len(one_language_students) != 0:
                new_unique_student_list = unique(list(one_language_students['Student Name']))
                if unique_student_list[ol] in new_unique_student_list:
                    to_be_paired = one_language_students[
                        one_language_students["Student Name"].isin([unique_student_list[ol]])]
                    to_be_paired['Order_Rating'] = to_be_paired['Rating'].rank(method='dense', ascending=False)
                    to_be_paired = to_be_paired.sort_values(by=['Order_Rating'], ascending=True)
                    to_be_paired = to_be_paired.reset_index(drop=True)
                    tutor_pair = to_be_paired['Tutor Name'][0]
                    Monday_time.append(to_be_paired['Monday'][0])
                    Tuesday_time.append(to_be_paired['Tuesday'][0])
                    Wednesday_time.append(to_be_paired['Wednesday'][0])
                    Thursday_time.append(to_be_paired['Thursday'][0])
                    Friday_time.append(to_be_paired['Friday'][0])
                    Saturday_time.append(to_be_paired['Saturday'][0])
                    Sunday_time.append(to_be_paired['Sunday'][0])
                    tutor_email_i = to_be_paired['Tutor Email'][0]
                    tutor_interest_i = to_be_paired['Tutor Interest'][0]
                    student_interest_i = to_be_paired['Student Interest'][0]
                    # Delete the paired information out of the complete table
                    new_one_language_students = one_language_students[
                        ~one_language_students["Student Name"].isin([unique_student_list[ol]])]
                    new_one_language_students = new_one_language_students[
                        ~new_one_language_students["Tutor Name"].isin([tutor_pair])]
                    # Use these two vectors to move the students/tutors from the entire population table
                    paired_tutor.append(tutor_pair)
                    paired_student.append(unique_student_list[ol])
                    # Additional vectors for final table
                    tutor_interest_fin.append(tutor_interest_i)
                    student_interest_fin.append(student_interest_i)
                    paired_language.append(language_list[lan])
                    paired_tutor_email.append(to_be_paired['Student Email'][0])
                    paired_student_email.append(tutor_email_i)
                    # Updating the table
                    one_language_students = new_one_language_students
                else:
                    unpaired_student.append(unique_student_list[ol])
                    unpaired_student_lan.append(language_list[lan])
            else:
                unpaired_student.append(unique_student_list[ol])
                unpaired_student_lan.append(language_list[lan])


    # Step 2: Remove those student from step 1 in both df and the student name list
    removed_df = df[~df["Student Name"].isin(paired_student)]
    removed_df = removed_df[~removed_df["Tutor Name"].isin(paired_tutor)]
    removed_df = removed_df[removed_df["Rating"] != 0]
    distinct_list_of_student = unique(list(removed_df["Student Name"]))
    removed_df2 = removed_df
    # Initializing vectors
    Monday_time = []
    Tuesday_time = []
    Wednesday_time = []
    Thursday_time = []
    Friday_time = []
    Saturday_time = []
    Sunday_time = []
    unpaired_student = []
    unpaired_student_lan = []
    paired_tutor = []
    paired_student = []
    paired_language = []
    paired_student_email = []
    paired_tutor_email = []
    tutor_interest_fin = []
    student_interest_fin = []

    ranking_total = []
    for ln in range(0, len(distinct_list_of_student)):
        removed_df_student = removed_df[removed_df["Student Name"].isin([distinct_list_of_student[ln]])]
        total = sum(removed_df_student['Rating'])
        total_vector = [total] * len(removed_df_student)  # Adjusting vector length
        if len(ranking_total) == 0:
            ranking_total = total_vector
        else:
            ranking_total = ranking_total + total_vector

    removed_df.insert(0, 'Ranking Total', ranking_total)

    # 1.Making sure all student has pairing, student with lower rankings will be ranked first
    for k in range(0, len(distinct_list_of_student)):
        removed_df['Order'] = removed_df['Ranking Total'].rank(method='dense', ascending=True)
        if len(removed_df) != 0:
            new_distinct_list_of_student = unique(list(removed_df["Student Name"]))
            if distinct_list_of_student[k] in new_distinct_list_of_student:
                # Selecting one student
                to_be_paired = removed_df[removed_df["Student Name"].isin([distinct_list_of_student[k]])]
                for r1 in range(0,len(to_be_paired)):
                    if to_be_paired['Tutor Interest'][r1] == to_be_paired['Student Interest'][r1]:
                        to_be_paired['Rating'][r1] = to_be_paired['Rating'][r1] + 5
                to_be_paired['Order_Rating'] = to_be_paired['Rating'].rank(method='dense', ascending=False)
                to_be_paired = to_be_paired.sort_values(by=['Order_Rating'], ascending=True)
                to_be_paired = to_be_paired.reset_index(drop=True)

                for r in range(0,len(to_be_paired)):
                    tutor_pair = to_be_paired['Tutor Name'][r]
                    tutor_email_i = to_be_paired['Tutor Email'][r]
                    tutor_interest_i = to_be_paired['Tutor Interest'][r]
                    student_interest_i = to_be_paired['Student Interest'][r]

                    # Delete the paired information out of the complete table
                    new_removed_df = removed_df[~removed_df["Student Name"].isin([distinct_list_of_student[k]])]
                    new_removed_df = new_removed_df.reset_index(drop=True)
                    # If repairing all the rating of the previous one, and still cannot ensure everyone is paired, keep the current pairing
                    check_reduction = []
                    for n in range(0,len(new_removed_df)):
                        if new_removed_df['Tutor Name'][n] == tutor_pair:
                            check_reduction.append(new_removed_df['Ranking Total'][n] - new_removed_df['Rating'][n])

                    if (0 not in check_reduction):
                        new_removed_df = new_removed_df[~new_removed_df["Tutor Name"].isin([tutor_pair])]
                        Monday_time.append(to_be_paired['Monday'][r])
                        Tuesday_time.append(to_be_paired['Tuesday'][r])
                        Wednesday_time.append(to_be_paired['Wednesday'][r])
                        Thursday_time.append(to_be_paired['Thursday'][r])
                        Friday_time.append(to_be_paired['Friday'][r])
                        Saturday_time.append(to_be_paired['Saturday'][r])
                        Sunday_time.append(to_be_paired['Sunday'][r])

                        # Use these two vectors to move the students/tutors from the entire population table
                        paired_tutor.append(tutor_pair)
                        paired_student.append(distinct_list_of_student[k])
                        # Additional vectors for final table
                        paired_language.append('English')
                        paired_tutor_email.append(to_be_paired['Student Email'][0])
                        paired_student_email.append(tutor_email_i)
                        tutor_interest_fin.append(tutor_interest_i)
                        student_interest_fin.append(student_interest_i)
                        # Updating the table
                        removed_df = new_removed_df
                    elif (0 in check_reduction) and r==(len(to_be_paired)-1):
                        tutor_pair = to_be_paired['Tutor Name'][0]
                        Monday_time.append(to_be_paired['Monday'][0])
                        Tuesday_time.append(to_be_paired['Tuesday'][0])
                        Wednesday_time.append(to_be_paired['Wednesday'][0])
                        Thursday_time.append(to_be_paired['Thursday'][0])
                        Friday_time.append(to_be_paired['Friday'][0])
                        Saturday_time.append(to_be_paired['Saturday'][0])
                        Sunday_time.append(to_be_paired['Sunday'][0])
                        tutor_email_i = to_be_paired['Tutor Email'][0]
                        new_removed_df = new_removed_df[~new_removed_df["Tutor Name"].isin([tutor_pair])]
                        # Use these two vectors to move the students/tutors from the entire population table
                        paired_tutor.append(tutor_pair)
                        paired_student.append(distinct_list_of_student[k])
                        # Additional vectors for final table
                        paired_language.append('English')
                        paired_tutor_email.append(to_be_paired['Student Email'][0])
                        paired_student_email.append(tutor_email_i)
                        tutor_interest_fin.append(tutor_interest_i)
                        student_interest_fin.append(student_interest_i)
                        # Updating the table
                        removed_df = new_removed_df
            else:
                unpaired_student.append(distinct_list_of_student[k])
                unpaired_student_lan.append('English')
        else:
            unpaired_student.append(distinct_list_of_student[k])
            unpaired_student_lan.append('English')

    Unpaired2 = {'Student': unpaired_student, 'Language': unpaired_student_lan}
    Unpaired_df2 = pd.DataFrame(data=Unpaired2)

    Paired_d = {'Student': paired_student, 'Tutor': paired_tutor, 'Language': paired_language, 'Student Interest':student_interest_fin,
                'Tutor Interest': tutor_interest_fin, 'Student Email': paired_student_email, 'Tutor Email': paired_tutor_email,
                'Monday': Monday_time, 'Tuesday': Tuesday_time, 'Wednesday': Thursday_time, 'Thursday': Wednesday_time,
                'Friday': Friday_time, 'Saturday': Saturday_time, 'Sunday': Sunday_time}

    Paired_df = pd.DataFrame(data=Paired_d)

    return Paired_df,Unpaired_df2
# /************************************************ Execution Starts ************************************************
print('---- For Tutors -----')
tutor,tutor_name_list, tutor_email_list, tutor_last_updated_date,tutor_language_list,tutor_interest_list, tutor_submission_date, tutor_error = initial_table(tutor_initial_csv)
print('---- For Students -----')
student,student_name_list, student_email_list, student_last_updated_date,student_language_list,student_interest_list, student_submission_date, student_error= initial_table(student_initial_csv)

tutor_comparison_table = vectorize_table(tutor,tutor_name_list, tutor_email_list, tutor_last_updated_date,tutor_language_list,tutor_interest_list, tutor_submission_date)
student_comparison_table = vectorize_table(student,student_name_list, student_email_list, student_last_updated_date,student_language_list,student_interest_list, student_submission_date)

df = comparison(tutor_comparison_table,student_comparison_table)

student_name_list = unique(list(df['Student Name']))
need_to_ask_for_availability = check(df,student_name_list)
#1. Ask for new available times
#2. Ask if the unpaired tutors time fits those students
print('-----------------------------------')
print('Need to ask for availability...')
print(need_to_ask_for_availability)

language_list,language_students,distinct_list_of_student,removed_df2,ELL_df,ELL_Unpaired_df,Paired_df,Unpaired_df2 = match(df)
Paired_interest,Unpaired_interest = match_with_interest(df)
Other_option_df = other_option(language_list,language_students,distinct_list_of_student,removed_df2)

# Output needed:
Paired = pd.concat([ELL_df,Paired_df])
Unpaired = pd.concat([ELL_Unpaired_df,Unpaired_df2])
Paired_Interest = pd.concat([ELL_df,Paired_interest])
Unpaired_Interest = pd.concat([ELL_Unpaired_df,Unpaired_interest])

Unpaired_name_list = unique(list(Unpaired['Student']))
unpaired_interest_name_list = unique(list(Unpaired_Interest['Student']))



lan = []
for f in range(0, len(Unpaired_name_list)):
    selected = Unpaired[Unpaired['Student']==Unpaired_name_list[f]]
    selected = selected.reset_index(drop=True)
    if len(selected) != 1:
        temp = []
        for fi in range(0, len(selected)):
            temp.append(selected['Language'][fi])
        lan.append(temp)
    else:
        lan.append(selected['Language'][0])

Unpaired_df = {'Student': Unpaired_name_list, 'Language': lan}
Unpaired = pd.DataFrame(data=Unpaired_df)

lan = []
for f in range(0, len(unpaired_interest_name_list)):
    selected = Unpaired_Interest[Unpaired_Interest['Student']==unpaired_interest_name_list[f]]
    selected = selected.reset_index(drop=True)
    if len(selected) != 1:
        temp = []
        for fi in range(0, len(selected)):
            temp.append(selected['Language'][fi])
        lan.append(temp)
    else:
        lan.append(selected['Language'][0])

Unpaired_Interest_df = {'Student': unpaired_interest_name_list, 'Language': lan}
Unpaired_Interest = pd.DataFrame(data=Unpaired_Interest_df)

Paired.to_csv('/Users/hwanyaur/Desktop/Paired.csv')
Unpaired.to_csv('/Users/hwanyaur/Desktop/Unpaired.csv')
Paired_Interest.to_csv('/Users/hwanyaur/Desktop/Paired_Interest.csv')
Unpaired_Interest.to_csv('/Users/hwanyaur/Desktop/Unpaired_Interest.csv')
df.to_csv('/Users/hwanyaur/Desktop/df.csv')
Other_option_df.to_csv('/Users/hwanyaur/Desktop/Other_option_df.csv')
# Other_option_df: show all the other pairing options.
# If a student is ELL student, both English and that language would show up if initial pairing was unsuccessful.
# Other_option_df needs to be used with df if more information is needed.

# ************************************************ Execution Ends ************************************************/

other_option
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
