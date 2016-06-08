import docx

document = docx.Document()
a = document.styles
b = a["Normal"]
print(b._element.__dir__())
b._element._add_pPr()
b._element.get_or_add_pPr()
b._element.pPr.get_or_add_shd()
b._element.pPr.shd_fill
b._element.pPr.shd_fill = "FEF2E8"

document.add_paragraph("asdsadsad", style="List Number")
document.save("123.docx")