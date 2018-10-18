<template>
<div>
  <div class="row">
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
          <button type="button" class="boldText marginButton btn btn-light textColor" v-on:click="editRequisition(requi.id)">VER</button>
        </div>
      </div>
    </div>
    <div class="textColor" id="dontExistRequisition" v-if="requisition.length == 0">
      <h1>NO HAY PEDIDOS</h1>
    </div>
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
</style>
