import nbformat, base64, os

nb = nbformat.read('monte_carlo_integration.ipynb', as_version=4)
os.makedirs('readme_images', exist_ok=True)

img_count = 0
for cell in nb.cells:
    for output in getattr(cell, 'outputs', []):
        data = getattr(output, 'data', {})
        if 'image/png' in data:
            img_path = f'readme_images/plot_{img_count}.png'
            with open(img_path, 'wb') as f:
                f.write(base64.b64decode(data['image/png']))
            print(f'Saved {img_path}')
            img_count += 1

print(f'Done — {img_count} images extracted')