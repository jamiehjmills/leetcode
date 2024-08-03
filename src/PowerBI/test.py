import json
import os

# Load JSON data
def load_json_data(filename):
    with open(os.path.join('run_config_files', filename), 'r') as file:
        return json.load(file)

def save_new_json_data(filename, data):
    with open(os.path.join('run_config_files', filename), 'w') as file:
        json.dump(data, file, indent=2)

# Sample data for demonstration
run_config_files = {
    'bank_fin_nifty': 'run_config_bank_fin_nifty.json',
    'bank_nifty': 'run_config_bank_nifty.json',
    'layout': 'run_config_bank.json',
    'rule': 'rule.json',
    'new': 'new.json'
}

layout_data=load_json_data(run_config_files['layout'])
rule_data=load_json_data(run_config_files['rule'])
#print(layout_data)
#print(rule_data)

found = False
selected_rule = ""
data_for_rendering = []
for layout in layout_data:
    #print(layout["name"])
    for rule in rule_data:
        if rule["name"] == layout["name"]:
            found = True
            selected_rule=rule
            continue

    if found:
        data_for_rendering.append(selected_rule)
        found = False
    else:
        data_for_rendering.append(layout)


#print(data_for_rendering)

rule_data=save_new_json_data(run_config_files['new'],data_for_rendering)