<template>
<div v-if="detailSection">
  <div class="col-8 center" id="detailSection">
    <label>Tipo de pedido</label>
    <h3 class="border text-center backgroundRequisition whiteText">{{ userRequisition.type }}</h3>
    <label>Asunto</label>
    <h3 class="border text-center backgroundRequisition whiteText">{{ userRequisition.subject }}</h3>
    <label>Detalle</label>
    <h4 class="border text-center backgroundRequisition whiteText">{{ userRequisition.details }}</h4>
    <label>Prioridad</label>
    <h3 class="border text-center backgroundRequisition whiteText">{{ priorityName }}</h3>
    <label>Sistema</label>
    <h3 class="border text-center backgroundRequisition whiteText">{{ systemName }}</h3>
    <label>Modulo</label>
    <h3 class="border text-center backgroundRequisition whiteText">{{ moduleName }}</h3>
    <label>Descargar archivo adjunto</label>
    <h3 class="border text-center backgroundRequisition whiteText">ARCHIVO</h3>
    <button type="button" class="boldText marginButton btn btn-light textColor" v-on:click="take_requisition(user, userRequisition.id)">TOMAR</button>
    <button type="button" class="boldText marginButton btn btn-danger" v-on:click="go_back()">VOLVER</button>
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
      system: null,
      module: null,
      priority: null,
      systemName: null,
      moduleName: null,
      priorityName: null
    }
  },
  mounted() {
    EventBus.$on('requisition_detail', (requisition) => {
      this.detailSection = true
      this.userRequisition = requisition
      this.search_affected_system(requisition.affectedSystem, requisition.module, requisition.priority, requisition)
    })

  },
  methods: {
    search_affected_system(systemId, moduleId, priorityId, requi) {
      axios.get('http://127.0.0.1:8000/requisitions/systems/' + systemId + '/')
        .then((response) => {
          this.system = response.data
          this.search_affected_module(moduleId, priorityId, requi)
        })
        .catch((error) => {
          console.log(error);
        });
    },
    search_affected_module(moduleId, priorityId, requi) {
      axios.get('http://127.0.0.1:8000/requisitions/modules/' + moduleId + '/')
        .then((response) => {
          this.module = response.data
          this.search_priority(priorityId, requi)
        })
        .catch((error) => {
          console.log(error);
        });
    },
    search_priority(priorityId, requi) {
      axios.get('http://127.0.0.1:8000/priority/' + priorityId + '/')
        .then((response) => {
          this.priority = response.data
          if (this.correct_parameters(requi.affectedSystem, requi.module, requi.priority)) {
            this.systemName = this.system.name
            this.moduleName = this.module.name
            this.priorityName = this.priority.name
            this.userRequisition = requi
          }
        })
        .catch((error) => {
          console.log(error);
        })
    },
    correct_parameters(systemId, moduleId, priorityId) {
      return this.correct_system(systemId) && this.correct_module(moduleId) && this.correct_priority(priorityId)
    },
    correct_system(systemId) {
      return systemId === this.system.id
    },
    correct_module(moduleId) {
      return moduleId === this.module.id
    },
    correct_priority(priorityId) {
      return priorityId === this.priority.id
    },
    go_back() {
      EventBus.$emit('go_back')
      this.detailSection = false;
    },
    take_requisition(userId, requisitionId) {
      // var self = this
      // this.userRequisition.forEach(function(requi) {
      //   if (requi.id === requisitionId) {
          var state = 2
          axios.put('http://127.0.0.1:8000/requisitions/update/' + requisitionId + '/', {
              type: this.userRequisition.type,
              assignedTechnician: userId,
              subject: this.userRequisition.subject,
              date: this.userRequisition.date,
              details: this.userRequisition.details,
              priority: this.userRequisition.priority,
              affectedSystem: this.userRequisition.affectedSystem,
              module: this.userRequisition.module,
              attached_file: this.userRequisition.attached_file,
              status: state
            })
            .then((data) => {
              EventBus.$emit('watch_requisition', 2)
              this.go_back()
              this.detailSection = false
            })
            .catch((error) => {
              console.log(error.response);
            });
      //   }
      // })
    }
  }

}
</script>
<style>

</style>
