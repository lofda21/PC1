mime_types = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}
archivo = input("Introduce el nombre del archivo: ").lower()
extension = archivo[archivo.rfind('.'):]
tipo_mime = mime_types.get(extension, "application/octet-stream")
print(f"El tipo MIME es: {tipo_mime}")
