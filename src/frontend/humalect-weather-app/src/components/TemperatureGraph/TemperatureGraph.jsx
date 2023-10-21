import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';
import './TemperatureGraph.css'

const parseTime = (dateTimeString) => {
  const date = new Date(dateTimeString);
  const hours = date.getHours() % 12 || 12;
  const ampm = date.getHours() >= 12 ? 'PM' : 'AM';
  return `${hours}:${String(date.getMinutes()).padStart(2, '0')} ${ampm}`;
};

export const TemperatureGraph = ({ data }) => {
  return (
    <div className='graph-container'>
    <LineChart width={800} height={400} data={data} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis dataKey={(entry) => parseTime(entry.DateTime)} stroke="#ffffff"/>
      <YAxis stroke="#ffffff"/>
      <Tooltip />
      <Legend />
      <Line type="monotone" dataKey="Temperature.Value" name="Temperature (°C)" stroke="#8884d8" activeDot={{ r: 8 }} />
    </LineChart>
    </div>
  );
};

