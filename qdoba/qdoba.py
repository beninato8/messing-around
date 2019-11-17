from geopy.geocoders import Nominatim
import requests
import re

from bs4 import BeautifulSoup
from tqdm import tqdm
from time import sleep

geolocator = Nominatim(user_agent="qdoba")

html = requests.get('https://locations.qdoba.com/us.html').text

soup = BeautifulSoup(html, 'html.parser')

soup = soup.find('ul', {'class':'c-directory-list-content'})

base = 'https://locations.qdoba.com/'

locations = []
rstate = re.compile(rf'{base}us/\w\w\.html')
rcity = re.compile(rf'{base}us/\w\w/[\w-]+\.html')
rlocation = re.compile(rf'{base}us/\w\w/[\w-]+/[\s\S]+.html')



def state_to_locations(state_url):
    print(state_url, f'{100*((723-len(locations))/723):.2f}%')
    out = []
    html = requests.get(state_url).text
    soup = BeautifulSoup(html, 'html.parser')
    soup = soup.find('ul', {'class':'c-directory-list-content'})
    for x in tqdm(soup.find_all('a', {'href':True})):
        url = f'{base}{x["href"].replace("../", "")}'
        if rcity.match(url):
            for location in city_to_locations(url):
                    out.append(location)
        elif rlocation.match(url):
            out.append(url)

    return out

def city_to_locations(city_url):
    out = []
    html = requests.get(city_url).text
    soup = BeautifulSoup(html, 'html.parser')
    soup = soup.find('div', {'class':'directory-list-row'})
    for x in soup.find_all('a', {'class':'location-card-visit'}):
        url = f'{base}{x["href"].replace("../", "")}'
        out.append(url)
    return out

def location_to_coords(location_url):
    address = location_url.replace(base, '').split('/')
    state = address[1].title()
    city = address[2]
    city = ' '.join(city.split('-')).title()

    street = address[3].replace('.html', '')
    street = ' '.join(street.split('-')).title()
    print(street, city, state)
    exit()
    location = get_location(street, city, state)
    try:
        return (location.latitude, location.longitude)
    except Exception as e:
        return ()

def get_location(street, city, state):
    try:
        location = geolocator.geocode(f"{street} {city} {state}")
    except Exception as e:
        sleep(1)
        print(f'error on {street} {city} {state}')
        return get_location(street, city, state)
    return location

def scrape_it():
    for x in soup.find_all('a', {'href':re.compile(r'us/.+\.html')}):
        url = f'{base}{x["href"]}'
        if rstate.match(url):
            for location in state_to_locations(url):
                locations.append(location_to_coords(location))
        elif rcity.match(url):
            for location in city_to_locations(url):
                    locations.append(location_to_coords(location))
        elif rlocation.match(url):
            locations.append(location_to_coords(url))
        else:
            print(url.replace(base, ''), error)

    for x in locations:
        print(x)

coords = [
(61.2122475100441, -149.733622),
(61.14316, -149.847988),
(61.1933420204082, -149.870271081633),
(61.5808596, -149.4417421),
(),
(35.1771116739107, -111.654376843345),
(33.512411, -112.1333961),
(33.3051828028303, -111.978452493025),
(33.4159384427414, -111.933352846485),
(36.1228824, -94.1486437707165),
(35.8171272857143, -90.6695469285714),
(36.3120390816327, -94.1791306938776),
(33.9852331, -118.3944704),
(34.1370151884244, -117.986236217989),
(34.0483127, -118.2576869),
(33.7933159, -117.8524231),
(),
(32.7293903, -117.1937029),
(32.825011, -117.129059),
(39.8128672, -105.1626968),
(39.8427535813953, -105.081921069767),
(39.6933703, -104.8646684),
(39.6334579, -104.7916123),
(39.5944711, -104.7993662),
(),
(39.6007117213197, -104.710011912811),
(40.0153676, -105.2589423),
(39.983708, -104.82382741993),
(39.9146663, -105.045211),
(39.9297055520587, -105.125491045225),
(39.412917, -104.8622919),
(39.4130181, -104.873682),
(39.5940571, -104.9485129),
(39.5946702, -104.9607846),
(39.59540585, -104.902034423524),
(),
(38.9648566976298, -104.794867547294),
(38.8042360715165, -104.81908107354),
(38.891102, -104.7592652),
(38.8855727676768, -104.71667620202),
(38.8968963897985, -104.83372915359),
(38.9405544113712, -104.798925088629),
(),
(39.7464073, -105.0018658),
(39.7429052, -104.9692685),
(39.7495331, -104.9989908),
(39.7802986, -104.8254021),
(39.7204281, -104.9031821),
(),
(39.6270112, -104.8952965),
(39.724734, -104.9830967),
(39.7400285, -104.9734064),
(39.6535152, -104.9053041),
(),
(39.8501877, -104.675327725053),
(39.6297094, -106.0590067),
(39.6520148, -104.9877144),
(39.6546795, -104.996252),
(),
(),
(40.5747075309686, -105.096162721322),
(40.5832558713918, -105.053084037539),
(40.523648969122, -105.074541750402),
(40.55380795, -105.096534491611),
(40.5500726, -105.0382485),
(40.5256797, -105.0259669),
(),
(39.1525771, -108.736862625045),
(38.73392, -104.7984979),
(39.7113155, -104.9406218),
(39.551012, -107.326905),
(39.09033125, -108.551935),
(),
(40.3967645922543, -104.697041493712),
(40.3955548232226, -104.743882688776),
(),
(39.5445161, -104.9423406),
(40.4060199, -104.983816),
(39.7090487291731, -105.133859794985),
(39.7369721, -105.1601534),
(39.7342721189281, -105.160500163511),
(),
(39.740534, -105.0819011),
(39.5861486, -105.0263081),
(39.6131346, -105.0251512),
(),
(39.5636025401337, -104.882836344556),
(39.5322858, -104.8826364),
(40.144035, -105.134012),
(39.9776393061224, -105.165637),
(),
(40.4237951, -105.076964099792),
(),
(38.4449424, -107.8605725),
(39.0692865, -104.8488475),
(39.511474, -104.7666484),
(40.460996, -106.821227),
(39.878092, -104.983225),
(39.9134306, -104.9425957),
(39.6303147, -106.4188081),
(39.9154139, -104.998693),
(39.8872724463766, -105.075721195013),
(39.871184, -105.0531475),
(39.7694422, -105.1096696),
(),
(41.1060279, -73.6676963),
(41.1563397, -73.422966),
(39.1825822, -75.5315886),
(),
(39.6832964, -75.7512078),
(),
(),
(),
(28.3848972838162, -81.5062208318787),
(28.5516892, -81.5205503),
(),
(),
(27.8517587, -82.3266058),
(),
(27.8942, -82.491871),
(27.973945, -82.53625),
(),
(34.0872809647019, -84.2676244010047),
(),
(),
(),
(31.8680365, -81.6118889),
(32.5982751, -83.5832948),
(33.9073363601316, -84.3641921085971),
(43.6051152, -116.1929374),
(),
(47.7465296736264, -116.789807562796),
(43.5904702214765, -116.35615638255),
(43.6360297174133, -116.354427998543),
(),
(46.725325, -117.018235),
(43.6132927139329, -116.590921276467),
(42.1390894, -88.0004073),
(38.5282365, -90.0350668),
(41.8833773, -87.6327655),
(42.324974, -87.845155),
(41.9325644782609, -87.6534243913043),
(38.6760048, -90.0151344),
(40.6756536428571, -89.5836474285714),
(38.7903011, -89.9506786),
(41.7912054, -87.6043965),
(41.4687010505193, -90.5071540576049),
(40.5118, -88.993299),
(40.7468585899564, -89.6118394015316),
(),
(42.0506018553884, -88.0446486682947),
(42.0248214212705, -88.1449446919929),
(38.5732803, -89.9275458),
(39.7640782, -89.6851149),
(40.10939235, -88.2272187093397),
(42.240546, -87.947391),
(39.502599, -96.31716),
(),
(),
(39.1657087, -86.5270708),
(39.853295, -86.394194),
(39.998393, -86.1302997),
(39.9580327, -86.1157881),
(38.3272456, -85.7619303),
(39.2383459, -85.9327027),
(41.7245242, -86.0407804),
(37.9851786179775, -87.4740999775281),
(39.9275871, -85.9347846),
(39.9567853, -86.0068613),
(41.1179509, -85.1309854),
(39.8144731294848, -85.769644344406),
(),
(),
(39.762978030303, -86.1545094444444),
(),
(),
(),
(),
(),
(),
(39.6933942, -86.0824761),
(39.809747, -86.121592),
(),
(39.7885097, -86.1572698),
(39.7774113, -86.1696869),
(39.767284, -86.131208),
(40.4174005, -86.851753625),
(41.4711676, -87.3316154),
(41.7084660507442, -86.1806791142169),
(40.2190421836735, -85.3939447346939),
(38.3058218504147, -85.8404659986549),
(38.3320365, -85.7995662),
(39.9933077, -85.9291299),
(40.0294864, -85.9947962),
(39.703872, -86.399477),
(),
(41.4689184595001, -87.0279917107207),
(40.4250282846271, -86.9080781410642),
(),
(),
(41.219787, -95.8346413),
(41.5567051308725, -90.5459235671141),
(41.5859238, -93.6460682),
(42.5143725102041, -96.4169413061224),
(42.4453716, -96.3398126),
(39.3623997, -101.0523376),
(39.0957359, -96.8233589),
(38.879212, -99.317817),
(38.0722816870998, -97.9005117483342),
(39.0219090055106, -96.8171631806444),
(33.8795089268293, -118.406150560976),
(33.890232, -118.3997459),
(38.8808010837432, -94.6677122913501),
(38.80145145, -97.6135052036044),
(39.0490434, -95.7622144),
(37.336243, -97.2408013),
(),
(36.9449013, -86.42433055),
(),
(38.9998407878788, -84.6533590454546),
(36.642752, -87.447086),
(37.882991, -85.952501),
(),
(),
(),
(),
(37.991255, -84.43443),
(38.0385119170123, -84.500415741836),
(),
(38.0885303, -85.6671036),
(38.233972, -85.457126),
(38.2694295, -85.6143816),
(38.23164485, -85.7088796681348),
(38.1968154, -85.5477),
(38.2207499, -85.7613982),
(38.21193285, -85.5969482296935),
(38.2131369, -85.7206099),
(38.2532102, -85.7572635),
(38.3075631, -85.5772914),
(38.2501742, -85.6293582),
(38.1376653695113, -85.6688403775096),
(38.1535734, -85.587804),
(38.1510699, -85.8373203),
(38.2330736, -85.6410978),
(36.619626881973, -88.3149112481419),
(37.0775888546578, -88.6839862941633),
(37.7365507113676, -84.3090461972705),
(30.4245629466633, -91.1263771999487),
(31.048428, -93.216281),
(43.6331844, -70.3342269),
(39.2775827, -76.5670639),
(39.3691805, -76.4521285),
(39.3713662, -76.6104502),
(),
(39.1991467, -76.8196148),
(39.403024, -76.948379),
(),
(39.1073245, -76.7380915),
(),
(),
(39.1598831, -76.6200868),
(38.9680504, -76.95238),
(39.4208083, -76.7792975),
(39.058674, -77.1230028571429),
(39.125833, -76.5893344),
(),
(39.4442416, -76.6262961),
(39.3954129, -76.5756936),
(42.3648833, -71.0618996),
(42.3405648186003, -71.0879574928538),
(42.348682760303, -71.0967504099),
(42.2201697621717, -71.0286693239894),
(42.23091725, -71.1773768333201),
(41.6649226650393, -71.1558015673425),
(),
(42.45246415, -71.2326499887747),
(42.01450635, -71.2295919339189),
(),
(42.4044927878788, -71.0816027272727),
(42.2000295, -71.7783002),
(42.2875585, -71.6720952),
(42.54728895, -70.9469400468032),
(42.4848151, -70.9008224137568),
(41.77253745, -70.7438206388266),
(42.30013005, -71.29085735),
(42.5056701, -71.1324297),
(42.2782629, -83.2076728),
(42.9607937, -85.889875),
(42.2984894, -83.7199365),
(42.2535854809141, -83.7500615565078),
(42.2577525, -83.7006205),
(42.6981179666667, -83.3063397333333),
(42.261082, -85.218229),
(42.210326, -83.493237),
(43.6889038056755, -85.4837790627017),
(42.5150597, -83.2855232),
(42.5469216360205, -83.2091476669472),
(42.6009598753585, -83.2620285937637),
(44.2805633, -85.4062104),
(),
(42.3233468, -83.4350602),
(42.713467, -83.4106389591837),
(),
(),
(),
(42.4993124, -83.3762267),
(),
(43.0308348636364, -82.4561278272727),
(45.0273187346939, -84.6870992857143),
(42.979508, -83.673823),
(43.0014038644068, -85.5905691355932),
(42.9705927065417, -85.6663145906879),
(42.9142413, -85.533004),
(),
(42.9142413, -85.533004),
(42.8846882, -85.744489),
(42.8275091005493, -86.0918789945849),
(42.59081755, -83.8767807879797),
(42.2699766842503, -84.4266049490416),
(42.2714630816327, -85.6481897755102),
(42.2594751860465, -85.5897152713178),
(42.295887, -85.6440221245467),
(42.3264295345466, -85.5152037964752),
(42.736163, -84.508444),
(42.7410752796209, -84.9399340900474),
(42.3956125, -83.4127045),
(42.3687278, -83.3514759),
(),
(41.942016321608, -83.4043858743719),
(43.5868895841924, -84.7673894329897),
(43.1551552276977, -86.2056484150419),
(42.676144, -82.7480576),
(42.4372635021065, -83.4358075012639),
(42.4839689, -83.4761872),
(),
(42.9975470336134, -84.1587598235294),
(42.2185989090909, -85.5895296464647),
(42.6817462702703, -83.1524232162162),
(),
(),
(42.529522, -83.197263),
(43.4819938, -83.975309),
(42.083294122449, -86.4855556428572),
(42.627723989899, -82.980435959596),
(),
(42.4751478571429, -83.2407448571429),
(42.1983059, -83.2402839),
(),
(),
(42.5627108, -83.1331976),
(42.5343148327326, -83.1107754182993),
(43.0219440869565, -85.6889362173913),
(42.5061094339623, -83.0524774213836),
(42.3371452236842, -83.4030730394737),
(42.1379492385336, -83.2261275394403),
(43.6809683561245, -93.3587885294679),
(),
(47.466194, -94.875894),
(),
(45.0582799, -93.3158274),
(44.822975, -93.579122),
(46.8170288222479, -92.0780391669266),
(44.837199, -93.158977),
(44.859744, -93.424957),
(),
(),
(),
(44.9744053333333, -93.2755383333333),
(),
(45.0546786, -93.4090422),
(44.0235344, -92.481485),
(44.780614, -93.4541937),
(45.5535460108617, -94.2094066209606),
(),
(44.8397014, -93.7935025),
(),
(45.1029242, -95.0368187),
(44.9433094650702, -92.9342251003278),
(31.3252518, -89.3447775),
(),
(38.4376165510204, -90.3875310816327),
(36.6502977, -93.220078),
(38.7442344, -90.4133438),
(37.3022117, -89.5755512),
(),
(38.6732255, -90.6552449),
(38.6693647, -90.4425208),
(38.7665943, -90.7669879),
(37.7909088, -90.4326441),
(38.50603535, -90.4477822185236),
(38.8075677, -90.2993965),
(37.7641632, -92.1157306),
(39.0372894029563, -94.3547027748968),
(37.0842516, -94.4771769),
(39.1898402, -94.5482792),
(38.5748239, -90.406968),
(38.593136, -90.499888),
(38.6219645, -90.3331322),
(),
(38.8127203571429, -94.489589744898),
(38.7718098, -90.4948571),
(38.567548, -90.2807464),
(38.6350004, -90.232970142694),
(38.60258, -90.242162),
(38.640062, -90.2445948036978),
(38.5940225, -90.2989328),
(38.5041217, -90.3283741),
(),
(37.180939, -93.243211),
(37.1395053, -93.3202179),
(37.1588989, -93.2833809),
(),
(38.6348215, -90.3165237797398),
(),
(38.6225726, -90.520044),
(45.7551722, -108.5642883),
(45.6706264, -111.076152),
(),
(48.2197298524687, -114.330153228821),
(46.8681000980392, -113.98081854902),
(40.940321, -98.384689),
(40.69955804, -99.0844846),
(40.8149645306122, -96.7041363877551),
(40.8146553, -96.6369048),
(41.1154371, -100.7633776),
(41.2485293, -96.0223372),
(41.2122431, -95.9637639),
(41.2341433, -96.1183425),
(41.27916525, -96.09983675),
(41.26063485, -95.9811819750221),
(41.17376913, -96.023017545),
(),
(36.0631794, -115.2423361),
(36.0775397, -115.0457376),
(),
(35.611697, -115.392187265823),
(39.545427, -119.8512194),
(39.6128296326531, -119.849874714286),
(39.419594611855, -119.755097739213),
(39.4029389, -119.7463742),
(39.5760318, -119.740806),
(42.8243642, -71.5061454),
(43.0899261, -70.7919738934096),
(),
(40.5858529, -74.6185906),
(),
(),
(),
(),
(),
(),
(40.741387, -74.029811),
(),
(40.7292241, -74.038366),
(40.7964483333333, -74.4814429375),
(40.7102484375, -74.1908089375),
(40.7402171428571, -74.1714803571429),
(),
(40.5258128, -74.4387424),
(40.3503288, -74.6580351),
(),
(40.9075816, -74.5582888),
(),
(),
(40.6418692466714, -74.4141827001254),
(40.8886486, -74.2601305),
(40.651313, -74.3479315),
(40.698677, -73.9185076),
(40.7251183333333, -73.5561946666667),
(44.042623, -75.78848),
(40.7394896, -73.7863017),
(41.0964215, -74.0159659),
(),
(43.127345255814, -77.5658031162791),
(40.5419817826087, -74.205794),
(40.5925174, -74.1631289),
(40.5160051960784, -74.2334291568627),
(40.7866478, -73.5029984),
(35.7444194, -78.8723612),
(35.2606184, -80.77591),
(),
(35.023708638029, -80.8491578998033),
(),
(35.1891442, -80.8824395),
(35.0962360848903, -80.7776796384132),
(),
(),
(35.1399186, -78.9946548),
(35.262084, -81.1335636),
(36.086324, -79.832835),
(36.0398113986394, -79.9620177243763),
(35.4459146921144, -80.8788965566799),
(35.7969230606061, -78.5104981212121),
(35.1276609161452, -80.7020774922395),
(35.0825255, -80.7282083),
(35.826003, -78.705116),
(),
(),
(36.0946933092956, -80.2746154640429),
(36.0626808, -80.3022328),
(46.788808, -100.785051),
(46.901663502121, -102.789847811669),
(46.8536644226804, -96.8621484948454),
(46.8589788, -96.8451989),
(47.889373, -97.0780591747851),
(48.233959, -101.295977),
(48.266889, -101.295605),
(48.168631, -103.621863142857),
(),
(39.3371348142857, -82.0724840285714),
(39.2580052, -84.3744595),
(41.37431005, -83.6501347415081),
(),
(40.1467823771841, -82.992578422274),
(39.9890445273887, -83.0519047409509),
(40.0022452, -83.0083092),
(),
(39.308057, -84.3190401),
(39.3721469, -84.3715323),
(39.4055804, -81.4149858),
(36.060849, -95.8160217),
(35.6816126, -97.5013691),
(),
(),
(34.6278488208955, -98.4923164029851),
(35.4352197, -97.3734862),
(35.3196794768616, -97.4959828026958),
(35.203777, -97.441085),
(35.2430318, -97.4805241),
(35.1918067407407, -97.4232257407407),
(35.5891367, -97.5493364),
(35.3633181111111, -97.5526872222222),
(35.4627201409822, -97.6360718262058),
(35.5652633, -97.6548267),
(35.3755908433938, -96.9296990358327),
(36.12087975, -97.0648469675),
(36.088143272, -95.922476604),
(36.0632283, -95.9578714),
(36.0561156, -96.0034045),
(36.0606895, -95.966752),
(36.0309056908, -95.9223684332),
(35.5263003, -98.6939674),
(45.4863133, -122.7967877),
(),
(44.0453366, -123.0796128),
(45.5365945, -122.87731704998),
(45.5176705, -122.6784495),
(45.5345332, -122.656911364563),
(44.8898199610257, -123.034446014995),
(),
(45.30245115, -122.772450148907),
(40.1121079, -75.4207879),
(40.0005009795918, -75.2284107346939),
(41.00889635, -76.4471403813962),
(39.9817826, -75.3610857),
(40.0199167, -75.3151179),
(),
(40.096256, -75.2965437),
(40.2557497, -76.8694236),
(40.1603666, -75.1488638),
(40.0901388, -75.1247486),
(),
(40.0246152838884, -76.1963957221205),
(39.9496467, -75.1673495),
(39.9777454, -75.158309),
(39.9537280617548, -75.2027773580192),
(40.426419324692, -79.9661756343908),
(40.440948, -79.995941),
(40.4427239520911, -79.9984384787396),
(39.9142692398981, -75.3425140448974),
(40.7967049, -77.8723137),
(40.7933087, -77.8628895),
(39.9691757, -75.5739401279576),
(),
(),
(39.984045, -76.726676),
(32.8317617260194, -79.8259607452834),
(45.4586756, -98.4350072),
(44.311282593985, -96.7654823233083),
(44.0903015267321, -103.183783755232),
(44.0794669, -103.2524656),
(43.51494, -96.748765),
(43.5469271, -96.6960587),
(43.5008258, -96.7716095),
(44.5017224, -103.8598617),
(42.78882465, -96.924596241181),
(44.8896136666667, -97.06809),
(36.0418634, -86.7801122),
(36.1862617416995, -86.6133385734218),
(35.95671685, -83.9288175294989),
(35.93046536127, -84.0304300427925),
(36.1510970727355, -86.7997146242477),
(),
(30.287877, -97.741902),
(),
(32.5204044690508, -97.3482602390453),
(),
(32.86449755, -96.8381653),
(),
(32.729289, -97.414171),
(32.8989211, -97.3215779),
(33.5441525140425, -101.956989031025),
(32.606207972973, -97.1166952567568),
(33.0271635, -96.7136645),
(32.940011, -96.768829),
(30.2013187, -93.7515551),
(33.8747253, -98.5390368),
(),
(38.8573815, -77.0451953),
(),
(),
(37.4033252, -77.6741146),
(38.8455318190469, -77.3031933156431),
(),
(),
(38.3073987397426, -77.511325010958),
(),
(),
(38.4370479812702, -78.8729335241581),
(38.4324157206284, -78.8503749331708),
(38.9573919, -77.4007252),
(38.7471101, -77.4510137),
(36.8605383, -76.2081806),
(36.9472776, -76.3192298),
(37.4996744, -77.5280523),
(37.5086567, -77.4883983),
(37.46254, -77.386799),
(37.550475746746, -77.4503313580718),
(37.2799764, -76.7184209),
(38.6493706, -77.2611285),
(47.666491, -117.5610124),
(47.296276, -122.2427513),
(47.7937321, -122.2157047),
(),
(47.3147737, -122.3165363),
(47.3595564, -122.602117424944),
(47.5477782265899, -122.04105482314),
(47.1071771, -122.5925575),
(),
(47.8208661, -122.317037),
(48.152237, -122.195685136667),
(47.586817, -122.236111),
(47.8498354, -122.2193769),
(47.115351, -122.095895),
(48.0777091, -122.1862682),
(47.6318975, -122.1383196),
(47.6750135, -122.1276484),
(47.6614113, -122.3152105),
(47.602733, -122.3332749),
(47.6095172, -122.3379659),
(47.6656969, -122.3010147),
(47.66784535, -117.410767273193),
(47.6714492, -117.2406004),
(47.6471912942122, -117.413788040175),
(47.4595705, -122.2533301),
(47.7554424401336, -122.155393121992),
(38.9053617, -77.042948),
(),
(38.896271, -77.026537),
(),
(37.8000669, -81.1776638),
(39.2798474999314, -80.2792838943614),
(39.6502635714286, -79.9728864464286),
(38.3261909, -81.7147693),
(44.2438228, -88.3519852),
(44.2731545, -88.4358336),
(42.5238521, -88.9862644),
(43.0359539173966, -88.1112955400461),
(43.0516777, -88.3665455),
(43.020234, -89.422282),
(43.7538834693776, -88.4532811281169),
(43.1761643, -87.9146271297568),
(43.1187323293104, -87.915724426036),
(43.3203418, -87.9191939),
(44.4873808947368, -87.9600873684211),
(44.517778, -88.0459303),
(42.952517020934, -88.0085181433765),
(42.720182, -88.996354),
(43.061218, -88.76245),
(42.5760905322581, -87.8852195806452),
(46.8152811199685, -117.883521340972),
(43.5720358, -89.7707938),
(42.5937039, -88.4151836),
(39.846446, -82.812613),
(43.0736914165054, -89.4348159499593),
(43.126681, -89.308121),
(38.682597877551, -90.1597287959184),
(43.0613652, -89.496578),
(44.0784993048694, -87.6980757961745),
(),
(43.045307, -87.9108121),
(43.0256747, -87.9698731),
(43.05321435, -87.8939474012271),
(43.0499922245257, -88.0075241321583),
(42.3732678, -83.0646668),
(42.95885535, -87.9204077152213),
(43.0403964279495, -87.9330495915711),
(),
(),
(),
(44.1760364081633, -88.4890062244898),
(42.9755836027397, -88.1096678219178),
(42.8855943, -87.9117436),
(),
(44.0055986326531, -88.5802474693878),
(43.7175195033557, -87.7539594295302),
(44.523265824049, -89.5217028736611),
(43.0399217046589, -88.2581074727182),
(43.0150628571429, -88.23352),
(44.9581428, -89.6634503),
(43.0897559021118, -88.0657589309391),
(43.0379, -88.047153),
(42.9930801474765, -88.0471597798098),
(43.3978406046726, -88.1894804789412),
(44.905185, -89.5734661),
(42.8349076460288, -88.7519035437151),
(42.8210340030349, -106.370033084524),
(42.845545, -106.2448693),
(41.1611415, -104.7927219),
(41.1454696350356, -104.761920510895),
(44.2703198, -105.4932265),
(41.3232563, -105.5922981),
(44.77464915, -106.9430784)]

print(len([x for x in coords if x]))

import gmplot 

def center_geolocation(geolocations):
    lats = []
    lons = []
    for x in geolocations:
        if x:
          lats.append(x[0])
          lons.append(x[1])

    return (sum(lats)/len(lats), sum(lons)/len(lons))
center = center_geolocation(coords)
lats = [x[0] for x in coords if x]
lons = [x[1] for x in coords if x]
gmap3 = gmplot.GoogleMapPlotter(center[0], center[1], 4) 

# gmap3.scatter(lats, lons, color='r', marker=False,size=20000 )
gmap3.heatmap(lats, lons, radius=20)
# gmap3.plot(lats, lons, 'cornflowerblue', edge_width = 2.5) 

gmap3.draw("/Users/Nicholas/GitHub/messing around/qdoba/qdoba.html")
# print(soup.prettify())
