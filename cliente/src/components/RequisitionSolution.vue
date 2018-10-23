<template>
  <div>
    <div class="col-8 centerForm" v-if="soluctionSection">
      <form v-on:submit.prevent id="form">
        <label>Fecha</label>
        <input required type="date" class="form-control" v-model="date">
        <label>Detalle</label>
        <textarea class="form-control" rows="5" v-model="description"></textarea>
        <label for="inputFile">Archivo adjunto</label>
        <input id="inputFile" type="file" >
        <button type="submit" class="btn btn-primary form-control boldText" v-on:click="save_constancy()">ENVIAR</button>
      </form>
    </div>
  </div>
</template>
<script>
import EventBus from '../bus/eventBus.js'
import axios from 'axios'
export default {
  data() {
    return {
      date: null,
      description: null,
      attachedFile: null,
      requisition: null,
      soluctionSection: false
    }
  },
  mounted() {
    EventBus.$on('save_constancy', (requisition) => {
      this.soluctionSection = true
      this.requisition = requisition
    })

  },
  methods: {
    save_constancy() {
      axios.post('http://127.0.0.1:8000/requisitions/constancys/', {
          finishDate: this.date,
          description: this.description,
          attachedFile: this.attachedFile
        })
        .then((data) => {
          this.update_constancyId_requisition(data.data.id)
          console.log("pasa");
        })
        .catch((error) => {
          console.log(error.response);
        });

    },
    update_constancyId_requisition(idConstancy) {
      axios.put('http://127.0.0.1:8000/requisitions/update/' + this.requisition.id + '/', {
          constancy: idConstancy,
          date: this.requisition.date,
          subject: this.requisition.subject,
          state: 4
        })
        .then((data) => {
          this.soluctionSection = false
          EventBus.$emit('go_back')
        })
        .catch((error) => {
          console.log(error.response);
        });
    }
  }

}
</script>
<style>
</style>
