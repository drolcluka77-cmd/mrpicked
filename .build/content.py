# Copy for the generic main pages (6 languages) and the industry pages (EN + SL).
# In a "faqs" list an int means: reuse that item from the base hospitality FAQ (T[L]['faqs'][i]).

GEN = {
'EN': dict(
 eyebrow="AI + Google visibility for local businesses",
 h1="Your next customer won’t Google you. They’ll ask AI.",
 sub="When someone asks ChatGPT, Gemini or Perplexity who to call, where to eat or which agent to trust, AI names three businesses. We make sure yours is one of them — in six languages.",
 dName="Business name", dNamePh="e.g. Dental Clinic Primer", dCat="What do you do?", catDef="dentist", dQ="{city}: best {cat} near me?",
 dYour="Your business", dOther="Another business", dIdle="Enter your business and press run to see how an AI answers a customer.",
 dDesc="Top-rated, open today, replies on WhatsApp.",
 steps=[
  dict(tab="AI Mirror", h="We ask the AIs about you", p="We run the questions your customers actually ask across ChatGPT, Gemini, Perplexity and Google’s AI answers.", items=["30 customer questions in 6 languages","Where you appear — and where competitors do","Every wrong fact the AI says about you"]),
  dict(tab="Fix", h="We make you readable", p="In the first 30 days we fix everything AI and Google read about you.", items=["Google profile, hours, services, photos, categories","Listings corrected on 15+ platforms","Services, prices and contact details machine-readable on your site"]),
  dict(tab="Stay picked", h="We keep you there", p="Every month we re-run the questions, add fresh content and report what changed.", items=["Monthly Mr. Picked Report with your visibility score","AI videos and Google posts every month","Review requests after every job or visit"])],
 vidP="No filming. Our AI turns your real photos into short clips — content for social, and one more reason for AI to recommend you.",
 vids=[dict(h="From your real photos", p="Your work, your team and your space, never stock footage. You approve every clip."), dict(h="One video, six languages", p="AI voiceover and subtitles, so every customer hears it in their own language."), dict(h="Posted where it counts", p="Instagram, TikTok, YouTube Shorts and your Google profile.")],
 lists=[
  ["Starting AI audit: 30 customer questions in 3 AIs and 6 languages","Full fix in the first 30 days: Google profile, hours, services, photos, categories","Your services, hours and location made machine-readable on your website","Listings corrected on 15+ platforms (Apple Maps, Bing, industry directories…)","Local Google SEO: tracked Maps ranking for your 10 key searches","4 Google profile posts per month","Monthly Mr. Picked Report with your visibility score"],
  ["Everything in Visible, plus:","2 AI videos / month in 3 languages, posted to Instagram, TikTok and Google","Automatic review request after every job or visit","We draft replies to all your Google reviews within 48 h","2 new customer-question pages / month in 3 languages","50 customer questions tracked + 3 nearby competitors","Quarterly results call"],
  ["Everything in Recommended, plus:","4 AI videos / month in 6 languages","WhatsApp concierge 24/7: answers questions, sends quotes and takes bookings","Appointment reminders & no-show follow-up","Your services and price list online in 6 languages","One seasonal campaign per quarter","Monthly strategy call + changes within 24 h (working days)"]],
 addons=[dict(name="AI video pack", desc="+3 AI videos every month"), dict(name="Review loop", desc="Review request after every job or visit"), dict(name="WhatsApp concierge", desc="Answers customers and takes bookings, 24/7"), dict(name="AI-ready website", desc="Multilingual, fast, readable by AI")],
 roiSpend="Average value of a customer", roiGuests="Extra customers per week", roiBreak="Mr. Picked pays for itself at {n} extra customers a week.",
 fdH="Built by people who run local businesses, not an agency.",
 fdP="I run businesses in hospitality, towing and insurance in Slovenia. I built Mr. Picked for my own businesses first — now we do it for yours.",
 faqs=[dict(q="What is GEO, in plain words?", a="Making sure AI assistants like ChatGPT, Gemini and Perplexity know your business, describe it correctly and recommend it. It builds on local SEO, so you also rank better on Google."), 1, 2,
  dict(q="Are the AI videos made from real footage?", a="From your real photos of your work, team and space, turned into short clips with AI. You approve each one, and they’re labelled as AI where platforms require it."),
  dict(q="Which businesses is this for?", a="Any business people look for locally: restaurants, hotels and apartments, towing services, insurance agents, dentists and clinics, salons, trades and professional services. The packages are the same; we tailor the questions and content to your industry."), 4],
 fBiz="Business name", mailPh="you@company.si",
 indK="Industries", indH="Built for businesses people look for nearby.", indP="Same packages and prices, tailored to the questions your customers ask.", indMore="See how it works",
 inds=[dict(name="Restaurants, hotels & apartments", desc="Get picked when guests ask where to eat or stay."), dict(name="Towing & roadside assistance", desc="Be the number AI gives when a car breaks down."), dict(name="Insurance agents", desc="Be the agent AI recommends for car, home and travel insurance."), dict(name="Health & beauty", desc="Dentists, physios, clinics and salons."), dict(name="Trades & car repair", desc="Plumbers, electricians, mechanics and installers."), dict(name="Professional services", desc="Lawyers, accountants and real estate agents.")]),
'SL': dict(
 eyebrow="AI + Google vidnost za lokalna podjetja",
 h1="Vaša naslednja stranka vas ne bo iskala na Googlu. Vprašala bo AI.",
 sub="Ko nekdo vpraša ChatGPT, Gemini ali Perplexity, koga poklicati, kje jesti ali kateremu zastopniku zaupati, AI imenuje tri podjetja. Poskrbimo, da je vaše med njimi — v šestih jezikih.",
 dName="Ime podjetja", dNamePh="npr. Zobna ambulanta Primer", dCat="S čim se ukvarjate?", catDef="zobozdravnik", dQ="{city}: {cat} — koga priporočaš?",
 dYour="Vaše podjetje", dOther="Drugo podjetje", dIdle="Vpišite svoje podjetje in zaženite, da vidite, kako AI odgovori stranki.",
 dDesc="Odlične ocene, danes odprto, odgovarja na WhatsAppu.",
 steps=[
  dict(tab="AI Mirror", h="AI vprašamo o vas", p="Postavimo vprašanja, ki jih stranke res sprašujejo, v ChatGPT, Gemini, Perplexity in Googlovih AI odgovorih.", items=["30 vprašanj strank v 6 jezikih","Kje se pojavite vi — in kje konkurenca","Vsak napačen podatek, ki ga AI pove o vas"]),
  dict(tab="Popravek", h="Poskrbimo, da vas AI razume", p="V prvih 30 dneh popravimo vse, kar AI in Google bereta o vas.", items=["Google profil, delovni čas, storitve, fotografije, kategorije","Popravljeni vpisi na 15+ platformah","Storitve, cene in kontakt strojno berljivi na vaši strani"]),
  dict(tab="Ostanite izbrani", h="Obdržimo vas tam", p="Vsak mesec ponovno postavimo vprašanja, dodamo svežo vsebino in poročamo, kaj se je spremenilo.", items=["Mesečno poročilo Mr. Picked z oceno vidnosti","AI videi in Google objave vsak mesec","Prošnje za oceno po vsakem opravljenem delu ali obisku"])],
 vidP="Brez snemanja. Naš AI iz vaših pravih fotografij ustvari kratke posnetke — vsebino za družbena omrežja in še en razlog, da vas AI priporoči.",
 vids=[dict(h="Iz vaših pravih fotografij", p="Vaše delo, vaša ekipa in vaš prostor, nikoli tuji posnetki. Vsak posnetek odobrite."), dict(h="En video, šest jezikov", p="AI glas in podnapisi, da ga vsaka stranka sliši v svojem jeziku."), dict(h="Objavljeno tam, kjer šteje", p="Instagram, TikTok, YouTube Shorts in vaš Google profil.")],
 lists=[
  ["Začetni AI pregled: 30 vprašanj strank v 3 AI orodjih in 6 jezikih","Celoten popravek v prvih 30 dneh: Google profil, ure, storitve, fotografije, kategorije","Storitve, delovni čas in lokacija strojno berljivi na vaši spletni strani","Popravljeni vpisi na 15+ platformah (Apple Maps, Bing, panožni imeniki …)","Lokalni Google SEO: spremljamo mesto na Zemljevidih za 10 ključnih iskanj","4 objave na Google profilu na mesec","Mesečno poročilo Mr. Picked z oceno vidnosti"],
  ["Vse iz paketa Visible, plus:","2 AI videa na mesec v 3 jezikih, objavljena na Instagramu, TikToku in Googlu","Samodejna prošnja za oceno po vsakem delu ali obisku","Pripravimo odgovore na vse vaše Google ocene v 48 urah","2 novi strani z vprašanji strank na mesec v 3 jezikih","Spremljanje 50 vprašanj strank + 3 bližnjih konkurentov","Četrtletni pregled rezultatov"],
  ["Vse iz paketa Recommended, plus:","4 AI videi na mesec v 6 jezikih","WhatsApp concierge 24/7: odgovarja na vprašanja, pošilja ponudbe in sprejema rezervacije","Opomniki za termine in sledenje neprihodom","Vaše storitve in cenik na spletu v 6 jezikih","Ena sezonska kampanja na četrtletje","Mesečni strateški sestanek + spremembe v 24 urah (delovni dnevi)"]],
 addons=[dict(name="AI video paket", desc="+3 AI videi vsak mesec"), dict(name="Zbiranje ocen", desc="Prošnja za oceno po vsakem delu ali obisku"), dict(name="WhatsApp concierge", desc="Odgovarja strankam in sprejema rezervacije, 24/7"), dict(name="Spletna stran za AI", desc="Večjezična, hitra, berljiva za AI")],
 roiSpend="Povprečna vrednost stranke", roiGuests="Dodatne stranke na teden", roiBreak="Mr. Picked se poplača že pri {n} dodatnih strankah na teden.",
 fdH="Naredili so ga ljudje, ki vodijo lokalna podjetja, ne agencija.",
 fdP="V Sloveniji vodim podjetja v gostinstvu, avtovleki in zavarovalništvu. Mr. Picked sem najprej naredil za svoja podjetja — zdaj ga delamo za vaše.",
 faqs=[dict(q="Kaj je GEO, preprosto povedano?", a="Poskrbimo, da AI pomočniki, kot so ChatGPT, Gemini in Perplexity, poznajo vaše podjetje, ga pravilno opišejo in priporočijo. Gradi na lokalnem SEO, zato ste višje tudi na Googlu."), 1, 2,
  dict(q="So AI videi narejeni iz pravih posnetkov?", a="Iz vaših pravih fotografij dela, ekipe in prostora, ki jih AI spremeni v kratke posnetke. Vsakega odobrite, kjer platforme to zahtevajo, pa so označeni kot AI."),
  dict(q="Za katera podjetja je to?", a="Za vsako podjetje, ki ga ljudje iščejo lokalno: restavracije, hotele in apartmaje, vlečne službe, zavarovalniške zastopnike, zobozdravnike in ambulante, salone, obrtnike in strokovne storitve. Paketi so enaki, vprašanja in vsebino prilagodimo vaši panogi."), 4],
 fBiz="Ime podjetja", mailPh="vi@podjetje.si",
 indK="Panoge", indH="Za podjetja, ki jih ljudje iščejo v bližini.", indP="Isti paketi in cene, prilagojeni vprašanjem, ki jih postavljajo vaše stranke.", indMore="Poglejte, kako deluje",
 inds=[dict(name="Restavracije, hoteli in apartmaji", desc="Da vas izberejo, ko gostje vprašajo, kje jesti ali spati."), dict(name="Avtovleka in pomoč na cesti", desc="Bodite številka, ki jo AI da, ko se avto pokvari."), dict(name="Zavarovalniški zastopniki", desc="Bodite zastopnik, ki ga AI priporoči za avto, dom in potovanja."), dict(name="Zdravje in lepota", desc="Zobozdravniki, fizioterapevti, ambulante in saloni."), dict(name="Obrtniki in avtoservisi", desc="Vodovodarji, električarji, mehaniki in monterji."), dict(name="Strokovne storitve", desc="Odvetniki, računovodje in nepremičninski agenti.")]),
'HR': dict(
 eyebrow="AI + Google vidljivost za lokalne tvrtke",
 h1="Vaš sljedeći klijent vas neće tražiti na Googleu. Pitat će AI.",
 sub="Kad netko pita ChatGPT, Gemini ili Perplexity koga nazvati, gdje jesti ili kojem zastupniku vjerovati, AI navede tri tvrtke. Pobrinut ćemo se da je vaša među njima — na šest jezika.",
 dName="Naziv tvrtke", dNamePh="npr. Stomatološka ordinacija Primjer", dCat="Čime se bavite?", catDef="zubar", dQ="{city}: {cat} — koga preporučuješ?",
 dYour="Vaša tvrtka", dOther="Druga tvrtka", dIdle="Upišite svoju tvrtku i pokrenite da vidite kako AI odgovara klijentu.",
 dDesc="Odlične ocjene, danas otvoreno, odgovara na WhatsAppu.",
 steps=[
  dict(tab="AI Mirror", h="Pitamo AI o vama", p="Postavljamo pitanja koja klijenti stvarno postavljaju u ChatGPT-u, Geminiju, Perplexityju i Googleovim AI odgovorima.", items=["30 pitanja klijenata na 6 jezika","Gdje se pojavljujete vi — a gdje konkurencija","Svaki pogrešan podatak koji AI kaže o vama"]),
  dict(tab="Popravak", h="Činimo vas čitljivima", p="U prvih 30 dana ispravljamo sve što AI i Google čitaju o vama.", items=["Google profil, radno vrijeme, usluge, fotografije, kategorije","Ispravljeni unosi na 15+ platformi","Usluge, cijene i kontakt strojno čitljivi na vašoj stranici"]),
  dict(tab="Ostanite odabrani", h="Zadržavamo vas ondje", p="Svaki mjesec ponovno postavljamo pitanja, dodajemo svježi sadržaj i javljamo što se promijenilo.", items=["Mjesečno Mr. Picked izvješće s ocjenom vidljivosti","AI videi i Google objave svaki mjesec","Zahtjevi za recenziju nakon svakog posla ili posjeta"])],
 vidP="Bez snimanja. Naš AI od vaših pravih fotografija izrađuje kratke isječke — sadržaj za društvene mreže i još jedan razlog da vas AI preporuči.",
 vids=[dict(h="Od vaših pravih fotografija", p="Vaš rad, vaš tim i vaš prostor, nikad tuđe snimke. Svaki isječak odobravate."), dict(h="Jedan video, šest jezika", p="AI glas i titlovi, da ga svaki klijent čuje na svom jeziku."), dict(h="Objavljeno gdje se računa", p="Instagram, TikTok, YouTube Shorts i vaš Google profil.")],
 lists=[
  ["Početna AI provjera: 30 pitanja klijenata u 3 AI alata i 6 jezika","Potpuni popravak u prvih 30 dana: Google profil, radno vrijeme, usluge, fotografije, kategorije","Usluge, radno vrijeme i lokacija strojno čitljivi na vašoj web stranici","Ispravljeni unosi na 15+ platformi (Apple Maps, Bing, strukovni imenici…)","Lokalni Google SEO: pratimo položaj na kartama za 10 ključnih pretraga","4 objave na Google profilu mjesečno","Mjesečno Mr. Picked izvješće s ocjenom vidljivosti"],
  ["Sve iz paketa Visible, plus:","2 AI videa mjesečno na 3 jezika, objavljena na Instagramu, TikToku i Googleu","Automatski zahtjev za recenziju nakon svakog posla ili posjeta","Pripremamo odgovore na sve vaše Google recenzije u 48 sati","2 nove stranice s pitanjima klijenata mjesečno na 3 jezika","Praćenje 50 pitanja klijenata + 3 obližnja konkurenta","Tromjesečni pregled rezultata"],
  ["Sve iz paketa Recommended, plus:","4 AI videa mjesečno na 6 jezika","WhatsApp concierge 24/7: odgovara na pitanja, šalje ponude i prima rezervacije","Podsjetnici za termine i praćenje nedolazaka","Vaše usluge i cjenik online na 6 jezika","Jedna sezonska kampanja po tromjesečju","Mjesečni strateški sastanak + izmjene u 24 sata (radnim danima)"]],
 addons=[dict(name="AI video paket", desc="+3 AI videa svaki mjesec"), dict(name="Prikupljanje recenzija", desc="Zahtjev za recenziju nakon svakog posla ili posjeta"), dict(name="WhatsApp concierge", desc="Odgovara klijentima i prima rezervacije, 24/7"), dict(name="Web stranica za AI", desc="Višejezična, brza, čitljiva za AI")],
 roiSpend="Prosječna vrijednost klijenta", roiGuests="Dodatni klijenti tjedno", roiBreak="Mr. Picked se isplati već s {n} dodatnih klijenata tjedno.",
 fdH="Izradili su ga ljudi koji vode lokalne tvrtke, a ne agencija.",
 fdP="U Sloveniji vodim tvrtke u ugostiteljstvu, vuči vozila i osiguranju. Mr. Picked sam najprije napravio za svoje tvrtke — sada ga radimo za vašu.",
 faqs=[dict(q="Što je GEO, jednostavno rečeno?", a="Pobrinemo se da AI pomoćnici poput ChatGPT-a, Geminija i Perplexityja poznaju vašu tvrtku, točno je opišu i preporuče. Temelji se na lokalnom SEO-u, pa ste bolje rangirani i na Googleu."), 1, 2,
  dict(q="Jesu li AI videi napravljeni od pravih snimki?", a="Od vaših pravih fotografija rada, tima i prostora, koje AI pretvara u kratke isječke. Svaki odobravate, a gdje platforme to traže, označeni su kao AI."),
  dict(q="Za koje je tvrtke ovo?", a="Za svaku tvrtku koju ljudi traže lokalno: restorane, hotele i apartmane, službe za vuču vozila, zastupnike osiguranja, stomatologe i ordinacije, salone, obrtnike i stručne usluge. Paketi su isti, pitanja i sadržaj prilagođavamo vašoj djelatnosti."), 4],
 fBiz="Naziv tvrtke", mailPh="vi@tvrtka.hr",
 indK="Djelatnosti", indH="Za tvrtke koje ljudi traže u blizini.", indP="Isti paketi i cijene, prilagođeni pitanjima koja postavljaju vaši klijenti.", indMore="Pogledajte kako funkcionira",
 inds=[dict(name="Restorani, hoteli i apartmani", desc="Da vas odaberu kad gosti pitaju gdje jesti ili spavati."), dict(name="Vuča vozila i pomoć na cesti", desc="Budite broj koji AI daje kad se auto pokvari."), dict(name="Zastupnici osiguranja", desc="Budite zastupnik kojeg AI preporuča za auto, dom i putovanja."), dict(name="Zdravlje i ljepota", desc="Stomatolozi, fizioterapeuti, ordinacije i saloni."), dict(name="Obrtnici i autoservisi", desc="Vodoinstalateri, električari, mehaničari i monteri."), dict(name="Stručne usluge", desc="Odvjetnici, računovođe i agenti za nekretnine.")]),
'IT': dict(
 eyebrow="Visibilità su AI e Google per le attività locali",
 h1="Il tuo prossimo cliente non ti cercherà su Google. Chiederà all’AI.",
 sub="Quando qualcuno chiede a ChatGPT, Gemini o Perplexity chi chiamare, dove mangiare o di quale agente fidarsi, l’AI nomina tre attività. Facciamo in modo che la tua sia tra queste — in sei lingue.",
 dName="Nome dell’attività", dNamePh="es. Studio Dentistico Esempio", dCat="Di cosa ti occupi?", catDef="dentista", dQ="{city}: {cat} — chi mi consigli?",
 dYour="La tua attività", dOther="Un’altra attività", dIdle="Inserisci la tua attività e avvia per vedere come l’AI risponde a un cliente.",
 dDesc="Ottime recensioni, aperto oggi, risponde su WhatsApp.",
 steps=[
  dict(tab="AI Mirror", h="Chiediamo all’AI di te", p="Facciamo le domande che i clienti fanno davvero su ChatGPT, Gemini, Perplexity e le risposte AI di Google.", items=["30 domande dei clienti in 6 lingue","Dove compari tu — e dove i concorrenti","Ogni informazione sbagliata che l’AI dice di te"]),
  dict(tab="Correzione", h="Ti rendiamo leggibile", p="Nei primi 30 giorni correggiamo tutto ciò che AI e Google leggono di te.", items=["Profilo Google, orari, servizi, foto, categorie","Schede corrette su oltre 15 piattaforme","Servizi, prezzi e contatti leggibili dalle macchine sul tuo sito"]),
  dict(tab="Resta scelto", h="Ti teniamo lì", p="Ogni mese ripetiamo le domande, aggiungiamo contenuti nuovi e ti diciamo cosa è cambiato.", items=["Mr. Picked Report mensile con il punteggio di visibilità","Video AI e post Google ogni mese","Richieste di recensione dopo ogni lavoro o visita"])],
 vidP="Niente riprese. La nostra AI trasforma le tue foto reali in clip brevi — contenuti per i social e un motivo in più per cui l’AI ti consiglia.",
 vids=[dict(h="Dalle tue foto reali", p="Il tuo lavoro, il tuo team e i tuoi spazi, mai immagini di repertorio. Approvi ogni clip."), dict(h="Un video, sei lingue", p="Voce AI e sottotitoli, così ogni cliente lo ascolta nella sua lingua."), dict(h="Pubblicato dove conta", p="Instagram, TikTok, YouTube Shorts e il tuo profilo Google.")],
 lists=[
  ["Analisi AI iniziale: 30 domande dei clienti su 3 AI e in 6 lingue","Correzione completa nei primi 30 giorni: profilo Google, orari, servizi, foto, categorie","Servizi, orari e posizione leggibili dalle macchine sul tuo sito","Schede corrette su oltre 15 piattaforme (Apple Maps, Bing, elenchi di settore…)","SEO locale: monitoriamo la posizione su Maps per le tue 10 ricerche chiave","4 post al mese sul profilo Google","Mr. Picked Report mensile con il tuo punteggio di visibilità"],
  ["Tutto di Visible, più:","2 video AI al mese in 3 lingue, pubblicati su Instagram, TikTok e Google","Richiesta automatica di recensione dopo ogni lavoro o visita","Prepariamo le risposte a tutte le tue recensioni Google entro 48 ore","2 nuove pagine di domande dei clienti al mese in 3 lingue","50 domande dei clienti monitorate + 3 concorrenti vicini","Call trimestrale sui risultati"],
  ["Tutto di Recommended, più:","4 video AI al mese in 6 lingue","Concierge WhatsApp 24/7: risponde alle domande, invia preventivi e prende prenotazioni","Promemoria degli appuntamenti e follow-up dei no-show","I tuoi servizi e il listino online in 6 lingue","Una campagna stagionale a trimestre","Call strategica mensile + modifiche entro 24 ore (giorni lavorativi)"]],
 addons=[dict(name="Pacchetto video AI", desc="+3 video AI ogni mese"), dict(name="Raccolta recensioni", desc="Richiesta di recensione dopo ogni lavoro o visita"), dict(name="Concierge WhatsApp", desc="Risponde ai clienti e prende prenotazioni, 24/7"), dict(name="Sito pronto per l’AI", desc="Multilingue, veloce, leggibile dall’AI")],
 roiSpend="Valore medio di un cliente", roiGuests="Clienti in più a settimana", roiBreak="Mr. Picked si ripaga già con {n} clienti in più a settimana.",
 fdH="Creato da chi gestisce attività locali, non da un’agenzia.",
 fdP="In Slovenia gestisco attività nella ristorazione, nel soccorso stradale e nelle assicurazioni. Ho creato Mr. Picked prima per le mie attività — ora lo facciamo per la tua.",
 faqs=[dict(q="Cos’è la GEO, in parole semplici?", a="Fare in modo che assistenti AI come ChatGPT, Gemini e Perplexity conoscano la tua attività, la descrivano correttamente e la consiglino. Si basa sulla SEO locale, quindi sali anche su Google."), 1, 2,
  dict(q="I video AI sono fatti con immagini reali?", a="Dalle tue foto reali del lavoro, del team e degli spazi, trasformate in clip brevi con l’AI. Approvi ognuno e, dove le piattaforme lo richiedono, sono etichettati come AI."),
  dict(q="Per quali attività è adatto?", a="Per ogni attività che le persone cercano in zona: ristoranti, hotel e appartamenti, soccorso stradale, agenti assicurativi, dentisti e ambulatori, saloni, artigiani e servizi professionali. I pacchetti sono gli stessi; adattiamo domande e contenuti al tuo settore."), 4],
 fBiz="Nome dell’attività", mailPh="tu@azienda.it",
 indK="Settori", indH="Per le attività che le persone cercano vicino a sé.", indP="Stessi pacchetti e prezzi, adattati alle domande dei tuoi clienti.", indMore="Scopri come funziona",
 inds=[dict(name="Ristoranti, hotel e appartamenti", desc="Fatti scegliere quando gli ospiti chiedono dove mangiare o dormire."), dict(name="Soccorso stradale", desc="Sii il numero che l’AI dà quando un’auto si guasta."), dict(name="Agenti assicurativi", desc="Sii l’agente che l’AI consiglia per auto, casa e viaggi."), dict(name="Salute e bellezza", desc="Dentisti, fisioterapisti, ambulatori e saloni."), dict(name="Artigiani e officine", desc="Idraulici, elettricisti, meccanici e installatori."), dict(name="Servizi professionali", desc="Avvocati, commercialisti e agenti immobiliari.")]),
'DE': dict(
 eyebrow="KI- und Google-Sichtbarkeit für lokale Unternehmen",
 h1="Ihr nächster Kunde googelt Sie nicht. Er fragt die KI.",
 sub="Wenn jemand ChatGPT, Gemini oder Perplexity fragt, wen er anrufen, wo er essen oder welchem Berater er vertrauen soll, nennt die KI drei Unternehmen. Wir sorgen dafür, dass Ihres dabei ist — in sechs Sprachen.",
 dName="Name des Unternehmens", dNamePh="z. B. Zahnarztpraxis Beispiel", dCat="Was machen Sie?", catDef="Zahnarzt", dQ="{city}: {cat} — wen empfiehlst du?",
 dYour="Ihr Unternehmen", dOther="Ein anderes Unternehmen", dIdle="Geben Sie Ihr Unternehmen ein und starten Sie — so sehen Sie, wie eine KI einem Kunden antwortet.",
 dDesc="Top bewertet, heute geöffnet, antwortet auf WhatsApp.",
 steps=[
  dict(tab="AI Mirror", h="Wir fragen die KI nach Ihnen", p="Wir stellen die Fragen, die Kunden wirklich stellen, in ChatGPT, Gemini, Perplexity und Googles KI-Antworten.", items=["30 Kundenfragen in 6 Sprachen","Wo Sie erscheinen — und wo die Konkurrenz","Jede falsche Angabe, die die KI über Sie macht"]),
  dict(tab="Korrektur", h="Wir machen Sie lesbar", p="In den ersten 30 Tagen korrigieren wir alles, was KI und Google über Sie lesen.", items=["Google-Profil, Öffnungszeiten, Leistungen, Fotos, Kategorien","Einträge auf 15+ Plattformen korrigiert","Leistungen, Preise und Kontakt maschinenlesbar auf Ihrer Website"]),
  dict(tab="Gewählt bleiben", h="Wir halten Sie dort", p="Jeden Monat stellen wir die Fragen neu, liefern frische Inhalte und berichten, was sich geändert hat.", items=["Monatlicher Mr. Picked-Bericht mit Sichtbarkeitswert","KI-Videos und Google-Beiträge jeden Monat","Bewertungsanfragen nach jedem Auftrag oder Besuch"])],
 vidP="Kein Dreh. Unsere KI macht aus Ihren echten Fotos kurze Clips — Inhalte für Social Media und ein Grund mehr für die KI, Sie zu empfehlen.",
 vids=[dict(h="Aus Ihren echten Fotos", p="Ihre Arbeit, Ihr Team und Ihre Räume, nie Stockbilder. Sie geben jeden Clip frei."), dict(h="Ein Video, sechs Sprachen", p="KI-Sprecherstimme und Untertitel, damit jeder Kunde es in seiner Sprache hört."), dict(h="Veröffentlicht, wo es zählt", p="Instagram, TikTok, YouTube Shorts und Ihr Google-Profil.")],
 lists=[
  ["KI-Startanalyse: 30 Kundenfragen in 3 KI-Tools und 6 Sprachen","Komplette Korrektur in den ersten 30 Tagen: Google-Profil, Öffnungszeiten, Leistungen, Fotos, Kategorien","Leistungen, Öffnungszeiten und Standort maschinenlesbar auf Ihrer Website","Einträge auf 15+ Plattformen korrigiert (Apple Maps, Bing, Branchenverzeichnisse…)","Lokales Google-SEO: Maps-Ranking für Ihre 10 wichtigsten Suchen im Blick","4 Beiträge pro Monat auf Ihrem Google-Profil","Monatlicher Mr. Picked-Bericht mit Ihrem Sichtbarkeitswert"],
  ["Alles aus Visible, plus:","2 KI-Videos pro Monat in 3 Sprachen, auf Instagram, TikTok und Google veröffentlicht","Automatische Bewertungsanfrage nach jedem Auftrag oder Besuch","Wir entwerfen Antworten auf alle Google-Bewertungen innerhalb von 48 h","2 neue Seiten mit Kundenfragen pro Monat in 3 Sprachen","50 Kundenfragen + 3 Mitbewerber in der Nähe im Blick","Quartalsgespräch zu den Ergebnissen"],
  ["Alles aus Recommended, plus:","4 KI-Videos pro Monat in 6 Sprachen","WhatsApp-Concierge 24/7: beantwortet Fragen, sendet Angebote und nimmt Buchungen an","Terminerinnerungen und No-Show-Nachfassung","Ihre Leistungen und Preisliste online in 6 Sprachen","Eine saisonale Kampagne pro Quartal","Monatliches Strategiegespräch + Änderungen innerhalb von 24 h (an Werktagen)"]],
 addons=[dict(name="KI-Video-Paket", desc="+3 KI-Videos jeden Monat"), dict(name="Bewertungsschleife", desc="Bewertungsanfrage nach jedem Auftrag oder Besuch"), dict(name="WhatsApp-Concierge", desc="Beantwortet Kunden und nimmt Buchungen an, 24/7"), dict(name="KI-taugliche Website", desc="Mehrsprachig, schnell, für KI lesbar")],
 roiSpend="Durchschnittlicher Wert eines Kunden", roiGuests="Zusätzliche Kunden pro Woche", roiBreak="Mr. Picked rechnet sich schon ab {n} zusätzlichen Kunden pro Woche.",
 fdH="Gebaut von Leuten, die lokale Unternehmen führen, nicht von einer Agentur.",
 fdP="Ich führe in Slowenien Unternehmen in Gastronomie, Abschleppdienst und Versicherung. Ich habe Mr. Picked zuerst für meine eigenen Unternehmen gebaut — jetzt machen wir es für Ihres.",
 faqs=[dict(q="Was ist GEO, einfach erklärt?", a="Wir sorgen dafür, dass KI-Assistenten wie ChatGPT, Gemini und Perplexity Ihr Unternehmen kennen, richtig beschreiben und empfehlen. Es baut auf lokalem SEO auf, deshalb ranken Sie auch bei Google besser."), 1, 2,
  dict(q="Werden die KI-Videos aus echtem Material gemacht?", a="Aus Ihren echten Fotos von Arbeit, Team und Räumen, die eine KI in kurze Clips verwandelt. Sie geben jeden frei, und wo Plattformen es verlangen, sind sie als KI gekennzeichnet."),
  dict(q="Für welche Unternehmen ist das?", a="Für jedes Unternehmen, das Menschen in der Nähe suchen: Restaurants, Hotels und Ferienwohnungen, Abschleppdienste, Versicherungsberater, Zahnärzte und Praxen, Salons, Handwerker und Dienstleister. Die Pakete sind gleich; Fragen und Inhalte passen wir an Ihre Branche an."), 4],
 fBiz="Name des Unternehmens", mailPh="sie@firma.at",
 indK="Branchen", indH="Für Unternehmen, die man in der Nähe sucht.", indP="Gleiche Pakete und Preise, zugeschnitten auf die Fragen Ihrer Kunden.", indMore="So funktioniert’s",
 inds=[dict(name="Restaurants, Hotels & Ferienwohnungen", desc="Gewählt werden, wenn Gäste fragen, wo sie essen oder schlafen sollen."), dict(name="Abschlepp- und Pannendienst", desc="Die Nummer sein, die die KI bei einer Panne nennt."), dict(name="Versicherungsberater", desc="Der Berater sein, den die KI für Auto, Haus und Reise empfiehlt."), dict(name="Gesundheit & Schönheit", desc="Zahnärzte, Physiotherapeuten, Praxen und Salons."), dict(name="Handwerk & Kfz-Werkstätten", desc="Installateure, Elektriker, Mechaniker und Monteure."), dict(name="Freie Berufe", desc="Anwälte, Steuerberater und Immobilienmakler.")]),
'HU': dict(
 eyebrow="AI- és Google-láthatóság helyi vállalkozásoknak",
 h1="A következő ügyfele nem a Google-ön keresi. Az AI-t kérdezi.",
 sub="Amikor valaki megkérdezi a ChatGPT-t, a Geminit vagy a Perplexityt, kit hívjon, hol egyen vagy melyik biztosítási tanácsadóban bízzon, az AI három vállalkozást nevez meg. Mi gondoskodunk róla, hogy az Öné köztük legyen — hat nyelven.",
 dName="A vállalkozás neve", dNamePh="pl. Példa Fogászat", dCat="Mivel foglalkozik?", catDef="fogorvos", dQ="{city}: {cat} — kit ajánlasz?",
 dYour="Az Ön vállalkozása", dOther="Egy másik vállalkozás", dIdle="Írja be a vállalkozását, és indítsa el, hogy lássa, hogyan válaszol az AI egy ügyfélnek.",
 dDesc="Kiváló értékelések, ma nyitva, WhatsAppon válaszol.",
 steps=[
  dict(tab="AI Mirror", h="Megkérdezzük az AI-t Önről", p="Feltesszük azokat a kérdéseket, amelyeket az ügyfelek valóban feltesznek, a ChatGPT-ben, a Geminiben, a Perplexityben és a Google AI-válaszaiban.", items=["30 ügyfélkérdés 6 nyelven","Hol jelenik meg Ön — és hol a versenytársak","Minden téves adat, amit az AI Önről mond"]),
  dict(tab="Javítás", h="Olvashatóvá tesszük Önt", p="Az első 30 napban kijavítunk mindent, amit az AI és a Google Önről olvas.", items=["Google-profil, nyitvatartás, szolgáltatások, fotók, kategóriák","Javított bejegyzések 15+ platformon","Szolgáltatások, árak és elérhetőség gépileg olvashatóan a weboldalán"]),
  dict(tab="Maradjon kiválasztott", h="Ott tartjuk Önt", p="Minden hónapban újra feltesszük a kérdéseket, friss tartalmat adunk, és beszámolunk a változásokról.", items=["Havi Mr. Picked-jelentés láthatósági pontszámmal","AI-videók és Google-bejegyzések minden hónapban","Értékeléskérés minden munka vagy látogatás után"])],
 vidP="Nincs forgatás. AI-unk az Ön valódi fotóiból rövid klipeket készít — tartalmat a közösségi médiára, és még egy okot, hogy az AI Önt ajánlja.",
 vids=[dict(h="Az Ön valódi fotóiból", p="Az Ön munkája, csapata és terei, soha nem stockfelvételek. Minden klipet Ön hagy jóvá."), dict(h="Egy videó, hat nyelv", p="AI-narráció és felirat, hogy minden ügyfél a saját nyelvén hallja."), dict(h="Ott jelenik meg, ahol számít", p="Instagram, TikTok, YouTube Shorts és az Ön Google-profilja.")],
 lists=[
  ["Kezdő AI-audit: 30 ügyfélkérdés 3 AI-eszközben és 6 nyelven","Teljes javítás az első 30 napban: Google-profil, nyitvatartás, szolgáltatások, fotók, kategóriák","Szolgáltatások, nyitvatartás és helyszín gépileg olvashatóan a weboldalán","Javított bejegyzések 15+ platformon (Apple Maps, Bing, szakmai címtárak…)","Helyi Google SEO: Térkép-helyezés követése a 10 fő keresésére","Havi 4 bejegyzés a Google-profilján","Havi Mr. Picked-jelentés láthatósági pontszámmal"],
  ["Minden, ami a Visible csomagban, plusz:","Havi 2 AI-videó 3 nyelven, Instagramon, TikTokon és a Google-ön","Automatikus értékeléskérés minden munka vagy látogatás után","48 órán belül megírjuk a válaszokat minden Google-értékelésre","Havi 2 új ügyfélkérdés-oldal 3 nyelven","50 ügyfélkérdés + 3 közeli versenytárs követése","Negyedéves eredménymegbeszélés"],
  ["Minden, ami a Recommended csomagban, plusz:","Havi 4 AI-videó 6 nyelven","WhatsApp concierge 0–24: válaszol a kérdésekre, árajánlatot küld és foglalást fogad","Időpont-emlékeztetők és a meg nem jelenők utánkövetése","Szolgáltatásai és árlistája online 6 nyelven","Negyedévente egy szezonális kampány","Havi stratégiai megbeszélés + módosítások 24 órán belül (munkanapokon)"]],
 addons=[dict(name="AI-videócsomag", desc="+3 AI-videó minden hónapban"), dict(name="Értékelésgyűjtés", desc="Értékeléskérés minden munka vagy látogatás után"), dict(name="WhatsApp concierge", desc="Válaszol az ügyfeleknek és foglalást fogad, 0–24"), dict(name="AI-ra kész weboldal", desc="Többnyelvű, gyors, AI számára olvasható")],
 roiSpend="Egy ügyfél átlagos értéke", roiGuests="Plusz ügyfél hetente", roiBreak="A Mr. Picked már heti {n} plusz ügyfélnél megtérül.",
 fdH="Helyi vállalkozásokat vezető emberek építették, nem egy ügynökség.",
 fdP="Szlovéniában vendéglátó-, autómentő és biztosítási vállalkozásokat vezetek. A Mr. Pickedet először a saját vállalkozásaimnak építettem — most az Önének csináljuk.",
 faqs=[dict(q="Mi az a GEO, egyszerűen?", a="Gondoskodunk róla, hogy az olyan AI-asszisztensek, mint a ChatGPT, a Gemini és a Perplexity ismerjék a vállalkozását, pontosan írják le és ajánlják. Helyi SEO-ra épül, így a Google-ön is jobb helyen lesz."), 1, 2,
  dict(q="Valódi anyagból készülnek az AI-videók?", a="Az Ön munkájáról, csapatáról és tereiről készült valódi fotókból, amelyeket AI alakít rövid klipekké. Mindegyiket Ön hagyja jóvá, és ahol a platformok előírják, AI-ként jelöljük."),
  dict(q="Milyen vállalkozásoknak szól?", a="Minden vállalkozásnak, amelyet az emberek a közelben keresnek: éttermeknek, szállodáknak és apartmanoknak, autómentőknek, biztosítási tanácsadóknak, fogorvosoknak és rendelőknek, szalonoknak, szakiparosoknak és szakmai szolgáltatóknak. A csomagok ugyanazok; a kérdéseket és a tartalmat az Ön ágazatához igazítjuk."), 4],
 fBiz="A vállalkozás neve", mailPh="on@ceg.hu",
 indK="Ágazatok", indH="Vállalkozásoknak, amelyeket a közelben keresnek.", indP="Ugyanazok a csomagok és árak, az ügyfelei kérdéseihez igazítva.", indMore="Nézze meg, hogyan működik",
 inds=[dict(name="Éttermek, szállodák és apartmanok", desc="Válasszák Önt, amikor a vendégek azt kérdezik, hol egyenek vagy aludjanak."), dict(name="Autómentés és segélyszolgálat", desc="Legyen az a szám, amit az AI ad, ha lerobban az autó."), dict(name="Biztosítási tanácsadók", desc="Legyen az a tanácsadó, akit az AI ajánl autóra, otthonra és utazásra."), dict(name="Egészség és szépség", desc="Fogorvosok, gyógytornászok, rendelők és szalonok."), dict(name="Szakiparosok és autószervizek", desc="Vízszerelők, villanyszerelők, szerelők és telepítők."), dict(name="Szakmai szolgáltatások", desc="Ügyvédek, könyvelők és ingatlanközvetítők.")]),
}

IND = {
'hospitality': {
 'EN': dict(eyebrow="AI + Google visibility for restaurants, hotels & apartments", mailPh="you@restaurant.si"),
 'SL': dict(eyebrow="AI + Google vidnost za restavracije, hotele in apartmaje", mailPh="vi@restavracija.si"),
},
'towing': {
 'EN': dict(
  eyebrow="AI + Google visibility for towing & roadside assistance",
  h1="When a car breaks down, nobody browses. They ask AI who to call.",
  sub="A driver on the hard shoulder asks ChatGPT, Gemini or Google “towing near me, open now” and calls the first number AI gives. We make sure that number is yours.",
  dName="Company name", dNamePh="e.g. Towing Primer", dQ="{city}: towing service open now?",
  dYour="Your towing company", dOther="Another towing company", dIdle="Enter your company and press run to see what AI tells a stranded driver.",
  dDesc="24/7, arrives in about 30 minutes. Call or WhatsApp.",
  steps=[
   dict(tab="AI Mirror", h="We ask the AIs about you", p="We run the questions stranded drivers actually ask across ChatGPT, Gemini, Perplexity and Google’s AI answers — at night, on the motorway, in other languages.", items=["30 driver questions in 6 languages","Where you appear — and which towing company appears instead","Wrong numbers, hours or service areas the AI gives about you"]),
   dict(tab="Fix", h="We make you readable", p="In the first 30 days we fix everything AI and Google read about you.", items=["Google profile: 24/7 hours, emergency number, service area, vehicle types","Listings corrected on 15+ platforms and assistance directories","Services, prices and service area machine-readable on your site"]),
   dict(tab="Stay picked", h="We keep you there", p="Every month we re-run the questions, add fresh content and report what changed.", items=["Monthly Mr. Picked Report with your visibility score","AI videos and Google posts every month","Review request after every tow"])],
  vidP="No filming. Our AI turns photos of your trucks, team and jobs into short clips that show drivers who will come for them.",
  vids=[dict(h="From your real photos", p="Your tow trucks, your drivers and real jobs, never stock footage. You approve every clip."), dict(h="One video, six languages", p="Foreign drivers on your roads hear it in their own language."), dict(h="Posted where it counts", p="Instagram, TikTok, YouTube Shorts and your Google profile.")],
  lists=[
   ["Starting AI audit: 30 driver questions in 3 AIs and 6 languages","Full fix in the first 30 days: Google profile, 24/7 hours, emergency number, service area, photos","Services, service area and prices machine-readable on your website","Listings corrected on 15+ platforms (Apple Maps, Bing, towing and assistance directories…)","Local Google SEO: tracked Maps ranking for your 10 key searches (e.g. “towing A1 Ljubljana”)","4 Google profile posts per month","Monthly Mr. Picked Report with your visibility score"],
   ["Everything in Visible, plus:","2 AI videos / month in 3 languages, posted to Instagram, TikTok and Google","Automatic review request after every tow","We draft replies to all your Google reviews within 48 h","2 new driver-question pages / month in 3 languages (e.g. “what to do after a breakdown on the motorway”)","50 driver questions tracked + 3 nearby competitors","Quarterly results call"],
   ["Everything in Recommended, plus:","4 AI videos / month in 6 languages","WhatsApp concierge 24/7: takes the driver’s location and vehicle, sends a price estimate and passes the job to your dispatcher","Status messages to the driver (on the way, arrival time)","Your services and price list online in 6 languages","One seasonal campaign per quarter (winter tyres, summer travel season…)","Monthly strategy call + changes within 24 h (working days)"]],
  addons=[dict(name="AI video pack", desc="+3 AI videos every month"), dict(name="Review loop", desc="Review request after every tow"), dict(name="WhatsApp concierge", desc="Takes location and vehicle details, sends an estimate, 24/7"), dict(name="AI-ready website", desc="Multilingual, fast, readable by AI")],
  roiSpend="Average value of a tow", roiGuests="Extra calls per week", roiBreak="Mr. Picked pays for itself at {n} extra calls a week.",
  fdH="Built by people who run a towing company, not an agency.",
  fdP="I’ve run a towing and roadside assistance company in Slovenia. I know what one missed night call costs — so I built Mr. Picked for my own trucks first.",
  faqs=[dict(q="What is GEO, in plain words?", a="Making sure AI assistants like ChatGPT, Gemini and Perplexity know your company, describe it correctly and recommend it. It builds on local SEO, so you also rank better on Google."),
   dict(q="Can AI really send me tows?", a="Drivers increasingly ask ChatGPT, Gemini or Google’s AI for a towing service instead of scrolling results. AI names the companies whose details it trusts: correct 24/7 hours, number, service area and good reviews. That is exactly what we fix and keep up to date."), 1,
   dict(q="Does the WhatsApp concierge replace my dispatcher?", a="No. It answers first, collects location, vehicle and photos, and sends an estimate from your price list. Your dispatcher confirms and sends the truck."), 4],
  fBiz="Company name", mailPh="you@company.si"),
 'SL': dict(
  eyebrow="AI + Google vidnost za vlečne službe in pomoč na cesti",
  h1="Ko se avto pokvari, nihče ne brska. Vprašajo AI, koga poklicati.",
  sub="Voznik ob avtocesti vpraša ChatGPT, Gemini ali Google »vlečna služba v bližini, odprto zdaj« in pokliče prvo številko, ki mu jo da AI. Poskrbimo, da je to vaša številka.",
  dName="Ime podjetja", dNamePh="npr. Avtovleka Primer", dQ="{city}: vlečna služba, ki dela zdaj?",
  dYour="Vaša vlečna služba", dOther="Druga vlečna služba", dIdle="Vpišite svoje podjetje in zaženite, da vidite, kaj AI pove obstalemu vozniku.",
  dDesc="24/7, prihod v približno 30 minutah. Klic ali WhatsApp.",
  steps=[
   dict(tab="AI Mirror", h="AI vprašamo o vas", p="Postavimo vprašanja, ki jih vozniki v okvari res sprašujejo, v ChatGPT, Gemini, Perplexity in Googlovih AI odgovorih — ponoči, na avtocesti, v tujih jezikih.", items=["30 vprašanj voznikov v 6 jezikih","Kje se pojavite vi — in katera vlečna služba namesto vas","Napačne številke, ure ali območja, ki jih AI navaja o vas"]),
   dict(tab="Popravek", h="Poskrbimo, da vas AI razume", p="V prvih 30 dneh popravimo vse, kar AI in Google bereta o vas.", items=["Google profil: delovni čas 24/7, dežurna številka, območje, vrste vozil","Popravljeni vpisi na 15+ platformah in imenikih pomoči na cesti","Storitve, območje in cene strojno berljivi na vaši strani"]),
   dict(tab="Ostanite izbrani", h="Obdržimo vas tam", p="Vsak mesec ponovno postavimo vprašanja, dodamo svežo vsebino in poročamo, kaj se je spremenilo.", items=["Mesečno poročilo Mr. Picked z oceno vidnosti","AI videi in Google objave vsak mesec","Prošnja za oceno po vsakem prevozu"])],
  vidP="Brez snemanja. Naš AI iz fotografij vaših vozil, ekipe in intervencij ustvari kratke posnetke, ki voznikom pokažejo, kdo bo prišel ponje.",
  vids=[dict(h="Iz vaših pravih fotografij", p="Vaša vlečna vozila, vozniki in prave intervencije, nikoli tuji posnetki. Vsak posnetek odobrite."), dict(h="En video, šest jezikov", p="Tuji vozniki na naših cestah ga slišijo v svojem jeziku."), dict(h="Objavljeno tam, kjer šteje", p="Instagram, TikTok, YouTube Shorts in vaš Google profil.")],
  lists=[
   ["Začetni AI pregled: 30 vprašanj voznikov v 3 AI orodjih in 6 jezikih","Celoten popravek v prvih 30 dneh: Google profil, delovni čas 24/7, dežurna številka, območje, fotografije","Storitve, območje in cene strojno berljivi na vaši spletni strani","Popravljeni vpisi na 15+ platformah (Apple Maps, Bing, imeniki vlečnih služb in pomoči na cesti …)","Lokalni Google SEO: spremljamo mesto na Zemljevidih za 10 ključnih iskanj (npr. »avtovleka A1 Ljubljana«)","4 objave na Google profilu na mesec","Mesečno poročilo Mr. Picked z oceno vidnosti"],
   ["Vse iz paketa Visible, plus:","2 AI videa na mesec v 3 jezikih, objavljena na Instagramu, TikToku in Googlu","Samodejna prošnja za oceno po vsakem prevozu","Pripravimo odgovore na vse vaše Google ocene v 48 urah","2 novi strani z vprašanji voznikov na mesec v 3 jezikih (npr. »kaj narediti ob okvari na avtocesti«)","Spremljanje 50 vprašanj voznikov + 3 bližnjih konkurentov","Četrtletni pregled rezultatov"],
   ["Vse iz paketa Recommended, plus:","4 AI videi na mesec v 6 jezikih","WhatsApp concierge 24/7: sprejme lokacijo in podatke o vozilu, pošlje oceno cene in preda nalog vašemu dispečerju","Sporočila vozniku o statusu (na poti, čas prihoda)","Vaše storitve in cenik na spletu v 6 jezikih","Ena sezonska kampanja na četrtletje (zimske pnevmatike, poletna turistična sezona …)","Mesečni strateški sestanek + spremembe v 24 urah (delovni dnevi)"]],
  addons=[dict(name="AI video paket", desc="+3 AI videi vsak mesec"), dict(name="Zbiranje ocen", desc="Prošnja za oceno po vsakem prevozu"), dict(name="WhatsApp concierge", desc="Sprejme lokacijo in podatke o vozilu, pošlje oceno cene, 24/7"), dict(name="Spletna stran za AI", desc="Večjezična, hitra, berljiva za AI")],
  roiSpend="Povprečna vrednost prevoza", roiGuests="Dodatni klici na teden", roiBreak="Mr. Picked se poplača že pri {n} dodatnih klicih na teden.",
  fdH="Naredili so ga ljudje, ki vodijo vlečno službo, ne agencija.",
  fdP="Sam sem vodil podjetje za avtovleko in pomoč na cesti v Sloveniji. Vem, koliko stane en zamujen nočni klic — zato sem Mr. Picked najprej naredil za svoja vozila.",
  faqs=[dict(q="Kaj je GEO, preprosto povedano?", a="Poskrbimo, da AI pomočniki, kot so ChatGPT, Gemini in Perplexity, poznajo vaše podjetje, ga pravilno opišejo in priporočijo. Gradi na lokalnem SEO, zato ste višje tudi na Googlu."),
   dict(q="Mi lahko AI res prinese prevoze?", a="Vozniki vse pogosteje vprašajo ChatGPT, Gemini ali Googlov AI za vlečno službo, namesto da brskajo po zadetkih. AI imenuje podjetja, katerih podatkom zaupa: pravilen delovni čas 24/7, številka, območje in dobre ocene. Točno to popravimo in vzdržujemo."), 1,
   dict(q="Ali WhatsApp concierge nadomesti dispečerja?", a="Ne. Odgovori prvi, zbere lokacijo, vozilo in fotografije ter pošlje oceno po vašem ceniku. Dispečer potrdi in pošlje vozilo."), 4],
  fBiz="Ime podjetja", mailPh="vi@podjetje.si"),
},
'insurance': {
 'EN': dict(
  eyebrow="AI + Google visibility for insurance agents",
  h1="Your next client won’t ask a friend for an agent. They’ll ask AI.",
  sub="When someone asks ChatGPT, Gemini or Perplexity which insurance agent to trust for car, home or travel insurance, AI names two or three. We make sure you are one of them.",
  dName="Agency name", dNamePh="e.g. Insurance Agency Primer", dQ="{city}: which insurance agent would you recommend for car insurance?",
  dYour="Your agency", dOther="Another agency", dIdle="Enter your agency and press run to see what AI tells someone looking for insurance.",
  dDesc="Compares several insurers, replies the same day. Book a call.",
  steps=[
   dict(tab="AI Mirror", h="We ask the AIs about you", p="We run the questions people actually ask before they choose an agent, across ChatGPT, Gemini, Perplexity and Google’s AI answers.", items=["30 client questions in 6 languages","Where you appear — and which agents appear instead","Wrong contact details, hours or insurers the AI lists for you"]),
   dict(tab="Fix", h="We make you readable", p="In the first 30 days we fix everything AI and Google read about you.", items=["Google profile: hours, insurance types, partner insurers, photos","Listings corrected on 15+ platforms","Insurance types, partner insurers and contact details machine-readable on your site"]),
   dict(tab="Stay picked", h="We keep you there", p="Every month we re-run the questions, add fresh content and report what changed.", items=["Monthly Mr. Picked Report with your visibility score","AI videos and Google posts every month","Review request after every new policy or claim"])],
  vidP="No filming. Our AI turns your photos into short, clear explainer clips — what to do after a car accident, how travel insurance works — that build trust before the first call.",
  vids=[dict(h="From your real photos", p="You, your team and your office, never stock footage. You approve every clip."), dict(h="One video, six languages", p="Foreign residents and tourists hear it in their own language."), dict(h="Posted where it counts", p="Instagram, TikTok, YouTube Shorts and your Google profile.")],
  lists=[
   ["Starting AI audit: 30 client questions in 3 AIs and 6 languages","Full fix in the first 30 days: Google profile, hours, insurance types, partner insurers, photos","Insurance types, insurers and contact details machine-readable on your website","Listings corrected on 15+ platforms (Apple Maps, Bing, business directories…)","Local Google SEO: tracked Maps ranking for your 10 key searches (e.g. “car insurance agent Kamnik”)","4 Google profile posts per month","Monthly Mr. Picked Report with your visibility score"],
   ["Everything in Visible, plus:","2 AI explainer videos / month in 3 languages, posted to Instagram, TikTok and Google","Automatic review request after every new policy or claim","We draft replies to all your Google reviews within 48 h","2 new client-question pages / month in 3 languages (e.g. “what to do after a car accident”)","50 client questions tracked + 3 nearby competitors","Quarterly results call"],
   ["Everything in Recommended, plus:","4 AI videos / month in 6 languages","WhatsApp concierge 24/7: answers common questions, collects details for a quote and books a call with you","Renewal reminders and follow-up for expiring policies","Your insurance types and FAQs online in 6 languages","One seasonal campaign per quarter (car renewal season, travel insurance before summer…)","Monthly strategy call + changes within 24 h (working days)"]],
  addons=[dict(name="AI video pack", desc="+3 AI videos every month"), dict(name="Review loop", desc="Review request after every new policy or claim"), dict(name="WhatsApp concierge", desc="Answers questions, collects details for a quote, books calls, 24/7"), dict(name="AI-ready website", desc="Multilingual, fast, readable by AI")],
  roiSpend="Average yearly value of a client", roiGuests="Extra clients per week", roiBreak="Mr. Picked pays for itself at {n} extra clients a week.",
  fdH="Built by people who run an insurance agency, not an agency.",
  fdP="I run an insurance agency company in Slovenia myself. I know clients pick the agent they trust first — so I built Mr. Picked to make sure AI knows and trusts you.",
  faqs=[dict(q="What is GEO, in plain words?", a="Making sure AI assistants like ChatGPT, Gemini and Perplexity know your agency, describe it correctly and recommend it. It builds on local SEO, so you also rank better on Google."),
   dict(q="Can AI really bring me clients?", a="More and more people ask ChatGPT, Gemini or Google’s AI which agent to trust instead of asking friends. AI recommends agents whose details and reviews it trusts. That is exactly what we fix and keep up to date."), 1,
   dict(q="Will the WhatsApp concierge give insurance advice?", a="No. It answers general questions, such as office hours, documents needed and which insurance types you offer, collects details for a quote and books a call. Advice and offers always come from you."), 4],
  fBiz="Agency name", mailPh="you@agency.si"),
 'SL': dict(
  eyebrow="AI + Google vidnost za zavarovalniške zastopnike",
  h1="Vaša naslednja stranka ne bo vprašala prijatelja za zastopnika. Vprašala bo AI.",
  sub="Ko nekdo vpraša ChatGPT, Gemini ali Perplexity, kateremu zastopniku zaupati za avtomobilsko, domsko ali potovalno zavarovanje, AI imenuje dva ali tri. Poskrbimo, da ste vi med njimi.",
  dName="Ime zastopništva", dNamePh="npr. Zavarovalno zastopništvo Primer", dQ="{city}: katerega zavarovalnega zastopnika priporočaš za avtomobilsko zavarovanje?",
  dYour="Vaše zastopništvo", dOther="Drugo zastopništvo", dIdle="Vpišite svoje zastopništvo in zaženite, da vidite, kaj AI pove nekomu, ki išče zavarovanje.",
  dDesc="Primerja več zavarovalnic, odgovori isti dan. Rezervirajte klic.",
  steps=[
   dict(tab="AI Mirror", h="AI vprašamo o vas", p="Postavimo vprašanja, ki jih ljudje res postavljajo, preden izberejo zastopnika, v ChatGPT, Gemini, Perplexity in Googlovih AI odgovorih.", items=["30 vprašanj strank v 6 jezikih","Kje se pojavite vi — in kateri zastopniki namesto vas","Napačni kontakti, ure ali zavarovalnice, ki jih AI navaja o vas"]),
   dict(tab="Popravek", h="Poskrbimo, da vas AI razume", p="V prvih 30 dneh popravimo vse, kar AI in Google bereta o vas.", items=["Google profil: delovni čas, vrste zavarovanj, partnerske zavarovalnice, fotografije","Popravljeni vpisi na 15+ platformah","Vrste zavarovanj, zavarovalnice in kontakt strojno berljivi na vaši strani"]),
   dict(tab="Ostanite izbrani", h="Obdržimo vas tam", p="Vsak mesec ponovno postavimo vprašanja, dodamo svežo vsebino in poročamo, kaj se je spremenilo.", items=["Mesečno poročilo Mr. Picked z oceno vidnosti","AI videi in Google objave vsak mesec","Prošnja za oceno po vsaki novi polici ali škodi"])],
  vidP="Brez snemanja. Naš AI iz vaših fotografij ustvari kratke, jasne razlagalne posnetke — kaj narediti po prometni nesreči, kako deluje potovalno zavarovanje — ki zgradijo zaupanje še pred prvim klicem.",
  vids=[dict(h="Iz vaših pravih fotografij", p="Vi, vaša ekipa in vaša pisarna, nikoli tuji posnetki. Vsak posnetek odobrite."), dict(h="En video, šest jezikov", p="Tujci, ki živijo pri nas, in turisti ga slišijo v svojem jeziku."), dict(h="Objavljeno tam, kjer šteje", p="Instagram, TikTok, YouTube Shorts in vaš Google profil.")],
  lists=[
   ["Začetni AI pregled: 30 vprašanj strank v 3 AI orodjih in 6 jezikih","Celoten popravek v prvih 30 dneh: Google profil, ure, vrste zavarovanj, partnerske zavarovalnice, fotografije","Vrste zavarovanj, zavarovalnice in kontakt strojno berljivi na vaši spletni strani","Popravljeni vpisi na 15+ platformah (Apple Maps, Bing, poslovni imeniki …)","Lokalni Google SEO: spremljamo mesto na Zemljevidih za 10 ključnih iskanj (npr. »zavarovalni zastopnik Kamnik«)","4 objave na Google profilu na mesec","Mesečno poročilo Mr. Picked z oceno vidnosti"],
   ["Vse iz paketa Visible, plus:","2 AI razlagalna videa na mesec v 3 jezikih, objavljena na Instagramu, TikToku in Googlu","Samodejna prošnja za oceno po vsaki novi polici ali škodi","Pripravimo odgovore na vse vaše Google ocene v 48 urah","2 novi strani z vprašanji strank na mesec v 3 jezikih (npr. »kaj narediti po prometni nesreči«)","Spremljanje 50 vprašanj strank + 3 bližnjih konkurentov","Četrtletni pregled rezultatov"],
   ["Vse iz paketa Recommended, plus:","4 AI videi na mesec v 6 jezikih","WhatsApp concierge 24/7: odgovarja na pogosta vprašanja, zbere podatke za ponudbo in rezervira klic z vami","Opomniki za podaljšanje in sledenje policam, ki se iztekajo","Vrste zavarovanj in pogosta vprašanja na spletu v 6 jezikih","Ena sezonska kampanja na četrtletje (obnova avtomobilskih zavarovanj, potovalno zavarovanje pred poletjem …)","Mesečni strateški sestanek + spremembe v 24 urah (delovni dnevi)"]],
  addons=[dict(name="AI video paket", desc="+3 AI videi vsak mesec"), dict(name="Zbiranje ocen", desc="Prošnja za oceno po vsaki novi polici ali škodi"), dict(name="WhatsApp concierge", desc="Odgovarja na vprašanja, zbere podatke za ponudbo, rezervira klic, 24/7"), dict(name="Spletna stran za AI", desc="Večjezična, hitra, berljiva za AI")],
  roiSpend="Povprečna letna vrednost stranke", roiGuests="Dodatne stranke na teden", roiBreak="Mr. Picked se poplača že pri {n} dodatnih strankah na teden.",
  fdH="Naredili so ga ljudje, ki vodijo zavarovalno zastopništvo, ne agencija.",
  fdP="Tudi sam imam zavarovalno zastopniško družbo v Sloveniji. Vem, da stranke izberejo zastopnika, ki mu najprej zaupajo — zato sem Mr. Picked naredil tako, da vas AI pozna in vam zaupa.",
  faqs=[dict(q="Kaj je GEO, preprosto povedano?", a="Poskrbimo, da AI pomočniki, kot so ChatGPT, Gemini in Perplexity, poznajo vaše zastopništvo, ga pravilno opišejo in priporočijo. Gradi na lokalnem SEO, zato ste višje tudi na Googlu."),
   dict(q="Mi lahko AI res prinese stranke?", a="Vse več ljudi namesto prijateljev vpraša ChatGPT, Gemini ali Googlov AI, kateremu zastopniku zaupati. AI priporoči zastopnike, katerih podatkom in ocenam zaupa. Točno to popravimo in vzdržujemo."), 1,
   dict(q="Ali WhatsApp concierge svetuje glede zavarovanj?", a="Ne. Odgovarja na splošna vprašanja, kot so delovni čas, potrebni dokumenti in vrste zavarovanj, ki jih ponujate, zbere podatke za ponudbo in rezervira klic. Nasvete in ponudbe vedno daste vi."), 4],
  fBiz="Ime zastopništva", mailPh="vi@zastopnistvo.si"),
},
}

# ROI slider settings per page variant: (default value, min, max, step) for value and for customers per week
ROI = {
 'main': ((60, 10, 300, 5), (5, 0, 60, 1)),
 'hospitality': ((35, 10, 150, 5), (10, 0, 80, 1)),
 'towing': ((150, 50, 500, 10), (3, 0, 40, 1)),
 'insurance': ((150, 50, 600, 10), (2, 0, 20, 1)),
}

# Industry page URLs per language; industry cards on main pages link here (other languages link to EN).
IND_PATH = {
 'hospitality': {'EN': 'hospitality/', 'SL': 'sl/gostinstvo/'},
 'towing': {'EN': 'towing/', 'SL': 'sl/avtovleka/'},
 'insurance': {'EN': 'insurance/', 'SL': 'sl/zavarovanje/'},
}

META_MAIN = {
 'EN': ("Mr. Picked — Get recommended by AI | AI + Google visibility for local businesses", "When customers ask ChatGPT, Gemini or Perplexity who to call or where to go, AI names three businesses. Mr. Picked makes sure yours is one of them — in 6 languages. Free AI check."),
 'SL': ("Mr. Picked — Naj vas priporoči AI | AI + Google vidnost za lokalna podjetja", "Ko stranke vprašajo ChatGPT, Gemini ali Perplexity, koga poklicati ali kam iti, AI imenuje tri podjetja. Mr. Picked poskrbi, da je vaše med njimi — v 6 jezikih. Brezplačen AI pregled."),
 'HR': ("Mr. Picked — Neka vas AI preporuči | AI + Google vidljivost za lokalne tvrtke", "Kad klijenti pitaju ChatGPT, Gemini ili Perplexity koga nazvati ili kamo ići, AI navede tri tvrtke. Mr. Picked se brine da je vaša među njima — na 6 jezika. Besplatna AI provjera."),
 'IT': ("Mr. Picked — Fatti consigliare dall’AI | Visibilità su AI e Google per attività locali", "Quando i clienti chiedono a ChatGPT, Gemini o Perplexity chi chiamare o dove andare, l’AI nomina tre attività. Mr. Picked fa in modo che la tua sia tra queste — in 6 lingue. Analisi AI gratuita."),
 'DE': ("Mr. Picked — Von der KI empfohlen werden | KI- und Google-Sichtbarkeit für lokale Unternehmen", "Wenn Kunden ChatGPT, Gemini oder Perplexity fragen, wen sie anrufen oder wohin sie gehen sollen, nennt die KI drei Unternehmen. Mr. Picked sorgt dafür, dass Ihres dabei ist — in 6 Sprachen. Gratis KI-Check."),
 'HU': ("Mr. Picked — Ajánljon az AI | AI- és Google-láthatóság helyi vállalkozásoknak", "Amikor az ügyfelek megkérdezik a ChatGPT-t, a Geminit vagy a Perplexityt, kit hívjanak vagy hova menjenek, az AI három vállalkozást nevez meg. A Mr. Picked gondoskodik róla, hogy az Öné köztük legyen — 6 nyelven. Ingyenes AI-ellenőrzés."),
}
META_IND = {
 'hospitality': {
  'EN': ("Mr. Picked for restaurants, hotels & apartments — get recommended by AI", "When guests ask ChatGPT, Gemini or Perplexity where to eat or stay, AI names three places. Mr. Picked makes sure yours is one of them — in 6 languages. Free AI check."),
  'SL': ("Mr. Picked za restavracije, hotele in apartmaje — naj vas priporoči AI", "Ko gostje vprašajo ChatGPT, Gemini ali Perplexity, kje jesti ali spati, AI imenuje tri lokale. Mr. Picked poskrbi, da je vaš med njimi — v 6 jezikih. Brezplačen AI pregled.")},
 'towing': {
  'EN': ("Mr. Picked for towing & roadside assistance — be the number AI gives", "When a driver asks ChatGPT, Gemini or Google for a towing service, AI names one or two companies. Mr. Picked makes sure yours is one of them. Free AI check."),
  'SL': ("Mr. Picked za avtovleko in pomoč na cesti — bodite številka, ki jo da AI", "Ko voznik vpraša ChatGPT, Gemini ali Google za vlečno službo, AI imenuje eno ali dve podjetji. Mr. Picked poskrbi, da je vaše med njimi. Brezplačen AI pregled.")},
 'insurance': {
  'EN': ("Mr. Picked for insurance agents — be the agent AI recommends", "When someone asks ChatGPT, Gemini or Google which insurance agent to trust, AI names two or three. Mr. Picked makes sure you are one of them. Free AI check."),
  'SL': ("Mr. Picked za zavarovalne zastopnike — bodite zastopnik, ki ga priporoči AI", "Ko nekdo vpraša ChatGPT, Gemini ali Google, kateremu zavarovalnemu zastopniku zaupati, AI imenuje dva ali tri. Mr. Picked poskrbi, da ste vi med njimi. Brezplačen AI pregled.")},
}

# Score line in the live preview ("3 of 30 … questions")
for _L, _v in {'EN': "of 30 customer questions", 'SL': "od 30 vprašanj strank", 'HR': "od 30 pitanja klijenata",
               'IT': "su 30 domande dei clienti", 'DE': "von 30 Kundenfragen", 'HU': "/ 30 ügyfélkérdés"}.items():
    GEN[_L]['dOf'] = _v
IND['towing']['EN']['dOf'] = "of 30 driver questions"
IND['towing']['SL']['dOf'] = "od 30 vprašanj voznikov"
IND['insurance']['EN']['dOf'] = "of 30 client questions"
IND['insurance']['SL']['dOf'] = "od 30 vprašanj strank"

# ---------------------------------------------------------------------------
# Apartments & dental clinics (EN + SL); hospitality narrowed to restaurants & hotels.

IND['hospitality']['EN']['eyebrow'] = "AI + Google visibility for restaurants & hotels"
IND['hospitality']['SL']['eyebrow'] = "AI + Google vidnost za restavracije in hotele"
META_IND['hospitality']['EN'] = ("Mr. Picked for restaurants & hotels — get recommended by AI", META_IND['hospitality']['EN'][1])
META_IND['hospitality']['SL'] = ("Mr. Picked za restavracije in hotele — naj vas priporoči AI", META_IND['hospitality']['SL'][1])

IND['apartments'] = {
 'EN': dict(
  eyebrow="AI + Google visibility for apartments & holiday rentals",
  h1="Your next guest won’t scroll Airbnb. They’ll ask AI where to stay.",
  sub="When travellers ask ChatGPT, Gemini or Perplexity for a place to stay, AI names only a few. We make sure yours is one of them — with a link to book you directly, without platform commission.",
  dName="Property name", dNamePh="e.g. Apartments Primer", dQ="{city}: nice apartment for 2 nights, close to the centre, with parking?",
  dYour="Your apartments", dOther="Another apartment", dIdle="Enter your property and press run to see what AI tells a traveller.",
  dDesc="Self check-in, free parking, best price when you book directly.", dOf="of 30 traveller questions",
  steps=[
   dict(tab="AI Mirror", h="We ask the AIs about you", p="We run the questions travellers actually ask across ChatGPT, Gemini, Perplexity and Google’s AI answers — in their own languages.", items=["30 traveller questions in 6 languages","Where you appear — and which places appear instead","Wrong prices, locations or rules the AI gives about you"]),
   dict(tab="Fix", h="We make you readable", p="In the first 30 days we fix everything AI and Google read about you.", items=["Google profile, photos, amenities, location and check-in times","Listings corrected on 15+ platforms, consistent with Airbnb and Booking","A direct booking page AI can read: prices, availability, house rules"]),
   dict(tab="Stay picked", h="We keep you there", p="Every month we re-run the questions, add fresh content and report what changed.", items=["Monthly Mr. Picked Report with your visibility score","AI videos and Google posts every month","Review request after every stay"])],
  vidP="No filming. Our AI turns photos of your rooms, view and surroundings into short clips that make travellers want to book.",
  vids=[dict(h="From your real photos", p="Your rooms, your view and your neighbourhood, never stock footage. You approve every clip."), dict(h="One video, six languages", p="Every guest hears it in their own language."), dict(h="Posted where it counts", p="Instagram, TikTok, YouTube Shorts and your Google profile.")],
  lists=[
   ["Starting AI audit: 30 traveller questions in 3 AIs and 6 languages","Full fix in the first 30 days: Google profile, photos, amenities, location, check-in times","Prices, amenities and house rules machine-readable on your website","Listings corrected on 15+ platforms (Apple Maps, Bing, travel directories…)","Local Google SEO: tracked Maps ranking for your 10 key searches (e.g. “apartment Piran with parking”)","4 Google profile posts per month","Monthly Mr. Picked Report with your visibility score"],
   ["Everything in Visible, plus:","2 AI videos / month in 3 languages, posted to Instagram, TikTok and Google","Automatic review request after every stay","We draft replies to all your Google reviews within 48 h","2 new traveller-question pages / month in 3 languages (e.g. “where to park in the old town”)","50 traveller questions tracked + 3 nearby competitors","Quarterly results call"],
   ["Everything in Recommended, plus:","4 AI videos / month in 6 languages","WhatsApp concierge 24/7: answers guests about check-in, parking, Wi-Fi and house rules, and takes direct booking requests","Arrival instructions and check-out reminders sent automatically","House rules and a local guide online in 6 languages","One seasonal campaign per quarter (summer, holidays, off-season deals…)","Monthly strategy call + changes within 24 h (working days)"]],
  addons=[dict(name="AI video pack", desc="+3 AI videos every month"), dict(name="Review loop", desc="Review request after every stay"), dict(name="WhatsApp concierge", desc="Answers guests and takes direct booking requests, 24/7"), dict(name="AI-ready website", desc="Multilingual, fast, readable by AI")],
  roiSpend="Average value of a direct booking", roiGuests="Extra direct bookings per week", roiBreak="Mr. Picked pays for itself at {n} extra direct bookings a week.",
  fdH="Built by an apartment host, not an agency.",
  fdP="I rent out several apartments myself. I know what it’s like to answer guests at midnight and pay platform commission on every booking — so I built Mr. Picked for my own apartments first.",
  faqs=[dict(q="What is GEO, in plain words?", a="Making sure AI assistants like ChatGPT, Gemini and Perplexity know your apartments, describe them correctly and recommend them. It builds on local SEO, so you also rank better on Google."),
   dict(q="Does this replace Airbnb and Booking?", a="No, keep them. We make sure AI also recommends you directly, so more guests book through your own page or WhatsApp, without commission."), 1,
   dict(q="What does the WhatsApp concierge answer?", a="Check-in and check-out times, parking, Wi-Fi, house rules, directions and local tips, in the guest’s language. Anything unusual it passes to you."), 4],
  fBiz="Property name", mailPh="you@apartments.si"),
 'SL': dict(
  eyebrow="AI + Google vidnost za apartmaje in turistične sobe",
  h1="Vaš naslednji gost ne bo brskal po Airbnbju. Vprašal bo AI, kje prespati.",
  sub="Ko popotniki vprašajo ChatGPT, Gemini ali Perplexity za prenočišče, AI imenuje le nekaj mest. Poskrbimo, da je vaše med njimi — s povezavo za neposredno rezervacijo, brez provizije platform.",
  dName="Ime nastanitve", dNamePh="npr. Apartmaji Primer", dQ="{city}: lep apartma za 2 noči blizu centra, s parkiriščem?",
  dYour="Vaši apartmaji", dOther="Druga nastanitev", dIdle="Vpišite svojo nastanitev in zaženite, da vidite, kaj AI pove popotniku.",
  dDesc="Samostojna prijava, brezplačno parkiranje, najboljša cena ob neposredni rezervaciji.", dOf="od 30 vprašanj popotnikov",
  steps=[
   dict(tab="AI Mirror", h="AI vprašamo o vas", p="Postavimo vprašanja, ki jih popotniki res sprašujejo, v ChatGPT, Gemini, Perplexity in Googlovih AI odgovorih — v njihovih jezikih.", items=["30 vprašanj popotnikov v 6 jezikih","Kje se pojavite vi — in katere nastanitve namesto vas","Napačne cene, lokacije ali pravila, ki jih AI navaja o vas"]),
   dict(tab="Popravek", h="Poskrbimo, da vas AI razume", p="V prvih 30 dneh popravimo vse, kar AI in Google bereta o vas.", items=["Google profil, fotografije, oprema, lokacija in časi prihoda","Popravljeni vpisi na 15+ platformah, usklajeni z Airbnbjem in Bookingom","Stran za neposredne rezervacije, ki jo AI prebere: cene, razpoložljivost, hišni red"]),
   dict(tab="Ostanite izbrani", h="Obdržimo vas tam", p="Vsak mesec ponovno postavimo vprašanja, dodamo svežo vsebino in poročamo, kaj se je spremenilo.", items=["Mesečno poročilo Mr. Picked z oceno vidnosti","AI videi in Google objave vsak mesec","Prošnja za oceno po vsakem bivanju"])],
  vidP="Brez snemanja. Naš AI iz fotografij sob, razgleda in okolice ustvari kratke posnetke, zaradi katerih popotniki želijo rezervirati.",
  vids=[dict(h="Iz vaših pravih fotografij", p="Vaše sobe, vaš razgled in vaša soseska, nikoli tuji posnetki. Vsak posnetek odobrite."), dict(h="En video, šest jezikov", p="Vsak gost ga sliši v svojem jeziku."), dict(h="Objavljeno tam, kjer šteje", p="Instagram, TikTok, YouTube Shorts in vaš Google profil.")],
  lists=[
   ["Začetni AI pregled: 30 vprašanj popotnikov v 3 AI orodjih in 6 jezikih","Celoten popravek v prvih 30 dneh: Google profil, fotografije, oprema, lokacija, časi prihoda","Cene, oprema in hišni red strojno berljivi na vaši spletni strani","Popravljeni vpisi na 15+ platformah (Apple Maps, Bing, turistični imeniki …)","Lokalni Google SEO: spremljamo mesto na Zemljevidih za 10 ključnih iskanj (npr. »apartma Piran s parkiriščem«)","4 objave na Google profilu na mesec","Mesečno poročilo Mr. Picked z oceno vidnosti"],
   ["Vse iz paketa Visible, plus:","2 AI videa na mesec v 3 jezikih, objavljena na Instagramu, TikToku in Googlu","Samodejna prošnja za oceno po vsakem bivanju","Pripravimo odgovore na vse vaše Google ocene v 48 urah","2 novi strani z vprašanji popotnikov na mesec v 3 jezikih (npr. »kje parkirati v starem mestnem jedru«)","Spremljanje 50 vprašanj popotnikov + 3 bližnjih konkurentov","Četrtletni pregled rezultatov"],
   ["Vse iz paketa Recommended, plus:","4 AI videi na mesec v 6 jezikih","WhatsApp concierge 24/7: odgovarja gostom o prihodu, parkiranju, Wi-Fi in hišnem redu ter sprejema povpraševanja za neposredne rezervacije","Navodila za prihod in opomniki za odhod se pošljejo samodejno","Hišni red in lokalni vodič na spletu v 6 jezikih","Ena sezonska kampanja na četrtletje (poletje, prazniki, ponudbe izven sezone …)","Mesečni strateški sestanek + spremembe v 24 urah (delovni dnevi)"]],
  addons=[dict(name="AI video paket", desc="+3 AI videi vsak mesec"), dict(name="Zbiranje ocen", desc="Prošnja za oceno po vsakem bivanju"), dict(name="WhatsApp concierge", desc="Odgovarja gostom in sprejema povpraševanja za rezervacije, 24/7"), dict(name="Spletna stran za AI", desc="Večjezična, hitra, berljiva za AI")],
  roiSpend="Povprečna vrednost neposredne rezervacije", roiGuests="Dodatne neposredne rezervacije na teden", roiBreak="Mr. Picked se poplača že pri {n} dodatnih neposrednih rezervacijah na teden.",
  fdH="Naredil ga je gostitelj apartmajev, ne agencija.",
  fdP="Tudi sam oddajam več apartmajev. Vem, kako je odgovarjati gostom ob polnoči in plačevati provizijo za vsako rezervacijo — zato sem Mr. Picked najprej naredil za svoje apartmaje.",
  faqs=[dict(q="Kaj je GEO, preprosto povedano?", a="Poskrbimo, da AI pomočniki, kot so ChatGPT, Gemini in Perplexity, poznajo vaše apartmaje, jih pravilno opišejo in priporočijo. Gradi na lokalnem SEO, zato ste višje tudi na Googlu."),
   dict(q="Ali to nadomesti Airbnb in Booking?", a="Ne, obdržite ju. Poskrbimo, da vas AI priporoči tudi neposredno, zato več gostov rezervira prek vaše strani ali WhatsAppa, brez provizije."), 1,
   dict(q="Na kaj odgovarja WhatsApp concierge?", a="Na čas prihoda in odhoda, parkiranje, Wi-Fi, hišni red, navodila za pot in lokalne nasvete, v jeziku gosta. Kar je neobičajno, preda vam."), 4],
  fBiz="Ime nastanitve", mailPh="vi@apartmaji.si"),
}

IND['dental'] = {
 'EN': dict(
  eyebrow="AI + Google visibility for dentists & aesthetic clinics",
  h1="Your next patient won’t ask a friend. They’ll ask AI which clinic to trust.",
  sub="When someone asks ChatGPT, Gemini or Perplexity for a good dentist or implant clinic — at home or from Italy and Austria — AI names two or three. We make sure your clinic is one of them, in your patients’ language.",
  dName="Clinic name", dNamePh="e.g. Dental Clinic Primer", dQ="{city}: which dental clinic would you recommend for implants?",
  dYour="Your clinic", dOther="Another clinic", dIdle="Enter your clinic and press run to see what AI tells a patient.",
  dDesc="Experienced team, transparent prices, appointments this week.", dOf="of 30 patient questions",
  steps=[
   dict(tab="AI Mirror", h="We ask the AIs about you", p="We run the questions patients actually ask before they choose a clinic, across ChatGPT, Gemini, Perplexity and Google’s AI answers.", items=["30 patient questions in 6 languages","Where you appear — and which clinics appear instead","Wrong hours, treatments or prices the AI gives about you"]),
   dict(tab="Fix", h="We make you readable", p="In the first 30 days we fix everything AI and Google read about you.", items=["Google profile: treatments, hours, team, photos, accessibility","Listings corrected on 15+ platforms and health directories","Treatments, price ranges and booking info machine-readable on your site"]),
   dict(tab="Stay picked", h="We keep you there", p="Every month we re-run the questions, add fresh content and report what changed.", items=["Monthly Mr. Picked Report with your visibility score","AI videos and Google posts every month","Review request after every completed treatment"])],
  vidP="No filming. Our AI turns photos of your clinic and team into short, calm clips that explain treatments and build trust before the first visit.",
  vids=[dict(h="From your real photos", p="Your clinic, your team and your equipment, never stock footage. You approve every clip."), dict(h="One video, six languages", p="Patients from Italy, Austria or Croatia hear it in their own language."), dict(h="Posted where it counts", p="Instagram, TikTok, YouTube Shorts and your Google profile.")],
  lists=[
   ["Starting AI audit: 30 patient questions in 3 AIs and 6 languages","Full fix in the first 30 days: Google profile, treatments, hours, team, photos","Treatments, price ranges and booking info machine-readable on your website","Listings corrected on 15+ platforms (Apple Maps, Bing, health directories…)","Local Google SEO: tracked Maps ranking for your 10 key searches (e.g. “dental implants Ljubljana”)","4 Google profile posts per month","Monthly Mr. Picked Report with your visibility score"],
   ["Everything in Visible, plus:","2 AI explainer videos / month in 3 languages, posted to Instagram, TikTok and Google","Automatic review request after every completed treatment","We draft replies to all your Google reviews within 48 h","2 new patient-question pages / month in 3 languages (e.g. “how long does an implant take”)","50 patient questions tracked + 3 nearby competitors","Quarterly results call"],
   ["Everything in Recommended, plus:","4 AI videos / month in 6 languages","WhatsApp concierge 24/7: answers questions about treatments, prices and hours, and takes appointment requests","Appointment reminders & no-show follow-up","Treatments and price list online in 6 languages, for patients from abroad","One seasonal campaign per quarter (check-ups before summer, whitening before the holidays…)","Monthly strategy call + changes within 24 h (working days)"]],
  addons=[dict(name="AI video pack", desc="+3 AI videos every month"), dict(name="Review loop", desc="Review request after every completed treatment"), dict(name="WhatsApp concierge", desc="Answers patients and takes appointment requests, 24/7"), dict(name="AI-ready website", desc="Multilingual, fast, readable by AI")],
  roiSpend="Average value of a new patient", roiGuests="Extra new patients per week", roiBreak="Mr. Picked pays for itself at {n} extra new patients a week.",
  fdH=GEN['EN']['fdH'], fdP=GEN['EN']['fdP'],
  faqs=[dict(q="What is GEO, in plain words?", a="Making sure AI assistants like ChatGPT, Gemini and Perplexity know your clinic, describe it correctly and recommend it. It builds on local SEO, so you also rank better on Google."),
   dict(q="Can we show prices and treatments?", a="Yes, within the rules for advertising health services. We publish factual information: treatments, price ranges, team and hours. No promised results, and no before-and-after material without your approval."), 1,
   dict(q="Will the WhatsApp concierge give medical advice?", a="No. It answers practical questions about hours, prices, location and the treatments you offer, and takes appointment requests. Medical questions always go to your team."), 4],
  fBiz="Clinic name", mailPh="you@clinic.si"),
 'SL': dict(
  eyebrow="AI + Google vidnost za zobozdravnike in estetske klinike",
  h1="Vaš naslednji pacient ne bo vprašal prijatelja. Vprašal bo AI, kateri ambulanti zaupati.",
  sub="Ko nekdo vpraša ChatGPT, Gemini ali Perplexity za dobrega zobozdravnika ali kliniko za vsadke — doma ali iz Italije in Avstrije — AI imenuje dve ali tri. Poskrbimo, da je vaša med njimi, v jeziku vaših pacientov.",
  dName="Ime ambulante", dNamePh="npr. Zobna ambulanta Primer", dQ="{city}: katero zobno ambulanto priporočaš za vsadke?",
  dYour="Vaša ambulanta", dOther="Druga ambulanta", dIdle="Vpišite svojo ambulanto in zaženite, da vidite, kaj AI pove pacientu.",
  dDesc="Izkušena ekipa, pregledne cene, termini še ta teden.", dOf="od 30 vprašanj pacientov",
  steps=[
   dict(tab="AI Mirror", h="AI vprašamo o vas", p="Postavimo vprašanja, ki jih pacienti res postavljajo, preden izberejo ambulanto, v ChatGPT, Gemini, Perplexity in Googlovih AI odgovorih.", items=["30 vprašanj pacientov v 6 jezikih","Kje se pojavite vi — in katere ambulante namesto vas","Napačne ure, storitve ali cene, ki jih AI navaja o vas"]),
   dict(tab="Popravek", h="Poskrbimo, da vas AI razume", p="V prvih 30 dneh popravimo vse, kar AI in Google bereta o vas.", items=["Google profil: storitve, delovni čas, ekipa, fotografije, dostopnost","Popravljeni vpisi na 15+ platformah in zdravstvenih imenikih","Storitve, cenovni razponi in naročanje strojno berljivi na vaši strani"]),
   dict(tab="Ostanite izbrani", h="Obdržimo vas tam", p="Vsak mesec ponovno postavimo vprašanja, dodamo svežo vsebino in poročamo, kaj se je spremenilo.", items=["Mesečno poročilo Mr. Picked z oceno vidnosti","AI videi in Google objave vsak mesec","Prošnja za oceno po vsakem zaključenem zdravljenju"])],
  vidP="Brez snemanja. Naš AI iz fotografij vaše ambulante in ekipe ustvari kratke, mirne posnetke, ki razložijo posege in zgradijo zaupanje še pred prvim obiskom.",
  vids=[dict(h="Iz vaših pravih fotografij", p="Vaša ambulanta, ekipa in oprema, nikoli tuji posnetki. Vsak posnetek odobrite."), dict(h="En video, šest jezikov", p="Pacienti iz Italije, Avstrije ali Hrvaške ga slišijo v svojem jeziku."), dict(h="Objavljeno tam, kjer šteje", p="Instagram, TikTok, YouTube Shorts in vaš Google profil.")],
  lists=[
   ["Začetni AI pregled: 30 vprašanj pacientov v 3 AI orodjih in 6 jezikih","Celoten popravek v prvih 30 dneh: Google profil, storitve, delovni čas, ekipa, fotografije","Storitve, cenovni razponi in naročanje strojno berljivi na vaši spletni strani","Popravljeni vpisi na 15+ platformah (Apple Maps, Bing, zdravstveni imeniki …)","Lokalni Google SEO: spremljamo mesto na Zemljevidih za 10 ključnih iskanj (npr. »zobni vsadki Ljubljana«)","4 objave na Google profilu na mesec","Mesečno poročilo Mr. Picked z oceno vidnosti"],
   ["Vse iz paketa Visible, plus:","2 AI razlagalna videa na mesec v 3 jezikih, objavljena na Instagramu, TikToku in Googlu","Samodejna prošnja za oceno po vsakem zaključenem zdravljenju","Pripravimo odgovore na vse vaše Google ocene v 48 urah","2 novi strani z vprašanji pacientov na mesec v 3 jezikih (npr. »kako dolgo traja vsadek«)","Spremljanje 50 vprašanj pacientov + 3 bližnjih konkurentov","Četrtletni pregled rezultatov"],
   ["Vse iz paketa Recommended, plus:","4 AI videi na mesec v 6 jezikih","WhatsApp concierge 24/7: odgovarja na vprašanja o storitvah, cenah in delovnem času ter sprejema prošnje za termin","Opomniki za termine in sledenje neprihodom","Storitve in cenik na spletu v 6 jezikih, za paciente iz tujine","Ena sezonska kampanja na četrtletje (pregledi pred poletjem, beljenje pred prazniki …)","Mesečni strateški sestanek + spremembe v 24 urah (delovni dnevi)"]],
  addons=[dict(name="AI video paket", desc="+3 AI videi vsak mesec"), dict(name="Zbiranje ocen", desc="Prošnja za oceno po vsakem zaključenem zdravljenju"), dict(name="WhatsApp concierge", desc="Odgovarja pacientom in sprejema prošnje za termin, 24/7"), dict(name="Spletna stran za AI", desc="Večjezična, hitra, berljiva za AI")],
  roiSpend="Povprečna vrednost novega pacienta", roiGuests="Dodatni novi pacienti na teden", roiBreak="Mr. Picked se poplača že pri {n} dodatnih novih pacientih na teden.",
  fdH=GEN['SL']['fdH'], fdP=GEN['SL']['fdP'],
  faqs=[dict(q="Kaj je GEO, preprosto povedano?", a="Poskrbimo, da AI pomočniki, kot so ChatGPT, Gemini in Perplexity, poznajo vašo ambulanto, jo pravilno opišejo in priporočijo. Gradi na lokalnem SEO, zato ste višje tudi na Googlu."),
   dict(q="Ali lahko objavimo cene in posege?", a="Da, v okviru pravil za oglaševanje zdravstvenih storitev. Objavljamo dejanske podatke: storitve, cenovne razpone, ekipo in delovni čas. Brez obljub rezultatov in brez fotografij pred in po brez vašega soglasja."), 1,
   dict(q="Ali WhatsApp concierge daje zdravniške nasvete?", a="Ne. Odgovarja na praktična vprašanja o urah, cenah, lokaciji in storitvah, ki jih ponujate, ter sprejema prošnje za termin. Zdravstvena vprašanja vedno preda vaši ekipi."), 4],
  fBiz="Ime ambulante", mailPh="vi@ambulanta.si"),
}

ROI['apartments'] = ((300, 50, 1500, 10), (2, 0, 30, 1))
ROI['dental'] = ((400, 100, 3000, 50), (2, 0, 20, 1))
IND_PATH['apartments'] = {'EN': 'apartments/', 'SL': 'sl/apartmaji/'}
IND_PATH['dental'] = {'EN': 'dental/', 'SL': 'sl/zobozdravniki/'}
META_IND['apartments'] = {
 'EN': ("Mr. Picked for apartments & holiday rentals — more direct bookings from AI", "When travellers ask ChatGPT, Gemini or Perplexity where to stay, AI names only a few places. Mr. Picked makes sure yours is one of them, with a direct booking link. Free AI check."),
 'SL': ("Mr. Picked za apartmaje in turistične sobe — več neposrednih rezervacij prek AI", "Ko popotniki vprašajo ChatGPT, Gemini ali Perplexity, kje prespati, AI imenuje le nekaj mest. Mr. Picked poskrbi, da je vaše med njimi, s povezavo za neposredno rezervacijo. Brezplačen AI pregled.")}
META_IND['dental'] = {
 'EN': ("Mr. Picked for dentists & aesthetic clinics — be the clinic AI recommends", "When patients ask ChatGPT, Gemini or Google which dental clinic to trust, AI names two or three. Mr. Picked makes sure yours is one of them, in 6 languages. Free AI check."),
 'SL': ("Mr. Picked za zobozdravnike in estetske klinike — bodite ambulanta, ki jo priporoči AI", "Ko pacienti vprašajo ChatGPT, Gemini ali Google, kateri zobni ambulanti zaupati, AI imenuje dve ali tri. Mr. Picked poskrbi, da je vaša med njimi, v 6 jezikih. Brezplačen AI pregled.")}

# Industry cards on the main pages, in this order; the first five link to their pages.
IND_ORDER = ['hospitality', 'apartments', 'towing', 'insurance', 'dental']
_cards = {
 'EN': [("Restaurants & hotels", "Get picked when guests ask where to eat or stay."), ("Apartments & holiday rentals", "More direct bookings, fewer commissions, guests answered 24/7."), ("Towing & roadside assistance", "Be the number AI gives when a car breaks down."), ("Insurance agents", "Be the agent AI recommends for car, home and travel insurance."), ("Dentists & aesthetic clinics", "Be the clinic AI recommends, in your patients’ language."), ("Trades, car repair & more", "Plumbers, electricians, mechanics, salons and professional services.")],
 'SL': [("Restavracije in hoteli", "Da vas izberejo, ko gostje vprašajo, kje jesti ali spati."), ("Apartmaji in turistične sobe", "Več neposrednih rezervacij, manj provizij, odgovori gostom 24/7."), ("Avtovleka in pomoč na cesti", "Bodite številka, ki jo AI da, ko se avto pokvari."), ("Zavarovalniški zastopniki", "Bodite zastopnik, ki ga AI priporoči za avto, dom in potovanja."), ("Zobozdravniki in estetske klinike", "Bodite ambulanta, ki jo AI priporoči, v jeziku vaših pacientov."), ("Obrtniki, avtoservisi in drugi", "Vodovodarji, električarji, mehaniki, saloni in strokovne storitve.")],
 'HR': [("Restorani i hoteli", "Da vas odaberu kad gosti pitaju gdje jesti ili spavati."), ("Apartmani i sobe za iznajmljivanje", "Više izravnih rezervacija, manje provizija, odgovori gostima 24/7."), ("Vuča vozila i pomoć na cesti", "Budite broj koji AI daje kad se auto pokvari."), ("Zastupnici osiguranja", "Budite zastupnik kojeg AI preporuča za auto, dom i putovanja."), ("Stomatolozi i estetske klinike", "Budite ordinacija koju AI preporuča, na jeziku vaših pacijenata."), ("Obrtnici, autoservisi i ostali", "Vodoinstalateri, električari, mehaničari, saloni i stručne usluge.")],
 'IT': [("Ristoranti e hotel", "Fatti scegliere quando gli ospiti chiedono dove mangiare o dormire."), ("Appartamenti e case vacanza", "Più prenotazioni dirette, meno commissioni, ospiti seguiti 24/7."), ("Soccorso stradale", "Sii il numero che l’AI dà quando un’auto si guasta."), ("Agenti assicurativi", "Sii l’agente che l’AI consiglia per auto, casa e viaggi."), ("Dentisti e cliniche estetiche", "Sii lo studio che l’AI consiglia, nella lingua dei tuoi pazienti."), ("Artigiani, officine e altri", "Idraulici, elettricisti, meccanici, saloni e servizi professionali.")],
 'DE': [("Restaurants & Hotels", "Gewählt werden, wenn Gäste fragen, wo sie essen oder schlafen sollen."), ("Ferienwohnungen & Apartments", "Mehr Direktbuchungen, weniger Provisionen, Gäste rund um die Uhr betreut."), ("Abschlepp- und Pannendienst", "Die Nummer sein, die die KI bei einer Panne nennt."), ("Versicherungsberater", "Der Berater sein, den die KI für Auto, Haus und Reise empfiehlt."), ("Zahnärzte & Ästhetikkliniken", "Die Praxis sein, die die KI empfiehlt — in der Sprache Ihrer Patienten."), ("Handwerk, Kfz & mehr", "Installateure, Elektriker, Werkstätten, Salons und freie Berufe.")],
 'HU': [("Éttermek és szállodák", "Válasszák Önt, amikor a vendégek azt kérdezik, hol egyenek vagy aludjanak."), ("Apartmanok és szálláshelyek", "Több közvetlen foglalás, kevesebb jutalék, vendégválasz 0–24."), ("Autómentés és segélyszolgálat", "Legyen az a szám, amit az AI ad, ha lerobban az autó."), ("Biztosítási tanácsadók", "Legyen az a tanácsadó, akit az AI ajánl autóra, otthonra és utazásra."), ("Fogorvosok és esztétikai klinikák", "Legyen az a rendelő, amelyet az AI ajánl, a páciensei nyelvén."), ("Szakiparosok, autószervizek és mások", "Vízszerelők, villanyszerelők, szerelők, szalonok és szakmai szolgáltatók.")],
}
for _L, _c in _cards.items():
    GEN[_L]['inds'] = [dict(name=n, desc=d) for n, d in _c]

# Break-even line phrased so it reads correctly for any number (1, 2, 5 …)
_BRK = {
 'main': {'EN': "Extra customers a week to cover Mr. Picked: {n}", 'SL': "Dodatne stranke na teden, ki pokrijejo Mr. Picked: {n}",
          'HR': "Dodatni klijenti tjedno koji pokrivaju Mr. Picked: {n}", 'IT': "Clienti in più a settimana per coprire Mr. Picked: {n}",
          'DE': "Zusätzliche Kunden pro Woche, um Mr. Picked zu decken: {n}", 'HU': "Ennyi plusz ügyfél hetente fedezi a Mr. Pickedet: {n}"},
 'hospitality': {'EN': "Extra guests a week to cover Mr. Picked: {n}", 'SL': "Dodatni gostje na teden, ki pokrijejo Mr. Picked: {n}"},
 'towing': {'EN': "Extra calls a week to cover Mr. Picked: {n}", 'SL': "Dodatni klici na teden, ki pokrijejo Mr. Picked: {n}"},
 'insurance': {'EN': "Extra clients a week to cover Mr. Picked: {n}", 'SL': "Dodatne stranke na teden, ki pokrijejo Mr. Picked: {n}"},
 'apartments': {'EN': "Extra direct bookings a week to cover Mr. Picked: {n}", 'SL': "Dodatne neposredne rezervacije na teden, ki pokrijejo Mr. Picked: {n}"},
 'dental': {'EN': "Extra new patients a week to cover Mr. Picked: {n}", 'SL': "Dodatni novi pacienti na teden, ki pokrijejo Mr. Picked: {n}"},
}
for _v, _m in _BRK.items():
    for _L, _s in _m.items():
        (GEN[_L] if _v == 'main' else IND[_v][_L])['roiBreak'] = _s
