Title: Gravity simulation with Bevy and WASM
Date: 2023-11-16 10:20
Category: Sandbox

I have been playing around with the [Bevy](https://bevyengine.org/) game engine (written in Rust) for
a while now and seemed like a good idea to showcase some small experiments in here. Making use of the Rust compilation
to `wasm32` target and `wasm-bindgen` crate, everybody can "play" interactively with some planets and gravity directly in the browser.

1. Modify the velocity, mass or position of the planets to generate orbital movements. The dotted trajectory will help you visualize where the bodies will move.
2. Click on `Run simulation` to start. `Reset` will start the simulation with default values and `Spawn new` will spawn an extra planet.

**_NOTE:_** Collisions are not implemented.

**It will take a few seconds to load at the bottom of the page**
<script type="module">
    import init from './gravity_simulation/rust-graphics.js'
    init()
</script>