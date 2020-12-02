## What is ChromeDriver/GeckoDriver?
WebDriver is an open source tool for automated testing of web apps across many browsers. It provides capabilities for navigating to web pages, user input, JavaScript execution, and many more. ChromeDriver is a standalone server which implements WebDriver’s wire protocol for Chromium. In order to instantiate the object of ChromeDriver, you can simply create the object with the help of below command.

## Why do you need ChromeDriver/GeckoDriver?

The main purpose of the ChromeDriver is to launch Google Chrome. Without that, it is not possible to execute Selenium test scripts in Google Chrome as well as automate any web application. This is the main reason why you need ChromeDriver to run test cases on Google Chrome browser. 

Now that you know what is ChromeDriver and why do you need it, let’s move ahead and understand how to set up ChromeDriver in the system.

## Ensure you have geckodriver/chromedriver installed
GeckoDriver is a web browser engine which is used in many applications developed by Mozilla Foundation and the Mozilla Corporation. GeckoDriver is the link between your tests in Selenium and the Firefox browser.
 
 if not :
 ```
sudo apt install firefox-geckodriver
 ```
## 1.Create a virtual env

```
virtualenv -p /usr/bin/python3 venv

```
## 2.Activate the virtual environ
```
source venv/bin/activate

```
## 2.Install selenium
```
pip3 install selenium
```

## 3. import selenium's packages required

```
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

```
## 4. Have Your Json Data prepared as a array of json objects
```

data = [
    {"name":"Supermarket",
    "description":"Large retail store operated on a self-service basis, selling groceries, fresh produce, meat, bakery and dairy products, and sometimes an assortment of nonfood goods. Supermarkets gained acceptance in the United States during the 1930s.",
    "icon":"fas fa-shopping-basket",
    "tags":"fruits, grocery, supermarket"
    },

    {"name":"Health & Beauty",
    "description":"Health and beauty encompasses a variety of products, including fragrances, makeup, hair care and coloring products, sunscreen, toothpaste, and products for bathing, nail care, and shaving. The industry overlaps with other markets like chemical, health care, and petroleum.",
    "icon":"fas fa-briefcase-medical",
    "tags":"healthandbeauty,skincare,beauty,healthylifestyle,health,healthandwellness,makeup,healthyskin,kayrahealthandbeauty,sihatdancantik,aloevera,antiaging,beautyproducts,wellness"
    },

    {"name":"Home & Office",
    "description":" consumables and equipment regularly used in offices by businesses and other organizations, by individuals engaged in written communications, recordkeeping or bookkeeping, janitorial and cleaning, and for storage of supplies or data. The range of items classified as office supplies varies, and typically includes small, expendable, daily use items, consumable products, small machines, higher cost equipment such as computers, as well as office furniture and art. ",
    "icon":"fas fa-building",
    "tags":"office,work,design,interiordesign,business,home,officedesign,architecture,interior,homeoffice,officespace,furniture,workspace,officedecor,instagood,covid,realestate,homedecor,job,like,instagram,coworking,love,workfromhome,workplace,officefurniture,life,working,coworkingspace"
    },

    {"name":"Phones & Tablets",
    "description":"Typically with a mobile operating system and touchscreen display processing circuitry, and a rechargeable battery in a single, thin and flat package. ",
    "icon":"fas fa-mobile-alt",
    "tags":"phone,iphone,mobile,smartphone,samsung,apple,android,technology,pro,photography,instagood,plus,tech,instagram,phonecases,love,ios,phonecase,case,photooftheday,oneplus,phones,xiaomi,photo,huawei,like,follow,nokia"
    },

    {"name":"Computing",
    "description":"any desktop, laptop, netbook, notebook, workstation or server computer; provided, however, that no Non-PC Product shall be a Computer Product. For clarity, any product that includes a screen with a diagonal size of seven (7) inches or greater (i) shall not automatically be considered a Computer Product and (ii) shall not be considered a Computer Product unless it meets this definition",
    "icon":"fas fa-laptop",
    "tags":"computing,technology,computer,computerscience,tech,computers,internet,software,industry,pc,robotics,automation,manufacturing,technological,communication,nanotechnology,gaming,application,technical,programming,hightechnology,techequipment,energy,instagramtechnology,instatechnology,technologystudy,appliedscience,business"
    },

    {"name":"Electronics",
    "description":"equipment intended for everyday use, typically in private homes.",
    "icon":"fas fa-charging-station",
    "tags":"electronics,technology,tech,engineering,iphone,gadgets,arduino,electrical,electronic,robotics,instagood,electricalengineering,instatech,gadget,raspberrypi,apple,diy,robot,smartphone,electronicsengineering,techie,innovation,samsung,iot,photooftheday,mobile,arduinoproject,android,engineer"
    },

    {"name":"Fashion",
    "description":"a product for which demand changes frequently because of changes in consumer tastes or product attributes. Where consumer tastes are fickle and consumers seek to be fashionable, suppliers can take advantage of this by frequent restyling of products.",
    "icon":"fas fa-vest",
    "tags":"fashion,style,love,instagood,like,photography,photooftheday,beautiful,follow,instagram,picoftheday,bhfyp,model,me,instadaily,smile,art,likeforlikes,beauty,followme,myself"
    },
  
    {"name":"Gaming",
    "description":"any intangible asset, good or interest that can be bought or sold or otherwise is the subject of an activity constituting a Gaming Business.",
    "icon":"fas fa-gamepad",
    "tags":"game,gamer,gaming,games,ps,playstation,videogames,xbox,gamers,memes,pubg,pc,videogame,art,fortnite,gamergirl,twitch,follow,youtube,anime,like,play,fun,love,xboxone,meme,nintendo,cosplay,pubgmobile"
    },

    {"name":"Baby Products",
    "description":"intended to be used on infants and children under the age of three",
    "icon":"fas fa-baby",
    "tags":"baby,love,babygirl,babyboy,kids,cute,newborn,family,babyshower,bebe,babies,photography,handmade,instagood,happy,pregnant,like,instagram,babylove,girl,fashion,beautiful,momlife,pregnancy,mom,follow,cutebaby,instababy"
    },

    {"name":"Sporting Goods",
    "description":"a good, a service, or any combination of the two that is designed to provide benefits to a sports spectator, participant, or sponsor.",
    "icon":"fas fa-dumbbell",
    "tags":"uniroleao,fitness,brigada,beretta,sportingsempre,futsalscp,shotguns,voleibolscp,perazzi,tiroavolo,vemdedentro,verdeebranco,andebolscp,varandasout,olympictrap,instagram,shotgun,compak,juve,tuvaisvencer,fifa,photography,gym,training,cristianoronaldo,love,perazzishotgun,perazzilove,euqueroosportingcampe"
    },
  
      {"name":"Garden & Outdoors",
    "description":"a good, a service, or any combination of the two that is designed to provide benefits to a sports spectator, participant, or sponsor.",
    "icon":"fas fa-hiking",
    "tags":"garden,nature,flowers,gardening,plants,flower,photography,green,naturephotography,love,gardenlife,spring,summer,jardin,gardendesign,garten,home,beautiful,landscape,plant,photooftheday,gardeninspiration,flowerstagram,art,instagood,mygarden,macro,gardener,gardens"
    },

      {"name":"Other Categories",
    "description":"Other Categories",
    "icon":"fas fa-ellipsis-h",
    "tags":"other,categories"
    },

   
  ]

```

## 5.Define your function
```
def How():
  driver = webdriver.Firefox()
  driver.get("http://127.0.0.1:8000/admin/")
  driver.set_window_size(1920, 1012)
  driver.find_element(By.ID, "id_username").click()
  driver.find_element(By.ID, "id_username").send_keys("ngecu")
  driver.find_element(By.ID, "id_password").send_keys("d")
  driver.find_element(By.CSS_SELECTOR, ".submit-row > input").click()
  driver.find_element(By.LINK_TEXT, "Categories").click()
  driver.find_element(By.CSS_SELECTOR, "li > .addlink").click()
  for item in data:
    driver.find_element(By.ID, "id_name").send_keys(Keys.DOWN)
    driver.find_element(By.ID, "id_name").send_keys(item['name'])
    driver.find_element(By.ID, "id_description").click()
    driver.find_element(By.ID, "id_description").send_keys(item['description'])
    driver.find_element(By.ID, "id_icon").click()
    driver.find_element(By.ID, "id_icon").send_keys(item['icon'])
    driver.find_element(By.ID, "id_tags").click()
    driver.find_element(By.ID, "id_tags").send_keys(item['tags'])
    driver.find_element(By.NAME, "_addanother").click()
  driver.close()

How()
```
