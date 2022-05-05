from dataclasses import dataclass

MICROSERVICE_FILEPATH = "microservice.txt"
MICROSERVICE_REQUEST_TEXT = "GET"

clubs_dict = [
    {
        "name": "Liverpool",
        "league": "Premier League",
        "city": "Liverpool, England",
        "year_founded": 1892,
        "stadium_name": "Anfield",
        "image_url": "/static/images/liverpool_crest.png",
        "standings": {"2021": 3, "2020": 1, "2019": 2},
    },
    {
        "name": "Chelsea",
        "league": "Premier League",
        "city": "London, England",
        "year_founded": 1905,
        "stadium_name": "Stamford Bridge",
        "image_url": "/static/images/chelsea_crest.png",
        "standings": {"2021": 4, "2020": 4, "2019": 3},
    },
    {
        "name": "Juventus",
        "league": "Serie A",
        "city": "Turin, Italy",
        "year_founded": 1897,
        "stadium_name": "Allianz Stadium",
        "image_url": "/static/images/juventus_crest.png",
        "standings": {"2021": 4, "2020": 1, "2019": 1},
    },
    {
        "name": "Inter Milan",
        "league": "Serie A",
        "city": "Milan, Italy",
        "year_founded": 1908,
        "stadium_name": "San Siro",
        "image_url": "/static/images/inter_milan_crest.png",
        "standings": {"2021": 1, "2020": 2, "2019": 4},
    },
    {
        "name": "Paris Saint-Germain",
        "league": "Ligue 1",
        "city": "Paris, France",
        "year_founded": 1970,
        "stadium_name": "Parc des Princes",
        "image_url": "/static/images/psg_crest.png",
        "standings": {"2021": 2, "2020": 1, "2019": 1},
    },
    {
        "name": "Marseille",
        "league": "Ligue 1",
        "city": "Marseille, France",
        "year_founded": 1899,
        "stadium_name": "Stade Vélodrome",
        "image_url": "/static/images/marseille_crest.png",
        "standings": {"2021": 5, "2020": 2, "2019": 5},
    },
    {
        "name": "Barcelona",
        "league": "La Liga",
        "city": "Barcelona, Spain",
        "year_founded": 1925,
        "stadium_name": "Camp Nou",
        "image_url": "/static/images/barcelona_crest.png",
        "standings": {"2021": 3, "2020": 2, "2019": 1},
    },
    {
        "name": "Real Madrid",
        "league": "La Liga",
        "city": "Madrid, Spain",
        "year_founded": 1902,
        "stadium_name": "Santiago Bernabéu Stadium",
        "image_url": "/static/images/real_madrid_crest.png",
        "standings": {"2021": 2, "2020": 1, "2019": 3},
    },
    {
        "name": "Bayern Munich",
        "league": "Bundesliga",
        "city": "Munich, Germany",
        "year_founded": 1900,
        "stadium_name": "Allianz Arena",
        "image_url": "/static/images/bayern_munich_crest.png",
        "standings": {"2021": 1, "2020": 1, "2019": 1},
    },
    {
        "name": "Borussia Dortmund",
        "league": "Bundesliga",
        "city": "Dortmund, Germany",
        "year_founded": 1909,
        "stadium_name": "Westfalenstadion",
        "image_url": "/static/images/bvb_crest.png",
        "standings": {"2021": 3, "2020": 2, "2019": 2},
    },
]


@dataclass
class Club:
    name: str
    league: str
    city: str
    year_founded: int
    stadium_name: str
    image_url: str
    standings: dict[str, int] = None

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


def create_club_list(club_list: list[dict[str, str]]) -> list[Club]:
    return [Club(**club) for club in club_list]


clubs = create_club_list(club_list=clubs_dict)


def read_file(filepath: str) -> str:
    with open(filepath, "r") as f:
        line = f.readline()
        return line


def write_string_to_file(filepath: str, string: str):
    with open(filepath, "w") as f:
        f.write(string)
