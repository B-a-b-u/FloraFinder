import os

class_list = os.listdir("..\Dataset\Indian Medicinal Leaves Image Datasets\Medicinal plant dataset")
print(len(class_list))
print(type(class_list))
print(class_list)
"""
Plant_Details = plant_data = {
    'Aloevera': [
        {
            'scientific_name': 'Aloe vera',
            'scientific_medicinal_properties': 'Aloe vera contains various vitamins and minerals such as vitamins A, C, and E, as well as antioxidants and enzymes.',
            'common_location': 'Aloe vera is native to the Arabian Peninsula, but it is cultivated worldwide, especially in tropical climates.',
            'popular_usecase': 'Aloe vera gel is commonly used topically for skin conditions such as burns, wounds, and sunburns. It is also used in cosmetic products for its moisturizing properties.',
            'Disclaimer': 'Consult a healthcare professional before using aloe vera, especially if you have any skin allergies or medical conditions.',
            'lament_medicinal_property': 'Aloe vera gel is soothing and moisturizing for the skin. It has anti-inflammatory properties and may help promote wound healing.'
        }
    ],
    'Amla': [
        {
            'scientific_name': 'Phyllanthus emblica',
            'scientific_medicinal_properties': 'Amla, also known as Indian gooseberry, is rich in vitamin C, antioxidants, and other nutrients.',
            'common_location': 'Amla trees are native to India and are cultivated in various parts of Asia.',
            'popular_usecase': 'Amla is used in Ayurvedic medicine for its rejuvenating properties and is believed to promote longevity. It is also used in culinary dishes and as a dietary supplement for its health benefits.',
            'Disclaimer': 'Consult a healthcare professional before using amla, especially if you have any medical conditions or are taking medications.',
            'lament_medicinal_property': 'Amla is known for its high vitamin C content, which supports immune health and is beneficial for hair and skin.'
        }
    ],
    'Amruta_Balli': [
        {
            'scientific_name': 'Tinospora cordifolia',
            'scientific_medicinal_properties': 'Tinospora cordifolia, also known as guduchi or amruta, has been used in Ayurvedic medicine for its immunomodulatory, anti-inflammatory, and antioxidant properties.',
            'common_location': 'Tinospora cordifolia is native to the Indian subcontinent and is found growing in tropical and subtropical regions.',
            'popular_usecase': 'In Ayurveda, amruta balli is used to boost immunity, promote overall health, and treat various ailments such as fever, diabetes, and digestive disorders. It is also used in Ayurvedic formulations for its anti-aging and rejuvenating effects.',
            'Disclaimer': 'Consult a qualified Ayurvedic practitioner before using amruta balli, especially if you are pregnant, breastfeeding, or have any medical conditions.',
            'lament_medicinal_property': 'Amruta balli is valued for its ability to enhance immunity, support liver function, and promote overall well-being.'
        }
    ],
    'Arali': [
        {
            'scientific_name': 'Aralia elata',
            'scientific_medicinal_properties': 'Aralia elata, also known as Japanese angelica tree, is a deciduous shrub native to East Asia.',
            'common_location': 'Aralia elata grows in forests and mountainous regions of China, Korea, and Japan.',
            'popular_usecase': 'In traditional Chinese medicine, arali is used for its diuretic, antipyretic, and analgesic properties. It is believed to promote circulation, reduce inflammation, and alleviate pain. Arali root is also used as a culinary ingredient in Korean cuisine.',
            'Disclaimer': 'Consult a healthcare professional before using arali, especially if you have any medical conditions or are taking medications.',
            'lament_medicinal_property': 'Arali is valued for its anti-inflammatory and analgesic effects. It is used to relieve pain, reduce fever, and promote overall well-being.'
        }
    ],
    'Ashoka': [
        {
            'scientific_name': 'Saraca asoca',
            'scientific_medicinal_properties': 'Saraca asoca, commonly known as ashoka or sorrowless tree, is a medicinal plant native to India and Southeast Asia.',
            'common_location': 'Ashoka trees are found in the wild as well as cultivated in gardens and parks. They prefer tropical and subtropical climates.',
            'popular_usecase': 'In Ayurvedic medicine, ashoka is used to treat various gynecological disorders such as menstrual irregularities, menorrhagia, and uterine fibroids. It is also used to relieve pain, reduce inflammation, and promote overall reproductive health in women.',
            'Disclaimer': 'Consult a qualified Ayurvedic practitioner before using ashoka, especially if you have any reproductive health concerns or are pregnant.',
            'lament_medicinal_property': 'Ashoka is valued for its beneficial effects on women\'s health. It is used to regulate menstrual cycles, reduce menstrual pain, and support reproductive wellness.'
        }
    ],
    'Ashwagandha': [
        {
            'scientific_name': 'Withania somnifera',
            'scientific_medicinal_properties': 'Withania somnifera, commonly known as ashwagandha or Indian ginseng, is a medicinal herb used in traditional Ayurvedic and Unani medicine.',
            'common_location': 'Ashwagandha is native to India, the Middle East, and parts of Africa. It is cultivated in various regions for its medicinal properties.',
            'popular_usecase': 'Ashwagandha is used to reduce stress, improve cognitive function, and enhance overall vitality and longevity. It is also used to treat various health conditions such as anxiety, depression, insomnia, and arthritis.',
            'Disclaimer': 'Consult a healthcare professional before using ashwagandha, especially if you have any medical conditions or are taking medications.',
            'lament_medicinal_property': 'Ashwagandha is known as an adaptogen, helping the body adapt to stress and promoting balance. It is used to support mental clarity, physical endurance, and emotional well-being.'
        }
    ],
    'Avacado': [
        {
            'scientific_name': 'Persea americana',
            'scientific_medicinal_properties': 'Persea americana, commonly known as avocado, is a fruit tree native to South Central Mexico.',
            'common_location': 'Avocado trees are cultivated in subtropical and tropical regions worldwide, including California, Florida, and Mediterranean countries.',
            'popular_usecase': 'Avocado fruit is prized for its nutritional value, containing healthy fats, vitamins, minerals, and antioxidants. It is used in culinary dishes such as salads, sandwiches, and smoothies for its creamy texture and flavor.',
            'Disclaimer': 'Consult a healthcare professional before consuming avocado, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Avocado is valued for its heart-healthy fats, fiber, and nutrients. It is used to support cardiovascular health, improve digestion, and promote skin and hair health.'
        }
    ],
    'Bamboo': [
        {
            'scientific_name': 'Bambusoideae',
            'scientific_medicinal_properties': 'Bamboo is a fast-growing perennial grass belonging to the Bambusoideae subfamily of the Poaceae family.',
            'common_location': 'Bamboo is native to various regions worldwide, including Asia, Africa, and the Americas. It grows in diverse climates, from tropical rainforests to temperate forests.',
            'popular_usecase': 'Bamboo has numerous uses in construction, furniture making, paper production, culinary arts, and traditional medicine. It is used in Ayurveda and traditional Chinese medicine for its medicinal properties, including antimicrobial, anti-inflammatory, and antipyretic effects.',
            'Disclaimer': 'Consult a qualified healthcare professional before using bamboo for medicinal purposes, especially if you have any medical conditions or are pregnant.',
            'lament_medicinal_property': 'Bamboo is valued for its versatility and sustainability. It is used to promote wound healing, reduce inflammation, and support overall health and well-being.'
        }
    ],
    'Basale': [
        {
            'scientific_name': 'Basella alba',
            'scientific_medicinal_properties': 'Basella alba, also known as Malabar spinach or vine spinach, is a leafy green vegetable native to tropical Asia and Africa.',
            'common_location': 'Basella alba grows in warm, humid climates and is cultivated in tropical and subtropical regions worldwide.',
            'popular_usecase': 'Basale is rich in vitamins, minerals, and antioxidants. It is used as a culinary vegetable in various cuisines, including Indian, Thai, and Filipino cuisine. Basale leaves are cooked and eaten as a nutritious green vegetable.',
            'Disclaimer': 'Consult a healthcare professional before consuming basale, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Basale is valued for its nutritional content and health benefits. It is used to support eye health, boost immunity, and promote overall well-being.'
        }
    ],
    'Betel': [
        {
            'scientific_name': 'Piper betle',
            'scientific_medicinal_properties': 'Piper betle, commonly known as betel vine or betel leaf, is a perennial creeper native to South and Southeast Asia.',
            'common_location': 'Betel vines are cultivated in tropical and subtropical regions for their leaves, which are used in religious, cultural, and medicinal practices.',
            'popular_usecase': 'Betel leaves are used in traditional medicine for their antiseptic, anti-inflammatory, and digestive properties. They are chewed with betel nut and other ingredients in betel quids for their stimulant and euphoric effects. Betel leaves are also used in Ayurvedic formulations and as a mouth freshener.',
            'Disclaimer': 'Chewing betel quids can have adverse health effects, including oral cancer, gum disease, and addiction. Consult a healthcare professional before using betel leaves for medicinal purposes.',
            'lament_medicinal_property': 'Betel leaves are valued for their aromatic flavor and medicinal properties. They are used to freshen breath, aid digestion, and promote oral health.'
        }
    ],
    'Betel_Nut': [
        {
            'scientific_name': 'Areca catechu',
            'scientific_medicinal_properties': 'Areca catechu, commonly known as betel nut or areca nut, is the seed of the areca palm tree native to South and Southeast Asia.',
            'common_location': 'Areca palm trees are cultivated in tropical and subtropical regions for their nuts, which are used in cultural, religious, and medicinal practices.',
            'popular_usecase': 'Betel nuts are chewed with betel leaves and other ingredients in betel quids for their stimulant and psychoactive effects. They are also used in traditional medicine for their digestive, carminative, and aphrodisiac properties. In some cultures, betel nuts are consumed as a social and ceremonial tradition.',
            'Disclaimer': 'Chewing betel quids can have adverse health effects, including oral cancer, gum disease, and addiction. Consult a healthcare professional before using betel nuts for medicinal purposes.',
            'lament_medicinal_property': 'Betel nuts are valued for their stimulating effects on the nervous system. They are used to enhance alertness, improve digestion, and promote feelings of well-being.'
        }
    ],
    'Brahmi': [
        {
            'scientific_name': 'Bacopa monnieri',
            'scientific_medicinal_properties': 'Bacopa monnieri, commonly known as brahmi or water hyssop, is a perennial herb native to wetlands and marshy areas of India, Southeast Asia, and Australia.',
            'common_location': 'Bacopa monnieri grows in aquatic and semi-aquatic habitats such as ponds, rivers, and marshes. It is cultivated in gardens and farms for its medicinal properties.',
            'popular_usecase': 'Brahmi is used in Ayurvedic medicine for its cognitive-enhancing, adaptogenic, and neuroprotective properties. It is believed to improve memory, concentration, and learning ability. Brahmi is also used to reduce stress, anxiety, and symptoms of depression.',
            'Disclaimer': 'Consult a qualified Ayurvedic practitioner before using brahmi, especially if you have any medical conditions or are pregnant.',
            'lament_medicinal_property': 'Brahmi is valued for its ability to support brain health and cognitive function. It is used to enhance memory, mental clarity, and overall mental well-being.'
        }
    ],
    'Castor': [
        {
            'scientific_name': 'Ricinus communis',
            'scientific_medicinal_properties': 'Ricinus communis, commonly known as castor bean or castor oil plant, is a fast-growing perennial shrub native to the Mediterranean region, Eastern Africa, and India.',
            'common_location': 'Castor plants grow in tropical and subtropical regions worldwide, where they are cultivated for their seeds, which contain castor oil.',
            'popular_usecase': 'Castor oil is used in various applications, including pharmaceuticals, cosmetics, lubricants, and biodiesel production. It is known for its purgative, emollient, and anti-inflammatory properties. Castor oil is used topically for skin conditions, hair care, and massage, as well as orally for constipation relief and detoxification.',
            'Disclaimer': 'Castor beans contain toxic compounds, including ricin, which can be harmful if ingested or applied improperly. Consult a healthcare professional before using castor oil or castor beans for medicinal or other purposes.',
            'lament_medicinal_property': 'Castor oil is valued for its moisturizing and healing properties. It is used to soothe dry skin, promote hair growth, and relieve constipation.'
        }
    ],
    'Curry_Leaf': [
        {
            'scientific_name': 'Murraya koenigii',
            'scientific_medicinal_properties': 'Murraya koenigii, commonly known as curry leaf or sweet neem, is a tropical tree native to India and Sri Lanka.',
            'common_location': 'Curry leaf trees are cultivated in tropical and subtropical regions for their aromatic leaves, which are used as a culinary herb in Indian cuisine.',
            'popular_usecase': 'Curry leaves are used in Indian cooking to add flavor and aroma to dishes such as curries, rice, and soups. They are also used in traditional medicine for their digestive, carminative, and antioxidant properties. Curry leaves are believed to aid digestion, reduce cholesterol levels, and promote hair growth.',
            'Disclaimer': 'Consult a healthcare professional before using curry leaves, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Curry leaves are valued for their aromatic flavor and health benefits. They are used to improve digestion, lower cholesterol, and support hair and scalp health.'
        }
    ],
    'Doddapatre': [
        {
            'scientific_name': 'Plectranthus amboinicus',
            'scientific_medicinal_properties': 'Plectranthus amboinicus, commonly known as Cuban oregano, Indian borage, or doddapatre, is a perennial herb native to Southern and Eastern Africa, Madagascar, and the Indian subcontinent.',
            'common_location': 'Plectranthus amboinicus grows in tropical and subtropical regions worldwide and is cultivated for its culinary and medicinal uses.',
            'popular_usecase': 'Doddapatre leaves are used in culinary dishes, herbal teas, and traditional medicine for their aromatic flavor and medicinal properties. They are believed to have antibacterial, antifungal, anti-inflammatory, and antioxidant effects. Doddapatre leaves are used to treat respiratory conditions, digestive disorders, skin problems, and fever.',
            'Disclaimer': 'Consult a healthcare professional before using doddapatre, especially if you have any medical conditions or are pregnant.',
            'lament_medicinal_property': 'Doddapatre leaves are valued for their aromatic flavor and health-promoting properties. They are used to relieve coughs, colds, indigestion, and skin irritations.'
        }
    ],
    'Ekka': [
        {
            'scientific_name': 'Azadirachta indica',
            'scientific_medicinal_properties': 'Azadirachta indica, commonly known as neem or Indian lilac, is a fast-growing evergreen tree native to the Indian subcontinent.',
            'common_location': 'Neem trees are found in tropical and subtropical regions of South Asia, including India, Nepal, Pakistan, Bangladesh, and Sri Lanka.',
            'popular_usecase': 'Neem is used in Ayurvedic medicine for its antiseptic, antibacterial, antiviral, antifungal, and anti-inflammatory properties. It is used to treat various skin conditions such as acne, eczema, psoriasis, and fungal infections. Neem is also used in dental care products, herbal remedies, and organic agriculture.',
            'Disclaimer': 'Consult a qualified Ayurvedic practitioner before using neem, especially if you have any skin allergies or medical conditions.',
            'lament_medicinal_property': 'Neem is valued for its broad-spectrum antimicrobial and anti-inflammatory effects. It is used to cleanse and purify the skin, promote wound healing, and support overall skin health.'
        }
    ],
    'Ganike': [
        {
            'scientific_name': 'Solanum nigrum',
            'scientific_medicinal_properties': 'Solanum nigrum, commonly known as black nightshade or makoi, is a flowering plant native to Eurasia and North Africa.',
            'common_location': 'Black nightshade grows as a weed in cultivated fields, gardens, and waste areas. It is found in temperate, subtropical, and tropical regions worldwide.',
            'popular_usecase': 'In traditional medicine, black nightshade is used for its diuretic, anti-inflammatory, and antipyretic properties. It is used to treat various health conditions such as fever, cough, asthma, rheumatism, skin diseases, and digestive disorders. Black nightshade leaves and berries are also used as a culinary vegetable in some cuisines, although caution is advised due to potential toxicity.',
            'Disclaimer': 'Consult a qualified healthcare professional before using black nightshade, especially if you are pregnant, breastfeeding, or have any medical conditions.',
            'lament_medicinal_property': 'Black nightshade is valued for its medicinal properties, but caution is advised due to potential toxicity. It is used to reduce fever, relieve pain, and treat various health conditions, but its use should be supervised by a healthcare professional.'
        }
    ],
    'Gauva': [
        {
            'scientific_name': 'Psidium guajava',
            'scientific_medicinal_properties': 'Psidium guajava, commonly known as guava, is a tropical fruit tree native to Central America and the Caribbean.',
            'common_location': 'Guava trees are cultivated in tropical and subtropical regions worldwide for their edible fruits, which are rich in vitamins, minerals, and antioxidants.',
            'popular_usecase': 'Guava fruit is consumed fresh or processed into juice, jams, jellies, and other food products. It is known for its high vitamin C content, which supports immune health and collagen production. Guava leaves are used in traditional medicine for their antidiarrheal, antimicrobial, and antiparasitic properties. Guava leaf tea is consumed for its digestive and detoxifying effects.',
            'Disclaimer': 'Consult a healthcare professional before using guava, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Guava fruit and leaves are valued for their nutritional content and health benefits. They are used to support immune health, aid digestion, and promote overall well-being.'
        }
    ],
    'Geranium': [
        {
            'scientific_name': 'Pelargonium graveolens',
            'scientific_medicinal_properties': 'Pelargonium graveolens, commonly known as geranium or rose geranium, is a perennial shrub native to South Africa.',
            'common_location': 'Geranium plants are cultivated worldwide for their fragrant leaves and flowers, which are used in perfumery, aromatherapy, and traditional medicine.',
            'popular_usecase': 'Geranium essential oil is used in aromatherapy for its calming, uplifting, and balancing effects on the mind and body. It is believed to relieve stress, anxiety, depression, and insomnia. Geranium oil is also used in skincare products for its astringent, antiseptic, and anti-inflammatory properties. It is used to balance oily and combination skin, reduce acne and inflammation, and promote wound healing.',
            'Disclaimer': 'Consult a qualified aromatherapist or healthcare professional before using geranium essential oil, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Geranium essential oil is valued for its calming and skin-soothing properties. It is used to reduce stress, balance emotions, and promote clear, healthy skin.'
        }
    ],
    'Henna': [
        {
            'scientific_name': 'Lawsonia inermis',
            'scientific_medicinal_properties': 'Lawsonia inermis, commonly known as henna, is a flowering plant native to North Africa, West Asia, and South Asia.',
            'common_location': 'Henna plants are cultivated in arid and semi-arid regions for their leaves, which are dried and ground into a fine powder. Henna powder is used to dye hair, skin, and nails in various cultures.',
            'popular_usecase': 'Henna is used in traditional medicine and cosmetics for its cooling, astringent, and antimicrobial properties. It is used topically to soothe skin irritation, treat burns, and condition hair. Henna is also used as a natural dye for body art, temporary tattoos, and hair coloring.',
            'Disclaimer': 'Consult a qualified healthcare professional before using henna, especially if you have any skin allergies or medical conditions.',
            'lament_medicinal_property': 'Henna is valued for its natural coloring and conditioning properties. It is used to enhance hair color, nourish the scalp, and promote healthy skin.'
        }
    ],
    'Hibiscus': [
        {
            'scientific_name': 'Hibiscus rosa-sinensis',
            'scientific_medicinal_properties': 'Hibiscus rosa-sinensis, commonly known as hibiscus or Chinese hibiscus, is a flowering plant native to East Asia.',
            'common_location': 'Hibiscus plants are cultivated worldwide for their ornamental flowers, which are used in landscaping, gardens, and horticulture. They are also grown for their medicinal and culinary uses.',
            'popular_usecase': 'Hibiscus flowers are used in traditional medicine and herbal teas for their health benefits. Hibiscus tea is rich in antioxidants, vitamins, and minerals. It is believed to lower blood pressure, reduce cholesterol levels, promote weight loss, and improve liver health. Hibiscus flowers are also used in hair and skincare products for their moisturizing, anti-aging, and anti-inflammatory properties.',
            'Disclaimer': 'Consult a healthcare professional before using hibiscus, especially if you have any medical conditions or are pregnant.',
            'lament_medicinal_property': 'Hibiscus tea is valued for its refreshing taste and health-promoting properties. It is used to support cardiovascular health, promote hydration, and enhance skin and hair health.'
        }
    ],
    'Honge': [
        {
            'scientific_name': 'Pongamia pinnata',
            'scientific_medicinal_properties': 'Pongamia pinnata, commonly known as honge or Indian beech, is a fast-growing tree native to South Asia, Southeast Asia, and northern Australia.',
            'common_location': 'Honge trees grow in tropical and subtropical regions, where they are cultivated for their seeds, which contain bioactive compounds with medicinal properties.',
            'popular_usecase': 'Honge oil, also known as pongamia oil, is extracted from the seeds of the honge tree and used in traditional medicine, cosmetics, and biofuels. It is used topically for its antimicrobial, anti-inflammatory, and wound-healing properties. Honge oil is also used as a natural insect repellent, fertilizer, and lubricant.',
            'Disclaimer': 'Consult a qualified healthcare professional before using honge oil, especially if you have any skin allergies or medical conditions.',
            'lament_medicinal_property': 'Honge oil is valued for its therapeutic properties and versatility. It is used to soothe skin irritation, promote wound healing, and protect against insect bites and infections.'
        }
    ],
    'Insulin': [
        {
            'scientific_name': 'Syzygium cumini',
            'scientific_medicinal_properties': 'Syzygium cumini, commonly known as jamun or Indian blackberry, is a tropical evergreen tree native to India, Bangladesh, Nepal, Pakistan, and Indonesia.',
            'common_location': 'Jamun trees are found in tropical and subtropical regions, where they are cultivated for their edible fruits, seeds, and leaves, which have medicinal properties.',
            'popular_usecase': 'Jamun fruits are consumed fresh or processed into juice, jams, jellies, and culinary dishes. They are known for their sweet and tangy flavor, as well as their nutritional value. Jamun seeds and leaves are used in traditional medicine for their antidiabetic, antihyperlipidemic, and antioxidant properties. Jamun is believed to regulate blood sugar levels, improve insulin sensitivity, and prevent complications of diabetes.',
            'Disclaimer': 'Consult a healthcare professional before using jamun, especially if you have diabetes or are taking medications.',
            'lament_medicinal_property': 'Jamun is valued for its antidiabetic properties and is used to support blood sugar control and metabolic health.'
        }
    ],
    'Jasmine': [
        {
            'scientific_name': 'Jasminum officinale',
            'scientific_medicinal_properties': 'Jasminum officinale, commonly known as jasmine or common jasmine, is a flowering plant native to South Asia, Southeast Asia, and East Asia.',
            'common_location': 'Jasmine plants are cultivated worldwide for their fragrant flowers, which are used in perfumery, aromatherapy, and traditional medicine.',
            'popular_usecase': 'Jasmine essential oil is used in aromatherapy for its uplifting, calming, and aphrodisiac effects. It is believed to relieve stress, anxiety, depression, and insomnia. Jasmine oil is also used in skincare products for its moisturizing, soothing, and rejuvenating properties. It is used to hydrate dry skin, reduce inflammation, and promote a radiant complexion.',
            'Disclaimer': 'Consult a qualified aromatherapist or healthcare professional before using jasmine essential oil, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Jasmine essential oil is valued for its sensual aroma and skin-nourishing properties. It is used to uplift the mood, promote relaxation, and enhance skin health.'
        }
    ],
    'Lemon': [
        {
            'scientific_name': 'Citrus limon',
            'scientific_medicinal_properties': 'Citrus limon, commonly known as lemon, is a citrus fruit tree native to South Asia.',
            'common_location': 'Lemon trees are cultivated in subtropical and tropical regions worldwide for their acidic fruits, which are used in culinary, medicinal, and cosmetic applications.',
            'popular_usecase': 'Lemon juice is used as a flavoring agent in cooking, baking, beverages, and condiments. It is also used in household cleaning products and natural remedies for its antiseptic, antibacterial, and deodorizing properties. Lemon essential oil is used in aromatherapy for its invigorating, uplifting, and cleansing effects. It is believed to improve mood, boost energy, and support immune health.',
            'Disclaimer': 'Consult a healthcare professional before using lemon, especially if you have any citrus allergies or medical conditions.',
            'lament_medicinal_property': 'Lemon is valued for its refreshing flavor and versatile uses. It is used to cleanse, purify, and revitalize the body and mind.'
        }
    ],
    'Lemon_grass': [
        {
            'scientific_name': 'Cymbopogon citratus',
            'scientific_medicinal_properties': 'Cymbopogon citratus, commonly known as lemongrass, is a tropical grass native to South Asia and Southeast Asia.',
            'common_location': 'Lemongrass grows in warm, humid climates and is cultivated in tropical and subtropical regions worldwide for its culinary, medicinal, and aromatic properties.',
            'popular_usecase': 'Lemongrass is used in culinary dishes, herbal teas, and essential oils for its lemony flavor and fragrance. It is also used in traditional medicine for its antimicrobial, anti-inflammatory, and digestive properties. Lemongrass tea is consumed for its calming, detoxifying, and digestive benefits. Lemongrass essential oil is used in aromatherapy for its refreshing, energizing, and insect-repellent effects.',
            'Disclaimer': 'Consult a qualified healthcare professional before using lemongrass, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Lemongrass is valued for its citrusy aroma and health-promoting properties. It is used to soothe digestive discomfort, relieve stress, and repel insects.'
        }
    ],
    'Mango': [
        {
            'scientific_name': 'Mangifera indica',
            'scientific_medicinal_properties': 'Mangifera indica, commonly known as mango, is a tropical fruit tree native to South Asia.',
            'common_location': 'Mango trees are cultivated in subtropical and tropical regions worldwide for their sweet and juicy fruits, which are consumed fresh or processed into juice, jams, jellies, and culinary dishes.',
            'popular_usecase': 'Mango fruit is known for its delicious flavor, vibrant color, and nutritional value. It is rich in vitamins, minerals, and antioxidants, including vitamins A and C, potassium, and beta-carotene. Mangoes are used in culinary dishes, desserts, smoothies, and beverages. They are also used in traditional medicine for their anti-inflammatory, antioxidant, and immune-boosting properties. Mango leaves, bark, and seeds are used in herbal remedies for various health conditions such as diarrhea, dysentery, and diabetes.',
            'Disclaimer': 'Consult a healthcare professional before using mango, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Mango is valued for its delicious taste and health benefits. It is used to support immune health, promote digestion, and enhance overall well-being.'
        }
    ],
    'Mint': [
        {
            'scientific_name': 'Mentha',
            'scientific_medicinal_properties': 'Mentha is a genus of aromatic perennial herbs in the Lamiaceae family, which includes species such as spearmint (Mentha spicata) and peppermint (Mentha × piperita).',
            'common_location': 'Mint plants grow in temperate and subtropical regions worldwide, where they are cultivated for their aromatic leaves, which are used in culinary, medicinal, and cosmetic applications.',
            'popular_usecase': 'Mint leaves are used in culinary dishes, herbal teas, and essential oils for their refreshing flavor and fragrance. Peppermint oil is used in aromatherapy for its invigorating, cooling, and digestive properties. It is believed to relieve headaches, nausea, indigestion, and respiratory congestion. Peppermint tea is consumed for its digestive, calming, and decongestant effects. Mint leaves are also used in herbal remedies for digestive disorders, respiratory ailments, and headaches.',
            'Disclaimer': 'Consult a qualified healthcare professional before using mint, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Mint is valued for its refreshing taste and cooling properties. It is used to soothe digestive discomfort, alleviate respiratory congestion, and promote relaxation.'
        }
    ],
    'Nagadali': [
        {
            'scientific_name': 'Sesbania grandiflora',
            'scientific_medicinal_properties': 'Sesbania grandiflora, commonly known as sesban or agati, is a fast-growing perennial tree native to South Asia and Southeast Asia.',
            'common_location': 'Sesbania grandiflora grows in tropical and subtropical regions, where it is cultivated for its edible flowers, leaves, and pods, which have medicinal properties.',
            'popular_usecase': 'Sesbania flowers, leaves, and pods are used in culinary dishes, herbal teas, and traditional medicine for their nutritional and medicinal benefits. They are rich in vitamins, minerals, and antioxidants, including vitamins A, C, and E, calcium, and iron. Sesbania is used to promote overall health, boost immunity, and treat various health conditions such as anemia, diabetes, inflammation, and respiratory disorders.',
            'Disclaimer': 'Consult a healthcare professional before using sesbania, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Sesbania is valued for its nutritious flowers, leaves, and pods. It is used to support immune health, enhance energy levels, and promote overall well-being.'
        }
    ],
    'Neem': [
        {
            'scientific_name': 'Azadirachta indica',
            'scientific_medicinal_properties': 'Azadirachta indica, commonly known as neem or Indian lilac, is a fast-growing evergreen tree native to the Indian subcontinent.',
            'common_location': 'Neem trees are found in tropical and subtropical regions of South Asia, including India, Nepal, Pakistan, Bangladesh, and Sri Lanka.',
            'popular_usecase': 'Neem is used in Ayurvedic medicine for its antiseptic, antibacterial, antiviral, antifungal, and anti-inflammatory properties. It is used to treat various skin conditions such as acne, eczema, psoriasis, and fungal infections. Neem is also used in dental care products, herbal remedies, and organic agriculture.',
            'Disclaimer': 'Consult a qualified Ayurvedic practitioner before using neem, especially if you have any skin allergies or medical conditions.',
            'lament_medicinal_property': 'Neem is valued for its broad-spectrum antimicrobial and anti-inflammatory effects. It is used to cleanse and purify the skin, promote wound healing, and support overall skin health.'
        }
    ],
    'Nithyapushpa': [
        {
            'scientific_name': 'Vinca rosea',
            'scientific_medicinal_properties': 'Vinca rosea, commonly known as periwinkle or Madagascar periwinkle, is a flowering plant native to Madagascar and other Indian Ocean islands.',
            'common_location': 'Periwinkle plants are cultivated worldwide for their ornamental flowers, which are used in landscaping, gardens, and floral arrangements. They are also grown for their medicinal properties.',
            'popular_usecase': 'Periwinkle has been used in traditional medicine for centuries for its antidiabetic, anticancer, antimicrobial, and antihypertensive properties. It is used to treat various health conditions such as diabetes, cancer, infections, and high blood pressure. Periwinkle alkaloids, such as vincristine and vinblastine, are used in chemotherapy drugs to treat leukemia, lymphoma, and other cancers.',
            'Disclaimer': 'Consult a qualified healthcare professional before using periwinkle, especially if you have any medical conditions or are pregnant.',
            'lament_medicinal_property': 'Periwinkle is valued for its medicinal properties and is used to treat a wide range of health conditions. It is known for its antidiabetic, anticancer, and antimicrobial effects.'
        }
    ],
    'Pomegranate': [
        {
            'scientific_name': 'Punica granatum',
            'scientific_medicinal_properties': 'Punica granatum, commonly known as pomegranate, is a fruit-bearing shrub or small tree native to the region from Iran to northern India.',
            'common_location': 'Pomegranate trees are cultivated in subtropical and tropical regions worldwide for their edible fruits, which are prized for their sweet and tangy flavor, as well as their nutritional value.',
            'popular_usecase': 'Pomegranate fruit is consumed fresh or processed into juice, jams, jellies, and culinary dishes. It is known for its high antioxidant content, including punicalagins, anthocyanins, and vitamin C. Pomegranate juice is believed to promote heart health, lower blood pressure, reduce inflammation, and improve cognitive function. Pomegranate seeds and peel are used in traditional medicine for their antidiabetic, anti-inflammatory, and antimicrobial properties. Pomegranate extracts are used in skincare products for their moisturizing, anti-aging, and antioxidant effects.',
            'Disclaimer': 'Consult a healthcare professional before using pomegranate, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Pomegranate is valued for its delicious taste and health benefits. It is used to support heart health, enhance cognitive function, and promote overall well-being.'
        }
    ],
    'Rosemary': [
        {
            'scientific_name': 'Rosmarinus officinalis',
            'scientific_medicinal_properties': 'Rosmarinus officinalis, commonly known as rosemary, is a woody, perennial herb native to the Mediterranean region.',
            'common_location': 'Rosemary plants are cultivated worldwide for their aromatic leaves, which are used in culinary, medicinal, and cosmetic applications.',
            'popular_usecase': 'Rosemary leaves are used as a culinary herb to flavor roasted meats, poultry, fish, vegetables, and bread. Rosemary essential oil is used in aromatherapy for its stimulating, invigorating, and memory-enhancing effects. It is believed to improve concentration, reduce stress, and boost mood. Rosemary oil is also used in skincare and hair care products for its antimicrobial, antioxidant, and anti-inflammatory properties. It is used to cleanse and tone the skin, promote hair growth, and relieve scalp irritation.',
            'Disclaimer': 'Consult a qualified aromatherapist or healthcare professional before using rosemary essential oil, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Rosemary is valued for its culinary and therapeutic properties. It is used to flavor food, improve memory, and promote skin and hair health.'
        }
    ],
    'Sandalwood': [
        {
            'scientific_name': 'Santalum album',
            'scientific_medicinal_properties': 'Santalum album, commonly known as sandalwood, is a tropical evergreen tree native to South Asia, Southeast Asia, and Australia.',
            'common_location': 'Sandalwood trees are cultivated in tropical and subtropical regions worldwide for their fragrant heartwood, which is used in perfumery, incense, cosmetics, and traditional medicine.',
            'popular_usecase': 'Sandalwood essential oil is used in aromatherapy for its calming, grounding, and mood-enhancing effects. It is believed to reduce anxiety, promote relaxation, and enhance meditation. Sandalwood oil is also used in skincare products for its moisturizing, anti-inflammatory, and anti-aging properties. It is used to soothe dry skin, reduce inflammation, and minimize the appearance of scars and blemishes.',
            'Disclaimer': 'Consult a qualified aromatherapist or healthcare professional before using sandalwood essential oil, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Sandalwood is valued for its aromatic fragrance and therapeutic properties. It is used to calm the mind, promote relaxation, and nourish the skin.'
        }
    ],
    'Sarpagandha': [
        {
            'scientific_name': 'Rauwolfia serpentina',
            'scientific_medicinal_properties': 'Rauwolfia serpentina, commonly known as Indian snakeroot or sarpagandha, is a perennial shrub native to South Asia.',
            'common_location': 'Rauwolfia serpentina grows in subtropical and tropical regions, where it is cultivated for its medicinal properties.',
            'popular_usecase': 'Sarpagandha is used in traditional medicine for its antihypertensive, sedative, and antipsychotic properties. It contains alkaloids such as reserpine, which are used in pharmaceutical drugs to treat high blood pressure, anxiety, and mental disorders. Sarpagandha is also used in Ayurvedic medicine for its calming, anti-stress, and sleep-inducing effects.',
            'Disclaimer': 'Consult a qualified healthcare professional before using sarpagandha, especially if you have any medical conditions or are taking medications.',
            'lament_medicinal_property': 'Sarpagandha is valued for its therapeutic effects on the nervous system. It is used to reduce blood pressure, relieve anxiety, and promote relaxation and sleep.'
        }
    ],
    'Sesame': [
        {
            'scientific_name': 'Sesamum indicum',
            'scientific_medicinal_properties': 'Sesamum indicum, commonly known as sesame, is an annual flowering plant native to Africa and India.',
            'common_location': 'Sesame plants are cultivated in tropical and subtropical regions worldwide for their seeds, which are used as a culinary ingredient, cooking oil, and condiment.',
            'popular_usecase': 'Sesame seeds are rich in healthy fats, protein, vitamins, minerals, and antioxidants. They are used in culinary dishes, bakery products, sweets, and snacks. Sesame oil is used in cooking, frying, and salad dressings. Sesame seed extract, known as sesame oil cake, is used as a livestock feed and organic fertilizer. Sesame seeds are also used in traditional medicine for their anti-inflammatory, antioxidant, and immune-boosting properties. Sesame oil is used topically for skin and hair care, massage, and Ayurvedic treatments.',
            'Disclaimer': 'Consult a healthcare professional before using sesame seeds or sesame oil, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Sesame seeds and oil are valued for their nutritional content and health benefits. They are used to support heart health, improve digestion, and nourish the skin and hair.'
        }
    ],
    'Sunflower': [
        {
            'scientific_name': 'Helianthus annuus',
            'scientific_medicinal_properties': 'Helianthus annuus, commonly known as sunflower, is an annual flowering plant native to North and South America.',
            'common_location': 'Sunflowers are cultivated worldwide for their edible seeds and oil, as well as their ornamental value.',
            'popular_usecase': 'Sunflower seeds are consumed as a snack and used as an ingredient in bakery products, salads, and snacks. Sunflower oil is used in cooking, frying, and salad dressings. Sunflower seed meal is used as a livestock feed and organic fertilizer. Sunflower petals are used in herbal teas and traditional medicine for their diuretic, expectorant, and anti-inflammatory properties. Sunflower oil is also used topically for skincare and massage.',
            'Disclaimer': 'Consult a healthcare professional before using sunflower seeds or sunflower oil, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Sunflower seeds and oil are valued for their nutritional content and health benefits. They are used to support heart health, improve skin health, and promote overall well-being.'
        }
    ],
    'Tulsi': [
        {
            'scientific_name': 'Ocimum tenuiflorum',
            'scientific_medicinal_properties': 'Ocimum tenuiflorum, commonly known as holy basil or tulsi, is a sacred plant in Hinduism and Ayurveda. It is native to the Indian subcontinent.',
            'common_location': 'Tulsi is cultivated in home gardens, temples, and farms throughout India and Southeast Asia for its medicinal and religious significance.',
            'popular_usecase': 'Tulsi is used in Ayurvedic medicine for its adaptogenic, immunomodulatory, and antimicrobial properties. It is considered a rasayana herb, which promotes longevity, vitality, and overall well-being. Tulsi is used to reduce stress, support respiratory health, improve digestion, and enhance cognitive function. It is also used in religious rituals, prayers, and ceremonies as an offering to the gods and goddesses.',
            'Disclaimer': 'Consult a qualified Ayurvedic practitioner before using tulsi, especially if you have any medical conditions or are pregnant.',
            'lament_medicinal_property': 'Tulsi is valued for its sacred status and health-promoting properties. It is used to reduce stress, boost immunity, and promote overall wellness.'
        }
    ],
    'Nooni': [
        {
            'scientific_name': 'Mimusops elengi',
            'scientific_medicinal_properties': 'Mimusops elengi, commonly known as nooni, is a medium-sized evergreen tree native to South Asia and Southeast Asia.',
            'common_location': 'Nooni trees are found in tropical and subtropical regions, where they are cultivated for their fragrant flowers, which are used in traditional medicine, perfumery, and religious ceremonies.',
            'popular_usecase': 'Nooni flowers are used in Ayurvedic medicine for their astringent, antibacterial, and anti-inflammatory properties. They are used to treat oral health issues such as toothache, gum disease, and bad breath. Nooni flowers are also used in skincare products for their soothing, moisturizing, and anti-aging effects. They are used to tone the skin, reduce inflammation, and promote healing. Nooni bark and leaves are used in traditional medicine for their antidiabetic, analgesic, and antimicrobial properties.',
            'Disclaimer': 'Consult a qualified healthcare professional before using nooni flowers, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Nooni flowers are valued for their aromatic fragrance and therapeutic properties. They are used to promote oral health, skin health, and overall well-being.'
        }
    ],
    'Pappaya': [
        {
            'scientific_name': 'Carica papaya',
            'scientific_medicinal_properties': 'Carica papaya, commonly known as papaya, is a tropical fruit tree native to the Americas, particularly southern Mexico and Central America.',
            'common_location': 'Papaya trees are cultivated in tropical and subtropical regions worldwide for their edible fruits, which are prized for their sweet taste, vibrant color, and nutritional value.',
            'popular_usecase': 'Papaya fruit is consumed fresh or processed into juice, jams, jellies, and culinary dishes. It is rich in vitamins, minerals, antioxidants, and enzymes such as papain and chymopapain. Papaya is known for its digestive, anti-inflammatory, and immune-boosting properties. It is used to promote digestion, relieve constipation, and support gastrointestinal health. Papaya seeds are also used in traditional medicine for their antimicrobial, antiparasitic, and anthelmintic properties. They are used to treat intestinal worms, fungal infections, and bacterial infections.',
            'Disclaimer': 'Consult a healthcare professional before using papaya, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Papaya is valued for its delicious taste and health benefits. It is used to support digestion, boost immunity, and promote overall well-being.'
        }
    ],
    'Pepper': [
        {
            'scientific_name': 'Piper nigrum',
            'scientific_medicinal_properties': 'Piper nigrum, commonly known as pepper, is a flowering vine in the family Piperaceae, cultivated for its fruit, known as a peppercorn.',
            'common_location': 'Pepper plants are native to South Asia and are cultivated in tropical regions worldwide for their fruits, which are used as a spice and seasoning.',
            'popular_usecase': 'Pepper is one of the most commonly used spices in culinary dishes worldwide. It is known for its pungent flavor and aroma, as well as its medicinal properties. Pepper contains bioactive compounds such as piperine, which have antioxidant, anti-inflammatory, and digestive properties. Pepper is used to improve digestion, stimulate appetite, and relieve gastrointestinal discomfort. It is also used in traditional medicine for its analgesic, expectorant, and antimicrobial effects. Pepper oil is used topically for its warming, analgesic, and anti-inflammatory properties. It is used to relieve muscle pain, joint pain, and arthritis symptoms.',
            'Disclaimer': 'Consult a healthcare professional before using pepper, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Pepper is valued for its spicy flavor and therapeutic properties. It is used to support digestion, relieve pain, and promote overall well-being.'
        }
    ],
    'Raktachandini': [
        {
            'scientific_name': 'Hibiscus rosa-sinensis',
            'scientific_medicinal_properties': 'Hibiscus rosa-sinensis, commonly known as hibiscus or raktachandini, is a flowering plant native to East Asia.',
            'common_location': 'Hibiscus plants are cultivated worldwide for their ornamental flowers, which are used in landscaping, gardens, and floral arrangements.',
            'popular_usecase': 'Hibiscus flowers are used in herbal teas, beverages, and culinary dishes for their tart flavor and vibrant color. Hibiscus tea is known for its refreshing taste and health benefits. It is rich in antioxidants, vitamins, and minerals, and is believed to support heart health, lower blood pressure, and improve cholesterol levels. Hibiscus flowers are also used in traditional medicine for their diuretic, antimicrobial, and anti-inflammatory properties. They are used to promote urinary tract health, relieve menstrual cramps, and soothe sore throat.',
            'Disclaimer': 'Consult a healthcare professional before using hibiscus, especially if you are pregnant, breastfeeding, or have any medical conditions.',
            'lament_medicinal_property': 'Raktachandini is valued for its beautiful flowers and health-promoting properties. It is used to support heart health, promote urinary tract health, and enhance overall well-being.'
        }
    ],
    'Rose': [
        {
            'scientific_name': 'Rosa',
            'scientific_medicinal_properties': 'Rosa is a genus of flowering plants in the family Rosaceae, commonly known as roses. There are over three hundred species and thousands of cultivars.',
            'common_location': 'Roses are cultivated worldwide for their ornamental flowers, which are used in gardens, landscaping, and floral arrangements. They are also grown for their fragrant petals, which are used in perfumery, cosmetics, and culinary applications.',
            'popular_usecase': 'Rose petals are used in herbal teas, culinary dishes, and skincare products for their delicate fragrance and flavor. Rose water is used as a culinary ingredient and flavoring agent, as well as a skincare tonic and perfume. Rose essential oil is used in aromatherapy for its calming, uplifting, and mood-enhancing effects. It is believed to reduce stress, anxiety, and depression, as well as promote relaxation and sleep. Rose oil is also used in skincare products for its moisturizing, anti-inflammatory, and anti-aging properties. It is used to hydrate the skin, reduce redness, and minimize the appearance of wrinkles and fine lines.',
            'Disclaimer': 'Consult a qualified aromatherapist or healthcare professional before using rose essential oil, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Rose is valued for its beauty, fragrance, and therapeutic properties. It is used to promote relaxation, uplift the mood, and enhance skin health.'
        }
    ],
    'Sapota': [
        {
            'scientific_name': 'Manilkara zapota',
            'scientific_medicinal_properties': 'Manilkara zapota, commonly known as sapota or chikoo, is a tropical fruit tree native to Mexico and Central America.',
            'common_location': 'Sapota trees are cultivated in tropical and subtropical regions worldwide for their edible fruits, which are prized for their sweet taste and creamy texture.',
            'popular_usecase': 'Sapota fruit is consumed fresh or processed into juice, jams, jellies, and culinary dishes. It is rich in vitamins, minerals, antioxidants, and dietary fiber. Sapota is known for its digestive, anti-inflammatory, and immune-boosting properties. It is used to promote digestion, relieve constipation, and support gastrointestinal health. Sapota seeds are also used in traditional medicine for their antimicrobial, antiparasitic, and anthelmintic properties. They are used to treat intestinal worms, fungal infections, and bacterial infections.',
            'Disclaimer': 'Consult a healthcare professional before using sapota, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Sapota is valued for its delicious taste and health benefits. It is used to support digestion, boost immunity, and promote overall well-being.'
        }
    ],
    'Tulasi': [
        {
            'scientific_name': 'Ocimum tenuiflorum',
            'scientific_medicinal_properties': 'Ocimum tenuiflorum, commonly known as holy basil or tulsi, is a sacred plant in Hinduism and Ayurveda. It is native to the Indian subcontinent.',
            'common_location': 'Tulsi is cultivated in home gardens, temples, and farms throughout India and Southeast Asia for its medicinal and religious significance.',
            'popular_usecase': 'Tulsi is used in Ayurvedic medicine for its adaptogenic, immunomodulatory, and antimicrobial properties. It is considered a rasayana herb, which promotes longevity, vitality, and overall well-being. Tulsi is used to reduce stress, support respiratory health, improve digestion, and enhance cognitive function. It is also used in religious rituals, prayers, and ceremonies as an offering to the gods and goddesses.',
            'Disclaimer': 'Consult a qualified Ayurvedic practitioner before using tulsi, especially if you have any medical conditions or are pregnant.',
            'lament_medicinal_property': 'Tulsi is valued for its sacred status and health-promoting properties. It is used to reduce stress, boost immunity, and promote overall wellness.'
        }
    ],
    'Wood_sorel': [
        {
            'scientific_name': 'Oxalis',
            'scientific_medicinal_properties': 'Oxalis is a genus of flowering plants in the family Oxalidaceae, commonly known as wood sorrel. There are over eight hundred species distributed worldwide.',
            'common_location': 'Wood sorrel plants are found in a variety of habitats, including woodlands, meadows, and gardens. They are native to temperate and subtropical regions of the Northern Hemisphere.',
            'popular_usecase': 'Wood sorrel leaves are edible and have a tangy, citrus-like flavor. They are used fresh in salads, soups, and sauces, or cooked as a potherb. Wood sorrel is rich in vitamin C, antioxidants, and dietary fiber. It is known for its diuretic, anti-inflammatory, and antimicrobial properties. Wood sorrel tea is used in traditional medicine for its cooling and detoxifying effects. It is used to promote urinary tract health, reduce inflammation, and support digestion. Wood sorrel leaves are also used topically for their astringent and soothing properties. They are applied to insect bites, rashes, and minor skin irritations to relieve itching and inflammation.',
            'Disclaimer': 'Consult a qualified healthcare professional before using wood sorrel, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Wood sorrel is valued for its tangy flavor and medicinal properties. It is used to promote urinary tract health, reduce inflammation, and support overall well-being.'
        }
    ],
}
"""




Plant_Details = {
    'Aloevera': [
        {
            'scientific_name': 'Aloe vera',
            'scientific_medicinal_properties': 'Aloe vera is a succulent plant species of the genus Aloe. It is cultivated for agricultural and medicinal uses.',
            'common_location': 'Aloe vera is native to the Arabian Peninsula, but it is cultivated worldwide in tropical and subtropical regions.',
            'popular_usecase': 'Aloe vera gel is widely used in cosmetics, skincare products, and herbal remedies. It is known for its moisturizing, soothing, and healing properties. Aloe vera gel is used to treat sunburn, skin irritation, acne, and wounds. It is also consumed internally as a dietary supplement for its potential health benefits, including digestive support, immune enhancement, and anti-inflammatory effects.',
            'Disclaimer': 'Consult a qualified healthcare professional before using aloe vera, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Aloe vera is valued for its soothing gel and therapeutic properties. It is used to promote skin health, relieve inflammation, and support overall well-being.'
        }
    ],
    'Amla': [
        {
            'scientific_name': 'Phyllanthus emblica',
            'scientific_medicinal_properties': 'Phyllanthus emblica, commonly known as Indian gooseberry or amla, is a deciduous tree native to the Indian subcontinent.',
            'common_location': 'Amla trees are found in forests, plains, and hilly regions throughout India, Nepal, Sri Lanka, and Southeast Asia.',
            'popular_usecase': 'Amla fruit is consumed fresh or processed into juice, jams, jellies, and culinary dishes. It is rich in vitamin C, antioxidants, and other nutrients. Amla is known for its digestive, immune-boosting, and anti-inflammatory properties. It is used to support digestion, enhance immunity, and promote overall well-being. Amla is also used in Ayurvedic medicine for its rejuvenating, anti-aging, and hair growth-promoting effects.',
            'Disclaimer': 'Consult a qualified healthcare professional before using amla, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Amla is valued for its sour taste and health benefits. It is used to support digestion, boost immunity, and promote overall wellness.'
        }
    ],
    'Amruta_Balli': [
        {
            'scientific_name': 'Tinospora cordifolia',
            'scientific_medicinal_properties': 'Tinospora cordifolia, commonly known as guduchi or amruta balli, is a climbing shrub in the family Menispermaceae.',
            'common_location': 'Tinospora cordifolia is found in tropical and subtropical regions of India, Sri Lanka, Myanmar, and other parts of Southeast Asia.',
            'popular_usecase': 'Tinospora cordifolia is used in traditional Ayurvedic medicine for its immunomodulatory, antioxidant, and anti-inflammatory properties. It is considered an adaptogen, which helps the body adapt to stress and maintain homeostasis. Tinospora cordifolia is used to boost immunity, improve liver function, and support overall well-being. It is also used to treat fever, respiratory infections, and digestive disorders. Tinospora cordifolia extract is used in herbal supplements, tonics, and remedies for its health-promoting effects.',
            'Disclaimer': 'Consult a qualified Ayurvedic practitioner before using tinospora cordifolia, especially if you have any medical conditions or are pregnant.',
            'lament_medicinal_property': 'Tinospora cordifolia is valued for its bitter taste and medicinal properties. It is used to boost immunity, support liver health, and promote overall wellness.'
        }
    ],
    'Arali': [
        {
            'scientific_name': 'Ficus racemosa',
            'scientific_medicinal_properties': 'Ficus racemosa, commonly known as cluster fig or arali, is a species of plant in the family Moraceae.',
            'common_location': 'Ficus racemosa is native to tropical and subtropical regions of Asia, including India, Sri Lanka, Nepal, and Southeast Asia.',
            'popular_usecase': 'Ficus racemosa is used in traditional medicine for its medicinal properties. It is believed to have anti-inflammatory, analgesic, and antimicrobial effects. Ficus racemosa is used to treat various ailments, including skin disorders, respiratory problems, and digestive issues. Its leaves, bark, and fruits are used in herbal remedies, decoctions, and poultices. Ficus racemosa is also valued for its edible fruits, which are consumed fresh or processed into jams, jellies, and culinary dishes.',
            'Disclaimer': 'Consult a qualified healthcare professional before using ficus racemosa, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Ficus racemosa is valued for its medicinal properties and edible fruits. It is used to treat various health conditions and promote overall well-being.',
        }
    ],
    'Ashoka': [
        {
            'scientific_name': 'Saraca asoca',
            'scientific_medicinal_properties': 'Saraca asoca, commonly known as ashoka or sorrowless tree, is a species of flowering plant in the family Fabaceae.',
            'common_location': 'Saraca asoca is native to the Indian subcontinent, particularly the Western Ghats and Eastern Ghats of India.',
            'popular_usecase': 'Saraca asoca is considered a sacred tree in Hinduism and Buddhism. It is associated with love, fertility, and feminine energy. Saraca asoca bark is used in traditional Ayurvedic medicine for its uterine tonic, anti-inflammatory, and analgesic properties. It is used to treat gynecological disorders, menstrual problems, and reproductive issues. Saraca asoca flowers are used in religious rituals, prayers, and ceremonies as offerings to the gods and goddesses. Saraca asoca is also planted as an ornamental tree in gardens, parks, and temples for its attractive foliage and flowers.',
            'Disclaimer': 'Consult a qualified Ayurvedic practitioner before using saraca asoca, especially if you have any medical conditions or are pregnant.',
            'lament_medicinal_property': "Saraca asoca is valued for its cultural significance and medicinal properties. It is used to support women's health, promote fertility, and enhance overall well-being."
        }
    ],
    'Ashwagandha': [
        {
            'scientific_name': 'Withania somnifera',
            'scientific_medicinal_properties': 'Withania somnifera, commonly known as ashwagandha or Indian ginseng, is a medicinal plant in the nightshade family Solanaceae.',
            'common_location': 'Withania somnifera is native to India, Pakistan, and Sri Lanka, but it is cultivated in other parts of Asia, Africa, and the Mediterranean region.',
            'popular_usecase': 'Withania somnifera is used in traditional Ayurvedic medicine as an adaptogen, which helps the body cope with stress and promote overall well-being. It is believed to have anti-inflammatory, antioxidant, and immunomodulatory effects. Withania somnifera is used to reduce stress, improve cognitive function, and enhance physical performance. It is also used to treat anxiety, depression, and insomnia. Withania somnifera root extract is used in herbal supplements, tonics, and remedies for its health-promoting properties.',
            'Disclaimer': 'Consult a qualified healthcare professional before using withania somnifera, especially if you have any medical conditions or are pregnant.',
            'lament_medicinal_property': 'Withania somnifera is valued for its adaptogenic properties and health benefits. It is used to reduce stress, boost immunity, and promote overall wellness.'
        }
    ],
    'Avacado': [
        {
            'scientific_name': 'Persea americana',
            'scientific_medicinal_properties': 'Persea americana, commonly known as avocado, is a tree native to South Central Mexico.',
            'common_location': 'Avocado trees are cultivated in tropical and subtropical regions worldwide for their edible fruits, which are prized for their rich flavor and creamy texture.',
            'popular_usecase': 'Avocado fruit is consumed fresh or processed into guacamole, salads, sandwiches, and culinary dishes. It is rich in healthy fats, vitamins, minerals, and antioxidants. Avocado is known for its heart-healthy properties, including lowering cholesterol levels and reducing the risk of heart disease. It is also used in skincare products for its moisturizing and anti-aging effects. Avocado oil is used in cooking, cosmetics, and massage therapy for its nourishing and hydrating properties.',
            'Disclaimer': 'Consult a qualified healthcare professional before using avocado, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Avocado is valued for its delicious taste and health benefits. It is used to support heart health, promote skin health, and enhance overall well-being.'
        }
    ],
    'Bamboo': [
        {
            'scientific_name': 'Bambusoideae',
            'scientific_medicinal_properties': 'Bamboo is a group of perennial evergreen plants in the subfamily Bambusoideae of the grass family Poaceae.',
            'common_location': 'Bamboo is native to various regions of the world, including Asia, Africa, and the Americas. It is widely cultivated for its economic, environmental, and cultural significance.',
            'popular_usecase': 'Bamboo is used for a wide range of purposes, including construction, furniture, papermaking, textiles, and food. Bamboo shoots are consumed as a vegetable in Asian cuisines and are valued for their nutritional benefits. Bamboo leaves, stems, and roots are used in traditional medicine for their medicinal properties. Bamboo extract is used in herbal remedies, supplements, and skincare products for its antioxidant, anti-inflammatory, and anti-aging effects.',
            'Disclaimer': 'Consult a qualified healthcare professional before using bamboo, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Bamboo is valued for its versatility and medicinal properties. It is used to promote health, support sustainability, and enhance overall well-being.'
        }
    ],
    'Basale': [
        {
            'scientific_name': 'Basella alba',
            'scientific_medicinal_properties': 'Basella alba, commonly known as Malabar spinach or basale, is a fast-growing vine in the family Basellaceae.',
            'common_location': 'Basella alba is native to tropical Asia, but it is cultivated in other parts of the world for its edible leaves and shoots.',
            'popular_usecase': 'Basella alba leaves and stems are consumed as a leafy vegetable in various cuisines, including Indian, Southeast Asian, and African cuisines. They are valued for their high nutritional content, including vitamins, minerals, and antioxidants. Basella alba is known for its cooling and diuretic properties. It is used to promote hydration, support kidney health, and reduce inflammation. Basella alba leaves are also used in traditional medicine for their medicinal properties. They are used to treat gastrointestinal disorders, respiratory problems, and skin conditions.',
            'Disclaimer': 'Consult a qualified healthcare professional before using basella alba, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Basella alba is valued for its nutritional value and health benefits. It is used to promote hydration, support kidney health, and enhance overall well-being.'
        }
    ],
    'Betel': [
        {
            'scientific_name': 'Piper betle',
            'scientific_medicinal_properties': 'Piper betle, commonly known as betel leaf or paan, is a vine belonging to the Piperaceae family.',
            'common_location': 'Piper betle is native to Southeast Asia, but it is cultivated in other parts of Asia for its medicinal and cultural significance.',
            'popular_usecase': 'Piper betle leaves are used in traditional medicine and cultural practices for their medicinal and stimulant properties. Betel leaves are chewed with areca nut, slaked lime, and other ingredients to make betel quid, a traditional preparation known as paan. Betel quid is used for its stimulating, euphoric, and digestive effects. It is believed to improve digestion, freshen breath, and increase alertness. Betel leaves are also used in religious rituals, prayers, and ceremonies as offerings to deities and ancestors.',
            'Disclaimer': 'Chewing betel quid can have adverse effects on oral health, including staining of teeth, gum disease, and oral cancer. Consult a qualified healthcare professional before using betel leaves.',
            'lament_medicinal_property': 'Piper betle is valued for its cultural significance and medicinal properties. It is used as a stimulant, digestive aid, and breath freshener.'
        }
    ],
    'Betel_Nut': [
        {
            'scientific_name': 'Areca catechu',
            'scientific_medicinal_properties': 'Areca catechu, commonly known as betel nut or areca nut, is the seed of the areca palm tree.',
            'common_location': 'Areca catechu is native to tropical and subtropical regions of Asia and the Pacific Islands.',
            'popular_usecase': 'Areca catechu seeds are chewed with betel leaves, slaked lime, and other ingredients to make betel quid, a traditional preparation known as paan. Betel quid is used for its stimulating, euphoric, and digestive effects. It is believed to improve digestion, freshen breath, and increase alertness. Areca catechu is also used in traditional medicine for its medicinal properties. It is used to treat digestive disorders, oral health problems, and parasitic infections. Areca catechu extract is used in herbal remedies and supplements for its potential health benefits.',
            'Disclaimer': 'Chewing betel quid can have adverse effects on oral health, including staining of teeth, gum disease, and oral cancer. Consult a qualified healthcare professional before using areca catechu.',
            'lament_medicinal_property': 'Areca catechu is valued for its stimulating properties and potential health benefits. It is used to promote digestion, freshen breath, and support overall well-being.'
        }
    ],
    'Brahmi': [
        {
            'scientific_name': 'Bacopa monnieri',
            'scientific_medicinal_properties': 'Bacopa monnieri, commonly known as brahmi or water hyssop, is a perennial herb native to wetlands and marshy areas of India, Southeast Asia, and Australia.',
            'common_location': 'Bacopa monnieri is found in tropical and subtropical regions worldwide, including India, Nepal, Sri Lanka, China, and the United States.',
            'popular_usecase': 'Bacopa monnieri is used in traditional Ayurvedic medicine as a brain tonic and adaptogen. It is believed to enhance cognitive function, memory, and concentration. Bacopa monnieri is used to reduce stress, anxiety, and depression. It is also used to treat epilepsy, asthma, and other neurological and respiratory disorders. Bacopa monnieri extract is used in herbal supplements and remedies for its potential health benefits.',
            'Disclaimer': 'Consult a qualified Ayurvedic practitioner before using bacopa monnieri, especially if you have any medical conditions or are pregnant.',
            'lament_medicinal_property': 'Bacopa monnieri is valued for its cognitive-enhancing properties and adaptogenic effects. It is used to support brain health, reduce stress, and promote overall well-being.'
        }
    ],
    'Castor': [
        {
            'scientific_name': 'Ricinus communis',
            'scientific_medicinal_properties': 'Ricinus communis, commonly known as castor bean or castor oil plant, is a species of flowering plant in the spurge family Euphorbiaceae.',
            'common_location': 'Ricinus communis is native to tropical and subtropical regions of Africa and Asia, but it is cultivated worldwide for its seeds, which are used to produce castor oil.',
            'popular_usecase': 'Castor oil is extracted from the seeds of Ricinus communis and is used in various industries, including cosmetics, pharmaceuticals, and manufacturing. Castor oil is valued for its moisturizing, emollient, and anti-inflammatory properties. It is used to treat skin conditions, such as dryness, itching, and inflammation. Castor oil is also used in traditional medicine for its laxative and purgative effects. It is used to relieve constipation, promote bowel movements, and cleanse the digestive system. Castor oil is also used in hair care products for its nourishing and conditioning properties.',
            'Disclaimer': 'Consult a qualified healthcare professional before using ricinus communis, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Ricinus communis is valued for its versatile uses and medicinal properties. It is used to promote skin health, support digestive health, and enhance overall well-being.'
        }
    ],
    'Curry_Leaf': [
        {
            'scientific_name': 'Murraya koenigii',
            'scientific_medicinal_properties': 'Murraya koenigii, commonly known as curry leaf or kadi patta, is a tropical to sub-tropical tree in the family Rutaceae.',
            'common_location': 'Murraya koenigii is native to India and Sri Lanka, but it is cultivated in other parts of Asia, Africa, and the Americas for its culinary and medicinal uses.',
            'popular_usecase': 'Murraya koenigii leaves are used as a flavoring agent in Indian cuisine, particularly South Indian and Sri Lankan dishes. They are valued for their aromatic and medicinal properties. Murraya koenigii leaves are rich in antioxidants, vitamins, and minerals. They are used to enhance the flavor and aroma of curries, soups, stews, and other dishes. Murraya koenigii leaves are also used in traditional medicine for their health benefits. They are used to treat digestive disorders, diabetes, and skin problems. Murraya koenigii extract is used in herbal remedies and supplements for its potential health-promoting effects.',
            'Disclaimer': 'Consult a qualified healthcare professional before using murraya koenigii, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Murraya koenigii is valued for its culinary and medicinal properties. It is used to enhance flavor, promote digestion, and support overall well-being.'
        }
    ],
    'Doddapatre': [
        {
            'scientific_name': 'Coleus amboinicus',
            'scientific_medicinal_properties': 'Coleus amboinicus, commonly known as Indian borage or doddapatre, is a perennial herb in the mint family Lamiaceae.',
            'common_location': 'Coleus amboinicus is native to Southern and Eastern Africa, but it is cultivated in other parts of the world for its culinary and medicinal uses.',
            'popular_usecase': 'Coleus amboinicus leaves are used as a culinary herb in various cuisines, including Indian, African, and Caribbean cuisines. They are valued for their aromatic and medicinal properties. Coleus amboinicus leaves are rich in essential oils, vitamins, and minerals. They are used to flavor curries, soups, stews, and other dishes. Coleus amboinicus is also used in traditional medicine for its health benefits. It is used to treat respiratory problems, digestive disorders, and skin conditions. Coleus amboinicus extract is used in herbal remedies and supplements for its potential health-promoting effects.',
            'Disclaimer': 'Consult a qualified healthcare professional before using coleus amboinicus, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Coleus amboinicus is valued for its culinary and medicinal properties. It is used to enhance flavor, promote respiratory health, and support overall well-being.'
        }
    ],
    'Ekka': [
        {
            'scientific_name': 'Tamarindus indica',
            'scientific_medicinal_properties': 'Tamarindus indica, commonly known as tamarind, is a leguminous tree in the family Fabaceae.',
            'common_location': 'Tamarindus indica is native to tropical Africa, but it is cultivated in other parts of the world for its edible fruit and other uses.',
            'popular_usecase': 'Tamarind fruit is used in cooking, beverages, and traditional medicine. It is valued for its sweet and sour flavor and culinary versatility. Tamarind is used to flavor curries, chutneys, sauces, and beverages. It is also used as a natural preservative and digestive aid. Tamarind pulp is used in traditional medicine for its laxative, diuretic, and anti-inflammatory properties. It is used to treat digestive disorders, fever, and skin conditions. Tamarind extract is used in herbal remedies and supplements for its potential health benefits.',
            'Disclaimer': 'Consult a qualified healthcare professional before using tamarindus indica, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Tamarindus indica is valued for its culinary and medicinal properties. It is used to enhance flavor, promote digestion, and support overall well-being.'
        }
    ],
    'Ganike': [
        {
            'scientific_name': 'Basil',
            'scientific_medicinal_properties': 'Ocimum basilicum',
            'common_location': 'Basil is native to tropical regions from central Africa to Southeast Asia. It is prominently featured in various cuisines throughout the world.',
            'popular_usecase': 'Basil is used in cuisines worldwide, particularly in Italian, Thai, and Vietnamese dishes. It is known for its sweet, aromatic flavor with hints of pepper, anise, and mint. Basil is used fresh or dried in salads, sauces, soups, and pasta dishes. It is also used to flavor oils, vinegars, and beverages. Basil is valued not only for its culinary uses but also for its medicinal properties. It is used in traditional medicine for its antibacterial, anti-inflammatory, and antioxidant effects. Basil is believed to promote digestion, relieve stress, and support overall well-being.',
            'Disclaimer': 'Consult a qualified healthcare professional before using basil, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Basil is valued for its culinary versatility and medicinal properties. It is used to enhance flavor, promote digestion, and support overall well-being.'
        }
    ],
    'Gauva': [
        {
            'scientific_name': 'Psidium guajava',
            'scientific_medicinal_properties': 'Psidium guajava, commonly known as guava, is a tropical fruit tree in the family Myrtaceae.',
            'common_location': 'Psidium guajava is native to tropical regions of Central America, but it is cultivated in other parts of the world for its edible fruit and other uses.',
            'popular_usecase': 'Guava fruit is consumed fresh or processed into juice, jams, jellies, and culinary dishes. It is valued for its sweet and tangy flavor, rich aroma, and nutritional benefits. Guava is high in vitamin C, fiber, and antioxidants. It is known for its digestive, immune-boosting, and anti-inflammatory properties. Guava is used to promote digestion, enhance immunity, and support overall well-being. Guava leaves and bark are used in traditional medicine for their medicinal properties. They are used to treat diarrhea, dysentery, and other gastrointestinal problems. Guava extract is used in herbal remedies and supplements for its potential health benefits.',
            'Disclaimer': 'Consult a qualified healthcare professional before using psidium guajava, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Psidium guajava is valued for its delicious taste and health benefits. It is used to promote digestion, boost immunity, and enhance overall well-being.'
        }
    ],
    'Geranium': [
        {
            'scientific_name': 'Pelargonium graveolens',
            'scientific_medicinal_properties': 'Pelargonium graveolens, commonly known as geranium, is a species of flowering plant in the family Geraniaceae.',
            'common_location': 'Pelargonium graveolens is native to South Africa, but it is cultivated in other parts of the world for its ornamental and medicinal uses.',
            'popular_usecase': 'Pelargonium graveolens essential oil is used in aromatherapy, skincare, and traditional medicine. It is valued for its sweet, floral aroma and therapeutic properties. Pelargonium graveolens oil is used to reduce stress, anxiety, and depression. It is also used to balance hormones, improve mood, and promote relaxation. Pelargonium graveolens oil is used topically to treat skin conditions, such as acne, eczema, and dermatitis. It is also used in massage therapy for its soothing and anti-inflammatory effects. Pelargonium graveolens leaves and flowers are used in herbal teas, infusions, and poultices for their potential health benefits.',
            'Disclaimer': 'Consult a qualified healthcare professional before using pelargonium graveolens, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Pelargonium graveolens is valued for its aromatic fragrance and medicinal properties. It is used to promote relaxation, improve mood, and support skin health.'
        }
    ],
    'Henna': [
        {
            'scientific_name': 'Lawsonia inermis',
            'scientific_medicinal_properties': 'Lawsonia inermis, commonly known as henna, is a flowering plant in the family Lythraceae.',
            'common_location': 'Lawsonia inermis is native to tropical and subtropical regions of Africa, Asia, and Australia.',
            'popular_usecase': 'Henna leaves are used to produce a natural dye known as henna or mehndi. Henna dye is used to color hair, skin, and nails for cosmetic and decorative purposes. It is valued for its vibrant color, long-lasting stain, and cooling properties. Henna paste is applied to the skin in intricate designs for temporary body art and tattoos. Henna is also used in traditional medicine for its medicinal properties. It is used to treat various skin conditions, such as eczema, psoriasis, and burns. Henna extract is used in herbal remedies and cosmetics for its potential health benefits.',
            'Disclaimer': 'Consult a qualified healthcare professional before using lawsonia inermis, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Lawsonia inermis is valued for its cosmetic and medicinal uses. It is used to color hair, adorn skin, and treat various skin conditions.'
        }
    ],
    'Hibiscus': [
        {
            'scientific_name': 'Hibiscus sabdariffa',
            'scientific_medicinal_properties': 'Hibiscus sabdariffa, commonly known as roselle or hibiscus, is a species of flowering plant in the family Malvaceae.',
            'common_location': 'Hibiscus sabdariffa is native to West Africa, but it is cultivated in other parts of the world for its edible calyxes and other uses.',
            'popular_usecase': 'Hibiscus sabdariffa calyxes are used to produce a popular beverage known as hibiscus tea or sorrel. Hibiscus tea is valued for its tart flavor, deep red color, and health benefits. It is high in vitamin C, antioxidants, and other nutrients. Hibiscus tea is known for its cooling, diuretic, and cardiovascular benefits. It is used to lower blood pressure, reduce cholesterol levels, and promote overall well-being. Hibiscus sabdariffa flowers and leaves are used in traditional medicine for their medicinal properties. They are used to treat various health conditions, including hypertension, liver disorders, and digestive problems. Hibiscus extract is used in herbal remedies and supplements for its potential health-promoting effects.',
            'Disclaimer': 'Consult a qualified healthcare professional before using hibiscus sabdariffa, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Hibiscus sabdariffa is valued for its refreshing taste and health benefits. It is used to promote cardiovascular health, support digestion, and enhance overall well-being.'
        }
    ],
    'Honge': [
        {
            'scientific_name': 'Pongamia pinnata',
            'scientific_medicinal_properties': 'Pongamia pinnata, commonly known as Indian beech or honge, is a species of tree in the pea family Fabaceae.',
            'common_location': 'Pongamia pinnata is native to tropical and subtropical regions of Asia and Australia.',
            'popular_usecase': 'Pongamia pinnata seeds are used in traditional medicine and industrial applications. They are valued for their medicinal properties and biodiesel potential. Pongamia pinnata oil is extracted from the seeds and used in skincare products, soaps, and lubricants. Pongamia pinnata extract is used in herbal remedies and supplements for its potential health benefits. It is used to treat various health conditions, including skin disorders, inflammation, and infections. Pongamia pinnata leaves, bark, and roots are also used in traditional medicine for their medicinal properties.',
            'Disclaimer': 'Consult a qualified healthcare professional before using pongamia pinnata, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Pongamia pinnata is valued for its versatile uses and medicinal properties. It is used to promote skin health, reduce inflammation, and support overall well-being.'
        }
    ],
    'Insulin': [
        {
            'scientific_name': 'Coccinia grandis',
            'scientific_medicinal_properties': 'Coccinia grandis, commonly known as ivy gourd or insulin plant, is a tropical vine in the family Cucurbitaceae.',
            'common_location': 'Coccinia grandis is native to tropical regions of Asia, including India, Sri Lanka, and Southeast Asia.',
            'popular_usecase': 'Coccinia grandis leaves and fruits are used in traditional medicine and culinary dishes. They are valued for their medicinal properties and culinary uses. Coccinia grandis is used to regulate blood sugar levels and promote insulin sensitivity. It is used as a natural remedy for diabetes and related metabolic disorders. Coccinia grandis is also used to treat various health conditions, including digestive disorders, fever, and skin problems. Coccinia grandis extract is used in herbal remedies and supplements for its potential health benefits.',
            'Disclaimer': 'Consult a qualified healthcare professional before using coccinia grandis, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Coccinia grandis is valued for its medicinal properties and culinary uses. It is used to regulate blood sugar levels, support digestion, and promote overall well-being.'
        }
    ],
    'Jasmine': [
        {
            'scientific_name': 'Jasminum',
            'scientific_medicinal_properties': 'Jasminum is a genus of shrubs and vines in the olive family Oleaceae.',
            'common_location': 'Jasminum species are native to tropical and subtropical regions of Eurasia, Oceania, and Africa. They are cultivated for their fragrant flowers and essential oils.',
            'popular_usecase': 'Jasminum flowers are valued for their sweet, floral fragrance and ornamental beauty. They are used in perfumery, aromatherapy, and religious rituals. Jasminum essential oil is extracted from the flowers and used in skincare products, massage oils, and perfumes. Jasminum flowers are also used in traditional medicine for their medicinal properties. They are used to reduce stress, anxiety, and depression. Jasminum essential oil is used to promote relaxation, improve mood, and enhance overall well-being.',
            'Disclaimer': 'Consult a qualified healthcare professional before using jasminum, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Jasminum is valued for its fragrant flowers and medicinal properties. It is used to promote relaxation, reduce stress, and enhance overall well-being.'
        }
    ],
    'Lemon': [
        {
            'scientific_name': 'Citrus limon',
            'scientific_medicinal_properties': 'Citrus limon, commonly known as lemon, is a species of small evergreen tree in the flowering plant family Rutaceae.',
            'common_location': 'Citrus limon is native to South Asia, but it is cultivated in other parts of the world for its edible fruit and other uses.',
            'popular_usecase': 'Lemon fruit is consumed fresh or processed into juice, jams, jellies, and culinary dishes. It is valued for its tart flavor, refreshing taste, and nutritional benefits. Lemon is high in vitamin C, antioxidants, and other nutrients. It is known for its digestive, immune-boosting, and detoxifying properties. Lemon juice is used in cooking, baking, and beverages for its flavor-enhancing and preservative effects. Lemon peel and zest are used in culinary dishes, desserts, and herbal remedies. Lemon essential oil is used in aromatherapy, skincare, and household cleaning products for its fresh, uplifting fragrance and antibacterial properties.',
            'Disclaimer': 'Consult a qualified healthcare professional before using citrus limon, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Citrus limon is valued for its refreshing taste and health benefits. It is used to promote digestion, boost immunity, and enhance overall well-being.'
        }
    ],
    'Lemon_grass': [
        {
            'scientific_name': 'Cymbopogon citratus',
            'scientific_medicinal_properties': 'Cymbopogon citratus, commonly known as lemongrass, is a tropical plant in the grass family Poaceae.',
            'common_location': 'Cymbopogon citratus is native to Southeast Asia, but it is cultivated in other parts of the world for its culinary and medicinal uses.',
            'popular_usecase': 'Cymbopogon citratus leaves and stems are used as a culinary herb in various cuisines, particularly Southeast Asian, Indian, and African cuisines. They are valued for their citrusy flavor and aromatic fragrance. Cymbopogon citratus is used to flavor soups, curries, teas, and beverages. It is also used in marinades, sauces, and salad dressings. Cymbopogon citratus is known for its medicinal properties. It is used to promote digestion, relieve stress, and reduce inflammation. Cymbopogon citratus essential oil is used in aromatherapy, skincare, and massage therapy for its relaxing and antibacterial effects.',
            'Disclaimer': 'Consult a qualified healthcare professional before using cymbopogon citratus, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Cymbopogon citratus is valued for its culinary and medicinal properties. It is used to enhance flavor, promote relaxation, and support overall well-being.'
        }
    ],
    'Mango': [
        {
            'scientific_name': 'Mangifera indica',
            'scientific_medicinal_properties': 'Mangifera indica, commonly known as mango, is a species of flowering plant in the family Anacardiaceae.',
            'common_location': 'Mangifera indica is native to South Asia, but it is cultivated in other tropical and subtropical regions of the world for its edible fruit and other uses.',
            'popular_usecase': 'Mango fruit is consumed fresh or processed into juice, jams, jellies, and culinary dishes. It is valued for its sweet flavor, rich aroma, and nutritional benefits. Mango is high in vitamins, minerals, antioxidants, and fiber. It is known for its digestive, immune-boosting, and skin-nourishing properties. Mango is used to promote digestion, enhance immunity, and support overall well-being. Mango leaves, bark, and seeds are also used in traditional medicine for their medicinal properties. They are used to treat various health conditions, including diarrhea, fever, and inflammation. Mango extract is used in herbal remedies and supplements for its potential health benefits.',
            'Disclaimer': 'Consult a qualified healthcare professional before using mangifera indica, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Mangifera indica is valued for its delicious taste and health benefits. It is used to promote digestion, boost immunity, and enhance overall well-being.'
        }
    ],
    'Mint': [
        {
            'scientific_name': 'Mentha',
            'scientific_medicinal_properties': 'Mentha is a genus of flowering plants in the mint family Lamiaceae.',
            'common_location': 'Mentha species are native to temperate regions of Eurasia, but they are cultivated worldwide for their culinary and medicinal uses.',
            'popular_usecase': 'Mentha leaves and stems are used as a culinary herb and medicinal remedy. They are valued for their refreshing flavor and aromatic fragrance. Mentha is used to flavor beverages, desserts, salads, sauces, and other culinary dishes. It is also used in teas, infusions, and herbal remedies. Mentha is known for its medicinal properties. It is used to promote digestion, relieve nausea, and reduce inflammation. Mentha essential oil is used in aromatherapy, skincare, and massage therapy for its cooling and soothing effects. Mentha leaves are also used in traditional medicine for their potential health benefits.',
            'Disclaimer': 'Consult a qualified healthcare professional before using mentha, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Mentha is valued for its culinary and medicinal properties. It is used to enhance flavor, promote digestion, and support overall well-being.'
        }
    ],
    'Nagadali': [
        {
            'scientific_name': 'Cynodon dactylon',
            'scientific_medicinal_properties': 'Cynodon dactylon, commonly known as Bermuda grass or nagadali, is a perennial grass in the family Poaceae.',
            'common_location': 'Cynodon dactylon is native to tropical and subtropical regions worldwide and is widely cultivated as a turfgrass and forage crop.',
            'popular_usecase': 'Cynodon dactylon is used for various purposes, including landscaping, erosion control, and forage production. It is valued for its tolerance to heat, drought, and foot traffic. Cynodon dactylon is also used in traditional medicine for its medicinal properties. It is used to treat various health conditions, including digestive disorders, respiratory problems, and skin infections. Cynodon dactylon extract is used in herbal remedies and supplements for its potential health benefits.',
            'Disclaimer': 'Consult a qualified healthcare professional before using cynodon dactylon, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Cynodon dactylon is valued for its versatility and medicinal properties. It is used to promote health, support digestion, and enhance overall well-being.'
        }
    ],
    'Neem': [
        {
            'scientific_name': 'Azadirachta indica',
            'scientific_medicinal_properties': 'Azadirachta indica, commonly known as neem, is a tree native to the Indian subcontinent.',
            'common_location': 'Azadirachta indica is found in tropical and subtropical regions of Asia and Africa. It is widely cultivated for its medicinal, culinary, and environmental uses.',
            'popular_usecase': 'Azadirachta indica is used in traditional medicine, agriculture, and personal care products. Neem leaves, bark, seeds, and oil are used for their medicinal properties. They are used to treat various health conditions, including skin disorders, diabetes, and infections. Neem is also used as a natural pesticide, insect repellent, and fertilizer in agriculture. Neem oil is used in skincare products, soaps, and shampoos for its antibacterial, antifungal, and moisturizing properties. Neem extract is used in herbal remedies and supplements for its potential health benefits.',
            'Disclaimer': 'Consult a qualified healthcare professional before using azadirachta indica, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Azadirachta indica is valued for its versatile uses and medicinal properties. It is used to promote skin health, support immunity, and enhance overall well-being.'
        }
    ],
    'Nithyapushpa': [
        {
            'scientific_name': 'Catharanthus roseus',
            'scientific_medicinal_properties': 'Catharanthus roseus, commonly known as Madagascar periwinkle or nithyapushpa, is a species of flowering plant in the family Apocynaceae.',
            'common_location': 'Catharanthus roseus is native to Madagascar, but it is cultivated in other parts of the world for its ornamental and medicinal uses.',
            'popular_usecase': 'Catharanthus roseus is used in traditional medicine and pharmaceuticals. It is valued for its medicinal properties and compounds, such as alkaloids and vincristine. Catharanthus roseus is used to treat various health conditions, including cancer, diabetes, and malaria. It is also used as a natural insecticide and pesticide in agriculture. Catharanthus roseus extract is used in herbal remedies and supplements for its potential health benefits.',
            'Disclaimer': 'Consult a qualified healthcare professional before using catharanthus roseus, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Catharanthus roseus is valued for its medicinal properties and compounds. It is used to treat cancer, diabetes, and other health conditions.'
        }
    ],
    'Nooni': [
        {
            'scientific_name': 'Solanum nigrum',
            'scientific_medicinal_properties': 'Solanum nigrum, commonly known as black nightshade or nooni, is a species of flowering plant in the nightshade family Solanaceae.',
            'common_location': 'Solanum nigrum is found in temperate and tropical regions worldwide, including Asia, Africa, Europe, and North America.',
            'popular_usecase': 'Solanum nigrum is used in traditional medicine and culinary dishes. It is valued for its medicinal properties and culinary uses. Solanum nigrum is used to treat various health conditions, including inflammation, fever, and gastrointestinal disorders. It is also used as a natural diuretic and laxative. Solanum nigrum leaves, berries, and roots are used in herbal remedies and supplements for their potential health benefits.',
            'Disclaimer': 'Consult a qualified healthcare professional before using solanum nigrum, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Solanum nigrum is valued for its medicinal properties and culinary uses. It is used to promote health, support digestion, and enhance overall well-being.'
        }
    ],
    'Pappaya': [
        {
            'scientific_name': 'Carica papaya',
            'scientific_medicinal_properties': 'Carica papaya, commonly known as papaya, is a tropical fruit tree in the family Caricaceae.',
            'common_location': 'Carica papaya is native to tropical regions of the Americas, but it is cultivated in other parts of the world for its edible fruit and other uses.',
            'popular_usecase': 'Papaya fruit is consumed fresh or processed into juice, jams, jellies, and culinary dishes. It is valued for its sweet flavor, rich aroma, and nutritional benefits. Papaya is high in vitamins, minerals, antioxidants, and fiber. It is known for its digestive, immune-boosting, and skin-nourishing properties. Papaya is used to promote digestion, enhance immunity, and support overall well-being. Papaya seeds, leaves, and latex are also used in traditional medicine for their medicinal properties. They are used to treat various health conditions, including digestive disorders, inflammation, and parasitic infections. Papaya extract is used in herbal remedies and supplements for its potential health benefits.',
            'Disclaimer': 'Consult a qualified healthcare professional before using carica papaya, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Carica papaya is valued for its delicious taste and health benefits. It is used to promote digestion, boost immunity, and enhance overall well-being.'
        }
    ],
    'Pepper': [
        {
            'scientific_name': 'Piper nigrum',
            'scientific_medicinal_properties': 'Piper nigrum, commonly known as black pepper, is a flowering vine in the family Piperaceae.',
            'common_location': 'Piper nigrum is native to South India, but it is cultivated in other tropical regions of Asia, Africa, and the Americas.',
            'popular_usecase': 'Piper nigrum berries are used as a spice and seasoning in culinary dishes worldwide. They are valued for their spicy, pungent flavor and aromatic fragrance. Piper nigrum is used to flavor soups, stews, sauces, marinades, and other savory dishes. It is also used in pickling, preserves, and beverages. Piper nigrum is known for its medicinal properties. It is used to promote digestion, relieve nausea, and reduce inflammation. Piper nigrum essential oil is used in aromatherapy, skincare, and massage therapy for its warming and analgesic effects. Piper nigrum extract is used in herbal remedies and supplements for its potential health benefits.',
            'Disclaimer': 'Consult a qualified healthcare professional before using piper nigrum, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Piper nigrum is valued for its culinary and medicinal properties. It is used to enhance flavor, promote digestion, and support overall well-being.'
        }
    ],
    'Pomegranate': [
        {
            'scientific_name': 'Punica granatum',
            'scientific_medicinal_properties': 'Punica granatum, commonly known as pomegranate, is a fruit-bearing deciduous shrub or small tree in the family Lythraceae.',
            'common_location': 'Punica granatum is native to the region of modern-day Iran, but it is cultivated in other parts of the world for its edible fruit and other uses.',
            'popular_usecase': 'Pomegranate fruit is consumed fresh or processed into juice, jams, jellies, and culinary dishes. It is valued for its sweet and tangy flavor, rich aroma, and nutritional benefits. Pomegranate is high in vitamins, minerals, antioxidants, and fiber. It is known for its cardiovascular, anti-inflammatory, and anti-cancer properties. Pomegranate is used to promote heart health, reduce inflammation, and protect against oxidative stress. Pomegranate juice and extract are used in functional foods, beverages, and dietary supplements for their potential health benefits.',
            'Disclaimer': 'Consult a qualified healthcare professional before using punica granatum, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Punica granatum is valued for its delicious taste and health benefits. It is used to promote heart health, reduce inflammation, and enhance overall well-being.'
        }
    ],
    'Raktachandini': [
        {
            'scientific_name': 'Hibiscus rosa-sinensis',
            'scientific_medicinal_properties': 'Hibiscus rosa-sinensis, commonly known as Chinese hibiscus or raktachandini, is a species of flowering plant in the family Malvaceae.',
            'common_location': 'Hibiscus rosa-sinensis is native to East Asia, but it is cultivated in other parts of the world for its ornamental and medicinal uses.',
            'popular_usecase': 'Hibiscus rosa-sinensis flowers are valued for their ornamental beauty and medicinal properties. They are used in landscaping, gardens, and traditional medicine. Hibiscus rosa-sinensis is used to treat various health conditions, including hypertension, diabetes, and fever. It is also used as a natural hair and skincare remedy. Hibiscus rosa-sinensis extract is used in herbal remedies and supplements for its potential health benefits.',
            'Disclaimer': 'Consult a qualified healthcare professional before using hibiscus rosa-sinensis, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Hibiscus rosa-sinensis is valued for its medicinal properties and ornamental beauty. It is used to promote health, treat diseases, and enhance overall well-being.'
        }
    ],
    'Rose': [
        {
            'scientific_name': 'Rosa',
            'scientific_medicinal_properties': 'Rosa is a genus of flowering plants in the rose family Rosaceae.',
            'common_location': 'Rosa species are native to temperate regions of the Northern Hemisphere, but they are cultivated worldwide for their ornamental and medicinal uses.',
            'popular_usecase': 'Rosa flowers are valued for their ornamental beauty and medicinal properties. They are used in gardens, landscaping, and traditional medicine. Rosa petals are used to make rose water, perfumes, and cosmetics. Rose water is used in skincare products, aromatherapy, and culinary dishes. Rosa hips, the fruit of the rose plant, are high in vitamin C and antioxidants. They are used to make herbal teas, jams, jellies, and dietary supplements. Rosa extract is used in herbal remedies and supplements for its potential health benefits.',
            'Disclaimer': 'Consult a qualified healthcare professional before using rosa, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Rosa is valued for its ornamental beauty and medicinal properties. It is used to promote health, enhance beauty, and support overall well-being.'
        }
    ],
    'Sapota': [
        {
            'scientific_name': 'Manilkara zapota',
            'scientific_medicinal_properties': 'Manilkara zapota, commonly known as sapodilla or sapota, is a tropical fruit tree in the family Sapotaceae.',
            'common_location': 'Manilkara zapota is native to southern Mexico, Central America, and the Caribbean, but it is cultivated in other tropical regions of the world for its edible fruit and other uses.',
            'popular_usecase': 'Sapodilla fruit is consumed fresh or processed into juice, jams, jellies, and culinary dishes. It is valued for its sweet flavor, rich aroma, and nutritional benefits. Sapodilla is high in vitamins, minerals, antioxidants, and fiber. It is known for its digestive, immune-boosting, and skin-nourishing properties. Sapodilla is used to promote digestion, enhance immunity, and support overall well-being. Sapodilla seeds, bark, and latex are also used in traditional medicine for their medicinal properties. They are used to treat various health conditions, including coughs, diarrhea, and skin problems. Sapodilla extract is used in herbal remedies and supplements for its potential health benefits.',
            'Disclaimer': 'Consult a qualified healthcare professional before using manilkara zapota, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Manilkara zapota is valued for its delicious taste and health benefits. It is used to promote digestion, boost immunity, and enhance overall well-being.'
        }
    ],
    'Tulasi': [
        {
            'scientific_name': 'Ocimum tenuiflorum',
            'scientific_medicinal_properties': 'Ocimum tenuiflorum, commonly known as holy basil or tulsi, is an aromatic perennial plant in the family Lamiaceae.',
            'common_location': 'Ocimum tenuiflorum is native to the Indian subcontinent, but it is cultivated in other parts of the world for its medicinal and spiritual significance.',
            'popular_usecase': 'Ocimum tenuiflorum leaves are used in culinary dishes, teas, and traditional medicine. They are valued for their aromatic fragrance and medicinal properties. Ocimum tenuiflorum is used to promote respiratory health, relieve stress, and support overall well-being. It is considered a sacred plant in Hinduism and is used in religious rituals and ceremonies. Ocimum tenuiflorum extract is used in herbal remedies and supplements for its potential health benefits.',
            'Disclaimer': 'Consult a qualified healthcare professional before using ocimum tenuiflorum, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Ocimum tenuiflorum is valued for its spiritual significance and medicinal properties. It is used to promote health, relieve stress, and enhance overall well-being.'
        }
    ],
    'Wood_sorel': [
        {
            'scientific_name': 'Oxalis',
            'scientific_medicinal_properties': 'Oxalis is a large genus of flowering plants in the wood-sorrel family Oxalidaceae.',
            'common_location': 'Oxalis species are found worldwide, especially in temperate and tropical regions. They are commonly cultivated as ornamental plants.',
            'popular_usecase': 'Oxalis leaves, stems, and flowers are used in culinary dishes and traditional medicine. They are valued for their tart flavor and medicinal properties. Oxalis is used as a culinary ingredient in salads, soups, sauces, and garnishes. It is also used in teas, infusions, and herbal remedies. Oxalis is known for its antioxidant, anti-inflammatory, and diuretic effects. It is used to promote urinary tract health, relieve inflammation, and support overall well-being. Oxalis extract is used in herbal remedies and supplements for its potential health benefits.',
            'Disclaimer': 'Consult a qualified healthcare professional before using oxalis, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Oxalis is valued for its culinary and medicinal properties. It is used to enhance flavor, promote urinary tract health, and support overall well-being.'
        }
    ]
} 

print(len(Plant_Details))
if __name__ == "__main__":
    pass