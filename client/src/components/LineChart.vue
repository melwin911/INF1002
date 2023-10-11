<template>
  <div class="container">
    <select v-model="selectedTown" @change="fetchResaleData">
      <option value="">Select a town</option>
      <option v-for="town in towns" :key="town" :value="town">{{ town }}</option>
    </select>
    <Line v-if="loaded" :data="chartData" :options="chartOptions" />
  </div>
</template>

<script>
import { Line } from 'vue-chartjs'
import axios from 'axios';
import {Chart as ChartJS,CategoryScale,LinearScale,PointElement,LineElement,Title,Tooltip,Legend} from 'chart.js'

ChartJS.register(CategoryScale,LinearScale,PointElement,LineElement,Title,Tooltip,Legend)

export default {
  name: 'LineChart',
  components: { Line },
  data: () => ({
    loaded: false,
    chartData: null,
  }),
  async mounted () {
    this.loaded = false

    try {
      // Fetch the list of towns from your Flask API
      const response = await axios.get('http://localhost:5000/town');
      const allTowns = response.data;

      // Remove duplicates from the list of towns
      const uniqueTowns = [...new Set(allTowns)];

      // Assign the unique towns to the component's data property
      this.towns = Object.values(uniqueTowns);

      console.log(Object.values(this.towns))

      // Update chartData with the processed data
      this.chartData = {
        labels: [], 
        datasets: [
          {
            label: 'Resale Prices',
            borderColor: 'rgb(255, 99, 132)',
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            data: [],
          },
        ],
      };

      this.loaded = true
    } catch (e) {
      console.error(e)
    }
  },
  methods: {
    async fetchResaleData() {
      if (this.selectedTown) {
        try {
          console.log("fetch resale data")

          // Make a GET request to your Flask API with the selected town as a query parameter
          const response = await axios.get(`http://localhost:5000/resale?town=${this.selectedTown}`);
          const data = response.data;

          console.log(data)

          const years = data.map(item => item.year);
          const resalePrices = data.map(item => item.resale_price);

          console.log(years)
          console.log(resalePrices)

          this.chartData = {
            labels: years, // Years as labels
            datasets: [
              {
                label: 'Resale Prices',
                borderColor: 'rgb(255, 99, 132)',
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                data: resalePrices,
              },
            ],
          };

          // Set chart options (customize as needed)
          this.chartOptions = {
            responsive: true,
            scales: {
              x: {
                title: {
                  display: true,
                  text: 'Year',
                },
              },
              y: {
                title: {
                  display: true,
                  text: 'Resale Price',
                },
              },
            },
          };

          this.loaded = true
        } catch (error) {
          console.error(error);
        }
      } else {
        // Clear the chart data if no town is selected
        this.chartData.labels = [];
        this.chartData.datasets[0].data = [];
      }
    },
  },
}
</script>