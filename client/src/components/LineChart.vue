<template>
  <div class="container">
    <h3 style="text-align:center;font-weight:bold">{{ receivedData }}</h3>
    <h5 style="text-align: center;font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;">Resale price over year</h5>
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
  props: {
    receivedData: String
  },
  data: () => ({
    loaded: false,
    chartData: null,
  }),
  async mounted () {
    this.loaded = false

    try {
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
      if (this.receivedData) {
        try {
          console.log("fetch resale data")

          const response = await axios.get(`http://localhost:5000/resale?town=${this.receivedData}`);
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
        this.chartData.labels = [];
        this.chartData.datasets[0].data = [];
      }
    },
  },
  watch: {
    receivedData(newVal, oldVal) {
      console.log(`receivedData changed from ${oldVal} to ${newVal}`);
      this.fetchResaleData(); // Call the method to update the chart
    }
  },
}
</script>
