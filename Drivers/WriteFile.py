import openpyxl


wk = openpyxl.Workbook()
sh = wk.active
sh.title = "Test"


print(sh.title)

sh['A2'].value="test.com"

#2nd Sheet is Created
wk.create_sheet(title="TestingW")
sh1 = wk['TestingW']
sh1['A2']='9988776655'

#Saving
wk.save("E:\\Test.xlsx")
