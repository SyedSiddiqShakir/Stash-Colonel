import os
import re
import pandas as pd
from itertools import zip_longest

comp_path = r"S:\Everything German\Werkstudent CVs and etc\Companies"
research_path = r"S:\Everything German\Werkstudent CVs and etc\Research Institutes and unis"
fraunhofer_path = r"S:\Everything German\Werkstudent CVs and etc\Research Institutes and unis\Fraunhofer"

def load_clean_names(path, skip_name=None):
    raw = [
        f for f in os.listdir(path)
        if os.path.isdir(os.path.join(path, f))
        and (skip_name is None or f.lower() != skip_name.lower())
    ]

    base = [re.sub(r"\d+$", "", name) for name in raw]

    unique = list(dict.fromkeys(base))

    return sorted(unique)

companies   = load_clean_names(comp_path)
research    = load_clean_names(research_path, skip_name="Fraunhofer")
fraunhofer  = load_clean_names(fraunhofer_path)


rows = zip_longest(companies, research, fraunhofer, fillvalue="")

df = pd.DataFrame(rows, columns=[
    "Companies",
    "Research Centers & Universities",
    "Fraunhofer"
])

output_file = "company_list_clean.csv"
df.to_csv(output_file, index=False)
print(f"Wrote {len(df)} rows to {output_file}")
