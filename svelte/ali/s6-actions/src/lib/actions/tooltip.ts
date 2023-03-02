import tippy from "tippy.js";

export default function tooltip(node, options) {
  console.log(options);
  const instance=tippy(node, options);

  function handleMouseover() {
    console.log("mouse clicked");
  }

  node.addEventListener("mouseup", handleMouseover);

  return {
    destroy(){
      //@ts-ignore
      instance.destroy()
    }
  }

}