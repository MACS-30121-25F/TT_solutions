import pandas as pd
import numpy as np

#### don't include in distribution
morg_df = pd.read_csv("data/morg_d07_strings.csv", index_col="h_id")

### Tasks 2-6
age_col = morg_df["age"]
h_id_1_2_2 = morg_df.loc["1_2_2"]
slice = morg_df[:4]
ft_hours = morg_df[morg_df["hours_worked_per_week"] >= 35]

fill_cols = {}
for col in morg_df.columns:
    if any(morg_df[col].isna()):
        fill_cols[col] = 0.0

morg_df.fillna(value=fill_cols, inplace=True)

### Task 7
#### include in distribution
### convert to categoricals
TO_CATEGORICALS = ["gender", "race", "ethnicity", "employment_status"]

#### don't include in distribution
for cat in TO_CATEGORICALS:
    morg_df[cat] = morg_df[cat].astype("category")


#### include in distribution
### add age bins
boundaries = range(16, 89, 8)
morg_df["age_bin"] = pd.cut(morg_df["age"],
                            bins=boundaries,
                            labels=range(len(boundaries)-1),
                            include_lowest=True, right=False)


### Task 8
#### don't include in distribution
### add hours worked per week
boundaries = np.linspace(0, 99, 10)
morg_df["hwpw_bin"] = pd.cut(morg_df["hours_worked_per_week"],
                             bins=boundaries,
                             labels=range(len(boundaries)-1),
                             include_lowest=True, right=True)

print("Morg columns types after Task 8")
print(morg_df.dtypes)

### Tasks 9-11
#### don't include in distribution
ft_filter = (morg_df["hours_worked_per_week"] >= 35)
ft = morg_df[ft_filter]

not_working_filter = ~ (morg_df["employment_status"] == "Working")
not_working = morg_df[not_working_filter]

ft_1k_filter = ((morg_df["hours_worked_per_week"] >= 35) |
               (morg_df["earnings_per_week"] > 1000))
ft_1k = morg_df[ft_1k_filter]


### Task 12-13
#### don't include in distribution
race_value_cnts = morg_df["race"].value_counts()[:5]

race_gb = morg_df.groupby("race").size()

### Task 14
#### include in distribution
students = pd.read_csv("data/students.csv")
extended_grades = pd.read_csv("data/extended_grades.csv")

#### don't include in distribution
df = pd.merge(students, extended_grades, on="UCID", how="inner")
df0 = df.groupby(["Grade", "Major"]).size().reset_index()
df0.rename(columns={0:"Count"}, inplace=True)
print(df0)
