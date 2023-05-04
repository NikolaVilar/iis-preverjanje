import pandas as pd
import evidently

reference_data = pd.read_csv('reference_data.csv')
current_data = pd.read_csv('current_data.csv')

data_drift_preset = evidently.pandas_profile(DataDriftPreset, reference_data, current_data, column_mapping=None)

report = data_drift_preset.json()
with open('../../reports/data_drift_report.html', 'w') as f:
    f.write(report)
