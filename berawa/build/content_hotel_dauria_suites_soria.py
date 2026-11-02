# Contenido de la demo Dauria Suites (Soria) (es/en/fr/de). Hechos de dauriasoria.es leidos el 02/11/2026 (ver berawa/sources.json). Sin valoraciones; sin precios.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran el alojamiento real.','en':' Images are illustrations and do not show the actual property.','fr':' Les images sont des illustrations et ne montrent pas l’établissement réel.','de':' Die Bilder sind Illustrationen und zeigen nicht die tatsächliche Unterkunft.'}
H={'es':['Suites: estándar, con terraza y con jardín','Apartamentos de 1 y 2 dormitorios'],'en':['Suites: standard, with terrace and with garden','One- and two-bedroom apartments'],'fr':['Suites : standard, avec terrasse et avec jardin','Appartements d’une et deux chambres'],'de':['Suiten: Standard, mit Terrasse und mit Garten','Apartments mit einem und zwei Schlafzimmern']}
RD={
'es':['La suite estándar (36 m², 1-2 personas) integra dormitorio, salón y cocina; las suites con terraza (40 m²) y con jardín (41 m², jardín de 35 m² con pérgola) acogen hasta 4 personas.','El apartamento de 1 dormitorio (40 m², hasta 4 personas) tiene el dormitorio separado; el de 2 dormitorios (60 m², hasta 6 personas) suma dos baños y lavavajillas.'],
'en':['The standard suite (36 m², 1-2 guests) combines bedroom, living room and kitchen; the suites with terrace (40 m²) and with garden (41 m², 35 m² garden with pergola) sleep up to 4.','The one-bedroom apartment (40 m², up to 4 guests) has a separate bedroom; the two-bedroom one (60 m², up to 6 guests) adds two bathrooms and a dishwasher.'],
'fr':['La suite standard (36 m², 1-2 personnes) réunit chambre, salon et cuisine ; les suites avec terrasse (40 m²) et avec jardin (41 m², jardin de 35 m² avec pergola) accueillent jusqu’à 4 personnes.','L’appartement d’une chambre (40 m², jusqu’à 4 personnes) a une chambre séparée ; celui de deux chambres (60 m², jusqu’à 6 personnes) ajoute deux salles de bain et un lave-vaisselle.'],
'de':['Die Standard-Suite (36 m², 1-2 Personen) vereint Schlafzimmer, Wohnzimmer und Küche; die Suiten mit Terrasse (40 m²) und mit Garten (41 m², 35 m² Garten mit Pergola) bieten Platz für bis zu 4 Personen.','Das Apartment mit einem Schlafzimmer (40 m², bis zu 4 Personen) hat ein separates Schlafzimmer; das mit zwei Schlafzimmern (60 m², bis zu 6 Personen) bietet zwei Bäder und eine Spülmaschine.']}
ART={
'hero':('hills',4201,['#1e2a22','#c58b4c','#f0cf9a','#5f7a52','#435a3a','#26341f']),
'intro':('arches',4202,['#f2ede4','#faf7f0','#8a6a3c','#5e4828','#2e2414']),
'r1':('columns',4211,['#efe9de','#c79858','#8a6a3c','#5e4828','#2e2414']),
'r2':('hills',4212,['#ece7da','#f0e0c0','#c99a5a','#8fa07a','#667a56','#46563a']),
'g1':('hills',4221,['#1e2a22','#c58b4c','#f0cf9a','#5f7a52','#435a3a','#26341f']),
'g2':('arches',4222,['#f0ebe2','#f9f5ee','#946f40','#64492a','#302414']),
'g3':('waves',4223,['#1e2a22','#c9925a','#f2d6a8','#6a8460','#4a6040','#2a3822']),
'g4':('skyline',4224,['#1e2a22','#c58b4c','#f0cf9a','#5f7a52','#435a3a','#26341f'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Dauria Suites · Apartamentos en el centro de Soria',see_rooms='Ver los apartamentos',nav_rooms='Apartamentos',hero_k='Soria · Ronda Eloy Sanz Villa, 2 bis',hero_t='Soria: relax en verde y siena',hero_s='22 amplios apartamentos de cuidado diseño junto al Parque de la Dehesa.',
 intro_t='En el antiguo convento de San Francisco',intro_p1='En pleno centro de Soria, junto al Parque de la Dehesa y dentro del recinto del antiguo convento de San Francisco, un lugar con siglos de arte e historia.',
 intro_p2='La Soria literaria de Bécquer y Machado, la natural que nace con el Duero, la histórica y la gastronómica: todas se descubren desde aquí.',
 stats=['22 apartamentos','De 36 a 60 m²','Limpieza diaria','Wifi gratuito'],rooms_t='Suites y apartamentos',rooms_s='Todos con cocina completa con menaje y electrodomésticos, baño con cabina de ducha, A/A frío/calor y Smart TV.',
 svcs=['Limpieza diaria','Wifi gratuito en todo el hotel','Adaptado para movilidad reducida','Café de cortesía','Lavadoras y secadoras en zonas comunes','Cocina completa en cada apartamento'],
 around_s='San Juan de Duero, el paseo de San Polo a San Saturio, el Palacio de los Condes de Gómara y el Parque de la Dehesa, a dos minutos a pie.',
 loc_p='Ronda Eloy Sanz Villa, 2 bis · 42003 Soria, en pleno centro, junto al Parque de la Dehesa.',
 chips=['¿Qué apartamentos tenéis?','¿Hay limpieza diaria?','¿Está adaptado?','¿Cómo reservo?']),
'en':dict(title='Dauria Suites · Apartments in central Soria',see_rooms='See the apartments',nav_rooms='Apartments',hero_k='Soria · Ronda Eloy Sanz Villa, 2 bis',hero_t='Soria: relaxing in green and sienna',hero_s='22 spacious, carefully designed apartments next to the Dehesa Park.',
 intro_t='In the former convent of San Francisco',intro_p1='In the very centre of Soria, next to the Dehesa Park and within the grounds of the former convent of San Francisco, a place with centuries of art and history.',
 intro_p2='The literary Soria of Bécquer and Machado, the natural one born with the Duero, the historic and the gastronomic: all to discover from here.',
 stats=['22 apartments','From 36 to 60 m²','Daily cleaning','Free wifi'],rooms_t='Suites and apartments',rooms_s='All with a full kitchen with utensils and appliances, shower room, hot/cold A/C and Smart TV.',
 svcs=['Daily cleaning','Free wifi throughout','Adapted for reduced mobility','Complimentary coffee','Washers and dryers in common areas','Full kitchen in every apartment'],
 around_s='San Juan de Duero, the walk from San Polo to San Saturio, the Palace of the Counts of Gómara and the Dehesa Park, two minutes’ walk away.',
 loc_p='Ronda Eloy Sanz Villa, 2 bis · 42003 Soria, right in the centre, next to the Dehesa Park.',
 chips=['Which apartments do you have?','Is there daily cleaning?','Is it accessible?','How do I book?']),
'fr':dict(title='Dauria Suites · Appartements au centre de Soria',see_rooms='Voir les appartements',nav_rooms='Appartements',hero_k='Soria · Ronda Eloy Sanz Villa, 2 bis',hero_t='Soria : détente en vert et sienne',hero_s='22 appartements spacieux au design soigné, à côté du parc de la Dehesa.',
 intro_t='Dans l’ancien couvent de San Francisco',intro_p1='En plein centre de Soria, à côté du parc de la Dehesa et dans l’enceinte de l’ancien couvent de San Francisco, un lieu chargé de siècles d’art et d’histoire.',
 intro_p2='La Soria littéraire de Bécquer et Machado, la naturelle née avec le Douro, l’historique et la gastronomique : toutes à découvrir d’ici.',
 stats=['22 appartements','De 36 à 60 m²','Ménage quotidien','Wifi gratuit'],rooms_t='Suites et appartements',rooms_s='Tous avec cuisine complète équipée, salle d’eau avec cabine de douche, climatisation chaud/froid et Smart TV.',
 svcs=['Ménage quotidien','Wifi gratuit partout','Adapté aux personnes à mobilité réduite','Café offert','Lave-linge et sèche-linge dans les parties communes','Cuisine complète dans chaque appartement'],
 around_s='San Juan de Duero, la promenade de San Polo à San Saturio, le palais des comtes de Gómara et le parc de la Dehesa, à deux minutes à pied.',
 loc_p='Ronda Eloy Sanz Villa, 2 bis · 42003 Soria, en plein centre, à côté du parc de la Dehesa.',
 chips=['Quels appartements avez-vous ?','Y a-t-il un ménage quotidien ?','Est-ce adapté ?','Comment réserver ?']),
'de':dict(title='Dauria Suites · Apartments im Zentrum von Soria',see_rooms='Apartments ansehen',nav_rooms='Apartments',hero_k='Soria · Ronda Eloy Sanz Villa, 2 bis',hero_t='Soria: Entspannung in Grün und Siena',hero_s='22 geräumige Apartments mit sorgfältigem Design am Dehesa-Park.',
 intro_t='Im ehemaligen Kloster San Francisco',intro_p1='Mitten im Zentrum von Soria, am Dehesa-Park und auf dem Gelände des ehemaligen Klosters San Francisco, ein Ort mit jahrhundertelanger Kunst und Geschichte.',
 intro_p2='Das literarische Soria von Bécquer und Machado, das natürliche am Duero, das historische und das kulinarische: alles von hier aus zu entdecken.',
 stats=['22 Apartments','Von 36 bis 60 m²','Tägliche Reinigung','Kostenloses WLAN'],rooms_t='Suiten und Apartments',rooms_s='Alle mit voll ausgestatteter Küche, Duschbad, Klimaanlage (warm/kalt) und Smart-TV.',
 svcs=['Tägliche Reinigung','Kostenloses WLAN im ganzen Haus','Barrierearm für eingeschränkte Mobilität','Kaffee gratis','Waschmaschinen und Trockner in Gemeinschaftsbereichen','Komplette Küche in jedem Apartment'],
 around_s='San Juan de Duero, der Spaziergang von San Polo nach San Saturio, der Palast der Grafen von Gómara und der Dehesa-Park, zwei Gehminuten entfernt.',
 loc_p='Ronda Eloy Sanz Villa, 2 bis · 42003 Soria, mitten im Zentrum, am Dehesa-Park.',
 chips=['Welche Apartments gibt es?','Gibt es tägliche Reinigung?','Ist es barrierefrei?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
R='https://booking.roomcloud.net/be/se1/hotel.jsp?hotel=16328&lang='
BOOK=dict(mode='engine',url=dict(es=R+'es',en=R+'en',fr=R+'fr',de=R+'de'))
D=dict(name='Dauria Suites',ac='#1f2a24',ac2='#8a6a3c',ac2_a11y='#6a5028',book=BOOK,around=['San Juan de Duero','San Saturio','Parque de la Dehesa'],foot=FOOT,
 address='Ronda Eloy Sanz Villa, 2 bis · 42003 Soria',phones=['+34 657 757 583','+34 975 044 648'],emails=['reservas@dauriasoria.es'],maps='Dauria Suites, Ronda Eloy Sanz Villa 2 bis, 42003 Soria',t=T)
META=dict(repo='demo-hotel-dauria-suites-soria',name='Dauria Suites',legal_name='DAURIA SUITES S.L. (aviso legal de su web)',registry_ids=['B42201988'],
 url='https://dauriasoria.es/',domain='dauriasoria.es',municipality='Soria',province='Soria',sector='hotel apartamentos en el antiguo convento de San Francisco, centro de Soria',
 read_at='2026-11-02T06:58:00+01:00',created_at='2026-11-02T06:57:00+01:00',built_at='2026-11-02T07:10:00+01:00',audit_date='2026-11-02T06:44:57+01:00',
 rating=dict(value=4.8,coincide=['web'],date='2026-10-29',url='https://www.google.com/maps/place/Dauria+Suites/@41.762631,-2.4712962,17z/data=!4m9!3m8!1s0xd44d3b9eacb2a9f:0x14028faf37a2230d!5m2!4m1!1i2!8m2!3d41.762631!4d-2.4712962!16s%2Fg%2F11t5f29903'),
 book=dict(mode='engine',url=R+'es',note='motor de reservas real enlazado desde su web (RoomCloud, hotel=16328), HTTP 200 comprobado el 02/11/2026 con lang=es, en, fr y de.'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué apartamentos tenéis?','K01'),('¿Cuántos apartamentos hay?','K01'),('¿Tenéis suite con terraza?','K02'),('¿Tenéis apartamento para 6 personas?','K03'),('¿Hay limpieza diaria?','K04'),('¿Hay wifi?','K05'),('¿Está adaptado para movilidad reducida?','K06'),('¿Hay lavadora?','K07'),('¿Tiene cocina?','K08'),('¿Dónde está?','K09'),('¿Qué ver en Soria?','K10'),('¿Cómo reservo?','K11'),('¿Podéis confirmarme disponibilidad para mañana?','K11'),('¿Cuánto cuesta la noche?',None),('¿Tenéis piscina?',None)],
'en':[('Which apartments do you have?','K01'),('How many apartments are there?','K01'),('Do you have a suite with terrace?','K02'),('Do you have an apartment for 6 people?','K03'),('Is there daily cleaning?','K04'),('Is there wifi?','K05'),('Is it adapted for reduced mobility?','K06'),('Is there a washing machine?','K07'),('Does it have a kitchen?','K08'),('Where is it?','K09'),('What to see in Soria?','K10'),('How do I book?','K11'),('Can you confirm availability for tomorrow?','K11'),('How much is a night?',None),('Do you have a swimming pool?',None)],
'fr':[('Quels appartements avez-vous ?','K01'),('Combien d’appartements y a-t-il ?','K01'),('Avez-vous une suite avec terrasse ?','K02'),('Avez-vous un appartement pour 6 personnes ?','K03'),('Y a-t-il un ménage quotidien ?','K04'),('Y a-t-il le wifi ?','K05'),('Est-ce adapté aux personnes à mobilité réduite ?','K06'),('Y a-t-il un lave-linge ?','K07'),('Y a-t-il une cuisine ?','K08'),('Où est-ce ?','K09'),('Que voir à Soria ?','K10'),('Comment réserver ?','K11'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K11'),('Combien coûte la nuit ?',None),('Avez-vous une piscine ?',None)],
'de':[('Welche Apartments gibt es?','K01'),('Wie viele Apartments gibt es?','K01'),('Haben Sie eine Suite mit Terrasse?','K02'),('Haben Sie ein Apartment für 6 Personen?','K03'),('Gibt es tägliche Reinigung?','K04'),('Gibt es WLAN?','K05'),('Ist es für eingeschränkte Mobilität geeignet?','K06'),('Gibt es eine Waschmaschine?','K07'),('Gibt es eine Küche?','K08'),('Wo liegt die Unterkunft?','K09'),('Was kann man in Soria sehen?','K10'),('Wie kann ich buchen?','K11'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K11'),('Was kostet eine Nacht?',None),('Haben Sie ein Schwimmbad?',None)]}
