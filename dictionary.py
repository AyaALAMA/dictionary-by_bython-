
info={"aya":776012202,"alaa":87638973,"nour":97238647}
#-----------------------------------------------------
#update
def update():
    up=input("Enter the name whose number you want to change:")
    upp=input("Enter new numper:")
    int(upp)
    info.update({up:upp})
#-----------------------------------------------------
#add
def add():
    addname=input("Add name:")
    addnum=input("Add number:")
    info[addname]=addnum

#-----------------------------------------------------
#remove
def remove():
    removename=input("Enter the name you want remove:")
    info.pop(removename)
#---------------------------------------------------------------------
def view():
    print(info)
#---------------------------------------------------------------------
listoption=["1-add","2-updat","3-delete","4-view"]
print(f"{listoption[0]}\n{listoption[1]}\n{listoption[2]}\n{listoption[3]}")
#---------------------------------------------------------------------

canedit=0
#ifcondation
while   canedit<=3:
    canedit+=1
    useroption=input("Enter number the option or the option:")

    if  "add"== useroption or "1" == useroption:
        add()
        print (info)
    else:
        print("")
    if  "updat" == useroption or "2" == useroption :
        update()
        print(info)
    elif "delete" == useroption or "3" == useroption:
        remove()   
        print(info)
    elif "view" == useroption or "4" == useroption:
        view()
        print(info)
    
 
    else:
        print(f" Error {useroption} out option")


 


#print(info)