from requests_html import HTMLSession


def getProduct(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)

    product = {
        'title': r.html.xpath('//*[@id="productTitle"]', first=True).text, # .text print out the exact values without tags,
        'price': r.html.xpath('//*[@id="olp_feature_div"]/div[2]/span/a', first=True), #this princt values with tags because no .text to filter out the tags   
        'price2': r.html.xpath('//*[@id="olp_feature_div"]/div[2]/span/a/span[2]', first=True)
    }
    
    print("product:", product)
 
    if product["price"] == None: # this block check if price is set so as to know if the product is in stock
        print("product not available:") 
        return 
    else:
        print("product available") # this is the output if the product is in stock
        return product 

# below are the urls to the product we are scrapping
getProduct('https://www.amazon.com/Intel-NUC-Mainstream-Kit-NUC8i5BEH/dp/B07GX59NY8/ref=sr_1_1?claim_type=EmailAddress&dchild=1&new_account=1&qid=1618211083&s=computers-intl-ship&sr=1-1')

getProduct('https://www.amazon.com/AmazonBasics-Puresoft-PU-Padded-Mid-Back-Computer/dp/B081H3Y5NW/ref=sr_1_2?dchild=1&keywords=amazonbasics&pd_rd_r=d8ea53fc-6e47-4a0f-acc9-258165ac137a&pd_rd_w=j6cRy&pd_rd_wg=U7QrV&pf_rd_p=9349ffb9-3aaa-476f-8532-6a4a5c3da3e7&pf_rd_r=K3M36WQ7436GPE0TTD0C&qid=1618184375&sr=8-2')

getProduct('https://www.amazon.com/Nintendo-Switch-Gray-Joy%E2%80%91-HAC-001/dp/B07VJRZ62R/ref=lp_16225016011_1_5')

