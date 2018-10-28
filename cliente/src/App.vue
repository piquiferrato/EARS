<template>
<div class="container">
  <router-view></router-view>
</div>
</template>

<script>
export default {
  // components: {PulseLoader},
  data() {
    return {}
  }
}
</script>

<style>
.backgroundColor {
  background-color: #2699FB;
}

.whiteText {
  color: #FFFFFF;

}

.hover:hover {
  background-color: #2699FB;
  color: #FFFFFF;
  border: 1px solid #FFFFFF;
  transition: background-color 0.5s, color 0.5s, border 0.5s;
}

.boldText {
  font-weight: bold;
}

.btnNavigationBorder {
  border: 1px solid #2699FB;
}

.whiteBackground {
  background-color: #FFFFFF;
}

.textColor {
  color: #2699FB;
}

@media (max-width:768px) {
  .elementPosition {
    padding-left: 370px;
    padding-bottom: 5px;
    position: fixed;
  }
}


@media (max-width:360px) {
  .elementPosition {
    padding-left: 220px;
    padding-bottom: 20px;
    position: fixed;
  }
}

</style>
