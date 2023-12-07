import csv

from requests_html import HTMLSession

session = HTMLSession()

# why do some obituaries print only their name?
# print text on page i extract death and place from

# open outfile
fout = csv.writer(open('/Users/jacobanderson/Documents/obituaries.csv', mode='w'))
fout.writerow(['date', 'place', 'obituary'])

# set iterator to one and declare r variable empty
i = 1
r = None

while True:

    # retrieve the url from each incremented page count
    url = "https://www.legacy.com/category/news/covid19-memorial/page/" + str(i) + "/"
    previous_r = r
    r = session.get(url)

    # if the links from the current page are the same as the previous break the loop
    if r == previous_r:
        break

    # if the links on the current page are different retrieve the links to each obituary
    links = r.html.find(".grid-title a")
    links = [l.attrs["href"] for l in links]

    # scrape out place and date of death for each individual's page
    for link in links:
        r = session.get(link)
        deaths = r.html.xpath("//h4[@class ='has-text-align-center'][2]/a/text()")
        # if previous xpath does not work for this page, try the xpath below
        if not deaths:
            deaths = r.html.xpath("//h4[@class = 'has-text-align-center'][2]")[0].text
        place = r.html.xpath("//h4[@class = 'has-text-align-center'][1]/a/text()")
        obituary = r.html.xpath("//div[@id ='penci-post-entry-inner']/p[em]/preceding::p/text()")
        print(obituary)

        # find “read full obituary” link, grab element, and pull out href
        full = r.html.xpath("//p[contains(a,'the full obituary') or contains(a, 'View the obituary')]/a")
        full = [f.attrs["href"] for f in full]
        for f in full:
            # open the link to the full obituary and pull out the text
            try:
                b = session.get(f)
                full_text = b.html.xpath("//div[@data-component = 'ObituaryParagraph']/text()")
                if len(full_text) == 0:
                    full_text_list = [b.html.xpath("//section[@class = 'Obituary']")]
                    for element in full_text_list:
                        full_text += element.text
            except:
                full_text = ["Broken Link"]

        # write data to outfile, one row per deceased individual
        fout.writerow([deaths[0], place[0], full_text[0]])

    # increment to the next page and repeat process
    i += 1
