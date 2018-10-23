<template>
  <div>
    <div class="col-8 centerForm">
      <form v-on:submit.prevent id="form">
        <label>Fecha</label>
        <input required type="date" class="form-control" v-model="requisition.date">
        <label>Detalle</label>
        <textarea class="form-control" rows="5" v-model="requisition.details"></textarea>
        <label for="inputFile">Archivo adjunto</label>
        <input id="inputFile" type="file" >
        <button type="submit" class="btn btn-primary form-control boldText" v-on:click="send">ENVIAR</button>
      </form>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      requisition: {
        type: '',
        author: sessionStorage.getItem('idUser'),
        subject: '',
        date: '',
        details: '',
        priority: null,
        affectedSystem: '',
        affectedModule: null,
        system: null,
        module: null,
        attached_file: null,
        status: '1'
      }
    }
  }

}
</script>
<style>
</style>
