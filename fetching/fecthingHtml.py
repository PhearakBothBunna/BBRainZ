from itertools import count
import requests
import json

def toFile(list):
    for x in list:
        with open('html3.txt', 'a') as f:
            f.write(getCourses(x))

def listToString(list, str1):
    return (str1.join(list))

def filter(list):
    res = []
    for x in list:
        if "%" in x:
            res.append(x)
    return res

def toJson(coursesId, prereq):
    res = []
    for x in range(len(coursesId)):
        list.append({coursesId[x] : prereq[x]})
    res = json.dumps(list)
    return res

def divide(list):
    coursesId = []
    prereq = []
    for x in list:
        cur = x.split("%")
        coursesId.append(cur[0])
        prereq.append(cur[1])
    return coursesId, prereq

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
        course = x.split('Course Prerequisite:')
        # only keep the courses that are under 500 level
        if len(course) > 1:
            courses.append(course)
    for course in courses:
        course[1] = course[1].split('.')[0]
        with open('courses.txt', 'a') as f:
            f.write(course[0] + "%" + course[1] + "\n")
    
# fetching the html file from wsu cs major
fetching = requests.get('https://catalog.wsu.edu/Pullman/Courses/BySubject/CPT_S')
str = "default"

if fetching.ok:
    str = fetching.text

getCourses(str)