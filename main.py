import http.client


conn = http.client.HTTPSConnection("irctc1.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "08671a8240msh89ea2c71ec59976p1dcaa8jsnf3ae9080f7f4",
    'X-RapidAPI-Host': "irctc1.p.rapidapi.com"
}

conn.request("GET", "/api/v1/searchStation?query=Mumbai", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
var = {"ResponseCode": "200",
       "Status": "SUCCESS",
       "Trains": [
           {"Name": "ASR-KIR EXPRESS",
            "Number": "15708",
            "Source": "ASR",
            "Destination": "KIR",
            "ScheduleArrival": "11:05",
            "ScheduleDeparture": "11:10",
            "Halt": "00:05",
            "ExpectedArrival": "17:10, 15 Sep",
            "DelayInArrival": "06:05",
            "ExpectedDeparture": "17:11, 15 Sep",
            "DelayInDeparture": "00:36"}], "Message": "SUCCESS"}
print(var)

import http.client

conn = http.client.HTTPSConnection("irctc1.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "08671a8240msh89ea2c71ec59976p1dcaa8jsnf3ae9080f7f4",
    'X-RapidAPI-Host': "irctc1.p.rapidapi.com"
}

conn.request("GET", "/api/v1/searchTrain?query=180", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

var = {"TrainNumber": "12565",
       "TrainName": "BIHAR S KRANTI",
       "From": "SEE", "To": "NDLS",
       "Distance": "1025",
       "TrainType": "SF",
       "Fares": [{"Name": "AC First Class",
                  "Code": "1A", "Fare": "3230"},
                 {"Name": "AC 2-Tier", "Code": "2A", "Fare": "1895"},
                 {"Name": "AC 3-Tier", "Code": "3A", "Fare": "1320"},
                 {"Name": "Sleeper", "Code": "SL", "Fare": "500"},
                 {"Name": "General", "Code": "GN", "Fare": "275"}], "Status": "SUCCESS",
       "ResponseCode": "200"}
print(var)

import http.client

conn = http.client.HTTPSConnection("irctc1.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "08671a8240msh89ea2c71ec59976p1dcaa8jsnf3ae9080f7f4",
    'X-RapidAPI-Host': "irctc1.p.rapidapi.com"
}

conn.request("GET", "/api/v3/getPNRStatus?pnrNumber=8528668549", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
var = {"PnrNumber": "6719687062",
       "Status": "SUCCESS",
       "ResponseCode": "200",
       "TrainNumber": "13164",
       "TrainName": "HATE BAZARE EXP",
       "JourneyClass": "SL",
       "ChatPrepared": "YES",
       "From": "NIMITITA [NILE]",
       "To": "SEALDAH [SDAH]",
       "JourneyDate": "23-09-2018",
       "Passengers": [{"Passenger": "Passenger 1",
                       "BookingStatus": "RLWL/-/16/GN",
                       "CurrentStatus": "CNF/S6/71/GN"},
                      {"Passenger": "Passenger 2",
                       "BookingStatus": "RLWL/-/17/GN",
                       "CurrentStatus": "CNF/S6/72/GN"}]}
print(var)

import http.client

conn = http.client.HTTPSConnection("irctc1.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "08671a8240msh89ea2c71ec59976p1dcaa8jsnf3ae9080f7f4",
    'X-RapidAPI-Host': "irctc1.p.rapidapi.com"
}

conn.request("GET",
             "/api/v1/checkSeatAvailability?classType=2A&fromStationCode=ST&quota=GN&toStationCode=BVI&trainNo=19038"
             "&date=2022-05-25",
             headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

var = {"ResponseCode": "200",
       "TrainNo": "12565",
       "From": "NDLS",
       "To": "null", "ClassCode": "3A",
       "Quota": "GN",
       "Availability": [{"JourneyDate": "06-10-2018", "Availability": "GNWL28/WL15", "Confirm": "36 %"},
                        {"JourneyDate": "07-10-2018", "Availability": "GNWL25/WL13", "Confirm": "40 %"},
                        {"JourneyDate": "08-10-2018", "Availability": "GNWL16/WL10", "Confirm": "72 %"},
                        {"JourneyDate": "09-10-2018", "Availability": "GNWL15/WL13", "Confirm": "85 %"},
                        {"JourneyDate": "10-10-2018", "Availability": "GNWL26/WL17", "Confirm": "66 %"},
                        {"JourneyDate": "11-10-2018", "Availability": "GNWL15/WL9", "Confirm": "78 %"},
                        {"JourneyDate": "12-10-2018", "Availability": "GNWL19/WL13", "Confirm": "78 %"}],
       "Message": "SUCCESS"}
print(var)

import http.client

conn = http.client.HTTPSConnection("irctc1.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "08671a8240msh89ea2c71ec59976p1dcaa8jsnf3ae9080f7f4",
    'X-RapidAPI-Host': "irctc1.p.rapidapi.com"
}

conn.request("GET", "/api/v2/getFare?trainNo=19038&fromStationCode=ST&toStationCode=BVI", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

var = {"TrainNumber": "12565", "TrainName": "BIHAR S KRANTI", "From": "SEE", "To": "NDLS", "Distance": "1025",
       "TrainType": "SF", "Fares": [{"Name": "AC First Class", "Code": "1A", "Fare": "3230"},
                                    {"Name": "AC 2-Tier", "Code": "2A", "Fare": "1895"},
                                    {"Name": "AC 3-Tier", "Code": "3A", "Fare": "1320"},
                                    {"Name": "Sleeper", "Code": "SL", "Fare": "500"},
                                    {"Name": "General", "Code": "GN", "Fare": "275"}], "Status": "SUCCESS",
       "ResponseCode": "200"}

print(var)

import http.client

conn = http.client.HTTPSConnection("irctc1.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "08671a8240msh89ea2c71ec59976p1dcaa8jsnf3ae9080f7f4",
    'X-RapidAPI-Host': "irctc1.p.rapidapi.com"
}

conn.request("GET", "/api/v3/getLiveStation?fromStationCode=12345&toStationCode=%3CREQUIRED%3E&hours=8", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

var = {"ResponseCode": "200",
       "Status": "SUCCESS",
       "Trains": [
    {"Name": "ASR-KIR EXPRESS",
     "Number": "15708",
     "Source": "ASR",
     "Destination": "KIR",
     "ScheduleArrival": "11:05",
     "ScheduleDeparture": "11:10",
     "Halt": "00:05",
     "ExpectedArrival": "17:10, 15 Sep",
     "DelayInArrival": "06:05",
     "ExpectedDeparture": "17:11, 15 Sep",
     "DelayInDeparture": "06:01"},
    {"Name": "CPR-TATA EXP",
     "Number": "18182",
     "Source": "CPR",
     "Destination": "TATA",
     "ScheduleArrival": "14:25",
     "ScheduleDeparture": "14:30",
     "Halt": "00:05",
     "ExpectedArrival": "17:45, 15 Sep",
     "DelayInArrival": "03:20",
     "ExpectedDeparture": "17:50, 15 Sep",
     "DelayInDeparture": "03:20"},
    {"Name": "NJP-NDLS BI-WEEKLY EXP.",
     "Number": "12523", "Source": "NJP",
     "Destination": "NDLS",
     "ScheduleArrival": "17:10",
     "ScheduleDeparture": "17:15",
     "Halt": "00:05",
     "ExpectedDeparture": "18:55, 15 Sep",
     "DelayInDeparture": "RT"}], "Message": "SUCCESS"}
print(var)
