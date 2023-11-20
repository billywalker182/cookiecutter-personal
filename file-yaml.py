import yaml

with open('requirements.txt', 'r') as f:
    dependencies = f.read().split('\n')

yaml_content = {'dependencies': dependencies}

with open('environment.yaml', 'w') as f:
    yaml.dump(yaml_content, f, default_flow_style=False)
