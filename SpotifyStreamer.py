from fycharts import SpotifyCharts 

api = SpotifyCharts.SpotifyCharts()
api.top200Daily(output_file = 'top_200_daily.csv')
