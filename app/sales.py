

class Sale:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        sale = self.session.get("sale")
        if not sale:
            sale = self.session["sale"]={}
           
        
        self.sale = sale




    def addproduct(self, product):
  
        if(str(product.sku) not in self.sale.keys()):
            self.sale[product.sku]={
                "sku":product.sku,
                "name":product.name,
                "acumulated": str(product.price),
                "quantity":1,
            }
            
        else:
            for key, value in self.sale.items():
                if key == str(product.sku):
                    value["quantity"]=value["quantity"]+1
                    value["acumulated"]=float(value["acumulated"])+float(product.price)
                    break

        self.save_sale()
        


    def save_sale(self):
        self.session["sale"] = self.sale
        self.session.modified = True



    def delete_sale(self, product):
       product.sku=str(product.sku)
       if product.sku in self.sale:
           del self.sale[product.sku]
           self.save_sale()



    def quit_product(self, product):
        for key, value in self.sale.items():
            if key==str(product.sku):
                value["quantity"]=value["quantity"]-1
                value["acumulated"]=float(value["acumulated"])-float(product.price)
                if value["quantity"]<1:
                    self.delete_sale(product)
                break
        self.save_sale()


    def clean(self):
        self.session["sale"] = {}
        self.session.modified = True    
    


    