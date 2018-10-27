<template>
<div v-if="privateSection">
  <div class="row" v-if="requisitionSection">
    <div v-for="(requi , index) in requisition" :key="index" class="col-md-12 col-lg-6 " v-if="requisition">
      <div class="card card-block backgroundColor text-center boldText marginCard">
        <div class="card-body">
          <h3 class="card-title whiteText">{{ requi.type }}</h3>
          <div class="whiteBackground border">
            <p class="card-text textColor">{{ requi.subject }}</p>
          </div>
          <h3 class="card-title whiteText">Prioridad</h3>
          <div class="whiteBackground border">
            <p class="card-text textColor" :class="{high: requi.priority == 'Alta', medium: requi.priority == 'Media',
              low: requi.priority == 'Baja'}">{{ requi.priority }}</p>
          </div>
          <h3 class="card-title whiteText">Fecha</h3>
          <div class="whiteBackground border">
            <p class="card-text textColor">{{ requi.date }}</p>
          </div>
          <h3 class="card-title whiteText">Tomado por</h3>
          <div class="whiteBackground border">
            <p class="card-text textColor">{{requi.assignedTechnician}}</p>
          </div>
          <div v-if="!inProcess">
            <button type="button" class="boldText marginButton btn btn-light textColor" v-on:click="watch_requisition(requi.id)">VER</button>
          </div>
          <div v-if="inProcess">
            <button type="button" class="boldText marginButton btn btn-light textColor" v-on:click="close_requisition(requi.id)">FINALIZAR</button>
            <button type="button" class="boldText marginButton btn btn-danger" v-on:click="cancel_requisition(requi.id)">CANCELAR</button>
          </div>
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
      cancelled: false,
      requisition: null,
      requisitionSection: true,
      requisitionDetails: false,
      technicianName: null,
      state: null,
      privateSection: false,
      inProcess: true
    }
  },
  mounted() {
    EventBus.$on('watch_my_requisitions_taken', () => {
      if (!this.privateSection) {
        this.privateSection = !this.privateSection
        this.load("inProgress")
      }else {
        this.load("inProgress")
      }
    })
    EventBus.$on('watch_my_requisitions_finish', () => {
      if (!this.privateSection) {
        this.privateSection = !this.privateSection
        this.load("finish")
      }else {
        this.load("finish")
      }
    })
    EventBus.$on('go_back', () => {
      this.load("finish")
    })
  },
  methods: {
    load(state) {
      if (state === 'inProgress') {
        axios.get('http://127.0.0.1:8000/requisitions/inprogress/technician/' + sessionStorage.getItem('idUser'))
          .then((response) => {
            this.requisition = response.data
            this.requisitionSection = true
            this.inProcess = true
          })
          .catch((error) => {
            console.log(error.response);
          });
      }else if (state === 'finish') {
        axios.get('http://127.0.0.1:8000/requisitions/done/technician/' + sessionStorage.getItem('idUser'))
          .then((response) => {
            this.requisition = response.data
            this.requisitionSection = true
            this.inProcess = false
          })
          .catch((error) => {
            console.log(error.response);
          });
      }
    },
    cancel_requisition(requisitionId) {
      var self = this
      this.requisition.forEach(function(requi) {
        if (requi.id === requisitionId) {
          var state = 3
          axios.put('http://127.0.0.1:8000/requisitions/update/' + requisitionId + '/', {
              assignedTechnician: null,
              status: state
            })
            .then((data) => {
              EventBus.$emit('load_quantity_requisition')
              self.load('inProgress')
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
          self.requisitionSection = false
          EventBus.$emit('save_constancy', requi)
        }
      })
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

.marginButtonSearch {
  margin-top: 30px;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity .5s
}

.fade-enter,
.fade-leave-to

/* .fade-leave-active in <2.1.8 */
  {
  opacity: 0
}

@media (max-width:768px) {
  .marginButtonSearch {
    margin: 0 auto;
  }
}
</style>
