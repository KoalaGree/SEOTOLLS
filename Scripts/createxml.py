from typing import List
import xml.etree.ElementTree as ET 
import datetime
from xml.dom import minidom


listurl = input(" Url List.txt ? ")
root = ET.Element('urlset')
with open(listurl, 'r') as list:
    line = list.read().splitlines()
    for lines in line:
        urlelement = ET.SubElement(root, 'url')
        name = ET.SubElement(urlelement, 'loc')
        name.text = lines
        dates = ET.SubElement(urlelement, 'lasmod')
        dates.text = str(datetime.date.today())
        color = ET.SubElement(urlelement, 'priority')
        color.text = '1.0'

xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
with open("Sitemap.xml", "w") as f:
    f.write(xmlstr)