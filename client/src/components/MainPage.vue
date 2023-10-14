<template>
    <div class="container">
        <header>
            <h1 class="title">HDB Price Prediction</h1>
        </header>
        <div class="row-modal">
            <div v-if="isLoading">
                <!-- Display a loading indicator here -->
                <p>Loading...</p>
            </div>
            <div v-else>
                <!-- Display the Modal when data is available -->
                <Modal @send-town="updateData"/>
            </div>
        </div>
        <br><br>
        
        <!-- <div class="row">
            <div class="container" style="float:left;width:100%">
                <TestChart/>
                <Chart :receivedData="dataReceived"/>
            </div>
            <div class="container" style="float:right;width:100%">
                <LineChart :receivedData="dataReceived"/>
            </div>
        </div> -->
        <div class="row">
            <div class="col-md-6">
                <div class="container">
                <!-- Place your first chart component here -->
                <Chart :receivedData="dataReceived" />
                </div>
            </div>
            <div class="col-md-6">
                <div class="container">
                <!-- Place your second chart component here -->
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
import TestChart from './TestChart.vue';
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
    TestChart,
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