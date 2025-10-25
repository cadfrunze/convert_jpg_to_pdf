import img2pdf

"""
Convertirea fisierelor .jpg in .pdf
"""



fisiere_jpg: list[str] = ["adev_master.jpg", "diploma_licenta.jpg"]

for fisier in fisiere_jpg:
    new_fisier: str = fisier[0: fisier.find(".")]
    with open(f"{new_fisier}.pdf", "wb") as f:
        f.write(img2pdf.convert(f"{new_fisier}.jpg"))
