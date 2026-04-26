# Foundation AI Advisory Outlook Signature

Clean, Outlook-ready email signature files for Ben DeMichael at Foundation AI Advisory.

## Closing Signature Text

Ben DeMichael  
Managing Partner & Principal Advisor  
Foundation AI Advisory  
Business First. AI Applied.  
m. (440)-503-2337  
FoundationAIAdvisory.com

## Files

- `signature.html` - the production Outlook signature HTML.
- `signature.txt` - a plain-text fallback signature for clients that strip HTML.
- `preview.html` - a browser preview that shows the signature with the included logo asset.
- `assets/faa-logo-trimmed-300.png` - the real Foundation AI Advisory logo, trimmed from the supplied 300px file.

## Outlook HTML

Use this HTML for Outlook. It is table-based, inline-styled, and uses a clickable website URL plus a QR code linked to the same site.

```html
<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;font-family:Arial,Helvetica,sans-serif;color:#2f3a40;">
  <tr>
    <td valign="middle" style="padding:0 28px 0 0;border-right:2px solid #2f66b3;width:250px;">
      <table role="presentation" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;width:250px;">
        <tr>
          <td align="center" style="padding:0 0 10px 0;">
            <img src="assets/faa-logo-trimmed-300.png" width="220" alt="Foundation AI Advisory" border="0" style="display:block;border:0;outline:none;text-decoration:none;width:220px;height:auto;">
          </td>
        </tr>
        <tr>
          <td align="center" style="font-size:17px;line-height:22px;mso-line-height-rule:exactly;color:#2f3a40;padding-top:8px;">
            Business First. <span style="color:#2f66b3;">AI Applied.</span>
          </td>
        </tr>
      </table>
    </td>
    <td valign="middle" style="padding:0 26px 0 28px;width:385px;">
      <table role="presentation" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;width:385px;">
        <tr>
          <td style="font-size:28px;line-height:34px;mso-line-height-rule:exactly;font-weight:700;color:#2f3a40;padding:0 0 4px 0;">Ben DeMichael</td>
        </tr>
        <tr>
          <td style="font-size:20px;line-height:26px;mso-line-height-rule:exactly;color:#2f3a40;padding:0 0 20px 0;">Managing Partner &amp; Principal Advisor</td>
        </tr>
        <tr>
          <td style="font-size:22px;line-height:26px;mso-line-height-rule:exactly;font-weight:700;color:#2f66b3;text-transform:uppercase;padding:0 0 6px 0;">Foundation AI Advisory</td>
        </tr>
        <tr>
          <td style="font-size:20px;line-height:26px;mso-line-height-rule:exactly;color:#2f3a40;padding:0 0 14px 0;">Business First. <span style="color:#2f66b3;">AI Applied.</span></td>
        </tr>
        <tr>
          <td style="padding:0 0 16px 0;">
            <table role="presentation" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;">
              <tr>
                <td style="height:2px;width:86px;background-color:#2f66b3;font-size:0;line-height:0;">&nbsp;</td>
                <td style="height:2px;width:34px;background-color:#c6d7ee;font-size:0;line-height:0;">&nbsp;</td>
              </tr>
            </table>
          </td>
        </tr>
        <tr>
          <td style="padding:0 0 8px 0;font-size:19px;line-height:25px;mso-line-height-rule:exactly;color:#2f3a40;">
            <span style="display:inline-block;width:28px;height:28px;line-height:28px;text-align:center;border-radius:14px;background-color:#2f66b3;color:#ffffff;font-size:16px;font-weight:bold;">m</span>
            <span style="padding-left:10px;">(440)-503-2337</span>
          </td>
        </tr>
        <tr>
          <td style="padding:0;font-size:19px;line-height:25px;mso-line-height-rule:exactly;color:#2f66b3;">
            <span style="display:inline-block;width:28px;height:28px;line-height:28px;text-align:center;border-radius:14px;background-color:#2f66b3;color:#ffffff;font-size:16px;font-weight:bold;">w</span>
            <a href="https://FoundationAIAdvisory.com" target="_blank" style="padding-left:10px;color:#2f66b3;text-decoration:none;">FoundationAIAdvisory.com</a>
          </td>
        </tr>
      </table>
    </td>
    <td valign="middle" style="padding:0 0 0 8px;width:85px;">
      <a href="https://FoundationAIAdvisory.com" target="_blank" style="text-decoration:none;">
        <img src="https://api.qrserver.com/v1/create-qr-code/?size=85x85&margin=4&data=https%3A%2F%2FFoundationAIAdvisory.com" width="85" height="85" alt="Foundation AI Advisory website QR code" border="0" style="display:block;border:0;outline:none;text-decoration:none;width:85px;height:85px;">
      </a>
    </td>
  </tr>
</table>
```

## Add It To Outlook

1. Open `signature.html` in a browser.
2. Select the rendered signature in the browser and copy it.
3. In Outlook, go to **File > Options > Mail > Signatures**.
4. Create a new signature, paste the copied signature into the editor, and save it.
5. Send a test email to confirm the website link and QR code work.

For a production business deployment, host `assets/faa-logo-trimmed-300.png` under your own domain or GitHub Pages and update that image `src` to the hosted URL. The visible website URL and QR code already link to `https://FoundationAIAdvisory.com`.
