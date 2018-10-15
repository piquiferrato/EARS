<template>
<div class="col-8 centerForm">
  <form @submit.prevent="enviar">
    <label>Tipo de pedido</label>
    <div class="form-group">
      <select name="" class="form-control" v-model="type">
        <option value="requerimiento">Requerimiento</option>
        <option value="error">Error</option>
      </select>
    </div>
    <label>Asunto</label>
    <input type="text" id="asunto" class="form-control" v-model="subject">
    <label>Fecha</label>
    <input type="text" class="form-control" name="date">
    <label>Detalle</label>
    <textarea class="form-control" rows="5" v-model="details"></textarea>
    <label>Prioridad</label>
    <div class="form-group">
      <select name="" class="form-control" v-model="priority">
        <option value="c">Baja</option>
        <option value="b">Media</option>
        <option value="a">Alta</option>
      </select>
    </div>
    <label>Sistema</label>
    <div class="form-group">
      <select name="" class="form-control" v-model="affected_system">
        <option value="administration">Administracion</option>
        <option value="stock">Stock</option>
        <option value="human resources">Recurso Humanos</option>
      </select>
    </div>
    <label>Modulo</label>
    <div class="form-group">
      <select name="" class="form-control" v-model="module">
        <option value="uno">uno</option>
        <option value="dos">dos</option>
        <option value="tres">tres</option>
      </select>
    </div>
    <label for="inputFile">Archivo adjunto</label>
    <input id="inputFile" type="file" >
    <button type="submit" class="btn btn-primary form-control boldText" v-on:click="enviar">ENVIAR</button>
  </form>
</div>
</template>
<script>
import axios from 'axios';
export default {

  data() {
    return {
      type: '',
      author: '18',
      subject: '',
      date: '',
      details: '',
      priority: '',
      affected_system: '',
      module: '',
      attached_file: null

    }
  },
  methods: {
    enviar() {
      axios.post('http://127.0.0.1:8000/requisitions/', {
          type: this.type,
          author: this.author,
          subject: this.subject,
          date: this.date,
          details: this.details,
          priority: this.priority,
          affected_system: this.affected_system,
          module: this.module,
          attached_file: this.attached_file
        })
        .then((data) => {
          console.log(data);
        })
        .catch((error) => {
          console.log(error.response);
        });
    }

  }
}
</script>
<style>
#inputFile {
  width: 0.1px;
  height: 0.1px;
  opacity: 0;
  overflow: hidden;
  position: absolute;
  z-index: -1;
}

label[for="inputFile"] {
  font-size: 14px;
  font-weight: 600;
  color: #FFFFFF;
  background-color: #2699FB;
  display: inline-block;
  cursor: pointer;
  padding: 15px 40px !important;
  text-transform: uppercase;
  width: fit-content;
  text-align: center;
}

.formWidth {
  width: 80%;
}

.centerForm {
  margin: 0 auto;
}
</style>
