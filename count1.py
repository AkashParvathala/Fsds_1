import glob
import lxml.etree as et
c = 0
c1=0
for f in glob.glob("C:/Users/akash/OneDrive - Purecode Software/Documents/management_templates/*.xml"):
    tree = et.parse(f)
    result = len(tree.xpath("object"))
    #print(f"number of components in {f} is : ",result)
    c1+=result
    c +=1
print("Number of templates : ",c)
print("Number of components : ",c1)