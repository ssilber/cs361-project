# Microservice Goal
Generically, a microservice that reads from a text file, makes a GET request to an endpoint that returns a JSON blob, and overwrites the same text file with a random string from that JSON blob. For my specific use case, the JSON blob will contain a list of the clubs in the database for my webapp, and the microservice would randomly write one of the club names back to the file.

## Text File
- Name: microservice.txt
- Keyword written to file start service: "GET" (no quotes)
- Data written back: A randomly selected club name (string)

## API

The GET request will get all clubs listed in the database. Note that I don't have my webapp hosted online at the moment, but you can [clone my repo here](https://github.com/ssilber/cs361-project) and run it. I've created a Docker container for the app and the README has instructions on how to deploy (you can also run it without the Docker container if needed)



Endpoint:
```bash
http://0.0.0.0:5000/api/clubs
```

Response Body Format:
JSON

Example Response:

```bash
[
	{
		"city": "Liverpool, England",
		"image_url": "/static/images/liverpool_crest.png",
		"league": "Premier League",
		"name": "Liverpool",
		"stadium_name": "Anfield",
		"standings": {
		"2019": 2,
		"2020": 1,
		"2021": 3
		},
		"year_founded": 1892
	},
	{
		"city": "London, England",
		"image_url": "/static/images/chelsea_crest.png",
		"league": "Premier League",
		"name": "Chelsea",
		"stadium_name": "Stamford Bridge",
		"standings": {
		"2019": 3,
		"2020": 4,
		"2021": 4
		},
		"year_founded": 1905
	},
	{
		"city": "Turin, Italy",
		"image_url": "/static/images/juventus_crest.png",
		"league": "Serie A",
		"name": "Juventus",
		"stadium_name": "Allianz Stadium",
		"standings": {
		"2019": 1,
		"2020": 1,
		"2021": 4
		},
		"year_founded": 1897
	},
	{
		"city": "Milan, Italy",
		"image_url": "/static/images/inter_milan_crest.png",
		"league": "Serie A",
		"name": "Inter Milan",
		"stadium_name": "San Siro",
		"standings": {
		"2019": 4,
		"2020": 2,
		"2021": 1
		},
		"year_founded": 1908
	},
	{
		"city": "Paris, France",
		"image_url": "/static/images/psg_crest.png",
		"league": "Ligue 1",
		"name": "Paris Saint-Germain",
		"stadium_name": "Parc des Princes",
		"standings": {
		"2019": 1,
		"2020": 1,
		"2021": 2
		},
		"year_founded": 1970
	},
	{
		"city": "Marseille, France",
		"image_url": "/static/images/marseille_crest.png",
		"league": "Ligue 1",
		"name": "Marseille",
		"stadium_name": "Stade Vélodrome",
		"standings": {
		"2019": 5,
		"2020": 2,
		"2021": 5
		},
		"year_founded": 1899
	},
	{
		"city": "Barcelona, Spain",
		"image_url": "/static/images/barcelona_crest.png",
		"league": "La Liga",
		"name": "Barcelona",
		"stadium_name": "Camp Nou",
		"standings": {
		"2019": 1,
		"2020": 2,
		"2021": 3
		},
		"year_founded": 1925
	},
	{
		"city": "Madrid, Spain",
		"image_url": "/static/images/real_madrid_crest.png",
		"league": "La Liga",
		"name": "Real Madrid",
		"stadium_name": "Santiago Bernabéu Stadium",
		"standings": {
		"2019": 3,
		"2020": 1,
		"2021": 2
		},
		"year_founded": 1902
	},
	{
		"city": "Munich, Germany",
		"image_url": "/static/images/bayern_munich_crest.png",
		"league": "Bundesliga",
		"name": "Bayern Munich",
		"stadium_name": "Allianz Arena",
		"standings": {
		"2019": 1,
		"2020": 1,
		"2021": 1
		},
		"year_founded": 1900
	},
	{
		"city": "Dortmund, Germany",
		"image_url": "/static/images/bvb_crest.png",
		"league": "Bundesliga",
		"name": "Borussia Dortmund",
		"stadium_name": "Westfalenstadion",
		"standings": {
		"2019": 2,
		"2020": 2,
		"2021": 3
		},
		"year_founded": 1909
	}
]
```

