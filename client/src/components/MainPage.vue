<template>
    <div class="container">
        <h1>HDB Price Prediction</h1>
        <div class="row">
            <Modal/>
        </div>
        <br><br>
        <div class="row">
            <Map/>
        </div>
        <div class="row">
            <div class="container" style="float:left;width:50%">
                <p>Median Resale Price</p>
                <BarChart/>
            </div>
            <div class="container" style="float:right;width:50%">
                <p>HDB Price Prediction</p>
                <LineChart/>
            </div>
        </div>
        <br><br>
        <div class="row">
            <Accordion/>
        </div>
    </div>
</template>

<script>
import Accordion from './Accordion.vue';
import Chart from './Chart.vue';
import Modal from './Modal.vue';
import Map from './Map.vue';
import BarChart from './BarChart.vue';
import LineChart from './LineChart.vue';

export default {
  name: "MainPage",
  props: {
    msg: String
  },
  components:{
    Accordion,
    Chart,
    Modal,
    Map,
    BarChart,
    LineChart
  },
}
</script>