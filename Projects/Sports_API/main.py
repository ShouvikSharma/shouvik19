import http.client

conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "ee2f1d4f7dmsh765018dd72d87a8p1660d3jsn67c975d384e5",
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com"
}

conn.request("GET", "/v2/topscorers/524", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# get("https://api-football-v1.p.rapidapi.com/v2/fixtures/team/{team_id}");
