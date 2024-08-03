import json
import os

# Load JSON data
def load_json_data(filename):
    with open(os.path.join('run_config_files', filename), 'r') as file:
        return json.load(file)

# Sample data for demonstration
run_config_files = {
    'bank_fin_nifty': 'run_config_bank_fin_nifty.json',
    'bank_nifty': 'run_config_bank_nifty.json',
    'layout': 'run_config_bank.json',
    'rule': 'rule.json'
}

layout_data=load_json_data(run_config_files['layout'])
rule_data=load_json_data(run_config_files['rule'])
#print(layout_data)
print(rule_data)

data_for_rendering = {}
for layout in layout_data:
    print(layout["name"])
    found_item = next(
        (item for item in rule if item["name"] == layout["name"]), None
    )
    if found_item:
        # TODO need to update here

