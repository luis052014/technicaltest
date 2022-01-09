

def total_sale(request):
    total = 0
    if request.user.is_authenticated:
        if "sale" in request.session.keys():
            for key, value in request.session["sale"].items():

              

                total=total+float(value["acumulated"])*value["quantity"]

    return {"total_sale": total}