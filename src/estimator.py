def number_of_days_in_period(periodType, timeToElapse):
    """ Receives the period type and calculates the number of days in that period """

    if periodType == "days":
        return timeToElapse
    elif periodType == "weeks":
        return timeToElapse * 7
    elif periodType == "months":
        return timeToElapse * 30
    else:
        return 0


def estimator(data):
    """ Receives data inputs and makes estimate calulations based on that data """

    reported_cases = data['reportedCases']

    # Currently infected calculations for both mild and severe impact
    mild_currenty_infected = reported_cases * 10
    severe_currently_infected = reported_cases * 50

    # Infections by requested time for both mild and severe impact
    mild_infections_by_requested_time = mild_currenty_infected * \
        number_of_days_in_period(data["periodType"], data["timeToElapse"])

    severe_infections_by_requested_time = severe_currently_infected * \
        number_of_days_in_period(data["periodType"], data["timeToElapse"])

    results = {
        "data": data,

        "impact": {
            "currentyInfected": mild_currenty_infected,
            "infectionsByRequestedTime": mild_infections_by_requested_time
        },

        "severeImpact": {
            "currentyInfected": severe_currently_infected,
            "infectionsByRequestedTime": severe_infections_by_requested_time
        }
    }
    return results


data = {
    'region': {
        'name': 'Africa',
        'avgAge': 19.7,
        'avgDailyIncomeInUSD': 5,
        'avgDailyIncomePopulation': 0.71
    },
    'periodType': 'days',
    'timeToElapse': 28,
    'reportedCases': 674,
    'population': 66622705,
    'totalHospitalBeds': 1380614


}

print(estimator(data))
