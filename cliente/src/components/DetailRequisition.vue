<template>
<div v-if="detailSection">
  <div class="row">
    <div class="col-8 center text-center" id="detailSection">
      <label>Tipo de pedido</label>
      <h3 class="border  backgroundRequisition whiteText">{{ userRequisition.type }}</h3>
      <label>Asunto</label>
      <h3 class="border  backgroundRequisition whiteText">{{ userRequisition.subject }}</h3>
      <label>Detalle</label>
      <h4 class="border  backgroundRequisition whiteText">{{ userRequisition.details }}</h4>
      <label>Prioridad</label>
      <h3 class="border  backgroundRequisition whiteText">{{ userRequisition.priority }}</h3>
      <label>Sistema</label>
      <h3 class="border  backgroundRequisition whiteText">{{ userRequisition.affectedSystem }}</h3>
      <label>Modulo</label>
      <h3 class="border  backgroundRequisition whiteText">{{ userRequisition.module }}</h3>
      <div v-if="watchConstancy">
        <label>Constancia</label>
        <h3 class="border  backgroundRequisition whiteText">{{ userRequisition.constancy }}</h3>
      </div>
      <label>Descargar archivo adjunto</label>
      <h3 class="border  backgroundRequisition whiteText">ARCHIVO</h3>
      <button type="button" class="boldText marginButton btn btn-light textColor" v-if="watchButton"
      v-on:click="take_requisition(user, userRequisition.id)">TOMAR</button>
      <button type="button" class="boldText marginButton btn btn-danger" v-on:click="go_back()">VOLVER</button>
    </div>
  </div>
</div>
</template>
<script>
import axios from 'axios'
import EventBus from '../bus/eventBus.js'
export default {
  data() {
    return {
      user: sessionStorage.getItem('idUser'),
      detailSection: false,
      userRequisition: null,
      watchButton: false,
      watchConstancy: false
    }
  },
  mounted() {
    EventBus.$on('requisition_detail', (requisition) => {
      if (requisition.status === 'En espera' || requisition.status === 'Cancelado') {
        this.watchButton = true
        this.watchConstancy = false
      } else if (requisition.status === 'Terminado') {
        this.watchButton = false
        this.watchConstancy = true
      } else {
        this.watchConstancy = false
        this.watchButton = false
      }
      this.detailSection = true
      this.userRequisition = requisition
    })

  },
  methods: {
    go_back() {
      this.detailSection = false
      EventBus.$emit('go_back')
    },
    take_requisition(userId, requisitionId) {
      var state = 2
      axios.put('http://127.0.0.1:8000/requisitions/update/' + requisitionId + '/', {
          assignedTechnician: userId,
          status: state
        })
        .then((data) => {
          this.$swal({
            type: 'success',
            title: 'Pedido tomado'
          })
          EventBus.$emit('watch_requisition', 2)
          this.detailSection = false;
        })
        .catch((error) => {
          console.log(error.response);
        });
    }
  }

}
</script>
<style>
.center {
  margin: 0 auto;
}

.request:before {
  content: "REQUERIMIENTO";
}

.error:before {
  content: "ERROR";
}
</style>
