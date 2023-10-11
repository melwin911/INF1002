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
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Town</th>
              <th scope="col">Flat type</th>
              <th scope="col">Storey range</th>
              <th scope="col">Floor area (sqm)</th>
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
              <td>{{ hdb.lease_commence_date }}</td>
              <td>S$ {{ hdb.resale_price }}</td>
              <!-- <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm">Update</button>
                  <button type="button" class="btn btn-danger btn-sm">Delete</button>
                </div>
              </td> -->
            </tr>
          </tbody>
        </table>
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
        activeAddHDBModal: false,
        addHDBForm: {
            town: '',
            flat_type: '',
            storey_range: '',
            floor_area: '',
            lease_date: '',
        },
        currentYear: new Date().getFullYear(),
        hdbs: [],
        towns: [],
        };
    },
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

      this.loaded = true
    } catch (e) {
      console.error(e)
    }
  },
    methods: {
        addHDB(payload) {
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
                lease_commence_date: this.addHDBForm.lease_date,
            };
            this.addHDB(payload);
            this.initForm();
        },
        initForm() {
            this.addHDBForm.town = '';
            this.addHDBForm.flat_type = '';
            this.addHDBForm.storey_range = '';
            this.addHDBForm.floor_area = '';
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