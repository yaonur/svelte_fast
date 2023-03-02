export default function longpress(node, options) {

  let timer;

  function handleMousedown(event) {
    console.log("mousedown");
    const { duration = 1000 } = options;

    timer = setTimeout(() => {
      console.log("long pressed");
      node.dispatchEvent(new CustomEvent("longpress"));
    }, duration);
  }

  function handleMouseup() {
    console.log("mouseup");
    clearTimeout(timer);
  }

  node.addEventListener("mouseup", handleMouseup);
  node.addEventListener("mousedown", handleMousedown);

  return {
    update(newOptions) {
      options = newOptions;
    },
    destroy() {
      console.log("destroy");
      clearTimeout(timer);
      node.removeEventListener("mouseup", handleMouseup);
      node.removeEventListener("mousedown", handleMousedown);

    }
  };
}