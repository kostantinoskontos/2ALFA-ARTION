from flask import Blueprint, render_template, request, flash, jsonify

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])

def home():
    


    return render_template("home.html")


@views.route('/Pites')
def Pites():
    PitesImage_data = [
        {'filename': '6ares-kaseri.jpg', 'categories': '6ares', 'onoma': '01-01-300 Χωριάτικη Τυρί 6άρα','keimeno': 'Βάρος ανά τεμάχιο: 1500gr<br />Τεμάχια ανά κιβώτιο/κιλά: 5<br />Κιβώτια ανά παλέτα: 92'},
        {'filename': '6ares-kimas.jpg', 'categories': '6ares', 'onoma': '01-01-301 Χωριάτικη Κασέρι 6άρα','keimeno': 'Βάρος ανά τεμάχιο: 1500gr<br />Τεμάχια ανά κιβώτιο/κιλά: 5<br />Κιβώτια ανά παλέτα: 92'},
        {'filename': '6ares-krema.jpg', 'categories': '6ares', 'onoma': '01-01-302 Χωριάτικη Ζαμπόν Κασέρι 6άρα','keimeno': 'Βάρος ανά τεμάχιο: 1500gr<br />Τεμάχια ανά κιβώτιο/κιλά: 5<br />Κιβώτια ανά παλέτα: 92'},
        {'filename': '6ares-praso-tyri.jpg', 'categories': '6ares', 'onoma': '01-01-303 Χωριάτικη Σπανάκι 6άρα','keimeno': 'Βάρος ανά τεμάχιο: 1500gr<br />Τεμάχια ανά κιβώτιο/κιλά: 5<br />Κιβώτια ανά παλέτα: 92'},
        {'filename': '6ares-praso.jpg', 'categories': '6ares', 'onoma': '01-01-304 Χωριάτικη Σπανάκι Τυρί 6άρα','keimeno': 'Βάρος ανά τεμάχιο: 1500gr<br />Τεμάχια ανά κιβώτιο/κιλά: 5<br />Κιβώτια ανά παλέτα: 92'},
        {'filename': '6ares-spanaki-tyri.jpg', 'categories': '6ares', 'onoma': '01-01-305 Χωριάτικη Πράσο 6άρα','keimeno': 'Βάρος ανά τεμάχιο: 1500gr<br />Τεμάχια ανά κιβώτιο/κιλά: 5<br />Κιβώτια ανά παλέτα: 92'},
        {'filename': '6ares-spanaki.jpg', 'categories': '6ares', 'onoma': '01-01-306 Χωριάτικη Πράσο Τυρί 6άρα','keimeno': 'Βάρος ανά τεμάχιο: 1500gr<br />Τεμάχια ανά κιβώτιο/κιλά: 5<br />Κιβώτια ανά παλέτα: 92'},
        {'filename': '6ares-xortopita.jpg', 'categories': '6ares', 'onoma': '01-01-307 Χωριάτικη Χορτόπιτα 6άρα','keimeno': 'Βάρος ανά τεμάχιο: 1500gr<br />Τεμάχια ανά κιβώτιο/κιλά: 5<br />Κιβώτια ανά παλέτα: 92'},
        {'filename': '6ares-zampon-kaseri.jpg', 'categories': '6ares', 'onoma': '01-01-308 Χωριάτικη Κρέμα 6άρα','keimeno': 'Βάρος ανά τεμάχιο: 1500gr<br />Τεμάχια ανά κιβώτιο/κιλά: 5<br />Κιβώτια ανά παλέτα: 92'},
        {'filename': '6ares-tyri.jpg', 'categories': '6ares', 'onoma': '01-01-309 Χωριάτικη Κιμάς 6άρα','keimeno': 'Βάρος ανά τεμάχιο: 1500gr<br />Τεμάχια ανά κιβώτιο/κιλά: 5<br />Κιβώτια ανά παλέτα: 92'},
        {'filename': '25X35-kima.jpg', 'categories': '25X35', 'onoma': '01-01-420 Χωριάτικη Τυρί Θρακιώτικη','keimeno': 'Βάρος ανά τεμάχιο: 1600gr<br />Τεμάχια ανά κιβώτιο/κιλά: 4<br />Κιβώτια ανά παλέτα: 88'},
        {'filename': '25X35-spanaki.jpg', 'categories': '25X35', 'onoma': '01-01-421 Χωριάτικη Σπανάκι Θρακιώτικη','keimeno': 'Βάρος ανά τεμάχιο: 1600gr<br />Τεμάχια ανά κιβώτιο/κιλά: 4<br />Κιβώτια ανά παλέτα: 88'},
        {'filename': '25X35-tyri-spanaki.jpg', 'categories': '25X35', 'onoma': '01-01-422 Χωριάτικη Σπανάκι Τυρί Θρακιώτικη','keimeno': 'Βάρος ανά τεμάχιο: 1600gr<br />Τεμάχια ανά κιβώτιο/κιλά: 4<br />Κιβώτια ανά παλέτα: 88'},
        {'filename': '25X35-tyri.jpg', 'categories': '25X35', 'onoma': '01-01-424 Χωριάτικη Κιμά Θρακιώτικη','keimeno': 'Βάρος ανά τεμάχιο: 1600gr<br />Τεμάχια ανά κιβώτιο/κιλά: 4<br />Κιβώτια ανά παλέτα: 88'},
        {'filename': '28X42-tyri.jpg', 'categories': '28X42', 'onoma': '01-01-200 Χωριάτικη Τυρί 28Χ42','keimeno': 'Βάρος ανά τεμάχιο: 2300gr<br />Τεμάχια ανά κιβώτιο/κιλά: 4<br />Κιβώτια ανά παλέτα: 72'},
        {'filename': '28X42-tyri-spanaki.jpg', 'categories': '28X42', 'onoma': '01-01-201 Σπανάκι 28Χ42','keimeno': 'Βάρος ανά τεμάχιο: 2300gr<br />Τεμάχια ανά κιβώτιο/κιλά: 4<br />Κιβώτια ανά παλέτα: 72'},
        {'filename': '28X42-spanaki.jpg', 'categories': '28X42', 'onoma': '01-01-202 Σπανάκι - Τυρί 28Χ42','keimeno': 'Βάρος ανά τεμάχιο: 2300gr<br />Τεμάχια ανά κιβώτιο/κιλά: 4<br />Κιβώτια ανά παλέτα: 72'},
        {'filename': 'agioritikes-kolokithi.jpg', 'categories': 'agioritikes', 'onoma': '01-05-151 Χωριάτικη Αγιορείτικη Χορτόπιτα','keimeno': 'Βάρος ανά τεμάχιο: 2300gr'},
        {'filename': 'agioritikes-kotopita.jpg', 'categories': 'agioritikes', 'onoma': '01-05-150 Χωριάτικη Αγιορείτικη Τυρί','keimeno': 'Βάρος ανά τεμάχιο: 2300gr'},
        {'filename': 'agioritikes-patata.jpg', 'categories': 'agioritikes', 'onoma': '01-05-153 Χωριάτικη Αγιορείτικη Πατάτα','keimeno': 'Βάρος ανά τεμάχιο: 2300gr'},
        {'filename': 'agioritikes-tyri.jpg', 'categories': 'agioritikes', 'onoma': '01-05-154 Χωριάτικη Αγιορείτικη Κολοκύθι','keimeno': 'Βάρος ανά τεμάχιο: 2300gr'},
        {'filename': 'agioritikes-kotopita.jpg', 'categories': 'agioritikes', 'onoma': '01-05-150 Χωριάτικη Αγιορείτικη Κοτόπιτα','keimeno': 'Βάρος ανά τεμάχιο: 2300gr'},
        {'filename': 'fakelos-kot.jpg', 'categories': 'fakelos', 'onoma': '01-02-051 Φάκελος Κοτόπουλο','keimeno': 'Βάρος ανά τεμάχιο: 250gr<br />Τεμάχια ανά κιβώτιο/κιλά: 25<br />Κιβώτια ανά παλέτα: 88'},
        {'filename': 'fakelos-manitarion.jpg', 'categories': 'fakelos', 'onoma': '01-02-053 Φάκελος Μανιταριών','keimeno': 'Βάρος ανά τεμάχιο: 250gr<br />Τεμάχια ανά κιβώτιο/κιλά: 25<br />Κιβώτια ανά παλέτα: 88'},
        {'filename': 'mpougatsakia-kima.jpg', 'categories': 'mpougatsakia', 'onoma': '01-02-003 Μπουγατσάκι Κρέμα','keimeno': 'Βάρος ανά τεμάχιο: 520gr<br />Τεμάχια ανά κιβώτιο/κιλά: 20<br />Κιβώτια ανά παλέτα: 70'},
        {'filename': 'mpougatsakia-krema.jpg', 'categories': 'mpougatsakia', 'onoma': '01-02-004 Μπουγατσάκι Τυρί','keimeno': 'Βάρος ανά τεμάχιο: 490gr<br />Τεμάχια ανά κιβώτιο/κιλά: 20<br />Κιβώτια ανά παλέτα: 70'},
        {'filename': 'mpougatsakia-spanaki-tyri.jpg', 'categories': 'mpougatsakia', 'onoma': '01-02-007 Μπουγατσάκι Σπανάκι Τυρί','keimeno': 'Βάρος ανά τεμάχιο: 490gr<br />Τεμάχια ανά κιβώτιο/κιλά: 20<br />Κιβώτια ανά παλέτα: 70'},
        {'filename': 'mpougatsakia-tyri.jpg', 'categories': 'mpougatsakia', 'onoma': '01-02-005 Μπουγατσάκι Κιμά','keimeno': 'Βάρος ανά τεμάχιο: 490gr<br />Τεμάχια ανά κιβώτιο/κιλά: 20<br />Κιβώτια ανά παλέτα: 70'},
        {'filename': 'mpoukitsa-kolokithi.jpg', 'categories': 'mpoukitsa', 'onoma': '01-01-106 Χωριάτικη Κολοκύθι Μπουκίτσα','keimeno': 'Βάρος ανά τεμάχιο: 2300gr<br />Τεμάχια ανά κιβώτιο/κιλά: 5<br />Κιβώτια ανά παλέτα: 54'},
        {'filename': 'mpoukitsa-praso-tyri.jpg', 'categories': 'mpoukitsa', 'onoma': '01-01-105 Χωριάτικη Πράσο Τυρί Μπουκίτσα','keimeno': 'Βάρος ανά τεμάχιο: 2300gr<br />Τεμάχια ανά κιβώτιο/κιλά: 5<br />Κιβώτια ανά παλέτα: 54'},
        {'filename': 'mpoukitsa-zampon-kaseri.jpg', 'categories': 'mpoukitsa', 'onoma': '01-01-100 Χωριάτικη Τυρί Μπουκίτσα','keimeno': 'Βάρος ανά τεμάχιο: 2300gr<br />Τεμάχια ανά κιβώτιο/κιλά: 5<br />Κιβώτια ανά παλέτα: 54'},
        {'filename': 'mpoukitsa-praso.jpg', 'categories': 'mpoukitsa', 'onoma': '01-01-101 Χωριάτικη Ζαμπόν-Κασέρι Μπουκίτσα','keimeno': 'Βάρος ανά τεμάχιο: 2300gr<br />Τεμάχια ανά κιβώτιο/κιλά: 5<br />Κιβώτια ανά παλέτα: 54'},
        {'filename': 'mpoukitsa-spanaki.jpg', 'categories': 'mpoukitsa', 'onoma': '01-01-102 Χωριάτικη Σπανάκι Μπουκίτσα','keimeno': 'Βάρος ανά τεμάχιο: 2300gr<br />Τεμάχια ανά κιβώτιο/κιλά: 5<br />Κιβώτια ανά παλέτα: 54'},
        {'filename': 'mpoukitsa-tyri-spanaki.jpg', 'categories': 'mpoukitsa', 'onoma': '01-01-103 Χωριάτικη Σπανάκι Τυρί Μπουκίτσα','keimeno': 'Βάρος ανά τεμάχιο: 2300gr<br />Τεμάχια ανά κιβώτιο/κιλά: 5<br />Κιβώτια ανά παλέτα: 54'},
        {'filename': 'mpoukitsa-tyri.jpg', 'categories': 'mpoukitsa', 'onoma': '01-01-104 Χωριάτικη Πράσο Μπουκίτσα','keimeno': 'Βάρος ανά τεμάχιο: 2300gr<br />Τεμάχια ανά κιβώτιο/κιλά: 5<br />Κιβώτια ανά παλέτα: 54'},
        {'filename': 'mpourekaki-patata.jpg', 'categories': 'mpourekaki', 'onoma': '01-02-307 Μπουρεκάκι Πατάτα','keimeno': 'Βάρος ανά τεμάχιο: 47gr<br />Τεμάχια ανά κιβώτιο/κιλά: 6<br />Κιβώτια ανά παλέτα: 88'},
        {'filename': 'mpourekaki-tyri.jpg', 'categories': 'mpourekaki', 'onoma': '01-02-304 Μπουρεκάκι Τυρί','keimeno': 'Βάρος ανά τεμάχιο: 250gr<br />Τεμάχια ανά κιβώτιο/κιλά: 25<br />Κιβώτια ανά παλέτα: 88'},
        {'filename': 'mpourekaki-zampon.jpg', 'categories': 'mpourekaki', 'onoma': '01-02-305 Μπουρεκάκι Ζαμπόν Κασσέρι','keimeno': 'Βάρος ανά τεμάχιο: 250gr<br />Τεμάχια ανά κιβώτιο/κιλά: 25<br />Κιβώτια ανά παλέτα: 88'},
        {'filename': 'mpoyrekaki-kotopoulo.jpg', 'categories': 'mpourekaki', 'onoma': '01-02-308 Μπουρεκάκι Κοτόπουλο','keimeno': 'Βάρος ανά τεμάχιο: 250gr<br />Τεμάχια ανά κιβώτιο/κιλά: 25<br />Κιβώτια ανά παλέτα: 88'},
        {'filename': 'mpoyrekaki-spanaki.jpg', 'categories': 'mpourekaki', 'onoma': '01-02-306 Μπουρεκάκι Σπανάκι','keimeno': 'Βάρος ανά τεμάχιο: 250gr<br />Τεμάχια ανά κιβώτιο/κιλά: 25<br />Κιβώτια ανά παλέτα: 88'},
        {'filename': 'petromilou.jpg', 'categories': 'petromilou', 'onoma': '01-01-400 Χωριάτικη Πετρόμυλου Σπανάκι-Μανιτάρι','keimeno': 'Βάρος ανά τεμάχιο: 1500gr'},
        {'filename': 'strifti-ntomata-elia.jpg', 'categories': 'strifti', 'onoma': '01-02-103 Στριφτή Ντομάτα Ελιά','keimeno': 'Βάρος ανά τεμάχιο: 220gr<br />Τεμάχια ανά κιβώτιο/κιλά: 30<br />Κιβώτια ανά παλέτα: 92'},
        {'filename': 'strifti-spanaki-tyri.jpg', 'categories': 'strifti', 'onoma': '01-02-102 Στριφτή Σπανάκι Τυρί','keimeno': 'Βάρος ανά τεμάχιο: 220gr<br />Τεμάχια ανά κιβώτιο/κιλά: 30<br />Κιβώτια ανά παλέτα: 92'},
        {'filename': 'strifti-spanaki.jpg', 'categories': 'strifti', 'onoma': '01-02-101 Στριφτή Σπανάκι','keimeno': 'Βάρος ανά τεμάχιο: 220gr<br />Τεμάχια ανά κιβώτιο/κιλά: 30<br />Κιβώτια ανά παλέτα: 92'},
        {'filename': 'strifti-tyri.jpg', 'categories': 'strifti', 'onoma': '01-02-100 Στριφτή Τυρί','keimeno': 'Βάρος ανά τεμάχιο: 220gr<br />Τεμάχια ανά κιβώτιο/κιλά: 30<br />Κιβώτια ανά παλέτα: 92'},
        {'filename': 'xoriatikh-10ara-spanaki-tyri.jpg', 'categories': 'xoriatikh', 'onoma': '01-01-003 Χωριάτικη Σπανάκι Τυρί 10αρα','keimeno': 'Βάρος ανά τεμάχιο: 2300gr<br />Τεμάχια ανά κιβώτιο/κιλά: 5<br />Κιβώτια ανά παλέτα: 54'},
        {'filename': 'xoriatikh-10ara-spanaki.jpg', 'categories': 'xoriatikh', 'onoma': '01-01-002 Χωριάτικη Σπανάκι 10αρα','keimeno': 'Βάρος ανά τεμάχιο: 2300gr<br />Τεμάχια ανά κιβώτιο/κιλά: 5<br />Κιβώτια ανά παλέτα: 54'},
        {'filename': 'xoriatikh-10ara-tyri.jpg', 'categories': 'xoriatikh', 'onoma': '01-01-001 Χωριάτικη Τυρί 10αρα','keimeno': 'Βάρος ανά τεμάχιο: 2300gr<br />Τεμάχια ανά κιβώτιο/κιλά: 5<br />Κιβώτια ανά παλέτα: 54'}
        
    ]
    return render_template("Pites.html", PitesImage_data=PitesImage_data)


@views.route('/Company')
def Company():
    return render_template("Company.html")

@views.route('/Sfoliata')
def Sfoliata():
    SfoliataImage_data = [
        {'filename': 'sfoliata.jpg', 'categories': 'Sfoliates', 'onoma': '01-03-001 Σφολιάτα Τρίγωνη 200γρ.','keimeno': 'Βάρος ανά τεμάχιο: 200gr<br />Τεμάχια ανά κιβώτιο/κιλά: 30<br />Κιβώτια ανά παλέτα: 88'},
        {'filename': 'sfoliata.jpg', 'categories': 'Sfoliates', 'onoma': '01-03-002 Σφολιάτα Τρίγωνη 150γρ.','keimeno': 'Βάρος ανά τεμάχιο: 150gr<br />Τεμάχια ανά κιβώτιο/κιλά: 35<br />Κιβώτια ανά παλέτα: 92'},
        {'filename': 'sfoliata-loykaniko.jpg', 'categories': 'Sfoliates', 'onoma': '01-03-004 Σφολιάτα Λουκάνικο Γίγας','keimeno': 'Βάρος ανά τεμάχιο: 200gr<br />Τεμάχια ανά κιβώτιο/κιλά: 35<br />Κιβώτια ανά παλέτα: 88'},
        {'filename': 'flogera-kotopoulo.jpg', 'categories': 'Sfoliates', 'onoma': '01-03-005 Φλογέρα Κοτόπουλο','keimeno': 'Βάρος ανά τεμάχιο: 230gr<br />Τεμάχια ανά κιβώτιο/κιλά: 30<br />Κιβώτια ανά παλέτα: 88'},
        {'filename': 'sfoliata-ntomata.jpg', 'categories': 'Sfoliates', 'onoma': '01-03-007 Σφολιάτα Ζαμπόν Κασέρι Ντομάτα','keimeno': 'Βάρος ανά τεμάχιο: 230gr<br />Τεμάχια ανά κιβώτιο/κιλά: 30<br />Κιβώτια ανά παλέτα: 88'},
        {'filename': 'sfoliata-zampon.jpg', 'categories': 'Sfoliates', 'onoma': '01-03-006 Σφολιάτα Έξτρα Ζαμπόν Κασέρι','keimeno': 'Βάρος ανά τεμάχιο: 240gr<br />Τεμάχια ανά κιβώτιο/κιλά: 28<br />Κιβώτια ανά παλέτα: 92'},
        {'filename': 'sfoliata-tyria.jpg', 'categories': 'Sfoliates', 'onoma': '01-03-016 Σφολιάτα Έξτρα Κρέμα Τυριών','keimeno': 'Βάρος ανά τεμάχιο: 240gr<br />Τεμάχια ανά κιβώτιο/κιλά: 28<br />Κιβώτια ανά παλέτα: 92'},
        {'filename': 'tyropitaki.jpg', 'categories': 'Mini-Sfoliates', 'onoma': '01-03-100 Τυροπιτάκι','keimeno': 'Βάρος ανά τεμάχιο: 48gr<br />Τεμάχια ανά κιβώτιο/κιλά: 6<br />Κιβώτια ανά παλέτα: 88'},
        {'filename': 'kaseropitaki.jpg', 'categories': 'Mini-Sfoliates', 'onoma': '01-03-101 Κασεροπιτάκι','keimeno': 'Βάρος ανά τεμάχιο: 55gr<br />Τεμάχια ανά κιβώτιο/κιλά: 6<br />Κιβώτια ανά παλέτα: 88'},
        {'filename': 'zamponokaseropitaki.jpg', 'categories': 'Mini-Sfoliates', 'onoma': '01-03-102 Ζαμπόνοκασεροπιτάκι','keimeno': 'Βάρος ανά τεμάχιο: 55gr<br />Τεμάχια ανά κιβώτιο/κιλά: 6<br />Κιβώτια ανά παλέτα: 88'},
        {'filename': 'loykanopitaki.jpg', 'categories': 'Mini-Sfoliates', 'onoma': '01-03-103 Λουκανοπιτάκι','keimeno': 'Βάρος ανά τεμάχιο: 35gr<br />Τεμάχια ανά κιβώτιο/κιλά: 7<br />Κιβώτια ανά παλέτα: 88'},
        {'filename': 'patata-ntomata.jpg', 'categories': 'Mini-Sfoliates', 'onoma': '01-03-104 Πατάτα-ντομάτα-ελιά μίνι','keimeno': 'Βάρος ανά τεμάχιο: 55gr<br />Τεμάχια ανά κιβώτιο/κιλά: 6<br />Κιβώτια ανά παλέτα: 88'},
        {'filename': 'strobylia-olikis.jpg', 'categories': 'Sfoliates-olikis', 'onoma': '01-03-450 Στροβιλιά Ολικής Ανθότυρο Γαλοπούλα','keimeno': 'Βάρος ανά τεμάχιο: 230gr<br />Τεμάχια ανά κιβώτιο/κιλά: 24<br />Κιβώτια ανά παλέτα: 92'},
        {'filename': 'sfoliataki-olikis.jpg', 'categories': 'Sfoliates-olikis', 'onoma': '01-03-452 Μίνι Σφολιατάκι Ολικής Ανθότυρο Γαλοπούλα','keimeno': 'Βάρος ανά τεμάχιο: 60gr<br />Τεμάχια ανά κιβώτιο/κιλά: 6<br />Κιβώτια ανά παλέτα: 88'},
        {'filename': 'kroyasan-zampon.jpg', 'categories': 'Zymes-Krouasan', 'onoma': '01-03-200 Κρουασάν Ζαμπόν Κασέρι Μπέικον','keimeno': 'Βάρος ανά τεμάχιο: 260gr<br />Τεμάχια ανά κιβώτιο/κιλά: 25<br />Κιβώτια ανά παλέτα: 88'},
        {'filename': 'krouasan-milopitaki.jpg', 'categories': 'Zymes-Krouasan', 'onoma': '01-03-201 Κρουασάν Μίνι Μηλοπιτάκι','keimeno': 'Βάρος ανά τεμάχιο: 55gr<br />Τεμάχια ανά κιβώτιο/κιλά: 6<br />Κιβώτια ανά παλέτα: 88'},
        {'filename': 'krouasan-kremopitaki.jpg', 'categories': 'Zymes-Krouasan', 'onoma': '01-03-202 Κρουασάν Μίνι Κρεμοπιτάκι','keimeno': 'Βάρος ανά τεμάχιο: 55gr<br />Τεμάχια ανά κιβώτιο/κιλά: 6<br />Κιβώτια ανά παλέτα: 88'},
        {'filename': 'kroyasan-margarinis.jpg', 'categories': 'Zymes-Krouasan', 'onoma': '02-01-003 Κρουασάν μαργαρίνης Μίνι 25γρ.','keimeno': ''},
        {'filename': 'kroyasan-margarinis125gr.jpg', 'categories': 'Zymes-Krouasan', 'onoma': '02-01-002 Κρουασάν μαργαρίνης 120γρ.','keimeno': ''},
        {'filename': 'kroyasan-margarinis150gr.jpg', 'categories': 'Zymes-Krouasan', 'onoma': '02-01-001 Κρουασάν μαργαρίνης 150γρ.','keimeno': ''},
        {'filename': 'strobylia-tyri.jpg', 'categories': 'Sfoliates-Strobilies', 'onoma': '01-03-009 Στροβιλιά Τυρί','keimeno': 'Βάρος ανά τεμάχιο: 230gr<br />Τεμάχια ανά κιβώτιο/κιλά: 24<br />Κιβώτια ανά παλέτα: 92'},
        {'filename': 'strobylia-kaseri.jpg', 'categories': 'Sfoliates-Strobilies', 'onoma': '01-03-010 Στροβιλιά Κασέρι','keimeno': 'Βάρος ανά τεμάχιο: 220gr<br />Τεμάχια ανά κιβώτιο/κιλά: 24<br />Κιβώτια ανά παλέτα: 92'},
        {'filename': 'strobylia-kaseri-zampon.jpg', 'categories': 'Sfoliates-Strobilies', 'onoma': '01-03-011 Στροβιλιά Ζαμπόν Κασέρι','keimeno': 'Βάρος ανά τεμάχιο: 230gr<br />Τεμάχια ανά κιβώτιο/κιλά: 24<br />Κιβώτια ανά παλέτα: 92'},
        {'filename': 'strobylia-grabiera.jpg', 'categories': 'Sfoliates-Strobilies', 'onoma': '01-03-012 Στροβιλιά Γραβιέρα Γαλοπούλα','keimeno': 'Βάρος ανά τεμάχιο: 230gr<br />Τεμάχια ανά κιβώτιο/κιλά: 24<br />Κιβώτια ανά παλέτα: 92'},
        {'filename': 'strobylia-patata.jpg', 'categories': 'Sfoliates-Strobilies', 'onoma': '01-03-013 Στροβιλιά Πατάτα Ελιά','keimeno': 'Βάρος ανά τεμάχιο: 230gr<br />Τεμάχια ανά κιβώτιο/κιλά: 24<br />Κιβώτια ανά παλέτα: 92'},
        {'filename': 'strobylia-ntomata.jpg', 'categories': 'Sfoliates-Strobilies', 'onoma': '01-03-014 Στροβιλιά Ντομάτα Ελιά','keimeno': 'Βάρος ανά τεμάχιο: 230gr<br />Τεμάχια ανά κιβώτιο/κιλά: 24<br />Κιβώτια ανά παλέτα: 92'},
        {'filename': 'strobylia-filadelfia.jpg', 'categories': 'Sfoliates-Strobilies', 'onoma': '01-03-015 Στροβιλιά Φιλαδέλφεια (με επικάλυψη φρυγανιάς)','keimeno': 'Βάρος ανά τεμάχιο: 230gr<br />Τεμάχια ανά κιβώτιο/κιλά: 24<br />Κιβώτια ανά παλέτα: 92'},
        {'filename': 'patiti.jpg', 'categories': 'Patites', 'onoma': '01-03-300 Πατητή Τυρί','keimeno': ''},
        {'filename': 'patiti.jpg', 'categories': 'Patites', 'onoma': '01-03-301 Πατητή Κασέρι','keimeno': ''},
        {'filename': 'patito-koulouri-tyri.jpg', 'categories': 'Patites', 'onoma': '','keimeno': ''},
        {'filename': 'patito-koulouri-kaseri.jpg', 'categories': 'Patites', 'onoma': '','keimeno': ''},
        {'filename': 'brioche-taxini.jpg', 'categories': 'Zymes-ZymesBrioche', 'onoma': '01-03-400 Brioche Στροβιλιά Ταχίνι','keimeno': ''},
        {'filename': 'brioche-grabiera.jpg', 'categories': 'Zymes-ZymesBrioche', 'onoma': '01-03-401 Brioche Γραβιέρα Μπέικον','keimeno': 'Βάρος ανά τεμάχιο: 240gr<br />Τεμάχια ανά κιβώτιο/κιλά: 30<br />Κιβώτια ανά παλέτα: 88'},
        {'filename': 'kaserokoulouro.jpg', 'categories': 'Zymes-ZymesBrioche', 'onoma': '01-03-502 Κασεροκούλουρο Προψημένο','keimeno': ''},
        {'filename': 'koulouri-filadelfia.jpg', 'categories': 'ZymesKourou-Polyspores', 'onoma': '01-03-252 Κουλούρι Φιλαδέλφεια','keimeno': ''},
        {'filename': 'kourou.jpg', 'categories': 'ZymesKourou-Polyspores', 'onoma': '01-03-250 Κουρουπιτάκι Τυρί','keimeno': ''},
        {'filename': 'kourou-loukaniko.jpg', 'categories': 'ZymesKourou-Polyspores', 'onoma': '01-03-251 Μίνι κουρού Λουκάνικο-Μουστάρδα','keimeno': ''},
        {'filename': 'koulouri-polysporo.jpg', 'categories': 'ZymesKourou-Polyspores', 'onoma': '01-03-254 Κουλούρι Πολύσπορο Φιλαδέλφεια','keimeno': ''},
        {'filename': 'kourou-anthotyro.jpg', 'categories': 'ZymesKourou-Polyspores', 'onoma': '01-03-255 Μίνι Κουρού Πολύσπορο Ανθότυρο','keimeno': ''},
        {'filename': 'mykoniatiko.jpg', 'categories': 'Sfoliates', 'onoma': '01-03-003 Μυκονιάτικο Λουκάνικο-Κασέρι Μουστάρδα','keimeno': 'Βάρος ανά τεμάχιο: 230gr<br />Τεμάχια ανά κιβώτιο/κιλά: 25<br />Κιβώτια ανά παλέτα: 88'}
        
    ]
    return render_template("Sfoliata.html", SfoliataImage_data=SfoliataImage_data)

@views.route('/Psimena')
def Psimena():
    PsimenaImage_data = [
        {'filename': 'Kritsini-Sousami.jpg', 'categories': 'Kritsinia', 'onoma': '01-04-001 Κριτσίνι Λευκό Σουσάμι','keimeno': ''},
        {'filename': 'Kritsini-Olikis.jpg', 'categories': 'Kritsinia', 'onoma': '01-04-002 Κριτσίνι Ολικής Σουσάμι','keimeno': ''},
        {'filename': 'Kritsini-Olikis.jpg', 'categories': 'Kritsinia', 'onoma': '01-04-003 Κριτσίνι Ολικής Ηλιόσπορος','keimeno': ''},
        {'filename': 'Kritsini-Olikis.jpg', 'categories': 'Kritsinia', 'onoma': '01-04-009 Κριτσίνι Ολικής Πολύσπορο','keimeno': ''},
        {'filename': 'Kritsini-Kalampoki.jpg', 'categories': 'Kritsinia', 'onoma': '01-04-004 Κριτσίνι Καλαμπόκι','keimeno': ''},
        {'filename': 'Kritsini-Kefalotyri.jpg', 'categories': 'Kritsinia', 'onoma': '01-04-005 Κριτσίνι Κεφαλοτύρι','keimeno': ''},
        {'filename': 'Kritsini-Zeas.jpg', 'categories': 'Kritsinia', 'onoma': '01-04-0010 Κριτσίνι Ζέας','keimeno': ''},
        {'filename': 'Stick-Mayro.jpg', 'categories': 'Stick', 'onoma': '01-04-100 Stick Μαύρο-σουσάμι','keimeno': ''},
        {'filename': 'Stick-Spanaki.jpg', 'categories': 'Stick', 'onoma': '01-04-101 Stick Σπανάκι','keimeno': ''},
        {'filename': 'Stick-Paprika.jpg', 'categories': 'Stick', 'onoma': '01-04-103 Stick Πάπρικα Ελιά','keimeno': ''},
        {'filename': 'Stick-Mesogiako.jpg', 'categories': 'Stick', 'onoma': '01-04-102 Stick Μεσογειακό με Ελαιόλαδο','keimeno': ''},
        {'filename': 'Krikos-Iliosporos.jpg', 'categories': 'Krikoi', 'onoma': '01-04-201 Κρίκος Ολικής Ηλιόσπορος','keimeno': ''},
        {'filename': 'Krikos-Kalampoki.jpg', 'categories': 'Krikoi', 'onoma': '01-04-202 Κρίκος καλαμπόκι','keimeno': ''},
        {'filename': 'Krikos-Taxini.jpg', 'categories': 'Krikoi', 'onoma': '01-04-203 Κρίκος Ταχίνι Σοκολάτα','keimeno': ''},
        {'filename': 'Krikos-Kanela.jpg', 'categories': 'Krikoi', 'onoma': '01-04-205 Κρίκος Κανέλας','keimeno': ''},
        {'filename': 'Krikos-Olikis-Sousami.jpg', 'categories': 'Krikoi', 'onoma': '01-04-200 Ολικής Σουσάμι','keimeno': ''},
        {'filename': 'Mpatonetaki.jpg', 'categories': 'Mpatonetes', 'onoma': '01-04-303 Μπατονετάκι κεφαλοτύρι','keimeno': ''},
        {'filename': 'Mpatonetaki.jpg', 'categories': 'Mpatonetes', 'onoma': '01-04-304 Μπατονετάκι Mix 4 Γεύσεις','keimeno': 'Μπατονετάκι Λευκό, Μπατονετάκι Καλαμπόκι, Μπατονετάκι Πάπρικα, Μπατονετάκι Κεφαλοτύρι'}
        
    ]
    return render_template("Psimena.html", PsimenaImage_data=PsimenaImage_data)