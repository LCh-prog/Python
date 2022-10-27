from xml.etree import ElementTree
from xml.dom import minidom

xml_file = open("put_your_file_name_here.xml", "rt+", encoding="utf-8")
root = ElementTree.parse(xml_file).getroot()
print(root)
if "channel" not in str(root):
 for item in root.findall("put_your_root_tag_name_here"):
    out_content = minidom.parseString(ElementTree.tostring(item)).toxml()
    out_content = str(out_content.replace("ns0:","g:").replace("""<?xml version="1.0" ?>""","")).replace("xmlns:ns0","xmlns:g")
 xml_file.seek(0)  # sets  point at the beginning of the file
 xml_file.truncate(20)  # Clear previous content
 xml_file.write(out_content)
 xml_file.close()
else:
  xml_file.close()
