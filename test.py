from bs4 import BeautifulSoup

# use relative path, for some reason it does not read inside this directory idk
with open('webscraper\home.html', 'r') as html_file:
    content = html_file.read()
    #print(content)

    soup = BeautifulSoup(content, 'lxml')
    #print(soup.prettify())

    #class_="global-nav-item secure-btn"
    course_cards = soup.find_all('div', class_="card")
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]

        print(f'{course_name} costs {course_price}')

    #courses_html_tags = soup.find_all('h5')
    #print(courses_html_tags)

    #for course in courses_html_tags:
    #    print(course.text)