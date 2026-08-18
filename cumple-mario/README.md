# Feliz cumpleaños, Mario

Tarjeta HTML estilo **Valorant** (UI masculina / esports) con animación de kill al abrir el sobre.

## Flujo WhatsApp

1. Pon la foto en:

```text
cumple-mario/assets/mario.jpg
```

2. Genera el HTML autocontenido:

```bash
cd cumple-mario
python3 build-whatsapp.py
```

3. Envía `feliz-cumple-mario.html` por WhatsApp.

## Experiencia

1. Sobre oscuro con sello **ACE**
2. Al tocarlo: flash + slash + kill feed (`Ubani » Mario`) + banner **ACE**
3. Carta con foto, mensaje y firma `atte Ubani`

## Nota

Pensada para teléfono y WebViews de WhatsApp (apertura fiable sin overlays frágiles).
