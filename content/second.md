Title: Interactive terrain generation
Date: 2023-11-16 10:20
Category: Sandbox

Terrain generation with [Perlin noise](https://en.wikipedia.org/wiki/Perlin_noise) with the same 
tech stack as in [gravity simulation](./gravity-simulation-with-bevy-and-wasm.html)

1. Use the mouse or trackpad to change the camera view.
2. Modify the `Frequency`, `Octaves`, `Persistance` and `Lacunarity` to get a terrain-like mesh.

**It will take a few seconds to load at the bottom of the page**
<script type="module">
    import init from './terrain_generation/terrain-generation.js'
    init()
</script>