from django.shortcuts import render
from django.http import HttpResponse 
import tensorflow as tf
from PIL import Image
import numpy as np

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

class_name = ['Aloevera', 'Amla', 'Amruta_Balli', 'Arali', 'Ashoka', 'Ashwagandha', 'Avacado', 'Bamboo', 'Basale', 'Betel', 'Betel_Nut', 'Brahmi', 'Castor', 'Curry_Leaf', 'Doddapatre', 'Ekka', 'Ganike', 'Gauva', 'Geranium', 'Henna', 'Hibiscus', 'Honge', 'Insulin', 'Jasmine', 'Lemon', 'Lemon_grass', 'Mango', 'Mint', 'Nagadali', 'Neem', 'Nithyapushpa', 'Nooni', 'Pappaya', 'Pepper', 'Pomegranate', 'Raktachandini', 'Rose', 'Sapota', 'Tulasi', 'Wood_sorel']


# Create your views here.
def home(request):
    model = tf.keras.models.load_model("D:/Coding/MachineLearning/FloraFinder/models/1/1.keras")
    print(model)
    result = ""
    details = ""
    if request.method == 'POST':
        # Get the uploaded image
        image_file = request.FILES['image']
        # Open the image using PIL
        image = Image.open(image_file)
        # Preprocess the image (if needed)
        # For example, resize the image to match the input size of the model
        image = image.resize((256, 256))  # Replace width and height with your model's input size
        # Convert the image to a numpy array
        image_array = np.array(image)
        image_array = np.expand_dims(image_array,0)
        # Perform prediction using your model
        prediction = model.predict(image_array)
        # Process the prediction (if needed)
        # For example, convert prediction to human-readable format
        result = class_name[np.argmax(prediction[0])]
        details = Plant_Details[result]
        return render(request,"home.html",{"prediction":details})
    return render(request,"home.html",{"prediction" : ""})