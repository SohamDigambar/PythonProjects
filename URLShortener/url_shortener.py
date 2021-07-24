'''
Created on Jul 20, 2021

@author: sohamdigambar
'''

class URL_Shortener:
    url_to_id = {}
    id_value = 100000
    
    def shorten_url(self, original_url):   #shortens the long url
        
        
        if original_url in self.url_to_id: #makes sure to return the same short link if given the same link
            self.id_value = self.url_to_id[original_url]
            short_url = self.encode(self.id_value)
        else:
            self.url_to_id[original_url] = self.id_value
            short_url = self.encode(self.id_value)
            self.id_value += 1
            
        return "www.your_short_url.com/" + str(short_url)
    
    
    def encode(self, id):    #converts url from base 10 to base 62: (0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ)
        characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        base = len(characters)
        
        return_value = []
        
        while id > 0:
            value = id % base
            return_value.append(characters[value])  #appends the associated character to the return_value list
            id = id // base  #integer division
            
            
        return "".join(return_value)



shortener = URL_Shortener()
url = input("Please enter the URL you wish to shorten: ")
print(shortener.shorten_url(url))
        