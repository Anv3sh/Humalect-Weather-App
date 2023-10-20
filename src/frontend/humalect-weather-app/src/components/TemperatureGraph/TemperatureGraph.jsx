import React, { useEffect, useRef } from 'react';
import Chart from 'chart.js';

const TemperatureGraph = ({ data }) => {
    const chartRef = useRef(null);
  
    useEffect(() => {
      if (data && chartRef.current) {
        const temperatures = data.map(entry => entry.Temperature.Value);
        const timestamps = data.map(entry => new Date(entry.DateTime).toLocaleTimeString());
  
        const ctx = chartRef.current.getContext('2d');
  
        new Chart(ctx, {
          type: 'line',
          data: {
            labels: timestamps,
            datasets: [{
              label: 'Temperature (°F)',
              data: temperatures,
              borderColor: 'rgb(75, 192, 192)',
              borderWidth: 2,
              fill: false
            }]
          },
          options: {
            scales: {
              x: {
                type: 'linear',
                position: 'bottom'
              }
            }
          }
        });
      }
    }, [data]);
  
    return <canvas ref={chartRef} width={400} height={200} />;
  };
  
export default TemperatureGraph;
  