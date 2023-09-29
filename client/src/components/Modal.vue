<template>
  <div class="container">
    <div class="row">
      <div>
        <br><br>
        <button
          type="button"
          class="btn btn-success btn-sm"
          @click="toggleAddBookModal">
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

    <!-- add new book modal -->
    <div
      ref="addBookModal"
      class="modal fade"
      :class="{ show: activeAddBookModal, 'd-block': activeAddBookModal }"
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
              @click="toggleAddBookModal">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>

          <div class="modal-body">
            <form>
              <div class="mb-3">
                <label for="addBookTown" class="form-label">Town:</label>
                <!-- <input
                  type="select"
                  class="form-control"
                  id="addBookTown"
                  v-model="addBookForm.Town"
                  placeholder="Enter title"> -->
                <select  
                  v-model="addBookForm.Town"
                  class="form-control" 
                  id="addBookTown"
                  required>
                    <option disabled value="">Please select one</option>
                    <option>Ang Mo Kio</option>
                    <option>Bedok</option>
                    <option>Bishan</option>
                </select>
              </div>
              <div class="mb-3">
                <label for="addBookAuthor" class="form-label">Flat type:</label>
                <select
                  v-model="addBookForm.Town"
                  class="form-control"
                  id="addBookTown"
                  required>
                    <option disabled value="">Please select one</option>
                    <option>Volvo</option>
                    <option>Saab</option>
                    <option>Opel</option>
                    <option>Audi</option>
                </select>
              </div>
              <div class="mb-3">
                <label for="addBookAuthor" class="form-label">Storey range:</label>
                <select  
                  v-model="addBookForm.Town"
                  class="form-control" 
                  id="addBookTown"
                  required>
                    <option disabled value="">Please select one</option>
                    <option>Ang Mo Kio</option>
                    <option>Bedok</option>
                    <option>Bishan</option>
                </select>              
                </div>
              <div class="mb-3 form-check">
                <label class="form-check-label" for="addBookRead">Floor area (sqm):</label>
                <br>
                <input
                  type="range"
                  id="addBookRead"
                  min="30"
                  max="300"
                  v-model="addBookForm.read"
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
    <div v-if="activeAddBookModal" class="modal-backdrop fade show"></div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
    name: "Modal",
    data() {
        return {
        activeAddBookModal: false,
        addBookForm: {
            title: '',
            author: '',
            read: [],
        },
        hdbs: [],
        };
    },
    methods: {
        addBook(payload) {
        const path = 'http://localhost:5000/hdbs';
            axios.post(path, payload)
                .then(() => {
                this.getBooks();
                })
                .catch((error) => {

                console.log(error);
                this.getBooks();
                });
        },
        getBooks() {
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
            handleAddReset() {
            this.initForm();
        },
        handleAddSubmit() {
            this.toggleAddBookModal();
            let read = false;
            if (this.addBookForm.read[0]) {
                read = true;
            }
            const payload = {
                title: this.addBookForm.title,
                author: this.addBookForm.author,
                read, // property shorthand
            };
            this.addBook(payload);
            this.initForm();
            },
            initForm() {
            this.addBookForm.title = '';
            this.addBookForm.author = '';
            this.addBookForm.read = [];
        },
        toggleAddBookModal() {
            const body = document.querySelector('body');
            this.activeAddBookModal = !this.activeAddBookModal;
            if (this.activeAddBookModal) {
                body.classList.add('modal-open');
            } else {
                body.classList.remove('modal-open');
            }
        },
    },
    created() {
        this.getBooks();
    },
};
</script>