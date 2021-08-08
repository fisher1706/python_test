import unittest
from homework.src import utils, variables, weather


class WeatherTests(unittest.TestCase):
    def setUp(self):
        utils.cleaner(variables.PATH_TEST)
        weather.generate_data_weather('Kyiv', path=variables.PATH_TEST)
        # weather.generate_data_weather('Kiev', path=variables.PATH_TEST)

    def test_first(self):
        filename = weather.generate_filename()
        data_csv = utils.read_csv(filename, variables.PATH_TEST)
        resp = weather.get_data_weather_api(data_csv.get('name'), url=variables.URL, key=variables.KEY)
        data_api = weather.generate_data_csv(resp, variables.FIELDS)
        data_api = utils.convert_dict(data_api)

        self.assertEqual(data_csv, data_api)



if __name__ == '__main__':
    unittest.main()




