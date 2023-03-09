import json
from module_classes import modules

def welcome_message():
    print('Hey welcome to about me, Select a option below')

    print('1-Add person\n2-Update Person\n3-Delete Person\n4-See all Data\n5-Search data by passion or name\n6-Exit')

def add_person(new_person,fileName='aboutMe.json'):
    with open(fileName,'r+') as file:
        file_data = json.load(file)
        file_data["about_me"].append(new_person)
        file.seek(0)
        json.dump(file_data,file,indent=4)
        file.close()

def delete_person(unique_id,fileName='aboutMe.json'):
    with open(fileName,'r') as file:
        data = json.load(file)

        iterable_data = data["about_me"]

        person_found = False
        for i in iterable_data:
            if i['unique_id'] == str(unique_id):                
                person_found = True
                iterable_data.remove(i)
                print('Data Removed Successfully')
        
        if person_found == False:
            print('Please Enter the valid ID')

        data['about_me'] = iterable_data

    with open(fileName,'w') as file:
        json.dump(data,file,indent=4)

def update_person(unique_id,fileName="aboutMe.json"):

    with open(fileName,'r') as file:
        data = json.load(file)

        found = False
        iterable_data = data['about_me']
        for person_data in iterable_data:
            if int(person_data['unique_id']) == unique_id:

                found = True

                print('Want to change name? YES/NO if yes Enter your name')
                if input().lower() == 'yes':
                    person_data['name'] = str(input())
                else:
                    pass

                print('Want to change passion? YES/NO if yes Enter your new passion')
                if input().lower() == 'yes':
                    person_data['passion'] = str(input())
                else:
                    pass

                print('Want to change contact info? YES/NO if yes Enter your new contact info')
                if input().lower() == 'yes':
                    person_data['contact_number'] = str(input())
                else:
                    pass
                
                print('Want to change Description? YES/NO if yes Enter your new description')
                if input().lower() == 'yes':
                    person_data['about_description'] = str(input())
                else:
                    pass
                
                print('Want to change Skillset? YES/NO if yes Enter your new Skill set')
                if input().lower() == 'yes':
                    entered_skills = []
                    for i in range(1,4):
                        entered_skills.append(str(input()))
                    person_data['skills'] = entered_skills
                else:
                    pass

        if found == False:
            print('person with the id not found and cannot be updated')

        data['about_me'] = iterable_data

        with open(fileName,'w') as file:
            json.dump(data,file,indent=4)

def query_data(fileName='aboutMe.json'):
    with open(fileName,'r') as file:
        data = json.load(file)
        iterable_data = data['about_me']

        for about_data in iterable_data:
            print(about_data)

def search_by_name_or_passion(name,passion,fileName='aboutMe.json'):
    with open(fileName,'r') as file:
        data = json.load(file)

        iterable_data = data['about_me']

        found = False
        for person_data in iterable_data:
            if person_data['passion'].lower() == passion.lower() or person_data['name'].lower() == name.lower():
                found = True
                print(person_data)

        if found == False:
            print('No people with required name or passion')

def perform_operation(option_selected):
    if option_selected == 1:

        name = input('Enter your name\n')    
        unique_id = input('Enter your ID\n')    
        passion = input('Enter your Passion\n')    
        contact_number = input('Enter your Contact Information\n')
        about_description = input('Enter your Short Description\n')

        print('Enter your top 3 skills')
        
        entered_skills = []
        for i in range(1,4):
            entered_skills.append(str(input()))
        skills = entered_skills

        person_to_add = modules.Person(name,unique_id,passion,contact_number,about_description,skills)
        
        add_person(person_to_add.__dict__)

    elif option_selected == 2:

        print('Enter your unique ID')
        person_to_update = int(input())
        update_person(person_to_update)

    elif option_selected == 3:
        print('Enter Your Unique ID')
        person_to_delete = int(input())
        delete_person(person_to_delete)

    elif option_selected == 4:
        print('Here you can see all the data from the storage')
        query_data()

    elif option_selected == 5:
        print('please enter name')
        name = input()
        print('please enter passion')
        passion = input()
        search_by_name_or_passion(name,passion)

    elif option_selected == 6:
        exit
        