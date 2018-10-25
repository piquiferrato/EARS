<template>
<div>
  <div class="row" v-if="requisitionSection">
    <div v-for="(requi , index) in requisition" :key="index" class="col-md-12 col-lg-6 " v-if="requisition">
      <div class="card card-block backgroundColor text-center boldText marginCard">
        <div class="card-body">
          <h3 class="card-title whiteText" :class="{request: requi.type == '1', error: requi.type == '2'}" ></h3>
          <div class="whiteBackground border">
            <p class="card-text textColor">{{ requi.subject }}</p>
          </div>
          <h3 class="card-title whiteText">Prioridad</h3>
          <div class="whiteBackground border">
            <p class="card-text textColor" :class="{low: requi.priority == '3',
            medium: requi.priority == '2', high: requi.priority == '1'}"></p>
          </div>
          <h3 class="card-title whiteText">Fecha</h3>
          <div class="whiteBackground border">
            <p class="card-text textColor">{{ requi.date }}</p>
          </div>
          <h3 class="card-title whiteText">Tomado por</h3>
          <div class="whiteBackground border">
            <!-- <spam>{{ technician_name(requi.assignedTechnician) }}</spam> -->
            <p class="card-text textColor">{{requi.assignedTechnician}}</p>
          </div>
          <div v-if="!inProcess">
            <button type="button" class="boldText marginButton btn btn-light textColor" v-on:click="watch_requisition(requi.id)">VER</button>
          </div>
          <div v-if="inProcess">
            <button type="button" class="boldText marginButton btn btn-light textColor" v-on:click="close_requisition(requi.id)">FINALIZAR</button>
            <button type="button" class="boldText marginButton btn btn-danger" v-on:click="cancel_requisition(requi.id)">CANCELAR</button>
          </div>
          <!-- <div v-if="cancelled">
            <button type="button" class="boldText marginButton btn btn-light textColor" v-on:click="">VER</button>
          </div> -->
        </div>
      </div>
    </div>
    <div class="textColor" id="dontExistRequisition" v-if="requisition.length == 0">
      <h1>NO HAY PEDIDOS</h1>
    </div>
  </div>
  <detailRequisition></detailRequisition>
  <requisitionSolution></requisitionSolution>
</div>
</template>
<script>
import axios from 'axios';
import EventBus from '../bus/eventBus.js';
import detailRequisition from './DetailRequisition.vue'
import requisitionSolution from './RequisitionSolution'
export default {
  components: {
    detailRequisition,
    requisitionSolution
  },
  data() {
    return {
      inProcess: false,
      cancelled: false,
      // user: sessionStorage.getItem('idUser'),
      requisition: null,
      requisitionSection: true,
      requisitionDetails: false,
      technicianName: null,
      requisitionCard: [{
        type: '',
        subject: '',
        date: '',
        priority: null,
        status: null
      }]
    }
  },
  // computed: {
  //   //   isHigh: function() {
  //   //     return this.requisition.priority;
  //   //   },
  //   //   isMedium: function() {
  //   //     return this.requisition.priority === 'media';
  //   //   },
  //   //   isLow: function() {
  //   //     return this.requisition.priority === 'baja';
  //   //   }
  //
  // },
  mounted() {
    this.load(1)
    EventBus.$on('watch_requisition', (status) => {
      this.load(status)
    })
    EventBus.$on('go_back', (status) => {
      this.load(status)
      this.requisitionSection = true
    })
  },
  methods: {
    load(status) {
      // Devuelve todos los pedidos de los usuarios
      axios.get('http://127.0.0.1:8000/requisitions/status/' + status + '/')
        .then((response) => {
          EventBus.$emit('select_nav_btn', status)
          if (status === 2) {
            this.inProcess = true
          } else if (status != 2) {
            this.inProcess = false
          }
          this.requisition = response.data
        })
        .catch((error) => {
          console.log(error.response);
        });
    },
    watch_requisition(id) {
      var self = this;
      this.requisition.forEach(function(requi) {
        if (requi.id == id) {
          self.requisitionDetails = true
          self.requisitionSection = false
          EventBus.$emit('requisition_detail', requi)
        }
      });

    },
    cancel_requisition(requisitionId) {
      var self = this
      this.requisition.forEach(function(requi) {
        if (requi.id === requisitionId) {
          var state = 3
          axios.put('http://127.0.0.1:8000/requisitions/update/' + requisitionId + '/', {
              assignedTechnician: null,
              subject: requi.subject,
              date: requi.date,
              status: state
            })
            .then((data) => {
              EventBus.$emit('watch_requisition', state)
              self.requisitionSection = true
              self.requisitionDetails = false
            })
            .catch((error) => {
              console.log(error.response);
            });
        }
      })
    },
    close_requisition(requisitionId) {
      var self = this
      this.requisition.forEach(function(requi) {
        if (requi.id === requisitionId) {
          EventBus.$emit('save_constancy', requi)
          self.requisitionSection = false
        }
      })
    },
    technician_name(technicianId) {
      axios.get('http://127.0.0.1:8000/users/' + technicianId + '/')
        .then((response) => {
          // this.technicianName = response.data.username
        })
        .catch((error) => {
          console.log(error.response);
        });
    },
    requisition_type(){
      axios.get('http://127.0.0.1:8000/users/' + technicianId + '/')
        .then((response) => {

        })
        .catch((error) => {
          console.log(error.response);
        });
    },
    create_requisition_card(){
      var self = this
      this.requisition.forEach(function(requi){

        assignedTechnician: self.technician_name(requi.assignedTechnician)
      })
    }
  }
}
</script>
<style>
.border {
  border-radius: 5px;
}

.marginButton {
  margin-top: 15px;
  margin-right: 25px;
  margin-left: 25px;
  width: 140px;
}

.marginCard {
  margin-top: 10px;
}

#dontExistRequisition {
  margin-top: 20px;
  margin: 0 auto;
}

.high {
  background-color: rgb(255, 0, 0);
  color: white;
  border: 1px solid rgb(255, 0, 0);
  border-radius: 5px;
}

.medium {
  background-color: rgb(255, 255, 0);
  color: black;
  border: 1px solid rgb(255, 255, 0);
  border-radius: 5px;
}

.low {
  background-color: rgb(0, 255, 0);
  color: white;
  border: 1px solid rgb(0, 255, 0);
  border-radius: 5px;
}

.backgroundRequisition {
  background-color: rgba(38, 153, 251, 0.83);
}

.center {
  margin: 0 auto;
}

.low:before {
  content: "Baja";
}

.medium:before {
  content: "Media";
}

.high:before {
  content: "Alta";
}

.request:before {
  content: "REQUERIMIENTO";
}

.error:before {
  content: "ERROR";
}
</style>
