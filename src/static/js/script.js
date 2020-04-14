const form = document.querySelector('.form');
const results = document.querySelector('.results');

const fetchEstimates = (data) => {
  const options = {
    method: 'POST',
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json'
    }
  };

  fetch(
    'https://whispering-waters-00388.herokuapp.com/api/v1/on-covid-19',
    options
  )
    .then((res) => {
      if (res.ok) {
        return res.json();
      }
      return alert('Fail');
    })
    .then((res) => {
      form.style.display = 'none';
      results.style.display = 'grid';

      Object.keys(res)
        .forEach((key) => {
          if (key === 'impact' || key === 'severeImpact') {
            document.querySelector(
              `.results__${key} .infected .figure`
            ).innerText = res[key].currentlyInfected.toLocaleString();

            document.querySelector(
              `.results__${key} .infections .figure`
            ).innerText = res[key].infectionsByRequestedTime.toLocaleString();

            document.querySelector(
              `.results__${key} .severeCases .figure`
            ).innerText = res[key].severeCasesByRequestedTime.toLocaleString();

            document.querySelector(
              `.results__${key} .hospitalBeds .figure`
            ).innerText = res[key].hospitalBedsByRequestedTime.toLocaleString();

            document.querySelector(
              `.results__${key} .casesForICI .figure`
            ).innerText = res[key].casesForICUByRequestedTime.toLocaleString();

            document.querySelector(
              `.results__${key} .casesForventilators .figure`
            ).innerText = res[
              key
            ].casesForVentilatorsByRequestedTime.toLocaleString();

            document.querySelector(
              `.results__${key} .dollarsInFlight .figure`
            ).innerText = res[key].dollarsInFlight.toLocaleString();
          }
        })
        .catch((error) => {
          alert(error);
        });
    });
};

form.addEventListener('submit', (e) => {
  e.preventDefault();
  const population = document.querySelector('#population').value;
  const timeToElapse = document.querySelector('#timeToElapse').value;
  const reportedCases = document.querySelector('#reportedCases').value;
  const totalHospitalBeds = document.querySelector('#totalHospitalBeds').value;
  const period = document.querySelector('#periodType');
  const periodType = period.options[period.selectedIndex].value;

  const region = {
    name: 'Africa',
    avgAge: 19.7,
    avgDailyIncomeInUSD: 5,
    avgDailyIncomePopulation: 0.71
  };

  const data = {
    region,
    population,
    timeToElapse,
    reportedCases,
    totalHospitalBeds,
    periodType
  };

  fetchEstimates(data);
});
