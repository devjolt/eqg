"""
This file generates URLS for testing the alerts_app API
Use:
1. Replace username, password, url and placeholder user_id and token 
2. Run file, create new user, get id, generate token and add actual user_id and token
3. Run file again with new data to get all urls to test
"""
username='example@example.com'
password='12example34!'
url='127.0.0.1:8000'
#url='167.71.34.183'

user_id=7
token='491ed0842354093993d94ef08c052854030ba1b0'

url_skeletons = [
    '\nRegister',
    f'''http POST http://{url}/api/register/ email={username} password={password}''',
    '\nGet token',
    f'''http http://{url}/auth/ username={username} password={password}''',
    '\nGet user id',
    f'''http GET http://{url}/api/id/ "Authorization:Token {token}"''',
    '\nView dash',
    f'''http GET http://{url}/api/dash/ "Authorization:Token {token}"''',
    '\nCreate, update and delete conditions',
    f'''http POST http://{url}/api/value_condition/ user={user_id} name=cond3 value_indicator_1=price lookback_period_1=1 relation=above value_indicator_2=tenkan lookback_period_2=5 m1=true "Authorization:Token {token}"
''',
    f'''http POST http://{url}/api/percentage_condition/ user={user_id} name=cond4 percentage_indicator=fast_stochastic_oscillator lookback_period_1=1 relation=above percentage=50 m1=true "Authorization:Token {token}"
''',
    f'''http PUT http://{url}/api/update_condition/ user={user_id} name=cond4 percentage_indicator=fast_stochastic_oscillator lookback_period_1=1 relation=above percentage=50 m1=true "Authorization:Token {token}"
''',
    f'''http DELETE http://{url}/api/delete_condition/ user={user_id} name=cond4 "Authorization:Token {token}"''',
    '\nGet instruments',
    f'''http GET http://{url}/api/get_instruments/ "Authorization:Token {token}"''',
    '\nCreate, view, add to, remove from, delete instrument set',
    f'''http POST http://{url}/api/create_instrument_set/ user={user_id} name=setone "Authorization:Token {token}"''',
    f'''http GET http://{url}/api/get_instrument_set/ user={user_id} name=setone "Authorization:Token {token}"''',
    f'''http PUT http://{url}/api/add_to_instrument_set/ name=Name instrument=1 "Authorization:Token {token}"''',
    f'''http PUT http://{url}/api/remove_from_instrument_set/ name=Name instrument=1 "Authorization:Token {token}"''',
    f'''http DELETE http://{url}/api/delete_instrument_set/ user={user_id} name=setone "Authorization:Token {token}"''',
    '\nCreate, view, add to, delete from, toggle activity, delete alert',
    f'''http POST http://{url}/api/create_alert/ user={user_id} name=alertone instrument_set=4 "Authorization:Token {token}"''',
    f'''http GET http://{url}/api/get_alert/ user={user_id} name=alertone "Authorization:Token {token}"''',
    f'''http PUT http://{url}/api/add_condition_to_alert/ alert_name=alertone condition_name=Cond4 "Authorization:Token {token}"''',#(alert_name OR alert_id AND condition_name OR condition_id)
    f'''http PUT http://{url}/api/remove_condition_from_alert/ alert_id=3 condition_name=Con2 "Authorization:Token {token}"''',#(alert_name OR alert_id AND condition_name OR condition_id)
    f'''http PUT http://{url}/api/toggle_alert_active/ alert_id=3 "Authorization:Token {token}"''',
    f'''http DELETE http://{url}/api/delete_alert/ user={user_id} id=7 "Authorization:Token {token}"''',
    f'''http DELETE http://{url}/api/delete_alert/ user={user_id} name=Alert "Authorization:Token {token}"''',
    '\nGet instrument data for certain interval',
    f'''http GET http://{url}/api/get_data/ id=7 interval=m2 "Authorization:Token {token}"''',
]

for url in url_skeletons:
    print(url)