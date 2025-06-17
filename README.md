# CTR_MATH

```markdown
# 📊 CTR Calculator: Google-Style Click-Through Rate

This script processes a CSV file containing click and impression data (such as from Google Search Console) and calculates the **true Click-Through Rate (CTR)** in **decimal format** (e.g., `0.30234` instead of `"30.23%"`).

---

## ✅ Output Format

The output is saved as a CSV file with the following exact columns:

| Column Name     | Description                                       |
|-----------------|---------------------------------------------------|
| `Landing Page`  | The full article URL (copied from original data) |
| `Impressions`   | Number of times the article was shown            |
| `Url Clicks`    | Number of user clicks on the article             |
| `URL CTR`       | Calculated CTR = `Clicks / Impressions` (float)  |

---

## 📁 Input File Format

The input CSV or TSV file must include at least:

- `URL` (used to create `Landing Page`)
- `Clicks` (numeric)
- `Impressions` (numeric)
- (Optional) `CTR` column with `%` format — used for validation

Example input:

```

Date,URL,Clicks,Impressions,CTR
2025-05-08,[https://example.com/article,136487,451539,30.23%](https://example.com/article,136487,451539,30.23%)

````

---

## ⚙️ How to Use

1. Install dependencies (if not already):

```bash
pip install pandas
````

2. Save the script as `calculate_ctr.py`

3. Place your data file (e.g., `data.csv`) in the same folder.

4. Run the script:

```bash
python calculate_ctr.py
```

5. Output will be saved as:

```
ctr_final_output.csv
```

---

## 🔍 Features

* ✅ Automatically computes CTR in decimal format (Google standard)
* ✅ Drops invalid rows (e.g., zero impressions)
* ✅ Performs internal validation if original CTR column exists
* ✅ Produces clean output ready for ML pipelines or dashboards

---

## 📄 Output Example

```
Landing Page,Impressions,Url Clicks,URL CTR
https://example.com/article,451539,136487,0.30234
```

---

## 🧪 Validation Logic (Optional)

If the input includes a `CTR` column (with `%`), the script will:

* Convert it to decimal (e.g., `"30.23%"` → `0.3023`)
* Compare it to the newly computed `URL CTR`
* Flag mismatches > 0.0001
* Print a report to console (not saved in the final CSV)

---

## ✏️ Customization Tips

* To filter by minimum impressions: add `df = df[df["Impressions"] > 1000]`
* To sort by CTR: use `df.sort_values(by="URL CTR", ascending=False)`
* To save as TSV: change `.to_csv(..., sep='\t')`

---

## 📬 Contact

For questions or improvements, feel free to open an issue or contribute!

```
