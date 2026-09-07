import json, pathlib, html

REPOS = [
    ("wallcal",            "Calendar wallpapers rendered from a URL",        "python · fastapi · pillow"),
    ("soniox-openai-shim", "OpenAI transcription endpoint backed by Soniox",  "python · docker · self-hosted"),
    ("cloud-lab",          "End-to-end automated VPN infrastructure",         "terraform · hetzner · cloudflare"),
    ("local-lab",          "Multi-cluster Kubernetes as code",                "talos · proxmox · flux · argo cd"),
    ("dotfiles",           "Nix-managed dev environment",                     "nix · macos · linux · neovim"),
    ("cv.cosmdandy.dev",   "CV-as-Code",                                      "latex · jinja2 · github actions"),
    ("blog.cosmdandy.dev", "Infrastructure notes",                            "quartz · obsidian · cloudflare"),
    ("cosmdandy.dev",      "Personal landing page",                           "html · css · svg"),
    ("pxe-server",         "Netboot bare metal from a laptop",                "ansible · lima · tftp · dhcp"),
    ("template-devpod",    "Starting point for my projects",                  "devcontainer · devpod · sops"),
    (".github",            "Default community health files",                  "security · contributing · templates"),
]

# Same visual language as cosmdandy.dev/assets/og.svg: black ground, dot grid,
# blurred gradient halo, Inter. Repo name replaces the person's name.
TPL = """<svg width="1200" height="630" viewBox="0 0 1200 630" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="halo" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%%"   stop-color="#ff3264" stop-opacity="0.55"/>
      <stop offset="25%%"  stop-color="#ff5096" stop-opacity="0.40"/>
      <stop offset="50%%"  stop-color="#7828dc" stop-opacity="0.30"/>
      <stop offset="75%%"  stop-color="#00dcff" stop-opacity="0.40"/>
      <stop offset="100%%" stop-color="#00ffff" stop-opacity="0.55"/>
    </linearGradient>
    <filter id="blur" x="-50%%" y="-50%%" width="200%%" height="200%%">
      <feGaussianBlur stdDeviation="120"/>
    </filter>
    <pattern id="dots" x="0" y="0" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#93a1a1" fill-opacity="0.18"/>
    </pattern>
  </defs>

  <rect width="1200" height="630" fill="#000"/>
  <rect width="1200" height="630" fill="url(#dots)"/>
  <g filter="url(#blur)">
    <rect x="-200" y="-200" width="900" height="900" fill="url(#halo)"/>
  </g>

  <text x="80" y="290" font-family="Inter, -apple-system, system-ui, sans-serif"
        font-weight="600" font-size="%(size)d" fill="#ededed" letter-spacing="-2.5">%(name)s</text>
  <text x="80" y="345" font-family="Inter, -apple-system, system-ui, sans-serif"
        font-weight="400" font-size="32" fill="#93a1a1">%(tag)s</text>
  <text x="80" y="400" font-family="Inter, -apple-system, system-ui, sans-serif"
        font-weight="400" font-size="24" fill="#586e75" letter-spacing="0.5">%(stack)s</text>

  <line x1="80" y1="540" x2="116" y2="540" stroke="#586e75" stroke-width="1.5"/>
  <text x="132" y="546" font-family="Inter, -apple-system, system-ui, sans-serif"
        font-weight="400" font-size="22" fill="#586e75" letter-spacing="0.5">github.com/CosmDandy</text>
</svg>
"""

out = pathlib.Path('.')
for name, tag, stack in REPOS:
    # long names would run off the canvas at 92px
    size = 92 if len(name) <= 14 else (72 if len(name) <= 19 else 62)
    svg = TPL % {"name": html.escape(name), "tag": html.escape(tag),
                 "stack": html.escape(stack), "size": size}
    fn = name.replace('.', '_').lstrip('_') or 'dotgithub'
    (out / f"{fn}.svg").write_text(svg, encoding='utf-8')
print(json.dumps([r[0] for r in REPOS]))
