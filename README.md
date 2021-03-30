# SpeechToText
cd SpeechToText/API_service/
virtualenv env -p python3
source env/bin/activate
pip install -r requirements.txt
python app.py

#Il servizio è accedibile da browser su http://localhost:9999/flaskAPI/
#accetta in ingresso una stringa "user_id"
#restituisce la solita stringa
