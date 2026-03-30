# palette.py — Project colour palette
# Usage: from palette import C, SENTIMENT_COLORS, INTENT_COLORS, apply_style
import matplotlib.pyplot as plt
import matplotlib as mpl

# ── Core colours ────────────────────────────────────────────────
C = {
    # Primary — Slate blue (DistilBERT, main model)
    "blue_dark":    "#0f3460",
    "blue":         "#4a90d9",
    "blue_light":   "#a8d4f5",
    "blue_bg":      "#e8f4fd",

    # Malachite — Positive sentiment, RoBERTa
    "green_dark":   "#1a3d2b",
    "green":        "#3ab56e",
    "green_light":  "#b8e8cc",
    "green_bg":     "#e5f6ec",

    # Gold — Neutral sentiment, escalation highlights
    "gold_dark":    "#7a5500",
    "gold":         "#f5c842",
    "gold_light":   "#fae08a",
    "gold_bg":      "#fdf3cc",

    # Red — Negative sentiment
    "red_dark":     "#7f2020",
    "red":          "#c0392b",
    "red_light":    "#f7c6c2",
    "red_bg":       "#fdf0ef",

    # Purple — Escalation
    "purple_dark":  "#5b2c6f",
    "purple":       "#8e44ad",
    "purple_light": "#e8c8f5",
    "purple_bg":    "#f8f0fc",

    # Neutral — Baseline model, axes, backgrounds
    "gray_dark":    "#1c1c1c",
    "gray":         "#596275",
    "gray_light":   "#d0d0d0",
    "gray_bg":      "#f2f2f2",

    # Info — second blue for comparisons
    "info":         "#2980b9",
}

# ── Semantic mappings ────────────────────────────────────────────
SENTIMENT_COLORS = {
    "negative": C["red"],
    "neutral":  C["gold"],
    "positive": C["green"],
}

INTENT_COLORS = {
    "account_management":  C["blue"],
    "billing_payment":     C["gold"],
    "complaint_service":   C["red"],
    "order_tracking":      C["info"],
    "product_inquiry":     C["green"],
    "refund_cancellation": C["purple"],
}

MODEL_COLORS = {
    "DistilBERT (fine-tuned)":        C["blue"],
    "TF-IDF + Logistic Regression":   C["gray"],
    "RoBERTa (CardiffNLP)":           C["green"],
    "IBM Watson NLU*":                C["info"],
    "Google Cloud NL*":               C["gray_light"],
}

# ── Matplotlib style ─────────────────────────────────────────────
def apply_style():
    """Call once at the top of each notebook after importing palette."""
    mpl.rcParams.update({
        "figure.facecolor":     "white",
        "axes.facecolor":       "white",
        "axes.edgecolor":       "#d0d0d0",
        "axes.linewidth":       0.8,
        "axes.grid":            True,
        "grid.color":           "#eeeeee",
        "grid.linewidth":       0.5,
        "xtick.color":          "#596275",
        "ytick.color":          "#596275",
        "xtick.labelsize":      10,
        "ytick.labelsize":      10,
        "axes.labelsize":       11,
        "axes.titlesize":       13,
        "axes.titleweight":     "bold",
        "axes.titlecolor":      "#1c1c1c",
        "axes.labelcolor":      "#596275",
        "font.family":          "sans-serif",
        "legend.framealpha":    0.9,
        "legend.edgecolor":     "#d0d0d0",
        "figure.dpi":           150,
    })

print("Palette loaded ✅")
