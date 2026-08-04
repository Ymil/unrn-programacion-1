# Plantilla Marp UNRN

Tema Marp para armar presentaciones en Markdown con un estilo similar a los PDFs de la cursada.

## Uso

Editar `clase-template.md`. En VS Code, la preview de Marp toma el tema desde `.vscode/settings.json`.

Exportar a PowerPoint:

```bash
npx @marp-team/marp-cli recursos/marp/clase-template.md --theme recursos/marp/unrn.css --allow-local-files --pptx -o clase.pptx
```

Exportar a PDF:

```bash
npx @marp-team/marp-cli recursos/marp/clase-template.md --theme recursos/marp/unrn.css --allow-local-files --pdf -o clase.pdf
```

Live preview:

```bash
npx @marp-team/marp-cli -s -I . --theme-set recursos/marp/unrn.css --html
```

Abrir la clase desde el navegador, por ejemplo:

```text
http://localhost:8080/clases/clase-14/material/clase-14.md
```

## Diapositivas utiles

- Portada: `<!-- _class: title -->`
- Separador oscuro o repaso: `<!-- _class: inverse -->`
- Diapositiva densa con codigo: `<!-- _class: compact -->`

Para una clase nueva, copiar `clase-template.md`, cambiar el titulo y reemplazar el contenido entre separadores `---`.
