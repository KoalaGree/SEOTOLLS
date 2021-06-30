from sys import path
from xml.dom import minidom
import datetime
import os
import os.path
doc = minidom.Document()

root = doc.createElement('urlset')
doc.appendChild(root)

leaf = doc.createElement('url')
txt = input("Url Input ? ")
text = doc.createTextNode(txt)
leaf.appendChild(text)
root.appendChild(leaf)

leaf2 = doc.createElement('lastmod')
tgl = datetime.datetime.now()
intgl = doc.createTextNode(str(tgl))
leaf2.appendChild(intgl)
root.appendChild(leaf2)

leaf3 = doc.createElement('priority')
prior = doc.createTextNode('1.0')
leaf3.appendChild(prior)
root.appendChild(leaf3)

xml_str = doc.toprettyxml(indent="\t")
with open("minidom_example.xml", "+a") as f:
    f.write(xml_str)
    f.write('\n')
    if os.path.exists('minidom_example.xml'):
        leaf = doc.createElement('url')
        txt = input("Url Input ? ")
        text = doc.createTextNode(txt)
        leaf.appendChild(text)
        root.appendChild(leaf)

        leaf2 = doc.createElement('lastmod')
        tgl = datetime.datetime.now()
        intgl = doc.createTextNode(str(tgl))
        leaf2.appendChild(intgl)
        root.appendChild(leaf2)

        leaf3 = doc.createElement('priority')
        prior = doc.createTextNode('1.0')
        leaf3.appendChild(prior)
        root.appendChild(leaf3)

        to_xml = doc.toprettyxml(indent='\t')
        with open("minidom_example.xml", "+a") as g:
            g.write(to_xml)
            g.write('\n')
