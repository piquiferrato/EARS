<template>
<div>
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
            <p class="card-text textColor" :class="{low: requi.priority == '3',
            medium: requi.priority == '2', high: requi.priority == '1'}"></p>
          </div>
          <h3 class="card-title whiteText">Fecha</h3>
          <div class="whiteBackground border">
            <p class="card-text textColor">{{ requi.date }}</p>
          </div>
          <h3 class="card-title whiteText">Tomado por</h3>
          <div class="whiteBackground border">
            <p class="card-text textColor">vacio</p>
          </div>
          <button type="button" class="boldText marginButton btn btn-light textColor" v-on:click="watch_requisition(requi.id)">VER</button>
        </div>
      </div>
    </div>
    <div class="textColor" id="dontExistRequisition" v-if="requisition.length == 0">
      <h1>NO HAY PEDIDOS</h1>
    </div>
  </div>
  <div class="col-8 center" v-if="requisitionDetails">
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
    <button type="button" class="boldText marginButton btn btn-light textColor" v-on:click="takeRequisition(user, userRequisition.id)">TOMAR</button>
    <button type="button" class="boldText marginButton btn btn-danger" v-on:click="cancelRequisition()">CANCELAR</button>
  </div>
</div>
</template>
<script>
import axios from 'axios';
import EventBus from '../bus/eventBus.js';
export default {
  data() {
    return {
      user: sessionStorage.getItem('idUser'),
      requisition: null,
      requisitionSection: true,
      requisitionDetails: false,
      userRequisition: null,
      system: null,
      module: null,
      priority: null,
      systemName: null,
      moduleName: null,
      priorityName: null
    }
  },
  // computed: {
  //   isHigh: function() {
  //     return this.requisition.priority;
  //   },
  //   isMedium: function() {
  //     return this.requisition.priority === 'media';
  //   },
  //   isLow: function() {
  //     return this.requisition.priority === 'baja';
  //   }
  // },
  mounted() {
    EventBus.$on('watch_requisition', (status) => {
      // Devuelve todos los pedidos del usuario
      axios.get('http://127.0.0.1:8000/requisitions/status/' + status + '/')
        .then((response) => {
          this.requisition = response.data
        })
        .catch((error) => {
          console.log(error.response);
        });
    })
  },
  methods: {
    watch_requisition(id) {
      var self = this;
      this.requisition.forEach(function(requi) {
        if (requi.id == id) {
          self.search_affected_system(requi.affectedSystem, requi.module, requi.priority, requi)
          // EventBus.$emit('change_module');
        }
      });
    },
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
            this.requisitionSection = false
            this.requisitionDetails = true
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
    cancelRequisition() {
      this.requisitionSection = true;
      this.requisitionDetails = false;
    },
    takeRequisition(userId, requisitionId) {
      var self = this
      this.requisition.forEach(function(requi) {
        if (requi.id === requisitionId) {
          axios.put('http://127.0.0.1:8000/requisitions/update/' + requisitionId + '/', {
              type: requi.type,
              assignedTechnician: userId,
              subject: requi.subject,
              date: requi.date,
              details: requi.details,
              priority: requi.priority,
              affectedSystem: requi.affectedSystem,
              module: requi.module,
              attached_file: requi.attached_file,
              status: 2
            })
            .then((data) => {
              // EventBus.$emit('change_section');
              console.log(data);
            })
            .catch((error) => {
              console.log(error.response);
            });
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

.low:before {
  content: "Baja";
}

.medium:before {
  content: "Media";
}

.high:before {
  content: "Alta";
}
</style>
