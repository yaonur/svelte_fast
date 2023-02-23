<script lang="ts">
  export let size = "small";
  export let shadow = false;
  export let bgColor = "inherit";
  export let textColor = "inherit";
  
  // console.log($$restProps);
</script>

<!--<button class={size === "large" ? "size-lg" : "size-sm"}>-->
<button
  on:click
  class:size-lg={size === "large"}
  class:size-sm={size === "small"}
  class:shadow
  style:--buttonBgColor={bgColor}
  style:--buttonTextColor={textColor}
  {...$$restProps}
>
  <slot>Fallback</slot>
</button>
<p>Button module</p>

<style lang="postcss">
  button {
    border: none;
    background-color: var(--buttonBgColor);
    color: var(--buttonTextColor);
    font-weight: bold;
    border-radius: 5px;
    cursor: pointer;

    &:hover {
      background-image: var(--linear);
    }
    &:disabled{
      opacity: 0.6;
      cursor: not-allowed;
    }
    &.size-sm {
      padding: 15px 20px;
    }

    &.size-lg {
      padding: 20px 30px;
    }
    &.shadow {
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
    }
  }
</style>

<!--<style lang="scss">-->
<!--  @use "../styles/variables.scss";-->

<!--  button {-->
<!--    border: none;-->
<!--    background-color: #e56441;-->
<!--    color: #fff;-->
<!--    font-weight: bold;-->
<!--    border-radius: 5px;-->
<!--    cursor: pointer;-->

<!--    &.size-sm {-->
<!--      padding: 15px 20px;-->
<!--    }-->

<!--    &.size-lg {-->
<!--      padding: 20px 30px;-->
<!--    }-->
<!--    &.shadow {-->
<!--      box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);-->
<!--    }-->

<!--    &:hover {-->
<!--      background-image: variables.$linear-effect;-->
<!--    }-->
<!--  }-->
<!--</style>-->

