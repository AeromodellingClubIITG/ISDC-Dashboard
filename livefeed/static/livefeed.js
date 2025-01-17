const fetchData = async () => {
    const response = await fetch('/save_data/');
    return response.json();
};

const updateCharts = async () => {
    const data = await fetchData();
    const labels = data.map(d => new Date(d.time).toLocaleTimeString());
    const temp = data.map(d => d.temperature);
    const pressure = data.map(d => d.pressure);
    const altitude = data.map(d => d.altitude);

    const tempTimeCtx = document.getElementById('tempTimeChart').getContext('2d');
    const tempAltitudeCtx = document.getElementById('tempAltitudeChart').getContext('2d');
    const pressureTimeCtx = document.getElementById('pressureTimeChart').getContext('2d');
    const pressureAltitudeCtx = document.getElementById('pressureAltitudeChart').getContext('2d');

    new Chart(tempTimeCtx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{ label: 'Temperature (°C)', data: temp, borderColor: 'red' }]
        }
    });

    new Chart(tempAltitudeCtx, {
        type: 'line',
        data: {
            labels: altitude,
            datasets: [{ label: 'Temperature (°C)', data: temp, borderColor: 'blue' }]
        }
    });

    new Chart(pressureTimeCtx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{ label: 'Pressure (Pa)', data: pressure, borderColor: 'green' }]
        }
    });

    new Chart(pressureAltitudeCtx, {
        type: 'line',
        data: {
            labels: altitude,
            datasets: [{ label: 'Pressure (Pa)', data: pressure, borderColor: 'purple' }]
        }
    });
};

setInterval(updateCharts, 5000);
