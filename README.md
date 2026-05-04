# Foundation AI Advisory Outlook Signatures

Outlook-ready email signatures for the Foundation AI Advisory team. Each
signature is plain HTML built from tables and inline styles for maximum
compatibility with the Outlook (Word) rendering engine, including dark mode.

## Signatures

| Person | Role | Preview |
| --- | --- | --- |
| Ben DeMichael | Managing Partner | [ben-demichael/preview.html](https://benjiai47.github.io/faa_outlook_signature/ben-demichael/preview.html) |
| Jason Kapcar | Partner & Chief AI Officer | [jason-kapcar/preview.html](https://benjiai47.github.io/faa_outlook_signature/jason-kapcar/preview.html) |
| Thomas Wagenberg | AI Business Analyst, Finance & Operations | [thomas-wagenberg/preview.html](https://benjiai47.github.io/faa_outlook_signature/thomas-wagenberg/preview.html) |

The landing page at
[preview.html](https://benjiai47.github.io/faa_outlook_signature/preview.html)
links to all three.

## Repository layout

```
.
├── README.md
├── build_signatures.py        # regenerates each person's HTML from one template
├── preview.html               # index page linking to all signatures
├── assets/
│   ├── faa-logo-dualmode-300.png   # logo with soft white halo (works on light + dark)
│   ├── faa-logo-transparent-300.png
│   ├── faa-logo-trimmed-300.png    # original logo on white background
│   ├── badge-e.png            # @ badge for the email row
│   ├── badge-m.png            # mobile badge
│   ├── badge-w.png            # website badge
│   └── badge-in.png           # LinkedIn badge
├── ben-demichael/
│   ├── signature.html         # paste-ready, references hosted assets
│   └── preview.html           # browser preview using relative asset paths
├── jason-kapcar/
│   ├── signature.html
│   └── preview.html
└── thomas-wagenberg/
    ├── signature.html
    └── preview.html
```

`signature.html` files use absolute URLs that point at the GitHub Pages
host so the images load no matter where the signature is pasted.
`preview.html` files use relative paths so they work both locally and on
Pages.

## Add a signature to Outlook

1. Open the appropriate preview URL in an **incognito / private window**
   (so you bypass the GitHub Pages CDN cache and any prior browser cache):
   - https://benjiai47.github.io/faa_outlook_signature/ben-demichael/preview.html
   - https://benjiai47.github.io/faa_outlook_signature/jason-kapcar/preview.html
   - https://benjiai47.github.io/faa_outlook_signature/thomas-wagenberg/preview.html
2. Click inside the white panel and press **Ctrl+A** to select the whole
   signature, then **Ctrl+C** to copy.
3. In Outlook (web or new desktop), open **Settings → Mail → Signatures**
   (or **File → Options → Mail → Signatures** in classic Outlook).
4. Create or edit a signature, paste with **Ctrl+V**, and **Save**.
5. Send a test email to yourself and verify in both light and dark mode:
   - The logo stays legible (the halo gives the dark wordmark contrast).
   - The `@`, `m`, `w`, and `in` badges sit beside their text, not above.
   - All links open the correct destination.

## Editing the signatures

All three signatures are generated from a single template inside
`build_signatures.py`. To change a contact detail, the layout, or the
LinkedIn label format:

1. Edit the `PEOPLE` list (or the `SIG_TEMPLATE` string) in
   `build_signatures.py`.
2. Run `python3 build_signatures.py` from the repo root.
3. Commit the regenerated `signature.html` and `preview.html` files.

## Design notes

- **Layout** is a single outer table with two cells: logo on the left
  (with a thin blue divider), text block on the right.
- **Contact rows** each use a nested 2-cell micro-table so the badge
  icon stays aligned next to its text. Outlook's Word engine ignores
  `display:inline-block` and `border-radius` on spans, so the original
  inline-block circle pills broke alignment in Outlook -- the PNG
  badges + micro-tables fix that.
- **Dark mode** is handled by the dual-mode logo
  (`faa-logo-dualmode-300.png`). Most email clients auto-invert dark
  text on dark backgrounds but never invert images, so the logo carries
  a soft white halo that is invisible on white and provides contrast on
  dark.
- **Branding palette**: dark slate text `#2f3a40`, FAA blue `#2f66b3`,
  light blue accent `#c6d7ee`, muted gray for the subtitle line
  `#5a6770`.
- **Font stack**: `Arial, Helvetica, sans-serif` -- safe everywhere.
  Swap to `'Segoe UI', Arial, Helvetica, sans-serif` if you want native
  Outlook Windows look.
