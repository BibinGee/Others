# *-*coding = utf-8 *-*

import requests
##import bs4
import os
from bs4 import BeautifulSoup 

##url = "https://www.kanunu8.com/files/old/2011/2554/"
##folder = "qjssx/"
##start_page = 75435
##end_page = 75614
##url = "http://www.zggdwx.com"

# get all histories in txt file

root_dir = './histories/'
catalog = "/chapters.txt"
chapter_list = "./lists/history_list.txt"
html_file = "./html files/lishi2.txt"

with open(html_file, 'r', encoding = 'utf-8') as f:
    fl = f.read()
##print(fl)
html = BeautifulSoup(fl, "html.parser")
a_tag = html.findAll('a')
##print(a_tag)
for novel in a_tag:
    print("downloading novel: ", novel.attrs['href'], novel.text)
    # get chapters in a novel
    novel_name = novel.text
    res = requests.get(novel.attrs['href'])
    soup = BeautifulSoup(res.text, "html.parser")
    fieldset = soup.find('fieldset', class_="catalog" )
    all_a_tags = fieldset.findAll('a')

    with open(chapter_list, "a+", encoding='utf-8') as f:
        f.write(novel_name)
        f.write(",/histories/" + novel_name +"/")
        f.write("\n")
    # retrieve all chapters
    ref_index = 0
    for a in all_a_tags:
        title = a.text
        link = a.attrs['href']
        print("downloading novel: ", link, title)
        
        # get context from a chapter
        page_resp = requests.get(link)
        soup = BeautifulSoup(page_resp.text, "html.parser")
        p_tag = soup.findAll('p')
        
        ### Create a folder in ./novel
        if not os.path.exists(root_dir + novel_name):
            os.mkdir(root_dir + novel_name)
        
        ref_index += 1
        
        ## write chapter title into ./chapters.txt
        with open(root_dir + novel_name + catalog, "a+", encoding='utf-8') as f:
            f.write(title)
            f.write(",href=" + str(ref_index).zfill(3))
            f.write("\n")
        
        ## ready to write context into file
        with open(root_dir + novel_name +"/"+ str(ref_index).zfill(3) +".txt", "a+", encoding='utf-8') as f:
            f.write(title)
            f.write("\n")
        for p in p_tag[11:]:
##            print(p.text)
            context = p.text
            k = 0
            for character in context:
                with open(root_dir + novel_name +"/"+ str(ref_index).zfill(3) +".txt", "a+", encoding='utf-8') as f:
                    if character != "<br\>":
                        f.write(character)
                    k += 1
                    if character == '\n':
                        k = 0
                    if k == 38:
                        f.write("\n")
                        k = 0
            with open(root_dir + novel_name +"/"+ str(ref_index).zfill(3) +".txt", "a+", encoding='utf-8') as f:
                f.write('\n')
print('Done')

            
##chapter_div = fieldset[-2].div
##all_a_tag = bs4.BeautifulSoup.findAll('a', chapter_div)
##print(all_a_tag)
##for n in novel_home_list:
##ref_index = 0
##for chapter in range (start_page, end_page + 1):
##    print("Reading webpage: ", url + str(chapter) + ".html")
##    res = requests.get(url + str(chapter) + ".html")
##    res.encoding = 'gbk'
####    print(res.text)
##    
##    html = bs4.BeautifulSoup(res.text, "html.parser")
####    print(html)
##    title = html.select('font')[0].text
##    print("Downloading: ", title)
##    context = html.select('p')[0].text
####    print(context)
####    context = context.text.replace('<br/>', "")
##
##    if not os.path.exists("./novels/" + folder):
##        os.mkdir("./novels/" + folder)
##    ref_index += 1
##    with open("./novels/" + folder + "chapters.txt", "a+", encoding='utf-8') as f:
##        f.write(title)
##        f.write(",href=" + str(ref_index).zfill(3))
##        f.write("\n")
##    k = 0
##    with open("./novels/" + folder + str(chapter-start_page + 1).zfill(3) +".txt", "a+", encoding='utf-8') as f:
##        f.write(title)
##        f.write("\n")
##    for character in context:
##        with open("./novels/"+ folder + str(chapter-start_page + 1).zfill(3) +".txt", "a+", encoding='utf-8') as f:
##            if character != "<br\>":
##                f.write(character)
##            k += 1
##            if character == '\n':
##                k = 0
##            if k == 38:
##                f.write("\n")
##                k = 0
##files = r"C:\Users\Administrator\Desktop\novels" +"\\" + folder
##for i in range(1,240):
##    with open(files + str(i).zfill(3) + ".txt", 'r', encoding='utf-8') as f:
##        txt = f.read()
##        txt = txt.replace("\n\n\n","\n")
##        txt = txt.replace("\n\n","\n")
##    with open(files + str(i).zfill(3) + ".txt", 'w', encoding='utf-8') as f:
##        f.write(txt)












##    print(context)
##    chapters = chapters[1:len(chapters)-1]
##    print(chapters)
##    for c in chapters:
####        print(c.attrs["href"])
##        res = requests.get(url + n + c.attrs["href"])
##        res.encoding = 'gbk'
##        html = bs4.BeautifulSoup(res.text, "html.parser")
##        if not os.path.exists("./novels/" + n[:3]):
##            os.mkdir("./novels/" + n[:3])
##        else:
##            #### write title to chapters ############
##            print('downloading: ',"./novels/" + n[:3] + "/" + c.attrs["href"] + ".txt", c.text)
##            with open("./novels/" + n[:3] + catalog, "a+", encoding='utf-8') as f:
##                f.write(c.text)
##                f.write("\n")
##            ###### write context to file ############
##            with open("./novels/" + n[:3] + "/" + c.attrs["href"][:3] + ".txt", "w", encoding='utf-8') as f:
####                f.write(c.text)
####                f.write("\n")
####                print( html.select('b')[0].text)
##                text = html.select('b')[0].text
##                f.write(text)
##                f.write("\n\n")
##                text = html.select('pre')[0].text
####                print(text)
##                f.write(text)

            
##print(html.select('pre')[0].text)
##for c in chapters:
##    print(c.text, c.attrs["href"])
    
