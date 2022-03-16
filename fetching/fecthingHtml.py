from itertools import count
import requests
import json

def getCourses(str):
    # create a txt file that holds the courses
    with open('courses.txt', 'w') as f:
        f.write("")

    # remove the useless part
    str = str.split('<p class="course">',1)[1]
    str = str.split('<div id="secondary">',1)[0]
    # map to an array
    str = str.split('<p class="course">')

    courses = []
    # remove the tags
    for x in str:
        x = x.replace('<span class="course_header">', '')
        x = x.replace('</p>','')
        x = x.replace('</span>','')
        x = x.replace('</div>','')
        x = x.replace('<p class="course_ending">','')
        x = x.replace('<span class="course_data">', '')
        # only keep the courses that are under 500 level
        if int(x[0:3]) < 500:
            if x[4] == '[':
                end = 4
                while x[end] != ']':
                    end = end + 1
                x = x.replace(x[4:end + 1], '')
            if "Course Prerequisite:" in x:
                temp = x.split("Course Prerequisite:")
                keep = temp[0][0:3]
                for i in range(3, (len(temp[0]))):
                    if not (temp[0][i].isnumeric() or temp[0][i] == '(' or temp[0][i] == ')' or temp[0][i] == '-'):
                        keep = keep + temp[0][i]
                x = keep + "Course Prerequisite:" + temp[1]
            courses.append(x)
            with open('courses.txt', 'a') as f:
                f.write(x + "\n")
    
# fetching the html file from wsu cs major
fetching = requests.get('https://catalog.wsu.edu/Pullman/Courses/BySubject/CPT_S')
str = "default"

if fetching.ok:
    str = fetching.text

getCourses(str)
