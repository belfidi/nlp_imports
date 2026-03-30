import sys
sys.path.append("/Users/olgashitikova/python_settings")
from palette import C

TABLE_STYLES_BASE = [
    {'selector': 'caption', 'props': [('font-size', '12px'), ('font-weight', 'bold'), ('color', '#1c1c1c'), ('padding-bottom', '8px'), ('text-align', 'left')]},
    {'selector': 'th', 'props': [('background-color', '#4a90d9'), ('color', 'white'), ('font-weight', 'bold'), ('font-size', '11px'), ('padding', '8px 12px'), ('text-align', 'center')]},
    {'selector': 'td', 'props': [('font-size', '11px'), ('padding', '6px 12px'), ('font-family', 'sans-serif')]},
    {'selector': 'tr:nth-child(even)', 'props': [('background-color', '#e8f4fd')]},
]

PROPS_BASE = {'font-size': '11px', 'font-family': 'sans-serif', 'border': '0.5px solid #d0d0d0', 'padding': '6px 12px'}

def style_report(df, caption="Classification Report", metric_cols=None, support_col='Support', error_col=None):
    if metric_cols is None:
        metric_cols = [c for c in ['Precision', 'Recall', 'F1-Score'] if c in df.columns]
    fmt = {col: '{:.2f}' for col in metric_cols}
    if support_col and support_col in df.columns:
        fmt[support_col] = '{:,}'
    if error_col and error_col in df.columns:
        fmt[error_col] = '{:,}'
    styled = (df.style.set_caption(caption).format(fmt).background_gradient(subset=metric_cols, cmap='Greens', vmin=0.7, vmax=1.0).set_properties(**PROPS_BASE).set_table_styles(TABLE_STYLES_BASE + [{'selector': 'tr:last-child', 'props': [('font-weight', 'bold'), ('border-top', '2px solid #d0d0d0')]}]).hide(axis='index'))
    if error_col and error_col in df.columns:
        styled = styled.bar(subset=[error_col], color='#f7c6c2', vmin=0)
    return styled

def style_benchmark(df, caption="Benchmark Comparison", value_col='Accuracy (%)', highlight_row=0):
    fmt = {col: '{:.1f}' for col in df.select_dtypes('number').columns}
    def highlight_your_model(row):
        if row.name == highlight_row:
            return ['background-color: #e5f6ec; font-weight: bold'] * len(row)
        return [''] * len(row)
    styled = (df.style.set_caption(caption).format(fmt, na_rep='—').apply(highlight_your_model, axis=1).set_properties(**PROPS_BASE).set_table_styles(TABLE_STYLES_BASE).hide(axis='index'))
    if value_col in df.columns:
        styled = styled.bar(subset=[value_col], color='#a8d4f5', vmin=df[value_col].min() * 0.95, vmax=100)
    return styled

def style_dataset(df, caption="Dataset Overview"):
    return (df.style.set_caption(caption).format(na_rep='—').set_properties(**PROPS_BASE).set_table_styles(TABLE_STYLES_BASE).hide(axis='index'))

def style_escalation(df, caption="Escalation Log Summary"):
    def highlight_escalated(row):
        if 'Escalated' in row.index and row['Escalated'] in [True, 'Yes', 'yes']:
            return ['background-color: #fdf0ef'] * len(row)
        return [''] * len(row)
    return (df.style.set_caption(caption).format(na_rep='—').apply(highlight_escalated, axis=1).set_properties(**PROPS_BASE).set_table_styles(TABLE_STYLES_BASE).hide(axis='index'))

def save_table(styled, path, dpi=150):
    import dataframe_image as dfi
    dfi.export(styled, path, dpi=dpi, max_rows=-1)
    print(f"Saved ✅ {path}")

print("Styling module loaded ✅")
