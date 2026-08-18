# Feliz cumpleaños, Daniela

Tarjeta HTML interactiva estilo sobre VIP, pensada para **teléfono** y para enviarse por **WhatsApp como un solo archivo**.

## Flujo recomendado (WhatsApp)

1. Pon la foto en:

```text
cumple-daniela/assets/daniela.jpg
```

2. Genera el HTML autocontenido:

```bash
cd cumple-daniela
python3 build-whatsapp.py
```

3. Descarga / toma el archivo generado:

```text
cumple-daniela/feliz-cumple-daniela.html
```

4. Envíalo por WhatsApp.

La foto va **embebida dentro del HTML** (no usa enlace de GitHub). Daniela solo recibe un archivo; no ve tu repositorio. Funciona aunque no tenga internet al abrirlo.

> ¿Por qué no cargar la foto “desde el repo”?  
> Eso pondría una URL de GitHub dentro del HTML. En el chat no se vería, pero quedaría en el archivo, necesitaría internet y podría fallar. Embebida es más limpio y seguro para WhatsApp.

## Desarrollo / vista previa

- Edita `index.html`
- Usa la foto local en `assets/daniela.jpg`
- Abre `index.html` en el navegador

## Detalles móviles

- Scroll natural en la carta
- Safe areas de iPhone
- Targets táctiles amplios
- Tipografía legible en pantalla chica
