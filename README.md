poetry new iis-preverjanje

poetry add pandas 
poetry add scikit-learn
poetry add evidently

git init
git add .
git commit -m "init"
git branch -M main
git remote add origin https://github.com/NikolaVilar/iis-preverjanje.git
git push -u origin main
