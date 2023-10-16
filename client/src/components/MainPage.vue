<template>
    <div class="container">
        <header>
            <h1 class="title">Predictive Data Analysis on HDB Resale Prices</h1>
        </header>
        <div class="row-modal">
            <div v-if="isLoading">
                <p>Loading...</p>
            </div>
            <div v-else>
                <Modal @send-town="updateData"/>
            </div>
        </div>
        <br><br>
	    
        <div class="row">
            <div class="col-md-6">
                <div class="container">
                <Chart :receivedData="dataReceived" />
                </div>
            </div>
            <div class="col-md-6">
                <div class="container">
                <LineChart :receivedData="dataReceived" />
                </div>
            </div>
        </div>

        <br><br>

        <div class="row">
            <Map/>
        </div>

        <br><br>
        <div class="row">
            <Accordion/>
        </div>

        <br><br>
    </div>
</template>

<style>
.title {
    font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
    font-size: 50px;
}
header {
	display: flex;
	z-index: 1;
	padding: 10px;
	/* background-color: rgba(75, 192, 192, 0.2); */
	width: 100%;
	top: 0;
	justify-content: center;
	transition: 0.33s;
}
.linechartdesc {
    text-align: center;
    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
}
</style>

<script>
import Accordion from './Accordion.vue';
import Modal from './Modal.vue';
import Map from './Map.vue';
import LineChart from './LineChart.vue';
import Chart from './Chart.vue';

export default {
  name: "MainPage",
  props: {
    msg: String
  },
  components:{
    Accordion,
    Modal,
    Map,
    LineChart,
    Chart
  },
  data(){
    return {
        dataReceived: ''
    }
  },
  methods: {
    updateData(data) {
      this.dataReceived = data;
      console.log(this.dataReceived)
    }
  }
}
</script>
