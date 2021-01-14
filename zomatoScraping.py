from bs4 import BeautifulSoup
import requests
import pandas 



url="https://www.zomato.com/cincinnati/restaurants"
header = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
response=requests.get(url,headers=header)    
soup=BeautifulSoup(response.content,"html.parser")

searchList=soup.find_all("div",{"class":"js-search-result-li"})


totalData=[]
for each in searchList:
      

     data={}
     data['restaurant']=each.find("a",{"data-result-type":"ResCard_Name"}).text.replace("/n","").strip()
     data['locality']=each.find("b").text.replace("/n","").strip()
     data['ratings']=each.find("span",{"class":"rating-value"}).text.replace("/n","").strip()
     foodContent=each.find("span",{"class":"pl0"})
     foods=foodContent.find_all("a")
     data['foods']= [food.string for food in foods]
     print("""
     Restaurant Name:{}\n
     Location:{}\n
     Ratings:{}\n
     Foods:{}\n
     ---------------------------
     """.format(data['restaurant'],data['locality'],data['ratings']," ".join(data['foods'])))
     totalData.append(data)

df = pandas.DataFrame(totalData)
df = df[["restaurant","locality","ratings","foods"]]
df.to_csv("zomatoData.csv")


    
