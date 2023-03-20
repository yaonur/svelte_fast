import { readable } from "svelte/store";

const location = readable(null, (set) => {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        // console.log(position)
        set({
          lat: position.coords.latitude,
          lon: position.coords.longitude,
        });
      },
      (error) => {
        console.log(error);
      }
    );
  }
  return ()=>{
    set(null)
  }
});
export default location
