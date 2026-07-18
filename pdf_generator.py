from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os
import re



def clean_filename(name):

    name = name.lower()

    name = re.sub(
        r'[^a-zA-Z0-9 ]',
        '',
        name
    )

    name = name.replace(
        " ",
        "_"
    )

    return name[:80]





def create_pdf(data, topic="AI_Report"):


    folder="reports"

    os.makedirs(
        folder,
        exist_ok=True
    )


    filename = clean_filename(topic)


    pdf_path = os.path.join(
        folder,
        f"{filename}.pdf"
    )


    doc = SimpleDocTemplate(
        pdf_path
    )


    styles=getSampleStyleSheet()


    content=[]


    title=Paragraph(
        f"AI Research Report: {topic}",
        styles["Title"]
    )


    content.append(title)

    content.append(
        Spacer(1,20)
    )


    for line in data.split("\n"):


        content.append(

            Paragraph(
                line,
                styles["BodyText"]
            )

        )


    doc.build(content)


    return pdf_path