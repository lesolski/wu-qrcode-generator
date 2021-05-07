# QR Code generator for Business and Economics University in Vienna (WU) <br>

This is a simple CLI program for generating custom QR Codes with embedded Wirtschaftsuniversitaet Wien (WU) logo init.

Positional argument: `text` <br>
Optional arguments: 
- `--color` default is `#000000` i.e. black, accepts any hex color code
- `--path` default is `./qrcode.png`
- `--size` default is `200x200` first number is width and second number is height

<br></br>
Example usage:
 <br><br>
`python3 qrcodes.py https://www.github.com/djyra --color "#008198" --path samples/wu-blue.png --size 200x200`
<br></br>
This will produce qr code with WU blue color as seen below. <br><br>
![WU Blue QR code](samples/wu-blue.png)
<br></br>
Other examples:
<br></br>
![WU default QR code](samples/default.png) ![WU Teams QR code](samples/teams.png) ![WU Zoom Invite QR code](samples/zoom.png) ![WU WhatsApp Invite QR code](samples/whatsapp.png)


