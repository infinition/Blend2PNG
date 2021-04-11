cd "C:\Users\Bjornulf\Desktop\fbxspace\BLEND2PNG\"
for %%f in (*blend) do ("C:\Program Files\Blender Foundation\Blender 2.82\blender.exe" "C:\Users\Bjornulf\Desktop\fbxspace\BLEND2PNG\%%~nf.blend" -P BLEND2PNG.py)

