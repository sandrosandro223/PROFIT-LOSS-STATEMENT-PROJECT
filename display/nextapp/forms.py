from django import forms

class Form1(forms.Form):
    field1_form1 = forms.IntegerField(label='Sales revenue', required=True)
    field2_form1 = forms.IntegerField(label='Other revenue',required=True)
    field3_form1 = forms.IntegerField(label='Cost of goods sold', required=True)
    field4_form1 = forms.IntegerField(label='(Other relevant costs)', required=False, help_text='OPERATING EXPENSES:')
    
    field5_marketing = forms.IntegerField(label = 'Marketing', required=False)
    field5_salaries_and_wages = forms.IntegerField(label = 'Salaries And Wages', required=False)
    field5_rent = forms.IntegerField(label='Rent', required=False)
    field5_utilities = forms.IntegerField(label = 'Utilities', required=False)
    field5_depreciation = forms.IntegerField(label='Depreciation', required=False)
    field5_Other_Operating_Expenses = forms.IntegerField(label='Other Operating Expenses', required=False, help_text='Non-Operating Income/Expenses:')
    field6_interest_income = forms.IntegerField(label='Interest Income ',required=False)
    field6_interest_expense = forms.IntegerField(label='Interest expense', required=False)
    


                                      

