<template>
  <div class="container">
    <h3 style="text-align:center;font-weight:bold">{{ receivedData }}</h3>
    <h5 style="text-align: center;font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;">Resale price over floor area sqm</h5>
    <Scatter v-if="loaded" :data="chartData" :options="chartOptions" />
  </div>
</template>

<script>
import { Scatter } from 'vue-chartjs'
import axios from 'axios';
import {Chart as ChartJS,CategoryScale,LinearScale,PointElement,LineElement,Title,Tooltip,Legend} from 'chart.js'

ChartJS.register(CategoryScale,LinearScale,PointElement,LineElement,Title,Tooltip,Legend)

export default {
  name: 'Chart',
  components: { Scatter },
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
            borderColor: 'rgba(54, 162, 235)',
            backgroundColor: 'rgba(54, 162, 235,0.2)',
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

          const response = await axios.get(`http://localhost:5000/resale_floorarea?town=${this.receivedData}`);
          const data = response.data;

          console.log(data)

          const floor_area_sqm = data.map(item => item.floor_area_sqm);
          const resalePrices = data.map(item => item.resale_price);

          console.log(floor_area_sqm)
          console.log(resalePrices)

          this.chartData = {
            labels: floor_area_sqm, // Years as labels
            datasets: [
              {
                label: 'Resale Prices',
                borderColor: 'rgba(54, 162, 235)',
                backgroundColor: 'rgba(54, 162, 235,0.2)',
                data: resalePrices,
              },
            ],
          };

          this.chartOptions = {
            responsive: true,
            scales: {
                x: {
                type: 'linear', 
                position: 'bottom',
                title: {
                    display: true,
                    text: 'Floor Area Sqm',
                },
                },
                y: {
                type: 'linear', 
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
