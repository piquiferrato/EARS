<template>
<div class="row">
  <div v-for="requi in requisition" class="col-md-12 col-lg-6 ">
    <div class="card card-block backgroundColor text-center boldText marginCard">
      <div class="card-body">
        <h3 class="card-title  whiteText">{{ requi.type }}</h3>
        <div class="whiteBackground border">
          <p class="card-text textColor">{{ requi.subject }}</p>
        </div>
        <h3 class="card-title  whiteText">Prioridad</h3>
        <div class="whiteBackground border">
          <p class="card-text textColor">{{ requi.priority }}</p>
        </div>
        <h3 class="card-title  whiteText">Fecha</h3>
        <div class="whiteBackground border">
          <p class="card-text textColor">{{ requi.date }}</p>
        </div>
        <button type="button" class="boldText marginButton btn btn-light textColor">EDITAR</button>
        <button type="button" class="boldText marginButton btn btn-danger">ELIMINAR</button>
      </div>
    </div>
  </div>
</div>
</template>
<script>
import axios from 'axios';

export default {
  data() {
    return {
      requisition: {}
    }
  },
  mounted() {
    axios.get('http://127.0.0.1:8000/requisitions/' +  sessionStorage.getItem('idUser'))
      .then((response) => {
        // for (var i = 0; i < response.data.length; i++) {
        //   this.requisition[i] = response.data[i];
        //
        // }
        console.log(response.data);

        // this.requisition = response.data.data;
      })
      .catch((error) => {
        console.log(error);
      });
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
</style>
