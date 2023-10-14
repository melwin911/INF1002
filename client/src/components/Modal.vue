<template>
  <div class="container">
    <div class="row">
      <div>
        <br><br>
        <button
          type="button"
          class="btn btn-success btn-sm"
          @click="toggleAddHDBModal">
          Price New HDB
        </button>
        <br><br>
        <div v-if="isLoading">
          <!-- Display a loading indicator here -->
          <i class="fa fa-spinner fa-spin fa-2x"></i>
          <p>Loading...</p>
        </div>
        <div v-else>
          <table class="table table-hover">
            <thead>
              <tr>
                <th scope="col">Town</th>
                <th scope="col">Flat type</th>
                <th scope="col">Storey range</th>
                <th scope="col">Floor area (sqm)</th>
                <th scope="col">Flat Model</th>
                <th scope="col">Lease commence date</th>
                <th scope="col">Resale price</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(hdb, index) in hdbs" :key="index">
                <td>{{ hdb.town }}</td>
                <td>{{ hdb.flat_type }}</td>
                <td>{{ hdb.storey_range }}</td>
                <td>{{ hdb.floor_area_sqm }}</td>
                <td>{{ hdb.flat_model }}</td>
                <td>{{ hdb.lease_commence_date }}</td>
                <td>S$ {{ hdb.resale_price }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- add new hdb modal -->
    <div
      ref="addHDBModal"
      class="modal fade"
      :class="{ show: activeAddHDBModal, 'd-block': activeAddHDBModal }"
      tabindex="-1"
      role="dialog">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Price a HDB</h5>
            <button
              type="button"
              class="close"
              data-dismiss="modal"
              aria-label="Close"
              @click="toggleAddHDBModal">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>

          <div class="modal-body">
            <form>
              <div class="mb-3">
                <label for="addhdbTown" class="form-label">Town:</label>
                <select 
                  v-model="addHDBForm.town"
                  class="form-control"
                  id="addhdbTown">
                  <option value="">Please select a town</option>
                  <option v-for="town in towns" :key="town" :value="town">{{ town }}</option>
                </select>
              </div>
              <div class="mb-3">
                <label for="addhdbType" class="form-label">Flat type:</label>
                <select
                  v-model="addHDBForm.flat_type"
                  class="form-control"
                  id="addhdbType"
                  required>
                    <option disabled value="">Please select a flat type</option>
                    <option>1 ROOM</option>
                    <option>2 ROOM</option>
                    <option>3 ROOM</option>
                    <option>4 ROOM</option>
                    <option>5 ROOM</option>
                    <option>EXECUTIVE</option>
                    <option>MULTI-GENERATION</option>
                </select>
              </div>
              <div class="mb-3">
                <label for="addhdbStorey" class="form-label">Storey Range:</label>
                <select  
                  v-model="addHDBForm.storey_range"
                  class="form-control" 
                  id="addhdbStorey"
                  required>
                    <option disabled value="">Please select a storey range</option>
                    <option>01 TO 03</option>
                    <option>04 TO 06</option>
                    <option>07 TO 09</option>
                    <option>10 TO 12</option>
                    <option>13 TO 15</option>
                    <option>16 TO 18</option>
                    <option>19 TO 21</option>
                    <option>22 TO 24</option>
                    <option>28 TO 30</option>
                    <option>31 TO 33</option>
                    <option>34 TO 36</option>
                    <option>37 TO 39</option>
                    <option>40 TO 42</option>
                    <option>43 TO 45</option>
                    <option>46 TO 48</option>
                    <option>49 TO 51</option>
                </select>              
                </div>
              <div class="mb-3">
                <label for="addhdbFlatModel" class="form-label">Flat Model:</label>
                <select  
                  v-model="addHDBForm.flat_model"
                  class="form-control" 
                  id="addhdbFlatModel"
                  required>
                    <option disabled value="">Please select a flat model</option>
                    <option>3RD GENERATION</option>
                    <option>ADJOURNED FLAT</option>
                    <option>APARTMENT</option>
                    <option>DBSS</option>
                    <option>IMPROVED</option>
                    <option>IMPROVED MAISONETTE</option>
                    <option>MAISONETTE</option>
                    <option>MODEL A</option>
                    <option>MODEL A2</option>
                    <option>MODEL A-MAISONETTE</option>
                    <option>MULTI-GENERATION</option>
                    <option>NEW GENERATION</option>
                    <option>PREMIUM APARTMENT</option>
                    <option>PREMIUM APARTMENT LOFT</option>
                    <option>PREMIUM MAISONETTE</option>
                    <option>SIMPLIFIED</option>
                    <option>STANDARD</option>
                    <option>TERRACE</option>
                    <option>TYPE S1</option>
                    <option>TYPE S2</option>
                </select>              
                </div>
              <div class="mb-3 form-check">
                <label class="form-check-label" for="addhdbFloor">Floor area (sqm):</label>
                <br>
                <input
                  type="range"
                  id="addhdbFloor"
                  min="30"
                  max="300"
                  v-model="addHDBForm.floor_area"
                  required>
              </div>
              <div class="mt-2">
                Value: {{ addHDBForm.floor_area }}
              </div>
              <div class="mb-3">
                <label for="addhdbLease" class="form-label">Lease commence date (Year):</label>
                <input
                  class="form-control"
                  id="addhdbLease"
                  type="number"
                  v-model="addHDBForm.lease_date"
                  min="1965"
                  :max="currentYear"
                  required>
              </div>
              <div class="btn-group" role="group">
                <button
                  type="button"
                  class="btn btn-primary btn-sm"
                  @click="handleAddSubmit">
                  Submit
                </button>
                <button
                  type="button"
                  class="btn btn-danger btn-sm"
                  @click="handleAddReset">
                  Reset
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    <div v-if="activeAddHDBModal" class="modal-backdrop fade show"></div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
    name: "Modal",
    data() {
        return {
        isLoading: true, // Initially, set isLoading to true
        activeAddHDBModal: false,
        addHDBForm: {
            town: '',
            flat_type: '',
            storey_range: '',
            floor_area: '',
            flat_model: '',
            lease_date: '',
        },
        currentYear: new Date().getFullYear(),
        hdbs: [],
        towns: [],
        };
    },
    async mounted () {
    this.isLoading = true;
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

      this.loaded = true
    } catch (e) {
      console.error(e)
    }
  },
    methods: {
        addHDB(payload) {
          this.isLoading = true;
          const path = 'http://localhost:5000/hdbs';
            axios.post(path, payload)
                .then(() => {
                this.getHDB();
                })
                .catch((error) => {

                console.log(error);
                this.getHDB();
                });
        },
        getHDB() {
          const path = 'http://localhost:5000/hdbs';
            axios.get(path)
                .then((res) => {
                    console.log(res)
                this.hdbs = res.data.hdbs;
                this.isLoading = false;
                })
                .catch((error) => {

                console.error(error);
                });
        },
        handleAddSubmit() {
            this.toggleAddHDBModal();

            const payload = {
                town: this.addHDBForm.town,
                flat_type: this.addHDBForm.flat_type,
                storey_range: this.addHDBForm.storey_range,
                floor_area_sqm: this.addHDBForm.floor_area,
                flat_model: this.addHDBForm.flat_model,
                lease_commence_date: this.addHDBForm.lease_date,
            };
            this.addHDB(payload);
            this.$emit('send-town', this.addHDBForm.town);
            this.initForm();
        },
        initForm() {
            this.addHDBForm.town = '';
            this.addHDBForm.flat_type = '';
            this.addHDBForm.storey_range = '';
            this.addHDBForm.floor_area = '';
            this.addHDBForm.flat_model= '';
            this.addHDBForm.lease_date = '';
        },
        handleAddReset() {
          this.initForm();
        },
        toggleAddHDBModal() {
            const body = document.querySelector('body');
            this.activeAddHDBModal = !this.activeAddHDBModal;
            if (this.activeAddHDBModal) {
                body.classList.add('modal-open');
            } else {
                body.classList.remove('modal-open');
            }
        },
    },
    created() {
        this.getHDB();
    },
};
</script>

<style>
/* Add Font Awesome styles */
@import 'node_modules/font-awesome/css/font-awesome.min.css';
</style>