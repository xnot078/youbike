from dataclasses import dataclass, field
from typing import List, Dict


@dataclass(frozen=True)
class ColSet:
    """為了把cols群組，並註記難記的col意義"""
    cols: List[str] = ''
    col_aliases: Dict[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class Recipe:
    """單純的把ColSet整合起來"""
    bike_station: ColSet = field(default_factory=ColSet)
    MRT: ColSet = field(default_factory=ColSet)
    school: ColSet = field(default_factory=ColSet)
    weather: ColSet = field(default_factory=ColSet)

    def update(self, name: str, col_set: ColSet):
        assert name in self.__dict__.keys(
        ), "Name must be in bike_station, date_type, MRT, school, weather."
        self.__dict__[name] = col_set


COL_RECIPE = Recipe()
COL_RECIPE.update(
    name="bike_station",
    col_set=ColSet(
        cols=[
            'station', 'Generation', 'sno', 'sna', 'sarea',
            'date', 'time', 'Hr',
            'bike_lat', 'bike_lng', 'ar',
            'rent_sec', 'rent_count', 'return_sec', 'return_count',
            'weekday', 'holiday', 'school_off', 'outlier'
        ],
        col_aliases=dict(
            sno="Youbike站代號", sna="Youbike站名", sarea="Youbike站區域", ar="Youbike站點地區",
            Generation="Youbike1.0/2.0",
            rent_count="租借量", return_count="還車量",
            rent_sec="租借的人騎的時間合計", return_sec="還車的人騎的時間合計"
        )
    )
)

mrt = {'MRT_Station': '捷運站名',
       'MRT_No': '捷運代號',
       'MRT_Exit_Name': '捷運站+出口名',
       'Exit_No': '出口數字',
       'MRT_lng': '捷運站經度',
       'MRT_lat': '捷運站緯度',
       'MRT_Dist': '捷運站到youbike距離',
       'MRT_Out_ppl': '捷運出站人數'
       }
COL_RECIPE.update(
    name="MRT",
    col_set=ColSet(cols=mrt.keys(), col_aliases=mrt)
)
COL_RECIPE.update(
    name="school",
    col_set=ColSet(cols=['School', 'School_lat', 'School_lng',
                   'School_Dist'], col_aliases={"School_Dist": "學校到youbike距離"})
)
COL_RECIPE.update(
    name="weather",
    col_set=ColSet(
        cols=[
            'WeatherSiteID', 'WeatherSite', 'Weather_lng', 'Weather_lat', 'Weather_Dist',
            'Temperature', 'RH', 'WS', 'Precp', 'UVI'
        ],
        col_aliases={'Weather_Dist': "氣象距離",
                     'RH': "相對溼度",
                     'WS': "風速",
                     'Precp': "降水量",
                     'UVI': "紫外線指數"}
    )
)
