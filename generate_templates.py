"""
generate_templates.py
Generates 100 distinct HTML templates inside templates/ folder.
Each template uses Jinja2 placeholders for dataset.json fields:
  {{ business_name }}, {{ business_type }}, {{ city }},
  {{ email }}, {{ phone }}, {{ services }}

Run once:
    python generate_templates.py
"""

import os

OUTPUT_DIR = "templates"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# Design token tables – 5 groups × 20 templates each
# ---------------------------------------------------------------------------

# Group A (1-20): Dark glassmorphism — warm amber/orange — food/bakery/cafe
GROUP_A = [
    {"bg": "#1a0a00", "accent": "#ff8c00", "card_bg": "rgba(255,140,0,0.08)", "font": "Playfair Display", "btn": "#ff8c00", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#3d1a00,#ff8c00)"},
    {"bg": "#1a0500", "accent": "#ff6347", "card_bg": "rgba(255,99,71,0.09)", "font": "Merriweather", "btn": "#ff6347", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#2d0000,#ff6347)"},
    {"bg": "#0d0d0d", "accent": "#ffc300", "card_bg": "rgba(255,195,0,0.08)", "font": "Lora", "btn": "#ffc300", "btn_text": "#000", "hero_grad": "linear-gradient(135deg,#1a1200,#ffc300)"},
    {"bg": "#180000", "accent": "#e25822", "card_bg": "rgba(226,88,34,0.09)", "font": "Playfair Display", "btn": "#e25822", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#2e0000,#e25822)"},
    {"bg": "#0a0a0a", "accent": "#d4a017", "card_bg": "rgba(212,160,23,0.08)", "font": "Merriweather", "btn": "#d4a017", "btn_text": "#000", "hero_grad": "linear-gradient(135deg,#1a1000,#d4a017)"},
    {"bg": "#12060a", "accent": "#ff4500", "card_bg": "rgba(255,69,0,0.08)", "font": "Lora", "btn": "#ff4500", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#2a0000,#ff4500)"},
    {"bg": "#1a1000", "accent": "#ff9500", "card_bg": "rgba(255,149,0,0.08)", "font": "Georgia", "btn": "#ff9500", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#2a1800,#ff9500)"},
    {"bg": "#0d0400", "accent": "#ff7043", "card_bg": "rgba(255,112,67,0.09)", "font": "Playfair Display", "btn": "#ff7043", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#1e0800,#ff7043)"},
    {"bg": "#150800", "accent": "#ffab40", "card_bg": "rgba(255,171,64,0.08)", "font": "Lora", "btn": "#ffab40", "btn_text": "#000", "hero_grad": "linear-gradient(135deg,#201000,#ffab40)"},
    {"bg": "#1c0d00", "accent": "#fb8c00", "card_bg": "rgba(251,140,0,0.08)", "font": "Merriweather", "btn": "#fb8c00", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#2e1200,#fb8c00)"},
    {"bg": "#0e0600", "accent": "#f57c00", "card_bg": "rgba(245,124,0,0.09)", "font": "Georgia", "btn": "#f57c00", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#1a0c00,#f57c00)"},
    {"bg": "#1a0c00", "accent": "#ff6d00", "card_bg": "rgba(255,109,0,0.08)", "font": "Playfair Display", "btn": "#ff6d00", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#2a1000,#ff6d00)"},
    {"bg": "#120800", "accent": "#ffca28", "card_bg": "rgba(255,202,40,0.08)", "font": "Lora", "btn": "#ffca28", "btn_text": "#000", "hero_grad": "linear-gradient(135deg,#1e1000,#ffca28)"},
    {"bg": "#0d0500", "accent": "#ff8f00", "card_bg": "rgba(255,143,0,0.09)", "font": "Merriweather", "btn": "#ff8f00", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#1a0a00,#ff8f00)"},
    {"bg": "#1a0800", "accent": "#e64a19", "card_bg": "rgba(230,74,25,0.09)", "font": "Georgia", "btn": "#e64a19", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#280c00,#e64a19)"},
    {"bg": "#100600", "accent": "#ffb300", "card_bg": "rgba(255,179,0,0.08)", "font": "Playfair Display", "btn": "#ffb300", "btn_text": "#000", "hero_grad": "linear-gradient(135deg,#1e0e00,#ffb300)"},
    {"bg": "#0a0600", "accent": "#ff5722", "card_bg": "rgba(255,87,34,0.09)", "font": "Lora", "btn": "#ff5722", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#1a0800,#ff5722)"},
    {"bg": "#180c00", "accent": "#ffd54f", "card_bg": "rgba(255,213,79,0.08)", "font": "Merriweather", "btn": "#ffd54f", "btn_text": "#000", "hero_grad": "linear-gradient(135deg,#221800,#ffd54f)"},
    {"bg": "#120a00", "accent": "#ff6e40", "card_bg": "rgba(255,110,64,0.08)", "font": "Georgia", "btn": "#ff6e40", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#1e0e00,#ff6e40)"},
    {"bg": "#0d0800", "accent": "#ffcc02", "card_bg": "rgba(255,204,2,0.08)", "font": "Playfair Display", "btn": "#ffcc02", "btn_text": "#000", "hero_grad": "linear-gradient(135deg,#1a1200,#ffcc02)"},
]

# Group B (21-40): Minimal clean white — gym/fitness/yoga/health
GROUP_B = [
    {"bg": "#ffffff", "accent": "#2563eb", "card_bg": "#f0f6ff", "font": "Inter", "btn": "#2563eb", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#1e3a8a,#3b82f6)"},
    {"bg": "#f9fafb", "accent": "#059669", "card_bg": "#ecfdf5", "font": "Roboto", "btn": "#059669", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#064e3b,#10b981)"},
    {"bg": "#ffffff", "accent": "#7c3aed", "card_bg": "#f5f3ff", "font": "Inter", "btn": "#7c3aed", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#4c1d95,#8b5cf6)"},
    {"bg": "#f8fafc", "accent": "#0891b2", "card_bg": "#ecfeff", "font": "Roboto", "btn": "#0891b2", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#164e63,#06b6d4)"},
    {"bg": "#ffffff", "accent": "#dc2626", "card_bg": "#fff1f2", "font": "Inter", "btn": "#dc2626", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#7f1d1d,#ef4444)"},
    {"bg": "#f9fafb", "accent": "#d97706", "card_bg": "#fffbeb", "font": "Roboto", "btn": "#d97706", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#78350f,#f59e0b)"},
    {"bg": "#ffffff", "accent": "#0f766e", "card_bg": "#f0fdfa", "font": "Inter", "btn": "#0f766e", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#042f2e,#14b8a6)"},
    {"bg": "#f8fafc", "accent": "#be185d", "card_bg": "#fdf2f8", "font": "Roboto", "btn": "#be185d", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#500724,#ec4899)"},
    {"bg": "#ffffff", "accent": "#1d4ed8", "card_bg": "#eff6ff", "font": "Inter", "btn": "#1d4ed8", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#1e3a8a,#60a5fa)"},
    {"bg": "#f9fafb", "accent": "#047857", "card_bg": "#ecfdf5", "font": "Roboto", "btn": "#047857", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#052e16,#34d399)"},
    {"bg": "#ffffff", "accent": "#6d28d9", "card_bg": "#f5f3ff", "font": "Inter", "btn": "#6d28d9", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#2e1065,#a78bfa)"},
    {"bg": "#f8fafc", "accent": "#0369a1", "card_bg": "#f0f9ff", "font": "Roboto", "btn": "#0369a1", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#082f49,#38bdf8)"},
    {"bg": "#ffffff", "accent": "#b91c1c", "card_bg": "#fff1f2", "font": "Inter", "btn": "#b91c1c", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#450a0a,#fca5a5)"},
    {"bg": "#f9fafb", "accent": "#15803d", "card_bg": "#f0fdf4", "font": "Roboto", "btn": "#15803d", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#052e16,#4ade80)"},
    {"bg": "#ffffff", "accent": "#9333ea", "card_bg": "#faf5ff", "font": "Inter", "btn": "#9333ea", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#3b0764,#c084fc)"},
    {"bg": "#f8fafc", "accent": "#0e7490", "card_bg": "#ecfeff", "font": "Roboto", "btn": "#0e7490", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#083344,#22d3ee)"},
    {"bg": "#ffffff", "accent": "#c2410c", "card_bg": "#fff7ed", "font": "Inter", "btn": "#c2410c", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#431407,#fb923c)"},
    {"bg": "#f9fafb", "accent": "#1e40af", "card_bg": "#eff6ff", "font": "Roboto", "btn": "#1e40af", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#1e3a8a,#93c5fd)"},
    {"bg": "#ffffff", "accent": "#065f46", "card_bg": "#ecfdf5", "font": "Inter", "btn": "#065f46", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#022c22,#6ee7b7)"},
    {"bg": "#f8fafc", "accent": "#5b21b6", "card_bg": "#f5f3ff", "font": "Roboto", "btn": "#5b21b6", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#2e1065,#ddd6fe)"},
]

# Group C (41-60): Vibrant gradients — tech/IT/startup/digital
GROUP_C = [
    {"bg": "#0f0c29", "accent": "#00d4ff", "card_bg": "rgba(0,212,255,0.07)", "font": "Outfit", "btn": "#00d4ff", "btn_text": "#000", "hero_grad": "linear-gradient(135deg,#0f0c29,#302b63,#24243e)"},
    {"bg": "#0a0a23", "accent": "#7f00ff", "card_bg": "rgba(127,0,255,0.08)", "font": "Space Grotesk", "btn": "#7f00ff", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#0a0a23,#7f00ff,#e100ff)"},
    {"bg": "#000428", "accent": "#00f5a0", "card_bg": "rgba(0,245,160,0.07)", "font": "Outfit", "btn": "#00f5a0", "btn_text": "#000", "hero_grad": "linear-gradient(135deg,#000428,#004e92)"},
    {"bg": "#1a1a2e", "accent": "#e94560", "card_bg": "rgba(233,69,96,0.08)", "font": "Space Grotesk", "btn": "#e94560", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#1a1a2e,#16213e,#0f3460)"},
    {"bg": "#0d0d0d", "accent": "#00ffff", "card_bg": "rgba(0,255,255,0.06)", "font": "Outfit", "btn": "#00ffff", "btn_text": "#000", "hero_grad": "linear-gradient(135deg,#0d0d0d,#1a1a2e)"},
    {"bg": "#11001c", "accent": "#ff00ff", "card_bg": "rgba(255,0,255,0.06)", "font": "Space Grotesk", "btn": "#ff00ff", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#11001c,#3d0b37)"},
    {"bg": "#000000", "accent": "#39ff14", "card_bg": "rgba(57,255,20,0.07)", "font": "Outfit", "btn": "#39ff14", "btn_text": "#000", "hero_grad": "linear-gradient(135deg,#000000,#001a00)"},
    {"bg": "#0c0032", "accent": "#3500d3", "card_bg": "rgba(53,0,211,0.1)", "font": "Space Grotesk", "btn": "#3500d3", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#0c0032,#190061,#240090)"},
    {"bg": "#00001a", "accent": "#ff6b35", "card_bg": "rgba(255,107,53,0.08)", "font": "Outfit", "btn": "#ff6b35", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#00001a,#001a33)"},
    {"bg": "#0a001f", "accent": "#c700ff", "card_bg": "rgba(199,0,255,0.07)", "font": "Space Grotesk", "btn": "#c700ff", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#0a001f,#200040)"},
    {"bg": "#050510", "accent": "#00b4d8", "card_bg": "rgba(0,180,216,0.07)", "font": "Outfit", "btn": "#00b4d8", "btn_text": "#000", "hero_grad": "linear-gradient(135deg,#050510,#090979)"},
    {"bg": "#030d18", "accent": "#0cffe1", "card_bg": "rgba(12,255,225,0.07)", "font": "Space Grotesk", "btn": "#0cffe1", "btn_text": "#000", "hero_grad": "linear-gradient(135deg,#030d18,#1a3a5c)"},
    {"bg": "#0d000f", "accent": "#ff00a0", "card_bg": "rgba(255,0,160,0.07)", "font": "Outfit", "btn": "#ff00a0", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#0d000f,#2d003e)"},
    {"bg": "#001a00", "accent": "#00ff7f", "card_bg": "rgba(0,255,127,0.07)", "font": "Space Grotesk", "btn": "#00ff7f", "btn_text": "#000", "hero_grad": "linear-gradient(135deg,#001a00,#003300)"},
    {"bg": "#0a0a0a", "accent": "#ffd700", "card_bg": "rgba(255,215,0,0.07)", "font": "Outfit", "btn": "#ffd700", "btn_text": "#000", "hero_grad": "linear-gradient(135deg,#0a0a0a,#1a1a00)"},
    {"bg": "#080016", "accent": "#6600cc", "card_bg": "rgba(102,0,204,0.09)", "font": "Space Grotesk", "btn": "#6600cc", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#080016,#1a0040)"},
    {"bg": "#00080f", "accent": "#00cfff", "card_bg": "rgba(0,207,255,0.07)", "font": "Outfit", "btn": "#00cfff", "btn_text": "#000", "hero_grad": "linear-gradient(135deg,#00080f,#001a2e)"},
    {"bg": "#100020", "accent": "#ff3399", "card_bg": "rgba(255,51,153,0.07)", "font": "Space Grotesk", "btn": "#ff3399", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#100020,#2a0050)"},
    {"bg": "#001010", "accent": "#00e5cc", "card_bg": "rgba(0,229,204,0.07)", "font": "Outfit", "btn": "#00e5cc", "btn_text": "#000", "hero_grad": "linear-gradient(135deg,#001010,#002020)"},
    {"bg": "#0a0015", "accent": "#aa00ff", "card_bg": "rgba(170,0,255,0.07)", "font": "Space Grotesk", "btn": "#aa00ff", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#0a0015,#220033)"},
]

# Group D (61-80): Card-grid bold — salon/boutique/retail/jewellery
GROUP_D = [
    {"bg": "#fdf2f8", "accent": "#db2777", "card_bg": "#fff", "font": "Poppins", "btn": "#db2777", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#9d174d,#f472b6)"},
    {"bg": "#fff7ed", "accent": "#ea580c", "card_bg": "#fff", "font": "Nunito", "btn": "#ea580c", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#7c2d12,#fb923c)"},
    {"bg": "#faf5ff", "accent": "#7e22ce", "card_bg": "#fff", "font": "Poppins", "btn": "#7e22ce", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#3b0764,#c084fc)"},
    {"bg": "#fff1f2", "accent": "#be123c", "card_bg": "#fff", "font": "Nunito", "btn": "#be123c", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#4c0519,#fb7185)"},
    {"bg": "#ecfdf5", "accent": "#15803d", "card_bg": "#fff", "font": "Poppins", "btn": "#15803d", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#052e16,#4ade80)"},
    {"bg": "#eff6ff", "accent": "#1d4ed8", "card_bg": "#fff", "font": "Nunito", "btn": "#1d4ed8", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#1e3a8a,#93c5fd)"},
    {"bg": "#fffbeb", "accent": "#b45309", "card_bg": "#fff", "font": "Poppins", "btn": "#b45309", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#451a03,#fcd34d)"},
    {"bg": "#f0fdfa", "accent": "#0f766e", "card_bg": "#fff", "font": "Nunito", "btn": "#0f766e", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#042f2e,#5eead4)"},
    {"bg": "#fdf4ff", "accent": "#a21caf", "card_bg": "#fff", "font": "Poppins", "btn": "#a21caf", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#4a044e,#e879f9)"},
    {"bg": "#fff7ed", "accent": "#c2410c", "card_bg": "#fff", "font": "Nunito", "btn": "#c2410c", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#431407,#fdba74)"},
    {"bg": "#fef2f2", "accent": "#dc2626", "card_bg": "#fff", "font": "Poppins", "btn": "#dc2626", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#7f1d1d,#fca5a5)"},
    {"bg": "#f0f9ff", "accent": "#0284c7", "card_bg": "#fff", "font": "Nunito", "btn": "#0284c7", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#082f49,#7dd3fc)"},
    {"bg": "#fafafa", "accent": "#374151", "card_bg": "#fff", "font": "Poppins", "btn": "#374151", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#111827,#9ca3af)"},
    {"bg": "#fff0f3", "accent": "#e11d48", "card_bg": "#fff", "font": "Nunito", "btn": "#e11d48", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#4c0519,#fda4af)"},
    {"bg": "#f0fdf4", "accent": "#16a34a", "card_bg": "#fff", "font": "Poppins", "btn": "#16a34a", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#052e16,#86efac)"},
    {"bg": "#faf5ff", "accent": "#9333ea", "card_bg": "#fff", "font": "Nunito", "btn": "#9333ea", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#3b0764,#d8b4fe)"},
    {"bg": "#fff7ed", "accent": "#d97706", "card_bg": "#fff", "font": "Poppins", "btn": "#d97706", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#78350f,#fbbf24)"},
    {"bg": "#eff6ff", "accent": "#2563eb", "card_bg": "#fff", "font": "Nunito", "btn": "#2563eb", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#1e3a8a,#bfdbfe)"},
    {"bg": "#fdf2f8", "accent": "#be185d", "card_bg": "#fff", "font": "Poppins", "btn": "#be185d", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#500724,#fbcfe8)"},
    {"bg": "#ecfdf5", "accent": "#059669", "card_bg": "#fff", "font": "Nunito", "btn": "#059669", "btn_text": "#fff", "hero_grad": "linear-gradient(135deg,#064e3b,#6ee7b7)"},
]

# Group E (81-100): Editorial single-column — all other types
GROUP_E = [
    {"bg": "#1c1c1e", "accent": "#f5f5f0", "card_bg": "#2c2c2e", "font": "DM Serif Display", "btn": "#f5f5f0", "btn_text": "#1c1c1e", "hero_grad": "linear-gradient(180deg,#1c1c1e,#2c2c2e)"},
    {"bg": "#f5f0eb", "accent": "#2c1a0e", "card_bg": "#fff", "font": "Cormorant Garamond", "btn": "#2c1a0e", "btn_text": "#fff", "hero_grad": "linear-gradient(180deg,#e8ddd0,#f5f0eb)"},
    {"bg": "#141414", "accent": "#c9a96e", "card_bg": "#1e1e1e", "font": "DM Serif Display", "btn": "#c9a96e", "btn_text": "#000", "hero_grad": "linear-gradient(180deg,#0a0a0a,#141414)"},
    {"bg": "#f0f0ec", "accent": "#333", "card_bg": "#fff", "font": "Cormorant Garamond", "btn": "#333", "btn_text": "#fff", "hero_grad": "linear-gradient(180deg,#e0e0dc,#f0f0ec)"},
    {"bg": "#0f1010", "accent": "#00e676", "card_bg": "#1a1c1c", "font": "DM Serif Display", "btn": "#00e676", "btn_text": "#000", "hero_grad": "linear-gradient(180deg,#050606,#0f1010)"},
    {"bg": "#faf8f5", "accent": "#c0392b", "card_bg": "#fff", "font": "Cormorant Garamond", "btn": "#c0392b", "btn_text": "#fff", "hero_grad": "linear-gradient(180deg,#ede8e3,#faf8f5)"},
    {"bg": "#1a0d00", "accent": "#d4a96a", "card_bg": "#261500", "font": "DM Serif Display", "btn": "#d4a96a", "btn_text": "#000", "hero_grad": "linear-gradient(180deg,#0d0600,#1a0d00)"},
    {"bg": "#eef2f7", "accent": "#1a3c5e", "card_bg": "#fff", "font": "Cormorant Garamond", "btn": "#1a3c5e", "btn_text": "#fff", "hero_grad": "linear-gradient(180deg,#dde5ef,#eef2f7)"},
    {"bg": "#101018", "accent": "#a78bfa", "card_bg": "#18182a", "font": "DM Serif Display", "btn": "#a78bfa", "btn_text": "#000", "hero_grad": "linear-gradient(180deg,#06060e,#101018)"},
    {"bg": "#f7f4ef", "accent": "#5a3e28", "card_bg": "#fff", "font": "Cormorant Garamond", "btn": "#5a3e28", "btn_text": "#fff", "hero_grad": "linear-gradient(180deg,#ece7df,#f7f4ef)"},
    {"bg": "#0d1117", "accent": "#58a6ff", "card_bg": "#161b22", "font": "DM Serif Display", "btn": "#58a6ff", "btn_text": "#000", "hero_grad": "linear-gradient(180deg,#010409,#0d1117)"},
    {"bg": "#fefce8", "accent": "#854d0e", "card_bg": "#fff", "font": "Cormorant Garamond", "btn": "#854d0e", "btn_text": "#fff", "hero_grad": "linear-gradient(180deg,#fef9c3,#fefce8)"},
    {"bg": "#0f0f23", "accent": "#e879f9", "card_bg": "#1a1a33", "font": "DM Serif Display", "btn": "#e879f9", "btn_text": "#000", "hero_grad": "linear-gradient(180deg,#050514,#0f0f23)"},
    {"bg": "#f0fdf4", "accent": "#14532d", "card_bg": "#fff", "font": "Cormorant Garamond", "btn": "#14532d", "btn_text": "#fff", "hero_grad": "linear-gradient(180deg,#dcfce7,#f0fdf4)"},
    {"bg": "#1e1b2e", "accent": "#f0abfc", "card_bg": "#2a2640", "font": "DM Serif Display", "btn": "#f0abfc", "btn_text": "#000", "hero_grad": "linear-gradient(180deg,#0f0c1e,#1e1b2e)"},
    {"bg": "#fafaf9", "accent": "#292524", "card_bg": "#fff", "font": "Cormorant Garamond", "btn": "#292524", "btn_text": "#fff", "hero_grad": "linear-gradient(180deg,#e7e5e4,#fafaf9)"},
    {"bg": "#0c0c0c", "accent": "#fb923c", "card_bg": "#181818", "font": "DM Serif Display", "btn": "#fb923c", "btn_text": "#000", "hero_grad": "linear-gradient(180deg,#000,#0c0c0c)"},
    {"bg": "#f8fafc", "accent": "#0f172a", "card_bg": "#fff", "font": "Cormorant Garamond", "btn": "#0f172a", "btn_text": "#fff", "hero_grad": "linear-gradient(180deg,#e2e8f0,#f8fafc)"},
    {"bg": "#130f0f", "accent": "#f87171", "card_bg": "#1f1717", "font": "DM Serif Display", "btn": "#f87171", "btn_text": "#000", "hero_grad": "linear-gradient(180deg,#050000,#130f0f)"},
    {"bg": "#fefdf8", "accent": "#365314", "card_bg": "#fff", "font": "Cormorant Garamond", "btn": "#365314", "btn_text": "#fff", "hero_grad": "linear-gradient(180deg,#ecfccb,#fefdf8)"},
]

ALL_GROUPS = GROUP_A + GROUP_B + GROUP_C + GROUP_D + GROUP_E  # 100 total


# ---------------------------------------------------------------------------
# Layout variations — cycle through for extra structural diversity
# ---------------------------------------------------------------------------

LAYOUT_VARIANTS = [
    "hero_left",    # text left, decorative block right
    "hero_center",  # centered hero
    "hero_banner",  # full-width banner
    "hero_split",   # 50/50 split with bg color
    "hero_minimal", # minimal top bar style
]

SECTION_ORDERS = [
    ["hero", "services", "contact"],
    ["hero", "contact", "services"],
    ["hero", "services", "about", "contact"],
    ["hero", "about", "services", "contact"],
    ["hero", "services", "contact", "about"],
]

ICON_SETS = [
    ("📍", "📞", "✉️", "🔧"),
    ("🏙️", "📱", "📧", "⚡"),
    ("📌", "☎️", "📨", "🛠️"),
    ("🌆", "📲", "💌", "✅"),
    ("🗺️", "🤙", "📩", "💼"),
]


def _is_dark(bg: str) -> bool:
    """Heuristic: dark bg if hex brightness < 100."""
    hex_color = bg.lstrip("#")
    if len(hex_color) != 6:
        return True
    r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
    return (r * 0.299 + g * 0.587 + b * 0.114) < 100


def build_template(n: int, tok: dict) -> str:
    """Return a complete Jinja2 HTML template string for template number n."""
    idx = n - 1  # 0-indexed
    dark = _is_dark(tok["bg"])
    text_color = "#f0f0f0" if dark else "#111111"
    sub_color = "#aaaaaa" if dark else "#555555"
    border_color = "rgba(255,255,255,0.1)" if dark else "rgba(0,0,0,0.1)"
    layout = LAYOUT_VARIANTS[idx % len(LAYOUT_VARIANTS)]
    sections = SECTION_ORDERS[idx % len(SECTION_ORDERS)]
    icon_city, icon_phone, icon_email, icon_service = ICON_SETS[idx % len(ICON_SETS)]

    # ---------------------------------------------------------------- HERO
    if layout == "hero_center":
        hero_html = f"""
  <section class="hero" style="background:{tok['hero_grad']};text-align:center;padding:80px 20px;">
    <p class="badge" style="color:{tok['accent']};font-size:0.85rem;text-transform:uppercase;letter-spacing:2px;">{{{{ business_type }}}}</p>
    <h1 style="color:#fff;font-size:clamp(2rem,5vw,3.5rem);margin:16px 0;">{{{{ hero.title or business_name }}}}</h1>
    <p style="color:rgba(255,255,255,0.8);font-size:1.1rem;max-width:600px;margin:0 auto 32px;">
      {{{{ hero.subtitle or ('Serving the people of ' ~ city ~ ' with excellence and dedication.') }}}}
    </p>
    <a href="{{{{ hero.cta.link or ('mailto:' ~ email) }}}}" class="cta-btn" style="background:{tok['btn']};color:{tok['btn_text']};padding:14px 36px;border-radius:30px;text-decoration:none;font-weight:700;display:inline-block;">
      {{{{ hero.cta.text or 'Get in Touch' }}}}
    </a>
  </section>"""
    elif layout == "hero_banner":
        hero_html = f"""
  <section class="hero" style="background:{tok['hero_grad']};padding:60px 40px;display:flex;align-items:center;gap:40px;flex-wrap:wrap;">
    <div style="flex:1;min-width:260px;">
      <span style="background:{tok['accent']};color:{tok['btn_text']};padding:4px 14px;border-radius:20px;font-size:0.8rem;font-weight:600;">{{{{ business_type }}}}</span>
      <h1 style="color:#fff;font-size:clamp(2rem,4vw,3rem);margin:20px 0 12px;">{{{{ hero.title or business_name }}}}</h1>
      <p style="color:rgba(255,255,255,0.75);line-height:1.7;">{{{{ hero.subtitle or ('Based in ' ~ city ~ ' — delivering quality services that matter.') }}}}</p>
    </div>
    <div style="flex:1;min-width:200px;display:flex;flex-direction:column;gap:12px;">
      <div style="background:rgba(255,255,255,0.1);border-radius:12px;padding:16px;color:#fff;">
        {icon_phone} {{{{ phone }}}}
      </div>
      <div style="background:rgba(255,255,255,0.1);border-radius:12px;padding:16px;color:#fff;">
        {icon_email} {{{{ email }}}}
      </div>
    </div>
  </section>"""
    elif layout == "hero_split":
        hero_html = f"""
  <section class="hero" style="display:grid;grid-template-columns:1fr 1fr;min-height:380px;">
    <div style="background:{tok['hero_grad']};display:flex;flex-direction:column;justify-content:center;padding:60px 40px;">
      <p style="color:{tok['accent']};text-transform:uppercase;letter-spacing:2px;font-size:0.85rem;">{{{{ business_type }}}}</p>
      <h1 style="color:#fff;font-size:clamp(1.8rem,3.5vw,2.8rem);margin:12px 0;">{{{{ hero.title or business_name }}}}</h1>
      <p style="color:rgba(255,255,255,0.7);">{{{{ hero.subtitle or city }}}}</p>
      <a href="{{{{ hero.cta.link or ('mailto:' ~ email) }}}}" style="margin-top:24px;background:{tok['btn']};color:{tok['btn_text']};display:inline-block;padding:12px 28px;border-radius:8px;text-decoration:none;font-weight:600;">{{{{ hero.cta.text or 'Contact Us' }}}}</a>
    </div>
    <div style="background:{tok['card_bg']};display:flex;flex-direction:column;justify-content:center;padding:40px;gap:16px;">
      <p style="font-size:1.1rem;font-weight:600;color:{text_color};">Our Services</p>
      {{% if services is mapping %}}
        {{% for service in services.features %}}
        <div style="border-left:3px solid {tok['accent']};padding-left:14px;color:{sub_color};">{icon_service} {{{{ service }}}}</div>
        {{% endfor %}}
      {{% else %}}
        {{% for service in services %}}
        <div style="border-left:3px solid {tok['accent']};padding-left:14px;color:{sub_color};">{icon_service} {{{{ service }}}}</div>
        {{% endfor %}}
      {{% endif %}}
    </div>
  </section>"""
    elif layout == "hero_minimal":
        hero_html = f"""
  <section class="hero" style="background:{tok['hero_grad']};padding:50px 60px;border-radius:0 0 24px 24px;margin-bottom:20px;">
    <div style="max-width:700px;">
      <span style="color:{tok['accent']};font-size:0.85rem;text-transform:uppercase;letter-spacing:3px;font-weight:700;">{{{{ business_type }}}}</span>
      <h1 style="color:#fff;font-size:clamp(2rem,4.5vw,3.2rem);margin:10px 0 18px;line-height:1.2;">{{{{ hero.title or business_name }}}}</h1>
      <div style="display:flex;gap:20px;flex-wrap:wrap;color:rgba(255,255,255,0.8);font-size:0.95rem;">
        <span>{icon_city} {{{{ city }}}}</span>
        <span>{icon_phone} {{{{ phone }}}}</span>
        <span>{icon_email} {{{{ email }}}}</span>
      </div>
    </div>
  </section>"""
    else:  # hero_left (default)
        hero_html = f"""
  <section class="hero" style="background:{tok['hero_grad']};padding:80px 60px;display:flex;align-items:center;gap:60px;flex-wrap:wrap;">
    <div style="flex:1;min-width:280px;">
      <p class="badge" style="color:{tok['accent']};text-transform:uppercase;letter-spacing:2px;font-size:0.85rem;font-weight:600;">{{{{ business_type }}}}</p>
      <h1 style="color:#fff;font-size:clamp(2.2rem,5vw,3.5rem);margin:16px 0;line-height:1.15;">{{{{ hero.title or business_name }}}}</h1>
      <p style="color:rgba(255,255,255,0.8);font-size:1rem;line-height:1.7;margin-bottom:32px;">
        {{{{ hero.subtitle or ('Proudly serving ' ~ city ~ '. Get in touch with us today.') }}}}
      </p>
      <a href="{{{{ hero.cta.link or ('mailto:' ~ email) }}}}" style="background:{tok['btn']};color:{tok['btn_text']};padding:14px 32px;border-radius:50px;text-decoration:none;font-weight:700;display:inline-block;">{{{{ hero.cta.text or 'Book Now' }}}}</a>
    </div>
    <div style="flex:0 0 260px;background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.15);border-radius:20px;padding:28px;backdrop-filter:blur(8px);">
      <p style="color:rgba(255,255,255,0.6);font-size:0.8rem;margin-bottom:16px;text-transform:uppercase;letter-spacing:1px;">Quick Info</p>
      <div style="color:#fff;display:flex;flex-direction:column;gap:10px;font-size:0.95rem;">
        <span>{icon_city} {{{{ city }}}}</span>
        <span>{icon_phone} {{{{ phone }}}}</span>
        <span>{icon_email} {{{{ email }}}}</span>
      </div>
    </div>
  </section>"""

    # ---------------------------------------------------------------- SECTIONS
    def make_services():
        return f"""
  <section style="padding:60px 40px;background:{tok['bg']};">
    <h2 style="color:{tok['accent']};font-size:1.8rem;margin-bottom:8px;text-align:center;">{{{{ services.title or 'What We Offer' }}}}</h2>
    <p style="color:{sub_color};text-align:center;margin-bottom:40px;font-size:0.95rem;">{{{{ services.description or 'Expert services tailored to your needs.' }}}}</p>
    <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:20px;max-width:900px;margin:0 auto;">
      {{% if services is mapping %}}
        {{% for service in services.features %}}
        <div style="background:{tok['card_bg']};border:1px solid {border_color};border-radius:16px;padding:24px;text-align:center;">
          <div style="font-size:2rem;margin-bottom:12px;">{icon_service}</div>
          <p style="color:{text_color};font-weight:600;font-size:0.95rem;">{{{{ service }}}}</p>
        </div>
        {{% endfor %}}
      {{% else %}}
        {{% for service in services %}}
        <div style="background:{tok['card_bg']};border:1px solid {border_color};border-radius:16px;padding:24px;text-align:center;">
          <div style="font-size:2rem;margin-bottom:12px;">{icon_service}</div>
          <p style="color:{text_color};font-weight:600;font-size:0.95rem;">{{{{ service }}}}</p>
        </div>
        {{% endfor %}}
      {{% endif %}}
    </div>
    {{% if services is mapping and services.stats %}}
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:20px;max-width:800px;margin:40px auto 0;text-align:center;border-top:1px solid {border_color};padding-top:30px;">
      {{% for label, val in services.stats.items() %}}
      <div>
        <div style="font-size:2.2rem;font-weight:700;color:{tok['accent']};">{{{{ val }}}}</div>
        <div style="font-size:0.8rem;color:{sub_color};text-transform:uppercase;margin-top:4px;">{{{{ label.replace('_', ' ') }}}}</div>
      </div>
      {{% endfor %}}
    </div>
    {{% endif %}}
  </section>"""

    def make_about():
        return f"""
  <section style="padding:60px 40px;background:{tok['card_bg']};">
    <div style="max-width:700px;margin:0 auto;text-align:center;">
      <h2 style="color:{tok['accent']};font-size:1.8rem;margin-bottom:16px;">About Us</h2>
      <p style="color:{sub_color};line-height:1.8;font-size:1rem;">
        {{{{ brand.name or business_name }}}} is a trusted {{{{ business_type }}}} based in {{{{ city }}}}.
        We are committed to delivering top-quality services to our clients every day.
        Our team of professionals ensures that every client receives personalized attention and outstanding results.
      </p>
    </div>
  </section>"""

    def make_contact():
        return f"""
  <section style="padding:60px 40px;background:{tok['bg']};">
    <h2 style="color:{tok['accent']};font-size:1.8rem;text-align:center;margin-bottom:40px;">Get In Touch</h2>
    <div style="display:flex;gap:20px;flex-wrap:wrap;justify-content:center;max-width:800px;margin:0 auto;">
      <div style="background:{tok['card_bg']};border:1px solid {border_color};border-radius:16px;padding:28px;flex:1;min-width:200px;text-align:center;">
        <div style="font-size:2rem;margin-bottom:12px;">{icon_city}</div>
        <p style="color:{sub_color};font-size:0.85rem;margin-bottom:6px;">Location</p>
        <p style="color:{text_color};font-weight:600;">{{{{ city }}}}</p>
      </div>
      <div style="background:{tok['card_bg']};border:1px solid {border_color};border-radius:16px;padding:28px;flex:1;min-width:200px;text-align:center;">
        <div style="font-size:2rem;margin-bottom:12px;">{icon_phone}</div>
        <p style="color:{sub_color};font-size:0.85rem;margin-bottom:6px;">Phone</p>
        <a href="tel:{{{{ phone }}}}" style="color:{tok['accent']};font-weight:600;text-decoration:none;">{{{{ phone }}}}</a>
      </div>
      <div style="background:{tok['card_bg']};border:1px solid {border_color};border-radius:16px;padding:28px;flex:1;min-width:200px;text-align:center;">
        <div style="font-size:2rem;margin-bottom:12px;">{icon_email}</div>
        <p style="color:{sub_color};font-size:0.85rem;margin-bottom:6px;">Email</p>
        <a href="mailto:{{{{ email }}}}" style="color:{tok['accent']};font-weight:600;text-decoration:none;word-break:break-all;">{{{{ email }}}}</a>
      </div>
    </div>
  </section>"""

    def make_categories():
        return f"""
  {{% if categories %}}
  <section style="padding:60px 40px;background:{tok['card_bg']};">
    <h2 style="color:{tok['accent']};font-size:1.8rem;margin-bottom:8px;text-align:center;">Categories</h2>
    <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:20px;max-width:900px;margin:24px auto 0;">
      {{% for cat in categories %}}
      <div style="background:{tok['bg']};border:1px solid {border_color};border-radius:12px;padding:16px;text-align:center;">
        {{% if cat.image %}}
        <img src="{{{{ cat.image }}}}" style="width:100%;height:120px;object-fit:cover;border-radius:8px;margin-bottom:10px;" />
        {{% endif %}}
        <p style="color:{text_color};font-weight:600;font-size:0.9rem;">{{{{ cat.name }}}}</p>
      </div>
      {{% endfor %}}
    </div>
  </section>
  {{% endif %}}"""

    def make_products():
        return f"""
  {{% if products %}}
  <section style="padding:60px 40px;background:{tok['bg']};">
    <h2 style="color:{tok['accent']};font-size:1.8rem;margin-bottom:8px;text-align:center;">Our Products</h2>
    <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:24px;max-width:1000px;margin:24px auto 0;">
      {{% for p in products %}}
      <div style="background:{tok['card_bg']};border:1px solid {border_color};border-radius:16px;overflow:hidden;display:flex;flex-direction:column;">
        {{% if p.image %}}
        <img src="{{{{ p.image }}}}" style="width:100%;height:180px;object-fit:cover;" />
        {{% endif %}}
        <div style="padding:16px;flex-grow:1;display:flex;flex-direction:column;gap:8px;">
          <span style="font-size:0.75rem;color:{tok['accent']};text-transform:uppercase;">{{% if p.category %}}{{{{ p.category }}}}{{% else %}}Product{{% endif %}}</span>
          <h3 style="color:{text_color};font-size:1.05rem;font-weight:600;margin:0;">{{% if p.name %}}{{{{ p.name }}}}{{% else %}}Item{{% endif %}}</h3>
          <p style="color:{sub_color};font-size:0.85rem;line-height:1.4;margin:0;flex-grow:1;">{{{{ p.description or '' }}}}</p>
          <div style="display:flex;justify-content:space-between;align-items:center;margin-top:12px;">
            <span style="font-weight:700;color:{text_color};">{{{{ p.currency or '$' }}}}{{{{ p.price or '0' }}}}</span>
            {{% if p.rating %}}
            <span style="color:#ffd700;font-size:0.9rem;">★ {{{{ p.rating }}}}</span>
            {{% endif %}}
          </div>
        </div>
      </div>
      {{% endfor %}}
    </div>
  </section>
  {{% endif %}}"""

    def make_deals():
        return f"""
  {{% if deals %}}
  <section style="padding:60px 40px;background:{tok['card_bg']};">
    <h2 style="color:{tok['accent']};font-size:1.8rem;text-align:center;margin-bottom:8px;">Special Deals</h2>
    <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:24px;max-width:900px;margin:24px auto 0;">
      {{% for deal in deals %}}
      <div style="background:{tok['bg']};border:1px solid {border_color};border-radius:16px;padding:20px;display:flex;flex-direction:column;gap:12px;position:relative;overflow:hidden;">
        {{% if deal.discount %}}
        <span style="position:absolute;top:12px;right:12px;background:#e53935;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.75rem;font-weight:700;">
          {{{{ deal.discount }}}}% OFF
        </span>
        {{% endif %}}
        <h3 style="color:{text_color};font-size:1.1rem;font-weight:600;margin:0 60px 0 0;">{{{{ deal.title }}}}</h3>
        <p style="color:{sub_color};font-size:0.85rem;line-height:1.4;margin:0;">{{{{ deal.description or '' }}}}</p>
        {{% if deal.image %}}
        <img src="{{{{ deal.image }}}}" style="width:100%;height:140px;object-fit:cover;border-radius:8px;" />
        {{% endif %}}
      </div>
      {{% endfor %}}
    </div>
  </section>
  {{% endif %}}"""

    section_map = {
        "services": make_services,
        "about": make_about,
        "contact": make_contact,
        "categories": make_categories,
        "products": make_products,
        "deals": make_deals,
        "hero": lambda: hero_html,
    }

    # Interleave categories, products, and deals dynamically relative to the core sections
    sections_to_render = []
    for s in sections:
        sections_to_render.append(s)
        if s == "hero":
            sections_to_render.append("categories")
            sections_to_render.append("products")
    
    if "contact" in sections_to_render:
        idx_contact = sections_to_render.index("contact")
        sections_to_render.insert(idx_contact, "deals")
    else:
        sections_to_render.append("deals")

    body_sections = "\n".join(
        section_map[s]() if s != "hero" else hero_html for s in sections_to_render
    )

    # ---------------------------------------------------------------- FULL PAGE
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{{{ brand.name or business_name }}}} — {{{{ business_type }}}} in {{{{ city }}}}</title>
  <meta name="description" content="{{{{ brand.name or business_name }}}} is a {{{{ business_type }}}} located in {{{{ city }}}}. Contact us at {{{{ email }}}} or {{{{ phone }}}}.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family={tok['font'].replace(' ', '+')}:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ scroll-behavior: smooth; }}
    body {{
      font-family: '{tok['font']}', system-ui, sans-serif;
      background: {tok['bg']};
      color: {text_color};
      line-height: 1.6;
    }}
    a {{ color: inherit; }}

    /* NAV */
    nav {{
      position: sticky; top: 0; z-index: 100;
      background: {tok['bg']};
      border-bottom: 1px solid {border_color};
      padding: 0 40px;
      display: flex; align-items: center; justify-content: space-between;
      height: 64px;
      backdrop-filter: blur(10px);
    }}
    .nav-brand {{
      font-size: 1.2rem; font-weight: 700;
      color: {text_color};
      text-decoration: none;
      display: flex; align-items: center; gap: 10px;
    }}
    .nav-brand::before {{
      content: '';
      width: 10px; height: 10px;
      background: {tok['accent']};
      border-radius: 50%;
      display: inline-block;
    }}
    .nav-links {{ display: flex; gap: 28px; list-style: none; }}
    .nav-links a {{
      color: {sub_color}; text-decoration: none;
      font-size: 0.9rem; font-weight: 500;
      transition: color 0.2s;
    }}
    .nav-links a:hover {{ color: {tok['accent']}; }}
    .nav-cta {{
      background: {tok['btn']}; color: {tok['btn_text']};
      padding: 8px 20px; border-radius: 6px;
      text-decoration: none; font-weight: 600; font-size: 0.9rem;
      transition: opacity 0.2s;
    }}
    .nav-cta:hover {{ opacity: 0.85; }}

    /* FOOTER */
    footer {{
      background: {tok['card_bg']};
      border-top: 1px solid {border_color};
      padding: 40px;
      text-align: center;
    }}
    footer p {{ color: {sub_color}; font-size: 0.875rem; margin-top: 8px; }}

    /* RESPONSIVE */
    @media (max-width: 768px) {{
      nav {{ padding: 0 20px; }}
      .nav-links {{ display: none; }}
      section[class] {{ padding: 40px 20px !important; }}
    }}
  </style>
</head>
<body>

  <!-- NAV -->
  <nav>
    <a class="nav-brand" href="#">{{{{ brand.name or business_name }}}}</a>
    <ul class="nav-links">
      {{% if nav %}}
        {{% for item in nav %}}
        <li><a href="{{{{ item.link or '#' }}}}">{{{{ item.label or item.name or 'Link' }}}}</a></li>
        {{% endfor %}}
      {{% else %}}
        <li><a href="#">Home</a></li>
        <li><a href="#">Services</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#">Contact</a></li>
      {{% endif %}}
    </ul>
    <a class="nav-cta" href="mailto:{{{{ email }}}}">Contact Us</a>
  </nav>

{body_sections}

  <!-- FOOTER -->
  <footer>
    <strong style="color:{text_color};font-size:1.05rem;">{{{{ brand.name or business_name }}}}</strong>
    {{% if footer and footer.about %}}
    <p style="max-width:600px;margin:10px auto;line-height:1.6;color:{sub_color};font-size:0.9rem;">{{{{ footer.about }}}}</p>
    {{% endif %}}
    <p style="margin-top:8px;">{{{{ business_type }}}} &bull; {{{{ city }}}}</p>
    <p style="margin-top:16px;">
      {icon_phone} <a href="tel:{{{{ phone }}}}" style="color:{tok['accent']};text-decoration:none;">{{{{ phone }}}}</a>
      &nbsp;&nbsp;|&nbsp;&nbsp;
      {icon_email} <a href="mailto:{{{{ email }}}}" style="color:{tok['accent']};text-decoration:none;">{{{{ email }}}}</a>
    </p>
    
    {{% set social_list = (footer.social or footer.socials or []) if footer else [] %}}
    {{% if social_list %}}
    <p style="margin-top:12px;">
      {{% for s in social_list %}}
      {{% if s is mapping %}}
      <a href="{{{{ s.url or '#' }}}}" style="color:{tok['accent']};text-decoration:none;margin:0 8px;">{{{{ s.platform or s }}}}</a>
      {{% else %}}
      <span style="margin:0 8px;font-size:0.85rem;color:{sub_color};">{{{{ s }}}}</span>
      {{% endif %}}
      {{% endfor %}}
    </p>
    {{% endif %}}
    
    <p style="margin-top:20px;">{{{{ (footer and footer.copyright) or ('&copy; 2026 ' ~ (brand.name or business_name) ~ '. All rights reserved.') }}}}</p>
  </footer>

</body>
</html>
"""


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    count = 0
    for i, tok in enumerate(ALL_GROUPS, start=1):
        html = build_template(i, tok)
        path = os.path.join(OUTPUT_DIR, f"template{i}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        count += 1

    print(f"[OK] Generated {count} templates in '{OUTPUT_DIR}'")


if __name__ == "__main__":
    main()
