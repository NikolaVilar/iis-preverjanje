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

pip install dvc
dvc init
dvc add data
git add .
git commit -m "..."

git push origin main
dvc remote add myremote /iis-preverjanje/data
dvc push -r myremote

cd data
python process_data.py



