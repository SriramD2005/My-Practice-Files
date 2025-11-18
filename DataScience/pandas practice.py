import pandas as pd

data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

def highlight_bg(val):
    return 'background-color: yellow' if val > 2 else ''

styled_df = df.style.applymap(highlight_bg)

print(styled_df)
