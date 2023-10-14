<template>
  <div class="container">
    <CAccordion>
      <CAccordionItem :item-key="1">
        <CAccordionHeader> Amenities </CAccordionHeader>
        <CAccordionBody>
          <br /><br />
          <button
            type="button"
            class="btn btn-success btn-sm"
            @click="toggleAddPostalModal"
          >
            Display Amenities by Postal Code
          </button>

          <br /><br />
          <div class="info-container">
    <h3>Nearby Amenities</h3>
    <br>
    <!--Render div only if hdbs[] exists and is populated-->
    <div v-if="hdbs && hdbs.length > 0">
        <h4>Address</h4>
        <!--Display amenities of the last item in hdbs[] (which is the appended item in Amenities[] from flask)-->
        <p>{{ hdbs[hdbs.length - 1].flat }}<br>Singapore {{ hdbs[hdbs.length - 1].postal }}</p>

        <h4>Park:</h4>
        <p>{{ hdbs[hdbs.length - 1].park }} ({{ hdbs[hdbs.length - 1].park_dist }}km)</p>

        <h4>Mall:</h4>
        <p>{{ hdbs[hdbs.length - 1].mall }} ({{ hdbs[hdbs.length - 1].mall_dist }}km)</p>

        <h4>Top School:</h4>
        <p>{{ hdbs[hdbs.length - 1].top_school }} ({{ hdbs[hdbs.length - 1].top_school_dist }}km)</p>

        <h4>Hawker Centre:</h4>
        <p>{{ hdbs[hdbs.length - 1].hawker }} ({{ hdbs[hdbs.length - 1].hawker_dist }}km)</p>

        <h4>Station Name:</h4>
        <p>{{ hdbs[hdbs.length - 1].station_name }} ({{ hdbs[hdbs.length - 1].station_dist }}km)</p>

        <h4>2027 Station Name:</h4>
        <p>{{ hdbs[hdbs.length - 1].station_name_2027_onwards }} ({{ hdbs[hdbs.length - 1].station_dist_2027_onwards }}km)</p>

    </div>
</div>

          <!-- Display Amenities by Postal Code Modal -->
          <div
            ref="addPostalModal"
            class="modal fade"
            :class="{
              show: activeAddPostalModal,
              'd-block': activeAddPostalModal,
            }"
            tabindex="-1"
            role="dialog"
          >
            <div class="modal-dialog" role="document">
              <div class="modal-content">
                <div class="modal-header">
                  <h5 class="modal-title">Get Amenities</h5>
                  <button
                    type="button"
                    class="close"
                    data-dismiss="modal"
                    aria-label="Close"
                    @click="toggleAddPostalModal"
                  >
                    <span aria-hidden="true">&times;</span>
                  </button>
                </div>

                <div class="modal-body">
                  <form>
                    <div class="mb-3">
                      <label class="form-label" for="addPostalCode"
                        >Postal Code:</label
                      >
                      <br />
                      <input
                        type="number"
                        id="addPostalCode"
                        min="0"
                        max="999999"
                        v-model="addPostalForm.postal"
                        required
                      />
                    </div>
                    <div class="btn-group" role="group">
                      <button
                        type="button"
                        class="btn btn-primary btn-sm"
                        @click="handleAddSubmit"
                      >
                        Submit
                      </button>
                      <button
                        type="button"
                        class="btn btn-danger btn-sm"
                        @click="handleAddReset"
                      >
                        Reset
                      </button>
                    </div>
                  </form>
                </div>
              </div>
            </div>
          </div>
          <div
            v-if="activeAddPostalModal"
            class="modal-backdrop fade show"
          ></div>
        </CAccordionBody>
      </CAccordionItem>
    </CAccordion>
  </div>
</template>

<script>
import {
  CAccordion,
  CAccordionItem,
  CAccordionHeader,
  CAccordionBody,
} from "@coreui/vue";
import axios from "axios";

export default {
  name: "Accordion",
  props: {
    msg: String,
  },
  components: {
    CAccordion,
    CAccordionItem,
    CAccordionHeader,
    CAccordionBody,
  },

  data() {
    return {
      activeAddPostalModal: false,
      addPostalForm: {
        postal: "",
      },
      hdbs: [],
    };
  },
  methods: {
    getHDBs() {
      const path = "http://localhost:5000/amenities";
      axios
        .get(path)
        .then((res) => {
          this.hdbs = res.data.amenities;
          console.log(this.hdbs)
        })
        .catch((error) => {
          console.error(error);
        });
    },
    addPostal(payload) {
      const path = "http://localhost:5000/amenities";
      axios
        .post(path, payload)
        .then(() => {
          this.getHDBs();
        })
        .catch((error) => {
          console.log(error);
          this.getHDBs();
        });
    },
    initForm() {
      this.addPostalForm.postal = 560505;
    },
    handleAddSubmit() {
      this.toggleAddPostalModal();
      const payload = {
        postal: this.addPostalForm.postal,
      };
      this.addPostal(payload);
      this.initForm();
    },
    handleAddReset() {
      this.toggleAddPostalModal();
      this.initForm();
    },

    toggleAddPostalModal() {
      const body = document.querySelector("body");
      this.activeAddPostalModal = !this.activeAddPostalModal;
      if (this.activeAddPostalModal) {
        body.classList.add("modal-open");
      } else {
        body.classList.remove("modal-open");
      }
    },
  },

  created() {
    this.getHDBs();
  },
};
</script>