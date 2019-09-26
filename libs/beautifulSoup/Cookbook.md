**Find All spans text with a specific class**


    soup = BeautifulSoup(html, 'html.parser')
    spans = soup.find_all('span' , attrs={'class' : 'text-large2'})
    print(spans[0].text)
