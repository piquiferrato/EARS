<template>
<div v-if="privateSection">
  <div class="row" v-if="requisitionSection && !loading">
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
  <div class="col-12 preload ">
    <moon-loader :loading="loading" :color="color" :size="size"></moon-loader>
  </div>
  <detailRequisition></detailRequisition>
  <requisitionSolution></requisitionSolution>
</div>
</template>
<script>
import axios from 'axios'
import EventBus from '../bus/eventBus.js'
import detailRequisition from './DetailRequisition.vue'
import requisitionSolution from './RequisitionSolution'
import MoonLoader from 'vue-spinner/src/MoonLoader.vue'
export default {
  components: {
    detailRequisition,
    requisitionSolution,
    MoonLoader
  },
  props: {
    color: {
      type: String,
      default: '#2699FB'
    },
    size: {
      type: String,
      default: '150px'
    }
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
      inProcess: true,
      loading: false
    }
  },
  mounted() {
    this.loading = false
    EventBus.$on('watch_my_requisitions_taken', () => {
      this.check_state_in_profress()
    })
    EventBus.$on('watch_my_requisitions_finish', () => {
      this.check_state_finished()
    })
    EventBus.$on('close_my_requisition', () => {
      this.privateSection = false
    })
    EventBus.$on('go_back', () => {
      this.load("finish")
    })
  },
  methods: {
    check_state_in_profress() {
      if (!this.privateSection) {
        this.privateSection = !this.privateSection
        this.load("inProgress")
      } else {
        this.load("inProgress")
      }
    },
    check_state_finished() {
      if (!this.privateSection) {
        this.privateSection = !this.privateSection
        this.load("finish")
      } else {
        this.load("finish")
      }
    },
    load(state) {
      this.loading = true
      if (state === 'inProgress') {
        this.load_in_progress()
      } else if (state === 'finish') {
        this.load_finished()
      }
    },
    load_in_progress() {
      axios.get('http://127.0.0.1:8000/requisitions/inprogress/technician/' + sessionStorage.getItem('idUser'))
        .then((response) => {
          this.requisition = response.data
          this.loading = false
          this.requisitionSection = true
          this.inProcess = true
        })
        .catch((error) => {
          console.log(error.response)
        })
    },
    load_finished() {
      axios.get('http://127.0.0.1:8000/requisitions/done/technician/' + sessionStorage.getItem('idUser'))
        .then((response) => {
          this.requisition = response.data
          this.loading = false
          this.requisitionSection = true
          this.inProcess = false
        })
        .catch((error) => {
          console.log(error.response)
        })
    },
    cancel_requisition(requisitionId) {
      var self = this
      this.$swal({
        title: '¿Estas seguro que quieres cancelar este pedido?',
        type: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#2699FB',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, estoy seguro',
        cancelButtonText: 'Volver'
      }).then((result) => {
        if (result.value) {
          this.$swal(
            'Pedido Cancelado',
            this.requisition.forEach(function(requi) {
              if (requi.id === requisitionId) {
                var statusCancelled = 3
                axios.put('http://127.0.0.1:8000/requisitions/update/' + requisitionId + '/', {
                    assignedTechnician: null,
                    status: statusCancelled
                  })
                  .then((data) => {
                    EventBus.$emit('load_quantity_requisition')
                    self.load('inProgress')
                  })
                  .catch((error) => {
                    console.log(error.response)
                  })
              }
            }),
          )
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
      var self = this
      this.requisition.forEach(function(requi) {
        if (requi.id === id) {
          self.requisitionDetails = true
          self.requisitionSection = false
          EventBus.$emit('requisition_detail', requi)
        }
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

.preload {
  position: fixed;
  top: 50%;
  left: 43%
}

@media (max-width:768px) {

  .preload {
    position: fixed;
    top: 50%;
    left: 25%
  }
}
</style>
