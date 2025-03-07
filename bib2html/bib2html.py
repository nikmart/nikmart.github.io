import os
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode

# Function to parse a single BibTeX file and return a list of entries
def parse_bibtex(file_path):
    with open(file_path) as bibtex_file:
        parser = BibTexParser()
        parser.customization = convert_to_unicode
        bib_database = bibtexparser.load(bibtex_file, parser=parser)
    return bib_database.entries

# Function to generate HTML for a list of publications of a certain type
def generate_html_for_publication_type(entries, publication_type):
    html = f'<h2>{publication_type.capitalize()}</h2>\n<ul>'
    for entry in entries:
        # Simplified representation, you might want to include more fields
        title = entry.get('title', 'No title')
        authors = entry.get('author', 'Unknown authors')
        year = entry.get('year', 'No year')
        html += f'<li><strong>{title}</strong> - {authors} ({year})</li>\n'
    html += '</ul>\n'
    return html

# Main script to process each .bib file in a specified folder and generate an HTML file
def main(folder_path):
    publication_types = {}
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.bib'):
            entries = parse_bibtex(os.path.join(folder_path, file_name))
            for entry in entries:
                entry_type = entry.get('ENTRYTYPE', 'other')
                if entry_type not in publication_types:
                    publication_types[entry_type] = []
                publication_types[entry_type].append(entry)
    
    html_content = '<html><head><title>Publications</title></head><body>\n'
    for publication_type, entries in publication_types.items():
        html_content += generate_html_for_publication_type(entries, publication_type)
    html_content += '</body></html>'
    
    with open('publications.html', 'w') as html_file:
        html_file.write(html_content)

if __name__ == '__main__':
    # Replace 'your/folder/path' with the actual folder path
    main('your/folder/path')
