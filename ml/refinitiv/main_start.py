import json
import refinitiv.data as rd
from refinitiv.data.content import search


rd.open_session(name='platform.rdp')

# ----------------------------QUICK SEARCH---------------------------- #
# response = search.Definition("aVNCGDPYA").get_data()
# print(response.data.df)

# ----------------------------GET TIMESERIES DATA---------------------------- #
ric = 'aVNCGDPYA'

df = rd.get_data(universe=ric)
print(df)

# ric_fields = rd.get_fields(universe=ric)

# print(ric_fields)


rd.close_session()