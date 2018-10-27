<template>
<div v-if="privateSection">
  <div class="row" v-if="requisitionSection">
    <!-- <div class="form-group  col-sm-6 col-md-4">
      <label for="">Ordenar por</label>
      <select class="form-control" v-model="orderBy" v-on:change="load(state)">
          <option value="priority">Prioridad</option>
          <option value="date">Fecha</option>
        </select>
    </div>
    <div class="form-group col-sm-6 col-md-4">
      <label for="">De manera</label>
      <select class="form-control" v-model="orderType"  v-if="!dateOrder" v-on:change="load(state)">
          <option value="0">Creciente</option>
          <option value="1">Decreciente</option>
        </select>
      <select class="form-control" v-model="orderType"  v-if="dateOrder" v-on:change="load(state)">
          <option value="0">Nuevo-Viejo</option>
          <option value="1">Viejo-Nuevo</option>
        </select>
    </div>
    <div class=" col-sm-6 col-md-4 marginButtonSearch">
      <button type="button" class="btn btn-primary form-control" v-on:click="advanceSearch= !advanceSearch">Busqueda Avanzada</button>
    </div>
    <transition name="fade">
      <div class="col-12" v-if="advanceSearch">
        <div class="form-group">
          <label for="">Sistema Afectado</label>
        </div>
        <div class="form-group">
          <label for="">Modulo Afectado</label>
        </div>
      </div>
    </transition> -->
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
          <div>
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
      // advanceSearch: false,
      cancelled: false,
      requisition: null,
      requisitionSection: true,
      requisitionDetails: false,
      technicianName: null,
      state: null,
      // orderBy: 'priority',
      // orderType: '1',
      // dateOrder: false
      privateSection: false
    }
  },
  mounted() {
    EventBus.$on('watch_my_requisitions_taken', () => {
      this.privateSection = !this.privateSection
      this.load()
    })
    EventBus.$on('go_back', (status) => {
      this.load()
    })
  },
  methods: {
    load() {
      axios.get('http://127.0.0.1:8000/requisitions/inprogress/technician/' + sessionStorage.getItem('idUser'))
        .then((response) => {
          this.requisition = response.data
          this.requisitionSection = true
        })
        .catch((error) => {
          console.log(error.response);
        });
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
              self.load()
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
