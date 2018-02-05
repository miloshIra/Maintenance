# Maintenance

   #TABELI
#masina (id, oddel, broj)
#aktivnost (id, ime)
#3masina_aktivnost(masina_id, aktivnost_id, #frekfentnost, datum_podmackuvanje)

SELECT m.id
FROM masina m
JOIN masina_aktivnost ma
ON m.id = ma.masina_id
WHERE NOW() - datum_podmackuvanje > frekfentnos

"""" CONNECTING DATABASES """""

import psycopg2 as psy

link = psy.connect("dbname='NAME' user='USER' password='PASSWORD' host='localhost' post='5432'"")
cur=link.cursor()
cur.execute("QUERY COMMAND HERE")
link.commit() > makes things happen
link.close() > closes the link connection
