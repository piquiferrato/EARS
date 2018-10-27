<template>
<div v-if="!privateSection">
  <div class="row" v-if="requisitionSection">
    <div class="form-group  col-sm-6 col-md-4">
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
        <label>Sistema</label>
        <div class="form-group">
          <v-select label="name" :options="system" :on-change="moduleSystem" :searchable="false"></v-select>
        </div>
        <div v-if="moduleSelect">
          <label >Modulo</label>
          <div class="form-group">
            <v-select label="name" :options="module" :on-change="moduleId" :searchable="false"></v-select>
          </div>
        </div>
      </div>
    </transition>
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
      advanceSearch: false,
      inProcess: false,
      cancelled: false,
      requisition: null,
      requisitionSection: true,
      requisitionDetails: false,
      technicianName: null,
      state: null,
      orderBy: 'priority',
      orderType: '1',
      dateOrder: false,
      privateSection: false,
      system: null,
      module: null,
      moduleSelect: false
    }
  },
  mounted() {
    EventBus.$on('watch_my_requisitions_taken', () => {
      this.privateSection = !this.privateSection
    })
    EventBus.$on('watch_my_requisitions_finish', () => {
      this.privateSection = !this.privateSection
    })
    EventBus.$on('watch_all_requisitions', () => {
      this.privateSection = !this.privateSection
    })
    this.load(1)
    EventBus.$on('watch_requisition', (status) => {
      this.load(status)
    })
    EventBus.$on('go_back', () => {
      // this.load(status)
      this.requisitionSection = true
    })
    //La API devuelve todos los sistemas
    axios.get('http://127.0.0.1:8000/requisitions/systems')
      .then((response) => {
        this.system = response.data
      })
      .catch((error) => {
        console.log(error);
      });
  },
  methods: {
    load(status) {
      EventBus.$emit('load_quantity_requisition')
      this.state = status
      if (this.orderBy === 'date') {
        this.dateOrder = true
      } else {
        this.dateOrder = false
      }
      // Devuelve todos los pedidos de los usuarios
      axios.get('http://127.0.0.1:8000/requisitions/status/' + status + '/order/' + this.orderBy + '/' + this.orderType + '/')
        .then((response) => {
          EventBus.$emit('select_nav_btn', status)
          if (status === 2) {
            this.inProcess = true
          } else if (status != 2) {
            this.inProcess = false
          }
          this.requisition = response.data
          this.requisitionSection = true

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
    moduleSystem(systemId) {
      axios.get('http://127.0.0.1:8000/search/' + this.orderBy + '/system/'+ systemId.id + '/status/' + this.state + '/order/' + this.orderType + '/')
        .then((response) => {
        this.requisition = response.data
        })
        .catch((error) => {
          console.log(error);
        });
      axios.get('http://127.0.0.1:8000/requisitions/modules/system/' + systemId.id + '/')
        .then((response) => {
          this.module = response.data
          this.moduleSelect = true
        })
        .catch((error) => {
          console.log(error);
        });
    },
    moduleId(module) {
      axios.get('http://127.0.0.1:8000/search/' + this.orderBy + '/module/'+ module.id + '/status/' + this.state + '/order/' + this.orderType + '/')
        .then((response) => {
        this.requisition = response.data
        })
        .catch((error) => {
          console.log(error);
        });
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
