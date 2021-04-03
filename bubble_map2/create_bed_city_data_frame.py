import random

import pandas as pd

cities_pak = ["Bagh",
        "Bhimber",
        "Kotli",
        "Mirpur",
        "Muzaffarabad",
        "Neelum",
        "Poonch",
        "Sudhnati",
        "Awaran",
        "Disputed Area 1",
        "Disputed Area 2",
        "Kalat",
        "Kharan",
        "Khuzdar",
        "Lasbela",
        "Mastung",
        "Gwadar",
        "Kech",
        "Panjgur",
        "Bolan",
        "Jafarabad",
        "Jhal Magsi",
        "Nasirabad",
        "Chagai",
        "Pishin",
        "Qilla Abdullah",
        "Quetta",
        "Dera Bugti",
        "Kholu",
        "Sibi",
        "Ziarat",
        "Barkhan",
        "Loralai",
        "Musakhel",
        "Qilla Saifullah",
        "Zhob",
        "Bajaur",
        "Khyber",
        "Kurram",
        "Largha Shirani",
        "Mohmand",
        "N. Waziristan",
        "Orakzai",
        "S. Waziristan",
        "Islamabad",
        "Bannu",
        "Lakki Marwat",
        "Dera Ismail Khan",
        "Tank",
        "Adam Khel",
        "Bhittani",
        "Abbottabad",
        "Battagram",
        "Haripur",
        "Kohistan",
        "Mansehra",
        "Hangu",
        "Karak",
        "Kohat",
        "Chitral",
        "Dir",
        "Malakand P.A.",
        "Shangla",
        "Swat",
        "Buner",
        "Mardan",
        "Swabi",
        "Charsadda",
        "Nowshera",
        "Peshawar",
        "Chilas",
        "Gilgit",
        "Gilgit (Tribal Territory)",
        "Kargil",
        "Kupwara (Gilgit Wazarat)",
        "Ladakh (Leh)",
        "Bahawalnagar",
        "Bahawalpur",
        "Rahimyar Khan",
        "Dera Ghazi Kha",
        "Layyah",
        "Muzaffargarh",
        "Rajan Pur",
        "Faisalabad",
        "Jhang",
        "Toba Tek Singh",
        "Gujarat",
        "Gujranwala 1",
        "Gujranwala 2",
        "Gujrat",
        "Hafizabad",
        "Narowal 1",
        "Narowal 2",
        "Sialkot",
        "Kasur",
        "Lahore",
        "Nankana Sahib",
        "Okara",
        "Okara 1",
        "Sheikhupura",
        "Khanewal",
        "Lodhran",
        "Multan",
        "Pakpattan",
        "Sahiwal",
        "Vehari",
        "Attok",
        "Chakwal",
        "Jhelum",
        "Rawalpindi",
        "Bhakkar",
        "Khushab",
        "Mianwali",
        "Sargodha",
        "Badin",
        "Dadu",
        "Hyderabad",
        "Jamshoro",
        "Matiari",
        "Tando Allahyar",
        "Tando M. Khan",
        "Thatta",
        "Karachi Central",
        "Karachi East",
        "Karachi South",
        "Karachi west",
        "Malir",
        "Jakobabad",
        "Kashmore",
        "Larkana",
        "Shikarpur",
        "Mirphurkhas",
        "Mithi",
        "Sanghar",
        "Umerkot",
        "Rann of Kutch",
        "Ghotki",
        "Khairpur",
        "Naushahro Firoz",
        "Nawab Shah",
        "Sukkur"]

cites_ind = ["Andaman Islands","Nicobar Islands","Anantapur","Chittoor","Cuddapah","East Godavari","Guntur","Krishna","Kurnool","Nellore","Prakasam","Srikakulam","Vishakhapatnam","Vizianagaram","West Godavari","Changlang","East Kameng","East Siang","Kurung Kumey","Lohit","Lower Dibang Valley","Lower Subansiri","Papum Pare","Tawang","Tirap","Upper Dibang Valley","Upper Siang","Upper Subansiri","West Kameng","West Siang","Barpeta","Bongaigaon","Cachar","Darrang","Dhemaji","Dhuburi","Dibrugarh","Goalpara","Golaghat","Hailakandi","Jorhat","Kamrup","Karbi Anglong","Karimganj","Kokrajhar","Lakhimpur","Marigaon","Nagaon","Nalbari","North Cachar Hills","Sibsagar","Sonitpur","Tinsukia","Araria","Aurangabad","Banka","Begusarai","Bhabua","Bhagalpur","Bhojpur","Buxar","Darbhanga","Gaya","Gopalganj","Jamui","Jehanabad","Katihar","Khagaria","Kishanganj","Lakhisarai","Madhepura","Madhubani","Munger","Muzaffarpur","Nalanda","Nawada","Pashchim Champaran","Patna","Purba Champaran","Purnia","Rohtas","Saharsa","Samastipur","Saran","Sheikhpura","Sheohar","Sitamarhi","Siwan","Supaul","Vaishali","Chandigarh","Bastar","Bilaspur","Dantewada","Dhamtari","Durg","Janjgir-Champa","Jashpur","Kanker","Kawardha","Korba","Koriya","Mahasamund","Raigarh","Raipur","Raj Nandgaon","Surguja","Dadra and Nagar Haveli","Daman","Junagadh","Delhi","North Goa","South Goa","Ahmadabad","Amreli","Anand","Banas Kantha","Bharuch","Bhavnagar","Dahod","Gandhinagar","Jamnagar","Junagadh","Kachchh","Kheda","Mahesana","Narmada","Navsari","Panch Mahals","Patan","Porbandar","Rajkot","Sabar Kantha","Surat","Surendranagar","The Dangs","Vadodara","Valsad","Ambala","Bhiwani","Faridabad","Fatehabad","Gurgaon","Hisar","Jhajjar","Jind","Kaithal","Karnal","Kurukshetra","Mahendragarh","Panchkula","Panipat","Rewari","Rohtak","Sirsa","Sonepat","Yamuna Nagar","Bilaspur","Chamba","Hamirpur","Kangra","Kinnaur","Kullu","Lahul and Spiti","Mandi","Shimla","Sirmaur","Solan","Una","Anantnag (Kashmir South)","Bagdam","Baramula (Kashmir North)","Doda","Jammu","Kargil","Kathua","Kupwara (Muzaffarabad)","Ladakh (Leh)","Pulwama","Punch","Rajauri","Srinagar","Udhampur","Bokaro","Chatra","Deoghar","Dhanbad","Dumka","Garhwa","Giridih","Godda","Gumla","Hazaribag","Jamtara","Koderma","Latehar","Lohardaga","Pakur","Palamu","Pashchim Singhbhum","Purba Singhbhum","Ranchi","Sahibganj","Saraikela Kharsawan","Simdega","Bagalkot","Bangalore Rural","Bangalore Urban","Belgaum","Bellary","Bidar","Bijapur","Chamrajnagar","Chikmagalur","Chitradurga","Dakshin Kannad","Davanagere","Dharwad","Gadag","Gulbarga","Hassan","Haveri","Kodagu","Kolar","Koppal","Mandya","Mysore","Raichur","Shimoga","Tumkur","Udupi","Uttar Kannand","Alappuzha","Ernakulam","Idukki","Kannur","Kasaragod","Kollam","Kottayam","Kozhikode","Malappuram","Palakkad","Pattanamtitta","Thiruvananthapuram","Thrissur","Wayanad","Kavaratti","Anuppur","Ashoknagar","Balaghat","Barwani","Betul","Bhind","Bhopal","Burhanpur","Chhatarpur","Chhindwara","Damoh","Datia","Dewas","Dhar","Dindori","East Nimar","Guna","Gwalior","Harda","Hoshangabad","Indore","Jabalpur","Jhabua","Katni","Mandla","Mandsaur","Morena","Narsinghpur","Neemuch","Panna","Raisen","Rajgarh","Ratlam","Rewa","Sagar","Satna","Sehore","Seoni","Shahdol","Shajapur","Sheopur","Shivpuri","Sidhi","Tikamgarh","Ujjain","Umaria","Vidisha","West Nimar","Ahmednagar","Akola","Amravati","Aurangabad","Bhandara","Bid","Buldana","Chandrapur","Dhule","Garhchiroli","Gondiya","Greater Bombay","Hingoli","Jalgaon","Jalna","Kolhapur","Latur","Nagpur","Nanded","Nandurbar","Nashik","Osmanabad","Parbhani","Pune","Raigarh","Ratnagiri","Sangli","Satara","Sindhudurg","Solapur","Thane","Wardha","Washim","Yavatmal","Bishnupur","Chandel","Churachandpur","East Imphal","Senapati","Tamenglong","Thoubal","Ukhrul","West Imphal","East Garo Hills","East Khasi Hills","Jaintia Hills","Ri-Bhoi","South Garo Hills","West Garo Hills","West Khasi Hills","Aizawl","Champhai","Kolasib","Lawngtlai","Lunglei","Mamit","Saiha","Serchhip","Dimapur","Kohima","Mokokchung","Mon","Phek","Tuensang","Wokha","Zunheboto","Angul","Baleshwar","Baragarh","Bhadrak","Bolangir","Boudh","Cuttack","Deogarh","Dhenkanal","Gajapati","Ganjam","Jagatsinghpur","Jajpur","Jharsuguda","Kalahandi","Kandhamal","Kendrapara","Keonjhar","Khordha","Koraput","Malkangiri","Mayurbhanj","Nabarangpur","Nayagarh","Nuapada","Puri","Rayagada","Sambalpur","Sonepur","Sundargarh","Karaikal","Mahe","Puducherry","Yanam","Amritsar","Bathinda","Faridkot","Fatehgarh Sahib","Firozpur","Gurdaspur","Hoshiarpur","Jalandhar","Kapurthala","Ludhiana","Mansa","Moga","Muktsar","Nawan Shehar","Patiala","Rupnagar","Sangrur","Ajmer","Alwar","Banswara","Baran","Barmer","Bharatpur","Bhilwara","Bikaner","Bundi","Chittaurgarh","Churu","Dausa","Dhaulpur","Dungarpur","Ganganagar","Hanumangarh","Jaipur","Jaisalmer","Jalor","Jhalawar","Jhunjhunun","Jodhpur","Karauli","Kota","Nagaur","Pali","Rajsamand","Sawai Madhopur","Sikar","Sirohi","Tonk","Udaipur","East","North Sikkim","South Sikkim","West Sikkim","Ariyalur","Chennai","Coimbatore","Cuddalore","Dharmapuri","Dindigul","Erode","Kancheepuram","Kanniyakumari","Karur","Madurai","Nagapattinam","Namakkal","Nilgiris","Perambalur","Pudukkottai","Ramanathapuram","Salem","Sivaganga","Thanjavur","Theni","Thiruvallur","Thiruvarur","Thoothukudi","Tiruchchirappalli","Tirunelveli Kattabo","Tiruvannamalai","Vellore","Villupuram","Virudhunagar","Adilabad","Hyderabad","Karimnagar","Khammam","Mahbubnagar","Medak","Nalgonda","Nizamabad","Rangareddi","Warangal","Dhalai","North Tripura","South Tripura","West Tripura","Agra","Aligarh","Allahabad","Ambedkar Nagar","Auraiya","Azamgarh","Badaun","Baghpat","Bahraich","Ballia","Balrampur","Banda","Bara Banki","Bareilly","Basti","Bijnor","Bulandshahr","Chandauli","Chitrakoot","Deoria","Etah","Etawah","Faizabad","Farrukhabad","Fatehpur","Firozabad","Gautam Buddha Nagar","Ghaziabad","Ghazipur","Gonda","Gorakhpur","Hamirpur","Hardoi","Hathras","Jalaun","Jaunpur","Jhansi","Jyotiba Phule Nagar","Kannauj","Kanpur Dehat","Kanpur","Kaushambi","Kushinagar","Lakhimpur Kheri","Lalitpur","Lucknow","Maharajganj","Mahoba","Mainpuri","Mathura","Mau","Meerut","Mirzapur","Moradabad","Muzaffarnagar","Pilibhit","Pratapgarh","Rae Bareli","Rampur","Saharanpur","Sant Kabir Nagar","Sant Ravi Das Nagar","Shahjahanpur","Shravasti","Siddharth Nagar","Sitapur","Sonbhadra","Sultanpur","Unnao","Varanasi","Almora","Bageshwar","Chamoli","Champawat","Dehra Dun","Haridwar","Naini Tal","Pauri Garhwal","Pithoragarh","Rudra Prayag","Tehri Garhwal","Udham Singh Nagar","Uttarkashi","Bankura","Barddhaman","Birbhum","Dakshin Dinajpur","Darjiling","East Midnapore","Haora","Hugli","Jalpaiguri","Kochbihar","Kolkata","Maldah","Murshidabad","Nadia","North 24 Parganas","Puruliya","South 24 Parganas","Uttar Dinajpur","West Midnapore"]


beds = [0 for i in range(len(cites_ind))]

data = pd.DataFrame({'cites': cites_ind, 'beds': beds})

city_with_data = ['Chennai', 'Kozhikode', 'Thiruvananthapuram', 'Shimoga']
city_data = [2.6, 2.3, 3.9, 5.9]

for idx, city in enumerate(city_with_data):
        data.loc[data.cites == city, 'beds'] = city_data[idx]

data.to_csv('city_ind_beds.csv')


