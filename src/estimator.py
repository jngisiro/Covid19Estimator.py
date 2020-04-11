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

    # Severe positive cases that will require ICU for both mild and severe scenarios
    mild_cases_for_ICU_by_requested_time = 0.05 * mild_infections_by_requested_time

    severe_cases_for_ICU_by_requested_time = 0.05 * \
        severe_infections_by_requested_time

    # Severe positive cases that will require ventilators for both mild and severe scenarios
    mild_cases_for_ventilators_by_requested_time = 0.02 * \
        mild_infections_by_requested_time

    severe_cases_for_ventilators_by_requested_time = 0.02 * \
        severe_infections_by_requested_time

    # Dollars in Flight for both mild and severe impact scenarios
    mild_dollars_in_flight = (mild_infections_by_requested_time * data["region"]["avgDailyIncomePopulation"] *
                              data["region"]["avgDailyIncomeInUSD"]) / number_of_days_in_period(data["periodType"], data["timeToElapse"])

    severe_dollars_in_flight = (severe_infections_by_requested_time * data["region"]["avgDailyIncomePopulation"] *
                                data["region"]["avgDailyIncomeInUSD"]) / number_of_days_in_period(data["periodType"], data["timeToElapse"])

    # Response data
    results = {
        "data": data,

        "impact": {
            "currentlyInfected": mild_currenty_infected,
            "infectionsByRequestedTime": mild_infections_by_requested_time,
            "hospitalBedsByRequestedTime": mild_hospital_beds_requested_time,
            "severeCasesByRequestedTime": mild_severe_cases_by_requested_time,
            "casesForICUByRequestedTime": mild_cases_for_ICU_by_requested_time,
            "casesForVentilatorsByRequestedTime": mild_cases_for_ventilators_by_requested_time,
            "dollarsInFlight": mild_dollars_in_flight
        },

        "severeImpact": {
            "currentlyInfected": severe_currently_infected,
            "infectionsByRequestedTime": severe_infections_by_requested_time,
            "hospitalBedsByRequestedTime": severe_hospital_beds_requested_time,
            "severeCasesByRequestedTime": severe_severe_cases_by_requested_time,
            "casesForICUByRequestedTime": severe_cases_for_ICU_by_requested_time,
            "casesForVentilatorsByRequestedTime": severe_cases_for_ventilators_by_requested_time,
            "dollarsInFlight": severe_dollars_in_flight
        }
    }
    return results
