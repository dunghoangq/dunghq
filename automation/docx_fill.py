# LIBRARIES
from docxtpl import DocxTemplate

doc = DocxTemplate('my_word_template.docx')

# the keys in context will replace ones in the template with their values.
# Keys in template must be put in {{}}
# i.e. {{company_name}}
context = {
    'company_name': 'Game of Thrones'
}
doc.render(context)
doc.save('generated_file.docx')