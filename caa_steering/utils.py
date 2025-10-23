from IPython.display import HTML, display
import html

def render_pretty(
    text: str,
    title: str = "🥳🍕 Pure Joy",
    tone: str = "happy",
    collapsible: bool = False,
):
    """
    Render a pretty, themed card in Jupyter from plain text.

    Args:
        text: The body text to display.
        title: Small heading shown at the top of the card.
        tone: One of {"happy", "angry", "calm", "info"} for quick styling.
        collapsible: If True, wraps the card in a <details> to collapse/expand.
    """
    palettes = {
        "happy": {
            "border": "#22c55e", "bg1": "#ecfeff", "bg2": "#f0fdf4",
            "color": "#065f46", "shadow": "rgba(34,197,94,0.18)",
            "label": "🌈"
        },
        "angry": {
            "border": "#ef4444", "bg1": "#fff1f2", "bg2": "#fee2e2",
            "color": "#7f1d1d", "shadow": "rgba(239,68,68,0.25)",
            "label": "🔥"
        },
        "calm": {
            "border": "#60a5fa", "bg1": "#eff6ff", "bg2": "#e0f2fe",
            "color": "#1e3a8a", "shadow": "rgba(96,165,250,0.22)",
            "label": "🌊"
        },
        "info": {
            "border": "#a78bfa", "bg1": "#faf5ff", "bg2": "#ecfeff",
            "color": "#4c1d95", "shadow": "rgba(167,139,250,0.20)",
            "label": "💡"
        },
    }

    p = palettes.get(tone, palettes["happy"])
    safe_title = html.escape(title)
    safe_text = html.escape(text).replace("\n", "<br/>")

    card_html = f"""
    <div style="
        border:3px solid {p['border']};
        border-radius:16px;
        padding:16px 18px;
        background:linear-gradient(135deg,{p['bg1']} 0%, {p['bg2']} 100%);
        box-shadow:0 10px 24px {p['shadow']};
        color:{p['color']};
        line-height:1.6;
        font-size:16px;">
      <div style="font-size:18px; margin-bottom:8px;">{p['label']} {safe_title}</div>
      <div>{safe_text}</div>
    </div>
    """

    if collapsible:
        card_html = f"""
        <details style="border:2px solid {p['border']}; border-radius:14px; padding:10px 12px; background:{p['bg1']}; color:{p['color']};">
          <summary style="cursor:pointer; font-size:17px;">{p['label']} {safe_title}</summary>
          <div style="margin-top:10px;">{card_html}</div>
        </details>
        """

    display(HTML(card_html))