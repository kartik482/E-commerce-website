from turtle import update
from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact, Order_update, Orders, product
from math import ceil
import json

# Create your views here.
def index(request):
    # products=product.objects.all()
    # print(products)
    # n=len(products)
    # nslides=n//4+ceil((n/4)-(n//4))

    allprods=[]
    catprods=product.objects.values("category")
    cats={item["category"] for item in catprods}
    for cat in cats:
        prod=product.objects.filter(category=cat)
        n=len(prod)
        nslides=n//4+ceil((n/4)-(n//4))
        allprods.append([prod,range(1,nslides),nslides])


    # params={"no_of_slides":nslides,"product":products,"range":range(1,nslides)}
    # allprods=[[products,range(1,nslides),nslides],
    #             [products,range(1,nslides),nslides]]
    params={"allprods":allprods}
    return render(request,'shop/index.html',params)

def searchmatch(query,item):
    if query in item.description.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True

    else:
        return False

def search(request):
    query=request.GET.get("search","").lower()
    allprods=[]
    catprods=product.objects.values("category","id")
    cats={item["category"] for item in catprods}
    for cat in cats:
        prodtemp=product.objects.filter(category=cat)
        prod=[item for item in prodtemp if searchmatch(query, item) ]
        n=len(prod)
        nslides=n//4+ceil((n/4)-(n//4))
        if len(prod)!=0:
            allprods.append([prod,range(1,nslides),nslides])
            


    # params={"no_of_slides":nslides,"product":products,"range":range(1,nslides)}
    # allprods=[[products,range(1,nslides),nslides],
    #             [products,range(1,nslides),nslides]]
    params={"allprods":allprods,"msg":""}
    if len(allprods)==0 or len(query)<1:
        params={"allprods":allprods,"msg":"Please Make Sure To Enter Relevent Query"}

    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')
    # return HttpResponse("we are at about")


def contact(request):
    thank=False
    if request.method=="POST":
        # print(request)
        name=request.POST.get("name","")
        email=request.POST.get("email","")
        subject=request.POST.get("subject","")
        desc=request.POST.get("desc","")
        contact=Contact(name=name,email=email,subject=subject,description=desc)
        contact.save()
        thank=True
        print(name,"\n",email,"\n",subject,"\n",desc )
    return render(request,'shop/contact.html',{"thank":thank})

def prodview(request,myid):
    products=product.objects.filter(id=myid)
    print(products)
    return render(request,'shop/prodview.html',{"accessprod":products[0]})
def checkout(request):

    if request.method=="POST":
        # print(request)
        item_json=request.POST.get("itemsJSON"," ")
        name=request.POST.get("name","")
        amount=request.POST.get("amount","")
        email=request.POST.get("email","")
        address=request.POST.get("address1","")+", "+request.POST.get("address2","")
        city=request.POST.get("city","")
        state=request.POST.get("state","")
        zip_code=request.POST.get("zip","")  
        phone=request.POST.get("phone","")  
        order=Orders(item_json=item_json,name=name,email=email,address=address,city=city,state=state,zip_code=zip_code,phone=phone,amount=amount)
        order.save()

        id=order.order_id
        
        update=Order_update(order_id=order.order_id, update_desc='your order has been placed')
        update.save()
        thank=True
        return render(request,'shop/checkout.html', {"thank":thank,"id":id})



    return render(request,'shop/checkout.html')



def tracker(request):
    if request.method=="POST":
        # print(request)
        
        order_id=request.POST.get("order_id","")
        email=request.POST.get("email","")
        # return HttpResponse(f"{order_id} and {email}")
        try:
            order=Orders.objects.filter(order_id=order_id,email=email)
            if len(order)>0:
                update=Order_update.objects.filter(order_id=order_id)
                updates=[]
                for item in update:
                    updates.append({"text": item.update_desc,"time":item.timestamp})
                    response=json.dumps([updates,order[0].item_json],default=str)
                return HttpResponse(response)
            else:
                return HttpResponse("{}")
        except Exception as e:
                return HttpResponse("{}")
            




    return render(request,'shop/tracker.html')