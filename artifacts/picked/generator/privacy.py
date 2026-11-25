"""Privacy policy (GDPR) for mrpicked.eu, in all 6 site languages.

Each language: path, title, meta description, updated line, intro, and sections.
A section is (heading, [blocks]); a block is a paragraph string or a list of bullet strings.
Keep the facts identical across languages when editing.
"""

PRIV_PATH = {'EN': 'privacy/', 'SL': 'sl/zasebnost/', 'HR': 'hr/privatnost/', 'IT': 'it/privacy/',
             'DE': 'de/datenschutz/', 'HU': 'hu/adatvedelem/'}

CO = 'Aurelia Group d.o.o., Zaloška cesta 161, 1000 Ljubljana, Slovenia'
IP_RS = 'Informacijski pooblaščenec RS, Dunajska cesta 22, 1000 Ljubljana, www.ip-rs.si'

PRIV = {
'EN': dict(
 title='Privacy policy — Mr. Picked',
 desc='How Mr. Picked (Aurelia Group d.o.o.) handles personal data on mrpicked.eu: what we collect, why, for how long, who processes it, and your GDPR rights.',
 h1='Privacy policy', updated='Last updated: 22 November 2026', back='Back to the home page',
 intro='This policy explains how we handle personal data when you visit mrpicked.eu, request a free AI report, book a call or work with us. We collect as little as possible and never sell your data.',
 sections=[
  ('1. Who is responsible', [
   f'The controller is {CO}, tax no. 71811435, registration no. 7533152000 (“Mr. Picked”, “we”).',
   'Contact for all privacy questions: info@mrpicked.eu, +386 40 290 963.']),
  ('2. What we collect and why', [[
   'Free AI report form: business name, email address, page language, whether you ticked the optional box, time of the request and a technical reference number. We use them to prepare and send your report, send a confirmation email and reply to you. Legal basis: steps taken at your request before a contract (Art. 6(1)(b) GDPR).',
   'Tips and follow-ups about your report: only if you tick the optional box. Legal basis: your consent (Art. 6(1)(a) GDPR). You can withdraw it at any time by replying to any of our emails or writing to info@mrpicked.eu.',
   'Emails, calls and messages you send us: we use them to answer you and, if you become a client, to provide the service (Art. 6(1)(b) and (f) GDPR).',
   'Technical data: when you visit the site, the server processes your IP address and browser information so it can deliver the pages. The form also uses the IP address to block abuse (no more than 5 requests in 15 minutes); this counter is kept in memory only and deleted after 15 minutes. Legal basis: our legitimate interest in a secure, working website (Art. 6(1)(f) GDPR).',
   'Clients: data we receive while providing paid services is processed under our contract, and where we act on your behalf, under a data processing agreement (Art. 28 GDPR).']]),
  ('3. What the report is based on', [
   'The AI report analyses publicly available information about your business: answers from AI assistants (such as ChatGPT, Gemini and Perplexity), Google search and maps results, and public listings and reviews. We do not need any other personal data for it.']),
  ('4. Cookies and browser storage', [
   'We use no advertising or analytics cookies and no tracking pixels. The site stores two small values in your browser only, for convenience: the language you chose (mp-lang) and whether the opening animation was already shown in this visit (mp-intro). They never leave your device and are not sent to us.']),
  ('5. Who processes data for us', [[
   'Replit, Inc. (USA) hosts the website, the form server and the explainer video (stored on Google Cloud).',
   'Our email provider sends and receives the emails for info@mrpicked.eu, including the report confirmation.',
   'Google Fonts (Google Ireland Ltd. / Google LLC): the pages load fonts from Google’s servers, so your browser sends your IP address to Google when a page opens.',
   'Calendly LLC (USA), only if you book a call through our booking link. Calendly’s own privacy policy applies to the booking.'],
   'These providers only process data to provide their service to us. We do not sell or rent personal data to anyone.']),
  ('6. Transfers outside the EU', [
   'Some providers above are based in the USA. Transfers rely on the EU–US Data Privacy Framework where the provider is certified, or on the European Commission’s standard contractual clauses.']),
  ('7. How long we keep data', [[
   'Report requests and related correspondence: up to 24 months after our last contact, unless you become a client.',
   'Consent to tips and follow-ups: until you withdraw it.',
   'Client data: for the duration of the contract and afterwards as long as accounting and tax law requires (invoices: 10 years).',
   'Server logs: only as long as our hosting provider keeps them for operation and security.']]),
  ('8. Your rights', [
   'You have the right to access your data, to have it corrected or deleted, to restrict or object to its processing, to data portability and to withdraw consent at any time (withdrawal does not affect processing done before it). Write to info@mrpicked.eu; we reply within one month.',
   f'You can also lodge a complaint with the Slovenian supervisory authority: {IP_RS}, or with the authority in your country.']),
  ('9. Do you have to give us data?', [
   'No. Your email address and business name are needed only if you want the free report; without them we cannot send it. Everything else is optional. We do not make automated decisions with legal or similarly significant effects about you.']),
  ('10. Changes', [
   'If we change how we handle data, we will update this page and the date at the top.']),
 ]),

'SL': dict(
 title='Politika zasebnosti — Mr. Picked',
 desc='Kako Mr. Picked (Aurelia Group d.o.o.) obdeluje osebne podatke na mrpicked.eu: kaj zbiramo, zakaj, kako dolgo, kdo jih obdeluje in vaše pravice po GDPR.',
 h1='Politika zasebnosti', updated='Zadnja sprememba: 22. november 2026', back='Nazaj na prvo stran',
 intro='Ta politika pojasnjuje, kako obdelujemo osebne podatke, ko obiščete mrpicked.eu, naročite brezplačno AI poročilo, rezervirate klic ali z nami sodelujete. Zbiramo čim manj podatkov in jih nikoli ne prodajamo.',
 sections=[
  ('1. Kdo je upravljavec', [
   f'Upravljavec je {CO.replace(", Slovenia", "")}, davčna številka 71811435, matična številka 7533152000 (»Mr. Picked«, »mi«).',
   'Kontakt za vsa vprašanja o zasebnosti: info@mrpicked.eu, 040 290 963.']),
  ('2. Kaj zbiramo in zakaj', [[
   'Obrazec za brezplačno AI poročilo: ime podjetja, e-poštni naslov, jezik strani, ali ste označili neobvezno polje, čas zahteve in tehnična referenčna številka. Uporabimo jih, da pripravimo in pošljemo poročilo, vam pošljemo potrditveno sporočilo in vam odgovorimo. Pravna podlaga: ukrepi na vašo zahtevo pred sklenitvijo pogodbe (6(1)(b) člen GDPR).',
   'Nasveti in nadaljnja sporočila o poročilu: samo, če označite neobvezno polje. Pravna podlaga: vaša privolitev (6(1)(a) člen GDPR). Kadar koli jo lahko prekličete, tako da odgovorite na katero koli naše sporočilo ali pišete na info@mrpicked.eu.',
   'E-pošta, klici in sporočila, ki nam jih pošljete: uporabimo jih za odgovor in, če postanete stranka, za izvajanje storitve (6(1)(b) in (f) člen GDPR).',
   'Tehnični podatki: ob obisku strani strežnik obdela vaš IP-naslov in podatke o brskalniku, da lahko prikaže strani. Obrazec IP-naslov uporabi tudi za preprečevanje zlorab (največ 5 zahtev v 15 minutah); ta števec je samo v pomnilniku in se izbriše po 15 minutah. Pravna podlaga: naš zakoniti interes za varno in delujočo spletno stran (6(1)(f) člen GDPR).',
   'Stranke: podatke, ki jih prejmemo pri izvajanju plačljivih storitev, obdelujemo na podlagi pogodbe, kjer pa podatke obdelujemo v vašem imenu, na podlagi pogodbe o obdelavi (28. člen GDPR).']]),
  ('3. Na čem temelji poročilo', [
   'AI poročilo analizira javno dostopne podatke o vašem podjetju: odgovore AI asistentov (npr. ChatGPT, Gemini, Perplexity), rezultate iskanja in zemljevidov Google ter javne vpise in ocene. Drugih osebnih podatkov za to ne potrebujemo.']),
  ('4. Piškotki in shramba brskalnika', [
   'Ne uporabljamo oglaševalskih ali analitičnih piškotkov in sledilnih pikslov. Stran v vašem brskalniku shrani le dve majhni vrednosti za udobje: izbrani jezik (mp-lang) in ali je bila uvodna animacija v tem obisku že prikazana (mp-intro). Ti vrednosti ostaneta na vaši napravi in se nam ne pošiljata.']),
  ('5. Kdo obdeluje podatke za nas', [[
   'Replit, Inc. (ZDA) gosti spletno stran, strežnik obrazca in predstavitveni video (shranjen v Google Cloud).',
   'Naš ponudnik e-pošte pošilja in prejema sporočila za info@mrpicked.eu, vključno s potrditvijo poročila.',
   'Google Fonts (Google Ireland Ltd. / Google LLC): strani nalagajo pisave z Googlovih strežnikov, zato vaš brskalnik ob odprtju strani Googlu pošlje vaš IP-naslov.',
   'Calendly LLC (ZDA), samo če rezervirate klic prek naše povezave. Za rezervacijo velja Calendlyjeva politika zasebnosti.'],
   'Ti ponudniki podatke obdelujejo le za izvajanje svoje storitve za nas. Osebnih podatkov nikomur ne prodajamo ali dajemo v najem.']),
  ('6. Prenos izven EU', [
   'Nekateri zgoraj navedeni ponudniki imajo sedež v ZDA. Prenos temelji na okviru EU-ZDA za zasebnost podatkov (Data Privacy Framework), če je ponudnik certificiran, sicer na standardnih pogodbenih klavzulah Evropske komisije.']),
  ('7. Kako dolgo hranimo podatke', [[
   'Zahteve za poročilo in povezana korespondenca: do 24 mesecev po zadnjem stiku, razen če postanete stranka.',
   'Privolitev za nasvete in nadaljnja sporočila: do preklica.',
   'Podatki strank: med trajanjem pogodbe in nato toliko časa, kot zahtevajo računovodski in davčni predpisi (računi: 10 let).',
   'Dnevniki strežnika: le toliko časa, kot jih ponudnik gostovanja hrani za delovanje in varnost.']]),
  ('8. Vaše pravice', [
   'Imate pravico do dostopa do podatkov, do popravka ali izbrisa, do omejitve obdelave ali ugovora, do prenosljivosti podatkov ter do preklica privolitve kadar koli (preklic ne vpliva na zakonitost prej opravljene obdelave). Pišite na info@mrpicked.eu; odgovorimo v enem mesecu.',
   f'Pritožbo lahko vložite tudi pri nadzornem organu: {IP_RS}, ali pri organu v vaši državi.']),
  ('9. Ali nam morate dati podatke?', [
   'Ne. E-poštni naslov in ime podjetja potrebujemo samo, če želite brezplačno poročilo; brez njih ga ne moremo poslati. Vse drugo je neobvezno. O vas ne sprejemamo avtomatiziranih odločitev s pravnimi ali podobno pomembnimi učinki.']),
  ('10. Spremembe', [
   'Če spremenimo način obdelave podatkov, bomo posodobili to stran in datum na vrhu.']),
 ]),

'HR': dict(
 title='Pravila privatnosti — Mr. Picked',
 desc='Kako Mr. Picked (Aurelia Group d.o.o.) obrađuje osobne podatke na mrpicked.eu: što prikupljamo, zašto, koliko dugo, tko ih obrađuje i vaša prava prema GDPR-u.',
 h1='Pravila privatnosti', updated='Zadnja izmjena: 22. studenoga 2026.', back='Natrag na početnu stranicu',
 intro='Ova pravila objašnjavaju kako obrađujemo osobne podatke kada posjetite mrpicked.eu, zatražite besplatno AI izvješće, rezervirate poziv ili surađujete s nama. Prikupljamo što manje podataka i nikada ih ne prodajemo.',
 sections=[
  ('1. Tko je voditelj obrade', [
   f'Voditelj obrade je {CO}, porezni broj 71811435, matični broj 7533152000 („Mr. Picked”, „mi”).',
   'Kontakt za sva pitanja o privatnosti: info@mrpicked.eu, +386 40 290 963.']),
  ('2. Što prikupljamo i zašto', [[
   'Obrazac za besplatno AI izvješće: naziv tvrtke, e-adresa, jezik stranice, jeste li označili neobavezno polje, vrijeme zahtjeva i tehnički referentni broj. Koristimo ih kako bismo pripremili i poslali izvješće, poslali potvrdu i odgovorili vam. Pravna osnova: radnje na vaš zahtjev prije sklapanja ugovora (čl. 6. st. 1. t. (b) GDPR-a).',
   'Savjeti i daljnje poruke o izvješću: samo ako označite neobavezno polje. Pravna osnova: vaša privola (čl. 6. st. 1. t. (a) GDPR-a). Možete je povući u bilo kojem trenutku odgovorom na bilo koju našu poruku ili porukom na info@mrpicked.eu.',
   'E-pošta, pozivi i poruke koje nam pošaljete: koristimo ih za odgovor i, ako postanete klijent, za pružanje usluge (čl. 6. st. 1. t. (b) i (f) GDPR-a).',
   'Tehnički podaci: kada posjetite stranicu, poslužitelj obrađuje vašu IP adresu i podatke o pregledniku kako bi prikazao stranice. Obrazac koristi IP adresu i za sprječavanje zlouporabe (najviše 5 zahtjeva u 15 minuta); taj se brojač čuva samo u memoriji i briše nakon 15 minuta. Pravna osnova: naš legitimni interes za sigurnu i funkcionalnu stranicu (čl. 6. st. 1. t. (f) GDPR-a).',
   'Klijenti: podatke koje primimo pri pružanju plaćenih usluga obrađujemo na temelju ugovora, a kada ih obrađujemo u vaše ime, na temelju ugovora o obradi (čl. 28. GDPR-a).']]),
  ('3. Na čemu se temelji izvješće', [
   'AI izvješće analizira javno dostupne podatke o vašoj tvrtki: odgovore AI asistenata (npr. ChatGPT, Gemini, Perplexity), rezultate Google pretraživanja i karata te javne upise i recenzije. Za to nam ne trebaju drugi osobni podaci.']),
  ('4. Kolačići i pohrana preglednika', [
   'Ne koristimo oglašivačke ni analitičke kolačiće ni piksele za praćenje. Stranica u vašem pregledniku sprema samo dvije male vrijednosti radi praktičnosti: odabrani jezik (mp-lang) i je li uvodna animacija u ovom posjetu već prikazana (mp-intro). One ostaju na vašem uređaju i ne šalju se nama.']),
  ('5. Tko obrađuje podatke za nas', [[
   'Replit, Inc. (SAD) udomljuje stranicu, poslužitelj obrasca i predstavljački video (pohranjen na Google Cloudu).',
   'Naš pružatelj e-pošte šalje i prima poruke za info@mrpicked.eu, uključujući potvrdu izvješća.',
   'Google Fonts (Google Ireland Ltd. / Google LLC): stranice učitavaju fontove s Googleovih poslužitelja, pa vaš preglednik pri otvaranju stranice Googleu šalje vašu IP adresu.',
   'Calendly LLC (SAD), samo ako rezervirate poziv putem naše poveznice. Za rezervaciju vrijede Calendlyjeva pravila privatnosti.'],
   'Ti pružatelji obrađuju podatke samo radi pružanja svoje usluge nama. Osobne podatke nikome ne prodajemo niti iznajmljujemo.']),
  ('6. Prijenos izvan EU-a', [
   'Neki od navedenih pružatelja imaju sjedište u SAD-u. Prijenos se temelji na Okviru EU-SAD za privatnost podataka (Data Privacy Framework) ako je pružatelj certificiran, a inače na standardnim ugovornim klauzulama Europske komisije.']),
  ('7. Koliko dugo čuvamo podatke', [[
   'Zahtjevi za izvješće i povezana korespondencija: do 24 mjeseca nakon posljednjeg kontakta, osim ako postanete klijent.',
   'Privola za savjete i daljnje poruke: do povlačenja.',
   'Podaci klijenata: tijekom trajanja ugovora i nakon toga koliko zahtijevaju računovodstveni i porezni propisi (računi: 10 godina).',
   'Zapisi poslužitelja: samo onoliko koliko ih pružatelj udomljavanja čuva radi rada i sigurnosti.']]),
  ('8. Vaša prava', [
   'Imate pravo na pristup podacima, ispravak ili brisanje, ograničenje obrade ili prigovor, prenosivost podataka te povlačenje privole u bilo kojem trenutku (povlačenje ne utječe na zakonitost ranije obrade). Pišite na info@mrpicked.eu; odgovaramo u roku od mjesec dana.',
   f'Pritužbu možete podnijeti i slovenskom nadzornom tijelu: {IP_RS}, ili tijelu u svojoj zemlji (u Hrvatskoj: AZOP).']),
  ('9. Morate li nam dati podatke?', [
   'Ne. E-adresa i naziv tvrtke potrebni su samo ako želite besplatno izvješće; bez njih ga ne možemo poslati. Sve ostalo je neobavezno. O vama ne donosimo automatizirane odluke s pravnim ili sličnim značajnim učincima.']),
  ('10. Izmjene', [
   'Ako promijenimo način obrade podataka, ažurirat ćemo ovu stranicu i datum na vrhu.']),
 ]),

'IT': dict(
 title='Informativa privacy — Mr. Picked',
 desc='Come Mr. Picked tratta i dati personali su mrpicked.eu: cosa raccogliamo, perché, per quanto tempo, chi li tratta e i tuoi diritti ai sensi del GDPR.',
 h1='Informativa privacy', updated='Ultimo aggiornamento: 22 novembre 2026', back='Torna alla home page',
 intro='Questa informativa spiega come trattiamo i dati personali quando visiti mrpicked.eu, richiedi il report AI gratuito, prenoti una call o lavori con noi. Raccogliamo il minimo indispensabile e non vendiamo mai i tuoi dati.',
 sections=[
  ('1. Titolare del trattamento', [
   f'Il titolare è {CO}, codice fiscale 71811435, numero di registrazione 7533152000 (“Mr. Picked”, “noi”).',
   'Contatto per ogni domanda sulla privacy: info@mrpicked.eu, +386 40 290 963.']),
  ('2. Cosa raccogliamo e perché', [[
   'Modulo del report AI gratuito: nome dell’attività, indirizzo email, lingua della pagina, se hai spuntato la casella facoltativa, ora della richiesta e un numero di riferimento tecnico. Li usiamo per preparare e inviare il report, inviarti un’email di conferma e risponderti. Base giuridica: misure precontrattuali adottate su tua richiesta (art. 6, par. 1, lett. b GDPR).',
   'Consigli e aggiornamenti sul report: solo se spunti la casella facoltativa. Base giuridica: il tuo consenso (art. 6, par. 1, lett. a GDPR). Puoi revocarlo in qualsiasi momento rispondendo a una nostra email o scrivendo a info@mrpicked.eu.',
   'Email, chiamate e messaggi che ci invii: li usiamo per risponderti e, se diventi cliente, per fornire il servizio (art. 6, par. 1, lett. b e f GDPR).',
   'Dati tecnici: quando visiti il sito, il server tratta il tuo indirizzo IP e i dati del browser per mostrare le pagine. Il modulo usa l’indirizzo IP anche per bloccare gli abusi (al massimo 5 richieste in 15 minuti); questo contatore resta solo in memoria e viene cancellato dopo 15 minuti. Base giuridica: il nostro legittimo interesse a un sito sicuro e funzionante (art. 6, par. 1, lett. f GDPR).',
   'Clienti: i dati ricevuti durante i servizi a pagamento sono trattati in base al contratto e, quando agiamo per tuo conto, in base a un accordo sul trattamento dei dati (art. 28 GDPR).']]),
  ('3. Su cosa si basa il report', [
   'Il report AI analizza informazioni pubbliche sulla tua attività: risposte degli assistenti AI (come ChatGPT, Gemini e Perplexity), risultati di ricerca e mappe di Google, schede e recensioni pubbliche. Non servono altri dati personali.']),
  ('4. Cookie e memoria del browser', [
   'Non usiamo cookie pubblicitari o di analisi né pixel di tracciamento. Il sito salva nel tuo browser solo due piccoli valori per comodità: la lingua scelta (mp-lang) e se l’animazione iniziale è già stata mostrata in questa visita (mp-intro). Restano sul tuo dispositivo e non ci vengono inviati.']),
  ('5. Chi tratta i dati per nostro conto', [[
   'Replit, Inc. (USA) ospita il sito, il server del modulo e il video di presentazione (archiviato su Google Cloud).',
   'Il nostro fornitore di posta elettronica invia e riceve le email di info@mrpicked.eu, compresa la conferma del report.',
   'Google Fonts (Google Ireland Ltd. / Google LLC): le pagine caricano i caratteri dai server di Google, quindi all’apertura di una pagina il tuo browser invia il tuo indirizzo IP a Google.',
   'Calendly LLC (USA), solo se prenoti una call tramite il nostro link. Per la prenotazione vale l’informativa privacy di Calendly.'],
   'Questi fornitori trattano i dati solo per fornirci il loro servizio. Non vendiamo né affittiamo dati personali a nessuno.']),
  ('6. Trasferimenti fuori dall’UE', [
   'Alcuni dei fornitori indicati hanno sede negli USA. I trasferimenti si basano sul Data Privacy Framework UE-USA, se il fornitore è certificato, oppure sulle clausole contrattuali tipo della Commissione europea.']),
  ('7. Per quanto tempo conserviamo i dati', [[
   'Richieste di report e relativa corrispondenza: fino a 24 mesi dall’ultimo contatto, salvo che tu diventi cliente.',
   'Consenso a consigli e aggiornamenti: fino alla revoca.',
   'Dati dei clienti: per la durata del contratto e poi per il tempo richiesto dalle norme contabili e fiscali (fatture: 10 anni).',
   'Log del server: solo per il tempo in cui il fornitore di hosting li conserva per funzionamento e sicurezza.']]),
  ('8. I tuoi diritti', [
   'Hai diritto di accedere ai tuoi dati, di chiederne la rettifica o la cancellazione, di limitarne il trattamento o di opporti, alla portabilità e di revocare il consenso in qualsiasi momento (la revoca non pregiudica il trattamento precedente). Scrivi a info@mrpicked.eu; rispondiamo entro un mese.',
   f'Puoi anche presentare reclamo all’autorità di controllo slovena: {IP_RS}, oppure all’autorità del tuo paese (in Italia: Garante per la protezione dei dati personali).']),
  ('9. Sei obbligato a fornirci i dati?', [
   'No. Email e nome dell’attività servono solo se vuoi il report gratuito; senza di essi non possiamo inviarlo. Tutto il resto è facoltativo. Non prendiamo decisioni automatizzate che producano effetti giuridici o analogamente significativi su di te.']),
  ('10. Modifiche', [
   'Se cambiamo il modo in cui trattiamo i dati, aggiorneremo questa pagina e la data in alto.']),
 ]),

'DE': dict(
 title='Datenschutzerklärung — Mr. Picked',
 desc='Wie Mr. Picked personenbezogene Daten auf mrpicked.eu verarbeitet: was wir erheben, warum, wie lange, wer sie verarbeitet und Ihre Rechte nach der DSGVO.',
 h1='Datenschutzerklärung', updated='Stand: 22. November 2026', back='Zurück zur Startseite',
 intro='Diese Erklärung beschreibt, wie wir personenbezogene Daten verarbeiten, wenn Sie mrpicked.eu besuchen, den kostenlosen KI-Bericht anfordern, ein Gespräch buchen oder mit uns zusammenarbeiten. Wir erheben so wenig wie möglich und verkaufen Ihre Daten nie.',
 sections=[
  ('1. Verantwortlicher', [
   f'Verantwortlich ist {CO}, Steuernummer 71811435, Firmennummer 7533152000 („Mr. Picked“, „wir“).',
   'Kontakt für alle Datenschutzfragen: info@mrpicked.eu, +386 40 290 963.']),
  ('2. Welche Daten wir erheben und warum', [[
   'Formular für den kostenlosen KI-Bericht: Firmenname, E-Mail-Adresse, Sprache der Seite, ob Sie das optionale Kästchen angekreuzt haben, Zeitpunkt der Anfrage und eine technische Referenznummer. Wir nutzen sie, um Ihren Bericht zu erstellen und zu senden, Ihnen eine Bestätigung zu schicken und Ihnen zu antworten. Rechtsgrundlage: vorvertragliche Maßnahmen auf Ihre Anfrage (Art. 6 Abs. 1 lit. b DSGVO).',
   'Tipps und weitere Infos zu Ihrem Bericht: nur wenn Sie das optionale Kästchen ankreuzen. Rechtsgrundlage: Ihre Einwilligung (Art. 6 Abs. 1 lit. a DSGVO). Sie können sie jederzeit widerrufen, indem Sie auf eine unserer E-Mails antworten oder an info@mrpicked.eu schreiben.',
   'E-Mails, Anrufe und Nachrichten an uns: Wir nutzen sie, um Ihnen zu antworten und, wenn Sie Kunde werden, um die Leistung zu erbringen (Art. 6 Abs. 1 lit. b und f DSGVO).',
   'Technische Daten: Beim Besuch der Website verarbeitet der Server Ihre IP-Adresse und Browserangaben, um die Seiten auszuliefern. Das Formular nutzt die IP-Adresse außerdem zur Missbrauchsabwehr (höchstens 5 Anfragen in 15 Minuten); dieser Zähler liegt nur im Arbeitsspeicher und wird nach 15 Minuten gelöscht. Rechtsgrundlage: unser berechtigtes Interesse an einer sicheren, funktionierenden Website (Art. 6 Abs. 1 lit. f DSGVO).',
   'Kunden: Daten, die wir bei bezahlten Leistungen erhalten, verarbeiten wir auf Grundlage des Vertrags und, soweit wir in Ihrem Auftrag handeln, auf Grundlage eines Auftragsverarbeitungsvertrags (Art. 28 DSGVO).']]),
  ('3. Grundlage des Berichts', [
   'Der KI-Bericht wertet öffentlich verfügbare Informationen über Ihr Unternehmen aus: Antworten von KI-Assistenten (z. B. ChatGPT, Gemini, Perplexity), Ergebnisse der Google-Suche und Google Maps sowie öffentliche Einträge und Bewertungen. Weitere personenbezogene Daten brauchen wir dafür nicht.']),
  ('4. Cookies und Browserspeicher', [
   'Wir verwenden keine Werbe- oder Analyse-Cookies und keine Tracking-Pixel. Die Website speichert in Ihrem Browser nur zwei kleine Werte zur Bequemlichkeit: die gewählte Sprache (mp-lang) und ob die Eröffnungsanimation bei diesem Besuch schon gezeigt wurde (mp-intro). Sie bleiben auf Ihrem Gerät und werden nicht an uns übertragen.']),
  ('5. Wer Daten für uns verarbeitet', [[
   'Replit, Inc. (USA) hostet die Website, den Formular-Server und das Erklärvideo (gespeichert in Google Cloud).',
   'Unser E-Mail-Anbieter versendet und empfängt die E-Mails für info@mrpicked.eu, einschließlich der Bestätigung zum Bericht.',
   'Google Fonts (Google Ireland Ltd. / Google LLC): Die Seiten laden Schriftarten von Google-Servern, daher übermittelt Ihr Browser beim Öffnen einer Seite Ihre IP-Adresse an Google.',
   'Calendly LLC (USA), nur wenn Sie über unseren Link ein Gespräch buchen. Für die Buchung gilt die Datenschutzerklärung von Calendly.'],
   'Diese Anbieter verarbeiten Daten nur, um ihre Leistung für uns zu erbringen. Wir verkaufen oder vermieten keine personenbezogenen Daten.']),
  ('6. Übermittlung außerhalb der EU', [
   'Einige der genannten Anbieter haben ihren Sitz in den USA. Die Übermittlung stützt sich auf das EU-US Data Privacy Framework, sofern der Anbieter zertifiziert ist, andernfalls auf die Standardvertragsklauseln der Europäischen Kommission.']),
  ('7. Speicherdauer', [[
   'Berichtsanfragen und zugehörige Korrespondenz: bis zu 24 Monate nach dem letzten Kontakt, sofern Sie nicht Kunde werden.',
   'Einwilligung zu Tipps und weiteren Infos: bis zum Widerruf.',
   'Kundendaten: für die Dauer des Vertrags und danach so lange, wie es Buchhaltungs- und Steuervorschriften verlangen (Rechnungen: 10 Jahre).',
   'Server-Logs: nur so lange, wie unser Hosting-Anbieter sie für Betrieb und Sicherheit aufbewahrt.']]),
  ('8. Ihre Rechte', [
   'Sie haben das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Widerspruch, Datenübertragbarkeit und auf jederzeitigen Widerruf Ihrer Einwilligung (der Widerruf berührt nicht die Rechtmäßigkeit der bisherigen Verarbeitung). Schreiben Sie an info@mrpicked.eu; wir antworten innerhalb eines Monats.',
   f'Sie können sich auch bei der slowenischen Aufsichtsbehörde beschweren: {IP_RS}, oder bei der Behörde in Ihrem Land (in Österreich: Datenschutzbehörde).']),
  ('9. Müssen Sie uns Daten geben?', [
   'Nein. E-Mail-Adresse und Firmenname brauchen wir nur, wenn Sie den kostenlosen Bericht möchten; ohne sie können wir ihn nicht senden. Alles andere ist freiwillig. Wir treffen keine automatisierten Entscheidungen mit rechtlicher oder ähnlich erheblicher Wirkung über Sie.']),
  ('10. Änderungen', [
   'Wenn wir die Verarbeitung ändern, aktualisieren wir diese Seite und das Datum oben.']),
 ]),

'HU': dict(
 title='Adatvédelmi tájékoztató — Mr. Picked',
 desc='Hogyan kezeli a Mr. Picked a személyes adatokat a mrpicked.eu oldalon: mit gyűjtünk, miért, meddig, ki kezeli, és milyen jogai vannak a GDPR szerint.',
 h1='Adatvédelmi tájékoztató', updated='Utolsó módosítás: 2026. november 22.', back='Vissza a kezdőlapra',
 intro='Ez a tájékoztató elmagyarázza, hogyan kezeljük a személyes adatokat, amikor felkeresi a mrpicked.eu oldalt, ingyenes AI-jelentést kér, hívást foglal vagy együtt dolgozik velünk. A lehető legkevesebb adatot gyűjtjük, és soha nem adjuk el.',
 sections=[
  ('1. Ki az adatkezelő', [
   f'Az adatkezelő: {CO}, adószám: 71811435, cégjegyzékszám: 7533152000 („Mr. Picked”, „mi”).',
   'Kapcsolat minden adatvédelmi kérdésben: info@mrpicked.eu, +386 40 290 963.']),
  ('2. Milyen adatokat gyűjtünk és miért', [[
   'Ingyenes AI-jelentés űrlap: cégnév, e-mail-cím, az oldal nyelve, bejelölte-e a nem kötelező mezőt, a kérés időpontja és egy technikai hivatkozási szám. Ezeket a jelentés elkészítésére és elküldésére, a visszaigazoló e-mail küldésére és a válaszadásra használjuk. Jogalap: az Ön kérésére a szerződés megkötését megelőzően tett lépések (GDPR 6. cikk (1) b)).',
   'Tippek és további üzenetek a jelentésről: csak ha bejelöli a nem kötelező mezőt. Jogalap: az Ön hozzájárulása (GDPR 6. cikk (1) a)). Bármikor visszavonhatja, ha válaszol bármelyik e-mailünkre, vagy ír az info@mrpicked.eu címre.',
   'Az Ön által küldött e-mailek, hívások és üzenetek: a válaszadásra, és ha ügyfelünk lesz, a szolgáltatás nyújtására használjuk (GDPR 6. cikk (1) b) és f)).',
   'Technikai adatok: az oldal megnyitásakor a szerver kezeli az IP-címét és a böngésző adatait, hogy megjeleníthesse az oldalakat. Az űrlap az IP-címet a visszaélések megelőzésére is használja (legfeljebb 5 kérés 15 perc alatt); ez a számláló csak a memóriában van, és 15 perc után törlődik. Jogalap: jogos érdekünk a biztonságos, működő weboldalhoz (GDPR 6. cikk (1) f)).',
   'Ügyfelek: a fizetős szolgáltatások során kapott adatokat a szerződés alapján, az Ön nevében végzett adatkezelés esetén adatfeldolgozási szerződés alapján kezeljük (GDPR 28. cikk).']]),
  ('3. Mire épül a jelentés', [
   'Az AI-jelentés a vállalkozásáról nyilvánosan elérhető információkat elemzi: AI-asszisztensek (pl. ChatGPT, Gemini, Perplexity) válaszait, a Google keresési és térképes találatait, valamint nyilvános adatlapokat és értékeléseket. Ehhez más személyes adatra nincs szükségünk.']),
  ('4. Sütik és böngészőtárhely', [
   'Nem használunk hirdetési vagy elemző sütiket, sem követőpixeleket. Az oldal kényelmi célból csak két apró értéket tárol a böngészőjében: a választott nyelvet (mp-lang), és azt, hogy a nyitóanimáció ebben a látogatásban már megjelent-e (mp-intro). Ezek az eszközén maradnak, és nem kerülnek hozzánk.']),
  ('5. Kik kezelnek adatokat a megbízásunkból', [[
   'Replit, Inc. (USA): a weboldal, az űrlap szervere és a bemutató videó tárhelye (Google Cloudon tárolva).',
   'E-mail-szolgáltatónk: küldi és fogadja az info@mrpicked.eu leveleit, a jelentés visszaigazolását is.',
   'Google Fonts (Google Ireland Ltd. / Google LLC): az oldalak a Google szervereiről töltik be a betűtípusokat, ezért a böngészője az oldal megnyitásakor elküldi IP-címét a Google-nak.',
   'Calendly LLC (USA): csak ha a linkünkön keresztül hívást foglal. A foglalásra a Calendly adatvédelmi tájékoztatója vonatkozik.'],
   'Ezek a szolgáltatók az adatokat csak a nekünk nyújtott szolgáltatásukhoz kezelik. Személyes adatot senkinek nem adunk el és nem adunk bérbe.']),
  ('6. Adattovábbítás az EU-n kívülre', [
   'A fenti szolgáltatók egy része az USA-ban működik. A továbbítás az EU–USA adatvédelmi keretrendszeren (Data Privacy Framework) alapul, ha a szolgáltató tanúsított, egyébként az Európai Bizottság általános szerződési feltételein.']),
  ('7. Meddig őrizzük az adatokat', [[
   'Jelentéskérések és kapcsolódó levelezés: legfeljebb 24 hónapig az utolsó kapcsolatfelvételtől, kivéve, ha ügyfelünk lesz.',
   'Hozzájárulás tippekhez és további üzenetekhez: visszavonásig.',
   'Ügyféladatok: a szerződés idejére, utána a számviteli és adójogszabályok által előírt ideig (számlák: 10 év).',
   'Szervernaplók: csak addig, amíg a tárhelyszolgáltató az üzemeltetéshez és a biztonsághoz megőrzi őket.']]),
  ('8. Az Ön jogai', [
   'Joga van az adataihoz való hozzáféréshez, azok helyesbítéséhez vagy törléséhez, az adatkezelés korlátozásához, tiltakozáshoz, az adathordozhatósághoz, valamint a hozzájárulás bármikori visszavonásához (a visszavonás nem érinti a korábbi adatkezelés jogszerűségét). Írjon az info@mrpicked.eu címre; egy hónapon belül válaszolunk.',
   f'Panaszt tehet a szlovén felügyeleti hatóságnál is: {IP_RS}, vagy a saját országa hatóságánál (Magyarországon: NAIH).']),
  ('9. Kötelező-e megadni az adatokat?', [
   'Nem. Az e-mail-címre és a cégnévre csak akkor van szükség, ha ingyenes jelentést kér; ezek nélkül nem tudjuk elküldeni. Minden más önkéntes. Önről nem hozunk joghatással vagy hasonlóan jelentős hatással járó automatizált döntést.']),
  ('10. Változások', [
   'Ha megváltoztatjuk az adatkezelést, frissítjük ezt az oldalt és a fenti dátumot.']),
 ]),
}
