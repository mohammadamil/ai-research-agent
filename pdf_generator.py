from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os



def create_pdf(content, filename):


    os.makedirs(
        "reports",
        exist_ok=True
    )


    file_path = f"reports/{filename}.pdf"



    doc = SimpleDocTemplate(
        file_path
    )


    styles=getSampleStyleSheet()


    story=[]


    story.append(
        Paragraph(
            content,
            styles["Normal"]
        )
    )


    doc.build(story)



    return file_path