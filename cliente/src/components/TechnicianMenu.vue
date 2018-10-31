<template>
<div>
  <div class="row justify-content-center align-items-center backgroundColor">
    <div class="col-10 text-center">
      <h3 class="boldText whiteText">BIENVENIDO {{ name }}</h3>
    </div>
    <div class="col-2 elementPosition">
      <a href="#" id="logOut" class="boldText whiteText" v-on:click="logOut">LOGOUT</a>
    </div>
  </div>
  <b-navbar toggleable="md" class="row backgroundColor">
    <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
    <b-collapse is-nav id="nav_collapse">
      <b-navbar-nav class="center">
        <b-nav-item class="btn textColor btnNavigationBorder whiteBackground hover boldText text-center mt-1" :class="{activeButton: disabledTaken}" :disabled="disabledTaken" v-on:click="watch_my_requisitions_taken">MIS PEDIDOS TOMADOS</b-nav-item>
        <b-nav-item class="btn textColor btnNavigationBorder whiteBackground hover boldText text-center mt-1" :class="{activeButton: disabledFinish}" :disabled="disabledFinish" v-on:click="watch_my_requisitions_finish">MIS PEDIDOS FINALIZADOS</b-nav-item>
        <b-nav-item class="btn textColor btnNavigationBorder whiteBackground hover boldText text-center mt-1" :class="{activeButton: disabledAll}" :disabled="disabledAll" v-on:click="watch_all_requisitions">TODOS LOS PEDIDOS</b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
  <div class="row backgroundColor font" v-if="!privateSection">
    <ul class="nav navBar">
      <li class="text-center textColor btnNavigationBorder whiteBackground hover nav-item" v-on:click="search_requisitions(1)" :class="{activeButton: onHold}">
        <span class="boldText">EN ESPERA({{ quantityOnHold }})</span>
      </li>
      <li class="text-center textColor btnNavigationBorder whiteBackground hover nav-item" v-on:click="search_requisitions(2)" :class="{activeButton: inProcess}">
        <span class="boldText">EN PROCESO({{ quantityInProcess }})</span>
      </li>
      <li class="text-center textColor btnNavigationBorder whiteBackground hover nav-item" v-on:click="search_requisitions(3)" :class="{activeButton: cancelled}">
        <span class="boldText">CANCELADO({{ quantityCancelled }})</span>
      </li>
      <li class="text-center textColor btnNavigationBorder whiteBackground hover nav-item" v-on:click="search_requisitions(4)" :class="{activeButton: finished}">
        <span class="boldText">TERMINADO({{ quantityFinished }})</span>
      </li>
    </ul>
  </div>
  <techCard></techCard>
  <technicianRequisitionTaken></technicianRequisitionTaken>
</div>
</template>
<script>
import axios from 'axios'
import techCard from './TechCard.vue'
import technicianRequisitionTaken from './TechnicianRequisitionTaken.vue'
import EventBus from '../bus/eventBus.js'
export default {
  components: {
    techCard,
    technicianRequisitionTaken
  },
  mounted() {
    axios.get('http://127.0.0.1:8000/users/' + sessionStorage.getItem('idUser'), {
        //  params: {
        //   id: sessionStorage.getItem('idUser')
        // },
        headers: {
          'Authorization': 'JWT' + sessionStorage.getItem('idToken')
        }
      })
      .then((response) => {
        this.name = response.data.username
      })
      .catch((error) => {
        console.log("No salio")
      })
    EventBus.$on('select_nav_btn', (status) => {
      this.correct_section(status)
    })
    this.load_quantity_requisition()
    EventBus.$on('load_quantity_requisition', () => {
      this.load_quantity_requisition()
    })
  },
  data() {
    return {
      name: null,
      onHold: true,
      inProcess: false,
      cancelled: false,
      finished: false,
      privateSection: false,
      quantityInProcess: null,
      quantityOnHold: null,
      quantityCancelled: null,
      quantityFinished: null,
      disabledTaken: false,
      disabledFinish: false,
      disabledAll: true,
    }
  },
  methods: {
    load_quantity_requisition() {
      axios.get('http://127.0.0.1:8000/requisitions/status/waiting/')
        .then((response) => {
          this.quantityOnHold = response.data.length
        })
        .catch((error) => {
          console.log("No salio")
        })
      axios.get('http://127.0.0.1:8000/requisitions/status/inprogress/')
        .then((response) => {
          this.quantityInProcess = response.data.length
        })
        .catch((error) => {
          console.log("No salio")
        })
      axios.get('http://127.0.0.1:8000/requisitions/status/cancelled/')
        .then((response) => {
          this.quantityCancelled = response.data.length
        })
        .catch((error) => {
          console.log("No salio")
        })
      axios.get('http://127.0.0.1:8000/requisitions/status/done/')
        .then((response) => {
          this.quantityFinished = response.data.length
        })
        .catch((error) => {
          console.log("No salio")
        })
    },
    logOut() {
      this.$swal({
        title: '¿Seguro que quieres salir?',
        type: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#2699FB',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, estoy seguro',
        cancelButtonText: 'Cancelar'
      }).then((result) => {
        if (result.value) {
          this.$swal(
            'Cierre de sesión exitoso',
          )
          sessionStorage.clear()
          this.$router.push('/')
        }
      })
    },
    search_requisitions(status) {
      this.correct_section(status)
      EventBus.$emit('watch_requisition', status)
    },
    correct_section(status) {
      var onHold = 1
      var inProcess = 2
      var cancelled = 3
      var finished = 4
      if (status === onHold) {
        this.onHold = true
        this.inProcess = false
        this.finished = false
        this.cancelled = false
      } else if (status === inProcess) {
        this.onHold = false
        this.inProcess = true
        this.finished = false
        this.cancelled = false
      } else if (status === cancelled) {
        this.onHold = false
        this.inProcess = false
        this.finished = false
        this.cancelled = true
      } else if (status === finished) {
        this.onHold = false
        this.inProcess = false
        this.finished = true
        this.cancelled = false
      }
    },
    watch_my_requisitions_taken() {
      this.disabledTaken = true
      this.disabledAll = false
      this.disabledFinish = false
      EventBus.$emit('watch_my_requisitions_taken')
      if (!this.privateSection) {
        this.privateSection = !this.privateSection
      } else {
        this.privateSection = true
      }
    },
    watch_my_requisitions_finish() {
      this.disabledTaken = false
      this.disabledAll = false
      this.disabledFinish = true
      if (!this.privateSection) {
        this.privateSection = !this.privateSection
        EventBus.$emit('watch_my_requisitions_finish')
      } else {
        this.privateSection = true
        EventBus.$emit('watch_my_requisitions_finish')
      }
    },
    watch_all_requisitions() {
      this.disabledTaken = false
      this.disabledAll = true
      this.disabledFinish = false
      EventBus.$emit('watch_all_requisitions')
      EventBus.$emit('close_my_requisition')
      this.privateSection = false
    }
  }
}
</script>
<style>
.activeButton {
  background: #2699FB;
  color: #FFFFFF;
  border: 1px solid #FFFFFF;
}

.navbar-light .navbar-nav .nav-link.disabled {
  color: #FFFFFF;
}

.navbar-light .navbar-nav .nav-link {
  color: #2699FB;
}

@media (max-width:768px) {
  .font {
    font-size: 0.7em;
  }
}

.navBar {
  width: 100%;
}

.navBar li {
  width: calc(100% / 4);
  height: 4em;
  display: table;
}

.navBar li span {
  display: table-cell;
  vertical-align: middle;
}
</style>
