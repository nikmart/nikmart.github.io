import bibtexparser
from bibtexparser.bparser import BibTexParser

def bibtex_to_html(bibtex_file):
    """
    Convert a BibTeX file to HTML.

    Args:
        bibtex_file (str): Path to the BibTeX file.

    Returns:
        str: HTML representation of the BibTeX entries.
    """
    parser = BibTexParser()
    with open(bibtex_file, 'r') as file:
        bib_database = bibtexparser.load(file, parser)

    html = '<ul>\n'
    for entry in bib_database.entries:
        html += '  <li>\n'
        html += '    <h2>{}</h2>\n'.format(entry['title'])
        html += '    <p>Authors: {}\n'.format(', '.join(entry['author'].split(' and ')))
        html += '    <p>Year: {}\n'.format(entry['year'])
        html += '    <p>Journal: {}\n'.format(entry.get('journal', ''))
        html += '    <p>Pages: {}\n'.format(entry.get('pages', ''))
        html += '    <p>DOI: <a href="{}">{}</a>\n'.format(entry.get('doi', ''), entry.get('doi', ''))
        html += '  </li>\n'
    html += '</ul>\n'

    return html

# Example usage
bibtex_file = 'example.bib'
html = bibtex_to_html(bibtex_file)
print(html)