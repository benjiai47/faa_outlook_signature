#!/usr/bin/env python3
"""Generate signature.html and preview.html for each Foundation AI Advisory partner."""
import os

SIG_TEMPLATE = """<!--
  Foundation AI Advisory Outlook signature -- {name}
  Sized ~62% of the original, table-only layout for Outlook (Word) compatibility.
-->
<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;font-family:Arial,Helvetica,sans-serif;color:#2f3a40;">
  <tr>
    <td valign="middle" style="padding:0 18px 0 0;border-right:2px solid #2f66b3;width:160px;">
      <table role="presentation" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;width:160px;">
        <tr>
          <td align="center" style="padding:0 0 6px 0;">
            <img src="{ASSETS}/faa-logo-dualmode-300.png" width="140" alt="Foundation AI Advisory" border="0" style="display:block;border:0;outline:none;text-decoration:none;width:140px;height:auto;">
          </td>
        </tr>
        <tr>
          <td align="center" style="font-size:11px;line-height:14px;mso-line-height-rule:exactly;color:#2f3a40;padding-top:4px;">
            Business First. <span style="color:#2f66b3;">AI Applied.</span>
          </td>
        </tr>
      </table>
    </td>
    <td valign="middle" style="padding:0 0 0 18px;">
      <table role="presentation" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;">
        <tr>
          <td style="font-size:18px;line-height:22px;mso-line-height-rule:exactly;font-weight:700;color:#2f3a40;padding:0 0 2px 0;">
            {name}
          </td>
        </tr>
        <tr>
          <td style="font-size:13px;line-height:16px;mso-line-height-rule:exactly;color:#2f3a40;padding:0 0 2px 0;">
            {title}
          </td>
        </tr>
        <tr>
          <td style="font-size:12px;line-height:15px;mso-line-height-rule:exactly;font-style:italic;color:#5a6770;padding:0 0 8px 0;">
            {subtitle}
          </td>
        </tr>
        <tr>
          <td style="font-size:14px;line-height:17px;mso-line-height-rule:exactly;font-weight:700;color:#2f66b3;text-transform:uppercase;letter-spacing:0.4px;padding:0 0 8px 0;">
            Foundation AI Advisory
          </td>
        </tr>
        <tr>
          <td style="padding:0 0 10px 0;font-size:0;line-height:0;">
            <table role="presentation" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;">
              <tr>
                <td bgcolor="#2f66b3" style="height:2px;width:54px;font-size:0;line-height:0;mso-line-height-rule:exactly;background-color:#2f66b3;">&nbsp;</td>
                <td bgcolor="#c6d7ee" style="height:2px;width:22px;font-size:0;line-height:0;mso-line-height-rule:exactly;background-color:#c6d7ee;">&nbsp;</td>
              </tr>
            </table>
          </td>
        </tr>
        <tr>
          <td style="padding:0 0 5px 0;">
            <table role="presentation" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;">
              <tr>
                <td valign="middle" style="width:18px;">
                  <img src="{ASSETS}/badge-e.png" width="18" height="18" alt="" border="0" style="display:block;border:0;outline:none;text-decoration:none;width:18px;height:18px;">
                </td>
                <td valign="middle" style="padding-left:8px;font-size:13px;line-height:18px;mso-line-height-rule:exactly;">
                  <a href="mailto:{email}" style="color:#2f66b3;text-decoration:none;">{email}</a>
                </td>
              </tr>
            </table>
          </td>
        </tr>
        <tr>
          <td style="padding:0 0 5px 0;">
            <table role="presentation" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;">
              <tr>
                <td valign="middle" style="width:18px;">
                  <img src="{ASSETS}/badge-m.png" width="18" height="18" alt="" border="0" style="display:block;border:0;outline:none;text-decoration:none;width:18px;height:18px;">
                </td>
                <td valign="middle" style="padding-left:8px;font-size:13px;line-height:18px;mso-line-height-rule:exactly;color:#2f3a40;">
                  {phone}
                </td>
              </tr>
            </table>
          </td>
        </tr>
        <tr>
          <td style="padding:0 0 5px 0;">
            <table role="presentation" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;">
              <tr>
                <td valign="middle" style="width:18px;">
                  <img src="{ASSETS}/badge-w.png" width="18" height="18" alt="" border="0" style="display:block;border:0;outline:none;text-decoration:none;width:18px;height:18px;">
                </td>
                <td valign="middle" style="padding-left:8px;font-size:13px;line-height:18px;mso-line-height-rule:exactly;">
                  <a href="https://FoundationAIAdvisory.com" target="_blank" style="color:#2f66b3;text-decoration:none;">FoundationAIAdvisory.com</a>
                </td>
              </tr>
            </table>
          </td>
        </tr>
        <tr>
          <td style="padding:0;">
            <table role="presentation" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;">
              <tr>
                <td valign="middle" style="width:18px;">
                  <img src="{ASSETS}/badge-in.png" width="18" height="18" alt="" border="0" style="display:block;border:0;outline:none;text-decoration:none;width:18px;height:18px;">
                </td>
                <td valign="middle" style="padding-left:8px;font-size:13px;line-height:18px;mso-line-height-rule:exactly;">
                  <a href="{linkedin_url}" target="_blank" style="color:#2f66b3;text-decoration:none;">{linkedin_label}</a>
                </td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
"""

PREVIEW_WRAPPER = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Foundation AI Advisory Signature -- {name}</title>
  <style>
    body {{ margin: 0; min-height: 100vh; display: grid; place-items: center;
           background: #f5f7fa; font-family: Arial, Helvetica, sans-serif; }}
    .frame {{ background: #ffffff; padding: 24px; max-width: 720px; }}
    .hint {{ position: fixed; top: 12px; left: 12px; font-size: 12px; color: #5a6770;
            background: #ffffff; padding: 6px 10px; border-radius: 4px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.08); }}
  </style>
</head>
<body>
  <div class="hint">Select all (Ctrl+A) inside the white panel and copy.</div>
  <main class="frame" aria-label="Email signature preview">
{signature}
  </main>
</body>
</html>
"""

PEOPLE = [
    dict(slug='ben-demichael',
         name='Ben DeMichael',
         title='Managing Partner',
         subtitle='Executive Leadership | Business Strategy &amp; Advisory',
         email='bdemichael@foundationaiadvisory.com',
         phone='(440) 503-2337',
         linkedin_url='https://www.linkedin.com/in/benjamindemichael',
         linkedin_label='Ben on LinkedIn'),
    dict(slug='jason-kapcar',
         name='Jason Kapcar',
         title='Partner &amp; Chief AI Officer',
         subtitle='Executive Leadership | AI Strategy &amp; Implementation',
         email='jkapcar@foundationaiadvisory.com',
         phone='(216) 849-6442',
         linkedin_url='https://www.linkedin.com/in/jasonkapcar',
         linkedin_label='Jason on LinkedIn'),
    dict(slug='thomas-wagenberg',
         name='Thomas Wagenberg',
         title='AI Business Analyst, Finance &amp; Operations',
         subtitle='Client Delivery | AI Advisory Delivery',
         email='twagenberg@foundationaiadvisory.com',
         phone='(440) 804-6477',
         linkedin_url='https://www.linkedin.com/in/thomaswagenberg',
         linkedin_label='Thomas on LinkedIn'),
]

ROOT = '/home/user/faa_outlook_signature'
GH_ASSETS = 'https://benjiai47.github.io/faa_outlook_signature/assets'
RELATIVE_ASSETS = '../assets'

for p in PEOPLE:
    folder = os.path.join(ROOT, p['slug'])
    os.makedirs(folder, exist_ok=True)

    # signature.html (uses absolute hosted asset URLs so paste-into-Outlook works)
    sig = SIG_TEMPLATE.format(ASSETS=GH_ASSETS, **p)
    with open(os.path.join(folder, 'signature.html'), 'w') as f:
        f.write(sig)

    # preview.html (uses relative paths so it works locally + on GitHub Pages)
    sig_rel = SIG_TEMPLATE.format(ASSETS=RELATIVE_ASSETS, **p)
    preview = PREVIEW_WRAPPER.format(name=p['name'], signature=sig_rel)
    with open(os.path.join(folder, 'preview.html'), 'w') as f:
        f.write(preview)

    print(f"wrote {p['slug']}/signature.html and preview.html")
