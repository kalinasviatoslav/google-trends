import os

geoPicker = [{"id": "AR", "name": "Argentina"}, {"id": "AU", "name": "Australia"}, {"id": "AT", "name": "Austria"},
             {"id": "BE", "name": "Belgium"}, {"id": "BR", "name": "Brazil"}, {"id": "CA", "name": "Canada"},
             {"id": "CL", "name": "Chile"}, {"id": "CO", "name": "Colombia"}, {"id": "CZ", "name": "Czechia"},
             {"id": "DK", "name": "Denmark"}, {"id": "EG", "name": "Egypt"}, {"id": "FI", "name": "Finland"},
             {"id": "FR", "name": "France"}, {"id": "DE", "name": "Germany"}, {"id": "GR", "name": "Greece"},
             {"id": "HK", "name": "Hong Kong"}, {"id": "HU", "name": "Hungary"}, {"id": "IN", "name": "India"},
             {"id": "ID", "name": "Indonesia"}, {"id": "IE", "name": "Ireland"}, {"id": "IL", "name": "Israel"},
             {"id": "IT", "name": "Italy"}, {"id": "JP", "name": "Japan"}, {"id": "KE", "name": "Kenya"},
             {"id": "MY", "name": "Malaysia"}, {"id": "MX", "name": "Mexico"}, {"id": "NL", "name": "Netherlands"},
             {"id": "NZ", "name": "New Zealand"}, {"id": "NG", "name": "Nigeria"}, {"id": "NO", "name": "Norway"},
             {"id": "PE", "name": "Peru"}, {"id": "PH", "name": "Philippines"}, {"id": "PL", "name": "Poland"},
             {"id": "PT", "name": "Portugal"}, {"id": "RO", "name": "Romania"}, {"id": "RU", "name": "Russia"},
             {"id": "SA", "name": "Saudi Arabia"}, {"id": "SG", "name": "Singapore"},
             {"id": "ZA", "name": "South Africa"}, {"id": "KR", "name": "South Korea"}, {"id": "ES", "name": "Spain"},
             {"id": "SE", "name": "Sweden"}, {"id": "CH", "name": "Switzerland"}, {"id": "TW", "name": "Taiwan"},
             {"id": "TH", "name": "Thailand"}, {"id": "TR", "name": "Türkiye"}, {"id": "UA", "name": "Ukraine"},
             {"id": "GB", "name": "United Kingdom"}, {"id": "US", "name": "United States"},
             {"id": "VN", "name": "Vietnam"}]
timePicker = [["Past 12 months", 0],
              ["Past hour", "?date=now%201-H"],
              ["Past 4 hours", "?date=now%204-H"],
              ["Past day", "?date=now%204-H"],
              ["Past 7 days", "?date=now%207-d"],
              ["Past 30 days", "?date=today%201-m"],
              ["Past 90 days", "date=today%203-m"],
              ["Past 5 years", "?date=today%205-y"],
              ["2004 - present", "?date=today%205-y"]]


GoogleTrendsLink = "https://trends.google.com/trends/explore"
GoogleTrendsConnectionError = 'Error 429 (Too Many Requests)!!1'
max_amount_of_search_suggestions = 4
sleep_time_for_uploading_data = 3
current_dir = os.getcwd()

