from bs4 import BeautifulSoup
import requests,json,pprint,csv
with open("clgdunia.com.html","r") as f:
    html=f.read()
soup=BeautifulSoup(html,"html.parser")
mainDiv = soup.find("div",class_="row listing-block-cont js-scrolling-container")
allDiv = mainDiv.find_all('div',class_="col-sm-4 automate_client_img_snippet")

# for college all links

listOfLinks = []
for college in allDiv:
    # # finding college name and link of that college
    a_nameOfCollege = college.find("a",class_="college_name")
    listOfLinks.append(a_nameOfCollege["href"])

# for required data of all colleges
count = 0
listOfcolleges = []
for clgLink in listOfLinks:
    count+=1
    dict_ = {}
    soup = BeautifulSoup(requests.get(clgLink).text,"html.parser")

    # #college name

    divClgName = soup.find("div",class_="college_data")
    h1ClgName = divClgName.find('h1').text.strip()

    # #college type and est date

    divClgType = soup.find('div',class_="extra_info")
    spanClgtype = divClgType.find_all("span")       

    # for  clg estd
    try:
        estd = spanClgtype[2].text.strip() 
    except:
        estd = "nothing"

    # for  clg type
    try:
        clgType = spanClgtype[4].text.strip()
    except:
        clgType = "nothing"       


    # # ratings and img_url

    ratingDiv = soup.find('div',class_="college_top_wrapper")
    ratingDiv1 = ratingDiv.find("div",class_="college-info")
    ratingDiv2 = ratingDiv1.find("div",class_="college_rating pull-right")

    # for rating

    try:
        ratingSpan = ratingDiv2.find("span",class_="rating_val").text.strip()
    except:
        ratingSpan = "nothing"

    #  for image 

    try:
        imageOfbuilding = ratingDiv.find("img")["src"]
    except:
        imageOfbuilding = "nothing"

    # # location and contact-number

    a = soup.find("div",class_="address row")

    locationDiv = a.find("div",class_="loc_block")

    #  for location

    try:
        locationH3 = locationDiv.find("h3").text.strip()
    except:
        locationH3 = "nothing"

    contactDiv = a.find("div",class_="contact_block")
    contactDiv1 = contactDiv.find("div",class_="lr lr_contact").text.strip()

    # for contact
    #  
    try:
        contactDiv1 = contactDiv.find("div",class_="lr lr_contact").text.strip()
    except:
        locationH3 = "nothing"

    # forming a dictionery
    
    dict_["college_name"] = h1ClgName
    dict_["college_type"] = clgType
    dict_["college_estd"] = estd
    dict_["college_rating"] = ratingSpan
    dict_["college_img_url"] = imageOfbuilding
    dict_["college_location"] = locationH3
    dict_["college_contactNumber"] = contactDiv1
    print(count)

    # appending all colleges in to one list
    
    listOfcolleges.append(dict_)
    

# json data of all colleges

finalData = open('allColleges.json',"w+")
json.dump(listOfcolleges,finalData,indent=4)


jsonData = open('allColleges.json',"r")
totalData = json.load(jsonData)

csvData = open("allColleges.csv","w+")
csv_file = csv.writer(csvData)
csv_file.writerow(["college_name","college_type","college_estd","college_rating","college_img_url","college_location","college_contactNumber"])
for college in totalData:
    csv_file.writerow([college["college_name"],college["college_type"],college["college_estd"],college["college_rating"],college["college_img_url"],college["college_location"],college["college_contactNumber"]])

















