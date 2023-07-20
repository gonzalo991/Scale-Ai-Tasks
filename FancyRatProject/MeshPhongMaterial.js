import * as THREE from 'three';

// Create a geometry
let geometry = new THREE.BoxGeometry(1, 1, 1); // dimensions of the cube

// Create a material
let material = new THREE.MeshPhongMaterial({ color: 0x00ff00 }); // green

// Create a mesh
let cube = new THREE.Mesh(geometry, material);

// Now you can add the cube to your scene
scene.add(cube);