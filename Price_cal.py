import pandas as pd

# Input data
data = [
    (14.16, "7.62x10.16"),
    (14.16, "10.92x7.62"),
    (15.00, "7.62x12.06"),
    (18.88, "20.32x16.51"),
    (21.24, "20.32x7.62"),
    (21.24, "17.78x22.86"),
    (21.24, ""),
    (22.42, "17.78x25.40"),
    (23.60, ""),
    (23.60, "10.16x12.70"),
    (24.00, "25.40x25.40"),
    (25.96, "15.72x20.88"),
    (29.50, "10.16x12.70"),
    (29.50, "20.93x25.40"),
    (29.50, "16.39x17.78"),
    (29.50, "20.95x25.40"),
    (30.00, ""),
    (35.00, "15.24x7.62"),
    (35.40, "12.70x25.40"),
    (35.40, "16.51x10.16"),
    (35.40, "17.78x35.56"),
    (35.40, "10.16x20.32"),
    (35.40, "24.41x26.88"),
    (35.40, "25.40x27.94"),
    (35.40, "39.37x19.05"),
    (35.40, "17.78x35.56"),
    (41.30, "50x70"),
    (47.20, "26.67x39.37"),
    (47.20, "17.78x40.64"),
    (47.20, "17.78x30.48"),
    (53.00, "12.70x30.48"),
    (53.00, "30.56x35.56"),
    (53.00, "30.48x30.48"),
    (57.00, "41.40x33.91"),
    (57.00, "25.40x25.40"),
    (59.00, "17.78x55.88"),
    (59.00, "26.67x62.23"),
    (59.00, "40.64x15.24"),
    (65.00, "17.78x60.96"),
    (65.00, "17.78x35.56"),
    (65.00, "27.94x52.07"),
    (65.00, "35.56x35.56"),
    (65.00, "25.40x22.86"),
    (65.00, "25.40x40.64"),
    (65.00, "10.16x20.32"),
    (71.00, "30.48x30.48"),
    (76.00, "100x700"),
    (118.00, "38.10x38.10"),
    (125.00, "38.48x43.18"),
    (148.00, "40.64x36.83"),
    (153.00, "55.88x55.88"),
    (224.00, "64.14x24.13"),
]

# Convert to DataFrame
df = pd.DataFrame(data, columns=["Price (Rs.)", "PCB Dimensions (mm)"])

# Function to compute area and per mm² price
def compute(row):
    if "x" not in row["PCB Dimensions (mm)"] or row["PCB Dimensions (mm)"] == "":
        return pd.Series([None, None])
    w, h = map(float, row["PCB Dimensions (mm)"].split("x"))
    area = w * h
    #price_per_mm2 = row["Price (Rs.)"] / area if area > 0 else None
    #return pd.Series([area, price_per_mm2])
    price_per_cm2 = (row["Price (Rs.)"] / area * 100) if area > 0 else None
    return pd.Series([area, price_per_cm2])

df[["Area (mm²)", "Price per mm² (Rs.)"]] = df.apply(compute, axis=1)

print(df)

#import caas_jupyter_tools
#caas_jupyter_tools.display_dataframe_to_user("PCB Price per mm² Table", df)

