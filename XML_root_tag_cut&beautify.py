from xml.etree import ElementTree
from xml.dom import minidom

xml_file = open("put_your_file_name_here.xml", "rt+", encoding="utf-8") #open file with read+write mode as a text
root = ElementTree.parse(xml_file).getroot() #checking root tag
print(root)
if "put_your_root_tag_name_here" not in str(root): #make sure that the searchable tag, not root tag in the beginning of the modification
 for item in root.findall("put_your_root_tag_name_here"): #find the necessary internal tag
    out_content = minidom.parseString(ElementTree.tostring(item)).toxml() #beautify the flat file to the XML structure 
    out_content = str(out_content.replace("ns0:","g:").replace("""<?xml version="1.0" ?>""","")).replace("xmlns:ns0","xmlns:g") #this part is optional,
    #specify whether to replace "ns0:" by default with the original boundaries, for example, with "g:"
 xml_file.seek(0)  # sets point at the beginning of the file
 xml_file.truncate(20)  # clear previous content
 xml_file.write(out_content) #write to the file the new content
 xml_file.close()
else:
  xml_file.close()
