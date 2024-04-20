# views.py
from django.shortcuts import render
from .forms import Form1

def my_view(request):
    Total_Revenue = None
    Total_Cost_Of_Goods_Sold = None
    Gross_Profit = None
    Total_Operating_Expenses = None
    Operating_Income = None
    Total_Non_Operating_Income_Expenses = None
    Net_income_before_taxes = None
    Income_Tax = None
    Net_Income = None
    lst = []
    if request.method == 'POST':
        form1 = Form1(request.POST)
        

        if form1.is_valid():
            num1 = form1.cleaned_data.get('field1_form1')
            num2 = form1.cleaned_data.get('field2_form1')
            num3 = form1.cleaned_data.get('field3_form1')
            num4 = form1.cleaned_data.get('field4_form1')
            num5 = form1.cleaned_data.get('field5_marketing')
            num6 = form1.cleaned_data.get('field5_salaries_and_wages')
            num7= form1.cleaned_data.get('field5_rent')
            num8 = form1.cleaned_data.get('field5_utilities')
            num9 = form1.cleaned_data.get('field5_depreciation')
            num10 = form1.cleaned_data.get('field5_Other_Operating_Expenses')
            lst = [num5,num6,num7,num8,num9,num10]
            num11 = form1.cleaned_data.get('field6_interest_income')
            num12 = form1.cleaned_data.get('field6_interest_expense')
            
            if num1 is not None and num2 is not None:
                Total_Revenue = num1 + num2
            
            if  num4 is None:
                Total_Cost_Of_Goods_Sold = num3 + int(0)

            if num3 is not None and num4 is not None:
                Total_Cost_Of_Goods_Sold = num3 + num4
            Gross_Profit = Total_Revenue - Total_Cost_Of_Goods_Sold
            for i in range(len(lst)):
                 if lst[i] is None:
                    lst[i] = int(0)
            if num11 is None:
                num11 = int(0)
            if num12 is None:
                num12 = int(0)
           
            Total_Operating_Expenses = int(sum(lst))
            Operating_Income = Gross_Profit - Total_Operating_Expenses
            Total_Non_Operating_Income_Expenses = num11-num12
            Net_income_before_taxes = Operating_Income + Total_Non_Operating_Income_Expenses
            Net_income_before_taxes = int(Net_income_before_taxes)
            if Net_income_before_taxes < 1000:
                Income_Tax = 10
            else:
                Income_Tax = 20
            Net_Income = Net_income_before_taxes - (Net_income_before_taxes*Income_Tax/100)
           

            

       
    else:
        form1 = Form1()
        

    return render(request, 'base.html', {'form1': form1,  'Total_Revenue': Total_Revenue, 'Total_Cost_Of_Goods_Sold':Total_Cost_Of_Goods_Sold,
                                         'Gross_Profit':Gross_Profit,'Total_Operating_Expenses':Total_Operating_Expenses,
                                           'Operating_Income': Operating_Income, 'Total_Non_Operating_Income_Expenses':Total_Non_Operating_Income_Expenses,
                                           "Net_income_before_taxes": Net_income_before_taxes,
                                           'Income_Tax':Income_Tax,
                                           'Net_Income':Net_Income})

