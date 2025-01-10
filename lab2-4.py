import xml.etree.ElementTree as ET

with open('currency.xml', 'r', encoding='windows-1251', errors='ignore') as file:
    xml_content = file.read()

xml_content = xml_content.replace('\x00', '')  

root = ET.fromstring(xml_content)

currency_dict = {}

for valute in root.findall('Valute'):
    name = valute.find('Name').text
    char_code = valute.find('CharCode').text
    currency_dict[name] = char_code

for name, char_code in currency_dict.items():
    print(f"{name}: {char_code}")