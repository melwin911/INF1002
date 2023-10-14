<template>
  <div class="container">
    <Bar v-if="loaded" :data="chartData" :options="chartOptions" />
  </div>
</template>

<script>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: 'BarChart',
  components: { Bar },
  data: () => ({
    loaded: false,
    chartData: null
  }),
  async mounted () {
    this.loaded = false

    try {
      const response  = await fetch('http://localhost:5000/town')
      const townlist = await response.json();
      this.chartData = townlist
      const townCounts = {};

      for (const town of townlist) {
        if (townCounts[town]) {
          townCounts[town]++;
        } else {
          townCounts[town] = 1;
        }
      }

      // Update chartData with the processed data
      this.chartData = {
        labels: Object.keys(townCounts),
        datasets: [
          {
            label: 'Town Count',
            backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(255, 159, 64, 0.2)',
            'rgba(255, 205, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(201, 203, 207, 0.2)'
            ],
            borderColor: [
            'rgb(255, 99, 132)',
            'rgb(255, 159, 64)',
            'rgb(255, 205, 86)',
            'rgb(75, 192, 192)',
            'rgb(54, 162, 235)',
            'rgb(153, 102, 255)',
            'rgb(201, 203, 207)'
            ],
            borderWidth: 1,
            data: Object.values(townCounts),
          },
        ],
      };

      // Set chart options (customize as needed)
      this.chartOptions = {
        responsive: true,
      };
      

      console.log(this.chartData)

      this.loaded = true
    } catch (e) {
      console.error(e)
    }
  }
}
</script>