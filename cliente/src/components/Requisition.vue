<template>
<div>
  <div class="card backgroundColor text-center boldText display">
    <div class="card-body">
      <h3 class="card-title  whiteText">{{ type }}</h3>
      <div class="whiteBackground border">
        <p class="card-text textColor">{{ subject }}</p>
      </div>
      <h3 class="card-title  whiteText">Prioridad</h3>
      <div class="whiteBackground border">
        <p class="card-text textColor">{{ priority }}</p>
      </div>
      <h3 class="card-title  whiteText">Fecha</h3>
      <div class="whiteBackground border">
        <p class="card-text textColor">{{ date }}</p>
      </div>
      <button type="button" class="boldText buttonMargin btn btn-light textColor">EDITAR</button>
      <button type="button" class="boldText buttonMargin btn btn-danger">ELIMINAR</button>
    </div>
  </div>
</div>
</template>
<script>
import axios from 'axios';

export default {
  data() {
    return {
      type: 'REQUERIMIENTO',
      subject: 'algo que no se',
      priority: 'alta',
      date: '12/4/94'
    }
  },
  mounted() {
    axios.get('./static/prueba.json')
      .then((response) => {
        this.type = response.data.data.type;
        this.subject = response.data.data.subject;
        this.priority = response.data.data.priority;
        this.date = response.data.data.date;
      })
      .catch((error) => {
        console.log("No salio");
      });
  }
}
</script>
<style>
.display {
  display: table;
}

.border {
  border-radius: 5px;
}

.buttonMargin {
  margin-top: 15px;
  margin-right: 25px;
  margin-left: 25px;
  width: 150px;
}
</style>
