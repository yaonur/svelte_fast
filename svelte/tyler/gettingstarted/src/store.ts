import {writable} from "svelte/store"

export const count_val = writable(0)

const createCounter = () => {
    const {set, update, subscribe} = writable(0)
    const add = () => {
        console.log("counter add runned on store")
        update(val => val += 1)
    }
    const subtract = () => {
        update(val => --val)
    }
    const reset = () => {
        set(0)
    }
    return {
        subscribe,
        add,
        subtract,
        reset
    }
}

export const counter = createCounter()