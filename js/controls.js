// controls.js
export function addCustomControls(cube, scene) {
    document.addEventListener('keydown', (event) => {
        switch (event.code) {
            case 'ArrowUp':
                cube.position.y += 0.1;
                break;
            case 'ArrowDown':
                cube.position.y -= 0.1;
                break;
            case 'ArrowLeft':
                cube.position.x -= 0.1;
                break;
            case 'ArrowRight':
                cube.position.x += 0.1;
                break;
        }
    });
}

