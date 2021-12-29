Python dependencies:
- Django
- psycopg2
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
- requests
- django_apscheduler
- django_crispy_forms
- django_crum
- tzlocal

You will also need:
- Django emails configured
- Twelvedataapi key

SETUP
With a fresh postgress database named alerts_app:
a. makemigrations and migrate as usual. 
b. Populate main.model.Asset table with assets
    main.views.populate_initial_assets:
    - assets: list of all required instrument types eg. ['forex_pairs', 'cryptocurrencies', 'etf'...]
    - num_assets: None for every asset in each instrument category
    - num_assets: int(n) for last n assets in each instrument category eg. if n is 100, last 100 in each cat will be populated 
    - populate_initial_assets calls main.utilities.twelvedata_api_tools.get_assets
c. url root/get_assets will populate Asset table with assets as above using twelvedataapi

FUNCTIONALITY IN BRIEF:
1. Users register and login
2. Allows users to Select sets of instruments and define conditions which will trigger an alert
3. Minutely updates database containing minutely datapoints for each asset in each User's asset sets
4. Daily ditches surplus values no longer required 
5. Calculates whether conditions are met for each asset in a User's asset sets if a user device is not available to do so
6. Forwards data to user device to do the above if it is available. 

FUNCTIONALITY IN DETAIL:
1. 
a. Custom user model requires registration with email address
b. main.views.register_request, login_request interact with DB using forms

2. 
a. model for storing conditions: main.models.Condition
b. model for storing asset sets: main.models.InstrumentSet
c. model for storing alerts: main.models.Alert
d. main.views.dash handles:
    - creation of conditions via: 
        - main.views.make_value_condition
        - main.views.make_percentage_condition
    - deletion of conditions via form
    - creation of instrument sets using form
    - editing instrument sets using main.views.edit_instrument_set
    - deletion of instrument sets via form
    - creation of alerts via form
    - addition of instrument set to alerts via form
    - addition and editing of conditions to alerts and activation of alert via main.views.edit_alert_condition
e. When an asset is added to an asset set using main.views.edit_instrument_set:
    - main.utilities.twelvedata_api_tools.get_cleaned_initial_load fetches values from twelvedata
    - main.views.add_rows_to_db adds each value to main.models.InstrumentValue model 

3.
minutely updates of assets in any given users' Asset_set updated:
    - in main.AssetValueScheduler.AssetValueScheduler
    - job at line 15 calls main.views.AssetValueViewset.save_instrument_value_data
    - ...save_asset_value_data calls main.utilities.twelvedata_api_tools.minutely_complex_request to get minutely value for each asset and add to database

4.
daily removal of excess data stored in main.models.Asset_price_period_interval model:
    - in main.AssetValueScheduler.AssetValueScheduler
    - job at line 131 calls main.utilities.database_cleanup.clear_redundant_data
    - ...clears each value greater than the 52nd value for each time interval (1m, 5m, 15m... month)

5. 
Calculation of conditions for each asset in each alert for each user with inactive device
    - in main.AssetValueScheduler.AssetValueScheduler
    - jobs from line 26-130 call main.utilities.indicator_calculations.check_m1, check_m5... etc
    - ...each call main.utilities.indicator_calculations.generic_check(interval) where interval is 'm1', 'm5', 'm15'... 'month'
    - for each user with an active alert containing a condition involving relevant time interval where main.models.User.device_active == False:
        - if every condition is met for an asset in an alert
        - user is alerted (currently via simulated email message)
OR
6.
    - for each user with an active alert containing a condition involving relevant time interval where main.models.User.device_active == True:
        - 52 data points for each asset for relevant interval is selected to be sent to user's device to see if condition is met 
    
Examples of API usage (httpie)

Register
required:
username=new username email
password=new email
http POST http://127.0.0.1:8000/api/register/ email=asdf@asdf.com password=asdf
http POST http://167.71.34.183/api/register/ email=asdf@asdf.com password=Nogr8erasdf

Get auth Token
required:
username=registered username
password=registered password
http POST http://127.0.0.1:8000/auth/ username=example@example.com password=password
http POST http://167.71.34.183/auth/ username=example@example.com password=password

API requiring:
In header: Authorization:Token tokenstring123qwer!123

Get user id
http GET http://127.0.0.1:8000/api/id/ "Authorization:Token 42d142c3f5b9b1411425404a6445b910e11fc02c"

Get dash data
http GET http://127.0.0.1:8000/api/dash/ "Authorization:Token a8c313fa7b8f6fa1d087c2c5e097454f3a79c5b1"
http GET http://167.71.34.183/api/dash/ "Authorization:Token 7afcd3419405ce395ef16177e4893381d4fb0f64"

Create conditions
user=int(user id)
name=str(name for new condition)
m1=true, m15=true... for each interval required in condition
http POST http://127.0.0.1:8000/api/value_condition/ user=1 name=cond4 value_indicator_1=price lookback_period_1=1 relation=above value_indicator_2=tenkan lookback_period_2=5 m1=true "Authorization:Token a8c313fa7b8f6fa1d087c2c5e097454f3a79c5b1" 
http POST http://167.71.34.183/api/value_condition/ user=1 name=cond4 value_indicator_1=price lookback_period_1=1 relation=above value_indicator_2=tenkan lookback_period_2=5 m1=true "Authorization:Token a8c313fa7b8f6fa1d087c2c5e097454f3a79c5b1"

Create a percentage condition
As above
http POST http://127.0.0.1:8000/api/percentage_condition/ user=1 name=cond4 percentage_indicator=fast_stochastic_oscillator lookback_period_1=1 relation=above percentage=50 m1=true "Authorization:Token a8c313fa7b8f6fa1d087c2c5e097454f3a79c5b1"
http POST http://167.71.34.183/api/percentage_condition/ user=1 name=cond4 percentage_indicator=fast_stochastic_oscillator lookback_period_1=1 relation=above percentage=50 m1=true "Authorization:Token a8c313fa7b8f6fa1d087c2c5e097454f3a79c5b1"

Update a condition
As above
http POST http://127.0.0.1:8000/api/update_condition/ user=1 name=cond4 percentage_indicator=fast_stochastic_oscillator lookback_period_1=1 relation=above percentage=50 m1=true "Authorization:Token a8c313fa7b8f6fa1d087c2c5e097454f3a79c5b1
http POST http://167.71.34.183/api/update_condition/ user=1 name=cond4 percentage_indicator=fast_stochastic_oscillator lookback_period_1=1 relation=above percentage=50 m1=true "Authorization:Token a8c313fa7b8f6fa1d087c2c5e097454f3a79c5b1

Delete a condition
http DELETE http://127.0.0.1:8000/api/delete_condition/ user=1 name=Con1 "Authorization:Token a8c313fa7b8f6fa1d087c2c5e097454f3a79c5b1"
http DELETE http://167.71.34.183/api/delete_condition/ user=1 name=Con1 "Authorization:Token a8c313fa7b8f6fa1d087c2c5e097454f3a79c5b1"

List all available instruments
http GET http://127.0.0.1:8000/api/get_instruments/ "Authorization:Token a8c313fa7b8f6fa1d087c2c5e097454f3a79c5b1"
http GET http://167.71.34.183/api/get_instruments/ "Authorization:Token a8c313fa7b8f6fa1d087c2c5e097454f3a79c5b1"

Create instrument set
http POST http://127.0.0.1:8000/api/create_instrument_set/ user=1 name=setone "Authorization:Token a8c313fa7b8f6fa1d087c2c5e097454f3a79c5b1"
http POST http://167.71.34.183/api/create_instrument_set/ user=1 name=setone "Authorization:Token a8c313fa7b8f6fa1d087c2c5e097454f3a79c5b1"

Get specific instrument set
http POST http://127.0.0.1:8000/api/get_instrument_set/ user=1 name=setone "Authorization:Token a8c313fa7b8f6fa1d087c2c5e097454f3a79c5b1
http POST http://167.71.34.183/api/get_instrument_set/ user=1 name=setone "Authorization:Token a8c313fa7b8f6fa1d087c2c5e097454f3a79c5b1

Add instrument to set
http PUT http://127.0.0.1:8000/api/add_to_instrument_set/ name=Name instrument=1 "Authorization:Token a8c313fa7b8f6fa1d087c2c5e097454f3a79c5b1"
http PUT http://167.71.34.183/api/add_to_instrument_set/ name=Name instrument=1 "Authorization:Token a8c313fa7b8f6fa1d087c2c5e097454f3a79c5b1"

Remove instrument from set
http PUT http://127.0.0.1:8000/api/remove_from_instrument_set/ name=Name instrument=1 "Authorization:Token a8c313fa7b8f6fa1d087c2c5e097454f3a79c5b1"
http PUT http://167.71.34.183/api/remove_from_instrument_set/ name=Name instrument=1 "Authorization:Token a8c313fa7b8f6fa1d087c2c5e097454f3a79c5b1"

Delete instrument set
http DELETE http://127.0.0.1:8000/api/delete_instrument_set/ user=1 name=setone "Authorization:Token a8c313fa7b8f6fa1d087c2c5e097454f3a79c5b1"
http DELETE http://167.71.34.183/api/delete_instrument_set/ user=1 name=setone "Authorization:Token a8c313fa7b8f6fa1d087c2c5e097454f3a79c5b1"

####
Create alert
http POST http://127.0.0.1:8000/api/create_alert/ user=1 name=setone instrument_set=4 "Authorization:Token a8c313fa7b8f6fa1d087c2c5e097454f3a79c5b1"
http POST http://167.71.34.183/api/create_alert/ user=1 name=setone instrument_set=4 "Authorization:Token a8c313fa7b8f6fa1d087c2c5e097454f3a79c5b1"

Get specific alert detail
http GET http://127.0.0.1:8000/api/get_alert/ user=1 name=setone "Authorization:Token a8c313fa7b8f6fa1d087c2c5e097454f3a79c5b1"
http GET http://167.71.34.183/api/get_alert/ user=1 name=setone "Authorization:Token a8c313fa7b8f6fa1d087c2c5e097454f3a79c5b1"

Add condition to an alert
http PUT http://127.0.0.1:8000/api/add_condition_to_alert/ alert_name=TestAlert condition_name=Con2 "Authorization:Token a8c313fa7b8f6fa1d087c2c5e097454f3a79c5b1" (alert_name OR alert_id AND condition_name OR condition_id)
http PUT http://167.71.34.183/api/add_condition_to_alert/ alert_name=TestAlert condition_name=Con2 "Authorization:Token a8c313fa7b8f6fa1d087c2c5e097454f3a79c5b1" (alert_name OR alert_id AND condition_name OR condition_id)

Remove condition from alert
http PUT http://127.0.0.1:8000/api/remove_condition_from_alert/ alert_id=3 condition_name=Con2 "Authorization:Token a8c313fa7b8f6fa1d087c2c5e097454f3a79c5b1" (alert_name OR alert_id AND condition_name OR condition_id)
http PUT http://167.71.34.183/api/remove_condition_from_alert/ alert_id=3 condition_name=Con2 "Authorization:Token a8c313fa7b8f6fa1d087c2c5e097454f3a79c5b1" (alert_name OR alert_id AND condition_name OR condition_id)

Toggle Alert active
http PUT http://127.0.0.1:8000/api/toggle_alert_active/ alert_id=3 "Authorization:Token a8c313fa7b8f6fa1d087c2c5e097454f3a79c5b1"
http PUT http://167.71.34.183/api/toggle_alert_active/ alert_id=3 "Authorization:Token a8c313fa7b8f6fa1d087c2c5e097454f3a79c5b1"

Delete alert
http DELETE http://127.0.0.1:8000/api/delete_alert/ user=1 id=7 "Authorization:Token a8c313fa7b8f6fa1d087c2c5e097454f3a79c5b1" or http DELETE http://127.0.0.1:8000/api/delete_alert/ user=1 name=Alert "Authorization:Token a8c313fa7b8f6fa1d087c2c5e097454f3a79c5b1"
http DELETE http://167.71.34.183/api/delete_alert/ user=1 id=7 "Authorization:Token a8c313fa7b8f6fa1d087c2c5e097454f3a79c5b1" or http DELETE http://127.0.0.1:8000/api/delete_alert/ user=1 name=Alert "Authorization:Token a8c313fa7b8f6fa1d087c2c5e097454f3a79c5b1"

Get data to perform calc on device
http GET http://127.0.0.1:8000/api/get_data/ id=7 interval=m2 "Authorization:Token a8c313fa7b8f6fa1d087c2c5e097454f3a79c5b1"
http GET http://167.71.34.183/api/get_data/ id=7 interval=m2 "Authorization:Token a8c313fa7b8f6fa1d087c2c5e097454f3a79c5b1"

Get archive data
http GET http://127.0.0.1:8000/api/archive/ "Authorization:Token a8c313fa7b8f6fa1d087c2c5e097454f3a79c5b1"
Note: always returns an array

Get active alert data
http GET http://127.0.0.1:8000/api/current_alerts/ "Authorization:Token a8c313fa7b8f6fa1d087c2c5e097454f3a79c5b1"
Note: always returns an array

Notes on setup for digital ocean:
https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-20-04

Changes to DB model:
push to GitHub
sudo rm-r main
sudo git clone...
sudo mv main_alerts main

sudo service postgresql restart #stop any current connections
sudo -u postgres psql
DROP DATABASE alerts_app;
CREATE DATABASE alerts_app;

sudo chown <your_username> <path_to_migrations_folder> #Grant ownership of migrations folder
sudo chown tom /home/tom/alerts_app/main/migrations

makemigrations, migrate, createsuperuser

go to url: get_instruments/ #populate initial assets
make sure that schedulers are switched on



