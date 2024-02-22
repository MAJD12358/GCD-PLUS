import json

def generate_gcdplus_from_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    gcdplus_code = f"# {data['language']} Configuration\n\n"
    gcdplus_code += f"Language#{data['language']}#{data['version']}\n"
    gcdplus_code += f"Author#{data['author']}\n\n"
    
    for feature, value in data['features'].items():
        gcdplus_code += f"{feature}#true\n" if value else f"{feature}#false\n"

    gcdplus_code += "\nDefaults\n"
    for key, value in data['defaults'].items():
        gcdplus_code += f"  {key}#{value}\n"

    return gcdplus_code

# Usage example:
json_file_path = 'gcdplus-config.json'
generated_code = generate_gcdplus_from_json(json_file_path)
print(generated_code)
        
