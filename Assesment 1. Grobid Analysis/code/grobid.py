import os
import shutil
from grobid_client.grobid_client import GrobidClient
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re

# Defino funciones auxiliares:
def get_abstract(root):
    abstract_tag = root.find(".//{http://www.tei-c.org/ns/1.0}abstract")
    if abstract_tag:
        abstract_text = ''.join(abstract_tag.itertext()).strip()
    else:
        abstract_text = None
    return abstract_text

def save_wordcloud(abstract, path):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(abstract)
    wordcloud.to_file(path)

def number_of_figures(root):
    figures  = 0
    for div in root.findall(".//{http://www.tei-c.org/ns/1.0}figure"):
        figures += 1
    return figures

def get_links(root):
    links = []
    if root.text:
        links.extend(re.findall(r'https://\S+', root.text))
    for child in root:
        links.extend(get_links(child))
        if child.tail:
            links.extend(re.findall(r'https://\S+', child.tail))
    return links

def save_links(links, path):
    with open(path, 'w') as file:
        for link in links:
            file.write(f'{link}\n')


def save_histogram(dict, path):
    keys = list(dict.keys())
    values = list(dict.values())
    plt.figure(figsize=(8, 10))
    plt.bar(keys, values, color='blue')
    plt.xlabel('Articles')
    plt.ylabel('Number of Figures')
    plt.title('Number of Figures per article')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(path)


dir = '../output' 
for f in os.listdir(dir): #Vacío la carpeta de outputs
    path = os.path.join(dir, f)
    if os.path.isfile(path):
        os.remove(path)
    else:
        shutil.rmtree(path)

os.mkdir(os.path.join(dir, "XMLs")) #Creo la carpeta donde iran los XMLs

client = GrobidClient(config_path="./config.json")
client.process("processFulltextDocument", "../input", output="../output/XMLs/", consolidate_citations=True, tei_coordinates=True) #Genero los XMLs outputs

n_figures = {}
for file in os.listdir("../output/XMLs"):
    if file.endswith('.xml'):
        os.mkdir(os.path.join(dir, file[:-15]))

        root = ET.parse("../output/XMLs/"+ file).getroot()

        abstract = get_abstract(root)
        save_wordcloud(abstract, os.path.join(dir, file[:-15], "wordcloud.png"))

        n_figures[file[:-15]] = number_of_figures(root)

        links = get_links(root)
        save_links(links, os.path.join(dir, file[:-15], "links.txt"))



save_histogram(n_figures, "../output/histogram.png")