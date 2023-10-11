<template>
    <div class="container">
        <header>
            <h1 class="title">HDB Price Prediction</h1>
        </header>
        <div class="row-modal">
            <Modal/>
        </div>
        <div class="row">
            <div class="container" style="float:left;width:100%">
                <p>Town </p>
                <TestChart/>        
            </div>
            <div class="container" style="float:right;width:100%">
                <p>Resale price over time</p>
                <LineChart/>
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
</style>

<script>
import Accordion from './Accordion.vue';
import Modal from './Modal.vue';
import Map from './Map.vue';
import LineChart from './LineChart.vue';
import TestChart from './TestChart.vue';

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
    TestChart
  },
}
</script>