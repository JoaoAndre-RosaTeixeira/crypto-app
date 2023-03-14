<h1>Cryptography app</h1>
<h2>Discover several encryption and hashing algorithms and learn more about their purpose and how they work</h2>
<p>Cryptography is playing a huge part in today's world. This application allows you to try many encryption and hashing techniques while giving you detailed information about them. KryptX is not meant to be a secure solution to encrypt your data. Instead, it aims to tell you more about the most commonly used systems today, as well as some old encryption techniques that made history.</p>
<h2>Features</h2>

 - 4 modern encryption tehniques: AES, Blowfish, RSA, DES
 - 3 historical encryption techniques: Caesar Cipher, Vigenère Cipher, Enigma M3
 - 2 hashing techniques: MD5 & SHA
-  Each technique comes with an information box that tells you more about its history as well as its main features



<h2>Test unitaires</h2>

<p>nous avons creer des test unitaires dans le dossier crypto_app nommées chacun test_<nom_du_fichier_tester> </p>


Pour lancer les test unitaires il suffit de sauvegarder vos changements et faire : 

 - git add <nom du fichie>
 - git commit  -m “message du commit”
 - git push gitlab <mon_nom_de_branche>
 - git push github <mon_nom_de_branche>



<h2>How it was made</h2>

 -   Backend in Flask
 -   Frontend in HTML-CSS-JavaScript

<h2>How to run the app</h2>

In the project's root folder, run:

`pip install -r requirements.txt`

`python run_test_server.py`
