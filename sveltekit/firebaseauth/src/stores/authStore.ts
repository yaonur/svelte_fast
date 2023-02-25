import {writable} from "svelte/store";
import {auth} from "$lib/firebase/firebase.client";
import {createUserWithEmailAndPassword,signOut} from "firebase/auth";

export const authStore=writable({
  isLoading:true,
  currentUser:null,
})

export const authHandlers={
  signup: async (email:string, password:string) => {
    try {
      await createUserWithEmailAndPassword(auth,email, password);
    } catch (error) {
      console.log(error);
    }
  }
}