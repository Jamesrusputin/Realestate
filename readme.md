
brew install mkcert
brew install nss # if you use Firefox

mkcert 127.0.0.1

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python .\manage.py runsslserver --certificate <certificate_path> --key <key_path>