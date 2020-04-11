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

    # Currently infected calculations for both mild and severe scenarios
    mild_currenty_infected = reported_cases * 10
    severe_currently_infected = reported_cases * 50

    # Infections by requested time for both mild and severe scenarios
    mild_infections_by_requested_time = mild_currenty_infected * \
        number_of_days_in_period(data["periodType"], data["timeToElapse"])

    severe_infections_by_requested_time = severe_currently_infected * \
        number_of_days_in_period(data["periodType"], data["timeToElapse"])

    # Severe positive cases by requested time for both mild and severe scenarios
    mild_severe_cases_by_requested_time = 0.15 * mild_infections_by_requested_time
    severe_severe_cases_by_requested_time = 0.15 * \
        severe_infections_by_requested_time

    # Available hospital beds for severe cases for both mild and severe scenarios
    mild_hospital_beds_requested_time = (
        data["totalHospitalBeds"] * 0.35) - mild_severe_cases_by_requested_time

    severe_hospital_beds_requested_time = (
        data["totalHospitalBeds"] * 0.35) - severe_severe_cases_by_requested_time

    results = {
        "data": data,

        "impact": {
            "currentyInfected": mild_currenty_infected,
            "infectionsByRequestedTime": mild_infections_by_requested_time,
            "hospitalBedsByRequestedTime": mild_hospital_beds_requested_time,
            "severeCasesByRequestedTime": mild_severe_cases_by_requested_time
        },

        "severeImpact": {
            "currentyInfected": severe_currently_infected,
            "infectionsByRequestedTime": severe_infections_by_requested_time,
            "hospitalBedsByRequestedTime": severe_hospital_beds_requested_time,
            "severeCasesByRequestedTime": severe_severe_cases_by_requested_time
        }
    }
    return results
