<template>
    <div>
        <canvas id="myChart" width="400" height="400"></canvas>
    </div>
</template>

<script>
import axios from 'axios';
import Chart from 'chart.js/auto'

export default {
  name: "Chart",
  props: {
    msg: String
  },
  data(){
    return{
        chartdata: [],
    }; 
  },
  methods: {
    getBooks() {
        console.log("run getbooks")
        const path = 'http://localhost:5000/books';
        axios.get(path)
            .then((res) => {
            console.log(res.data)
            this.chartdata = res.data.books;
            })
            .catch((error) => {
            console.error(error);
            });
        console.log("end of axious")
        console.log(this.chartdata)
    },
  },
  mounted() {
        console.log("Component mounted.")
        this.getBooks()
        console.log(this.chartdata)

        const ctx = document.getElementById('myChart');

        const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
            labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
            datasets: [{
                label: 'Number of Votes',
                data: [12, 19, 3, 5, 2, 3],
                borderWidth: 1
            }]
            },
            options: {
            scales: {
                y: {
                beginAtZero: true
                }
            }
            }
        });
        myChart;
    }
}
</script>