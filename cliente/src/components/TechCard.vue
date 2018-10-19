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
            <p class="card-text textColor" :class="{low: requi.priority == 'baja',
            medium: requi.priority == 'media', high: requi.priority == 'alta'}">{{ requi.priority }}</p>
          </div>
          <h3 class="card-title whiteText">Fecha</h3>
          <div class="whiteBackground border">
            <p class="card-text textColor">{{ requi.date }}</p>
          </div>
          <button type="button" class="boldText marginButton btn btn-light textColor" v-on:click="watchRequisition(requi.id)">VER</button>
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
    <h3 class="border text-center backgroundRequisition whiteText">{{ userRequisition.priority }}</h3>
    <label>Sistema</label>
    <h3 class="border text-center backgroundRequisition whiteText">{{ systemName }}</h3>
    <label>Modulo</label>
    <h3 class="border text-center backgroundRequisition whiteText">{{ moduleName }}</h3>
    <label>Descargar archivo adjunto</label>
    <h3 class="border text-center backgroundRequisition whiteText">ARCHIVO</h3>
    <button type="button" class="boldText marginButton btn btn-light textColor" v-on:click="takeRequisition()">TOMAR</button>
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
      requisition: null,
      requisitionSection: true,
      requisitionDetails: false,
      userRequisition: null,
      system: null,
      module: null,
      systemName: null,
      moduleName: null
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
    // Devuelve todos los pedidos del usuario
    axios.get('http://127.0.0.1:8000/requisitions/')
      .then((response) => {
        this.requisition = response.data;
      })
      .catch((error) => {
        console.log(error);
      });

  },
  methods: {
    watchRequisition(id) {
      var self = this;
      this.requisition.forEach(function(requi) {
        if (requi.id == id) {
          axios.get('http://127.0.0.1:8000/requisitions/systems/' + requi.affectedSystem + '/')
            .then((response) => {
              self.system = response.data
              console.log(requi.module)  
              axios.get('http://127.0.0.1:8000/requisitions/modules/' + requi.module + '/')
                .then((response) => {
                  self.module = response.data
                  if (requi.affectedSystem == self.system.id && requi.module == self.module.id) {
                    self.systemName = self.system.name
                    self.moduleName = self.module.name
                    self.userRequisition = requi;
                    self.requisitionSection = false;
                    self.requisitionDetails = true;
                  }
                })
                .catch((error) => {
                  console.log(error);
                });
            })
            .catch((error) => {
              console.log(error);
            });
          // EventBus.$emit('change_module');
        }
      });
    },
    cancelRequisition() {
      this.requisitionSection = true;
      this.requisitionDetails = false;

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
</style>
