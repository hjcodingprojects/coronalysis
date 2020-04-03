var values_data_covid_string = document.getElementById('data-covid').getAttribute('data-values')
var values_range_string = document.getElementById('data-range').getAttribute('data-values')
var data_covid = JSON.parse(values_data_covid_string)
var data_range = JSON.parse(values_range_string)

var data = [];
list_countries = Object.keys(data_covid);
console.log(list_countries)
for (var i = 0; i <list_countries.length; i++) {
  var trace = {
    x: data_range['x'],
    y: data_covid[list_countries[i]],
    name: list_countries[i],
    mode: 'lines'
  };
  data.push(trace);
}

var layout = {
  title: {
    text:'CoronaLysis V0.1',
  },
  xaxis: {
    title: {
      text: 'Days since first case COVID-19',
      font: {
        family: 'Courier New, monospace',
        size: 18,
        color: '#7f7f7f'
      }
    },
  },
  yaxis: {
    title: {
      text: ' Number of new cases',
      font: {
        family: 'Courier New, monospace',
        size: 18,
        color: '#7f7f7f'
      }
    }
  }
};

Plotly.newPlot('myDiv', data, layout, {showSendToCloud: true});