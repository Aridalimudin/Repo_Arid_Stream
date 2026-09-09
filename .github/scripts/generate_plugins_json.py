import os
import json

src_dir = os.path.join(os.environ.get('GITHUB_WORKSPACE', ''), 'main')
build_dir = os.path.join(os.environ.get('GITHUB_WORKSPACE', ''), 'builds')

print(f"Scanning: {src_dir}")
print(f"Output:   {build_dir}")

# First try to use Gradle-generated plugins.json
gradle_json = os.path.join(src_dir, 'build', 'plugins.json')
if os.path.exists(gradle_json):
    import shutil
    dest = os.path.join(build_dir, 'plugins.json')
    shutil.copy2(gradle_json, dest)
    print(f"Copied Gradle plugins.json to {dest}")
else:
    # Fallback: collect plugin-entry.json from each subproject
    print("Gradle plugins.json not found, generating from plugin-entry.json files...")
    entries = []
    for root, dirs, files in os.walk(src_dir):
        for f in files:
            if f == 'plugin-entry.json':
                path = os.path.join(root, f)
                try:
                    with open(path, 'r', encoding='utf-8') as fp:
                        data = json.load(fp)
                        entries.append(data)
                        print('Added entry: ' + str(data.get('name', path)))
                except Exception as e:
                    print('Error reading ' + path + ': ' + str(e))

    out_path = os.path.join(build_dir, 'plugins.json')
    with open(out_path, 'w', encoding='utf-8') as fp:
        json.dump(entries, fp, indent=2)
    print('Generated plugins.json with ' + str(len(entries)) + ' entries at ' + out_path)

print("Done!")
