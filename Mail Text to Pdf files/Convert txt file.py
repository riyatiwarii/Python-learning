from fpdf import FPDF
def covert_textfile(file):
    pdf = FPDF()
    pdf.add_page()
    for text in file:
        if len(text) <= 20:
            pdf.set_font("Arial","B",size=18)
            pdf.cell(w=200,h=10,txt=text,ln=1,align="C")
        else:
            pdf.set_font("Arial",size=15)
            pdf.multi_cell(w=0, h=10, txt=text)
    pdf.output("outputfile.pdf")
file = open("readfile.txt","r")
covert_textfile(file)

