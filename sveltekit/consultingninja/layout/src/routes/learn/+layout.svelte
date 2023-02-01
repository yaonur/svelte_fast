<div class="container">
  <div>
    <h1>Some learning stuff</h1>
    <p>and a paragraf </p>
  </div>
  <div>
    <h2>More learning stuff on h2</h2>
  </div>
  <div class="item">
    <slot></slot>
  </div>
</div>

<style>
  .container{
    display:flex;
    flex-direction:column;
    align-items:center;
  }
  .item{
    align-self:flex-start;
  }
</style>