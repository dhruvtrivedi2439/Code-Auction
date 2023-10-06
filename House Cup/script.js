const canvas = document.createElement("canvas");
const ctx = canvas.getContext("2d");

function grain(size, name, color) {
  canvas.width = size;
  canvas.height = size;

  ctx.fillStyle = color;

  for (let x = 0; x < size; x++) {
    for (let y = 0; y < size; y++) {
      if (Math.random() > 0.5) {
        ctx.fillRect(x, y, 1, 1);
      }
    }
  }

  canvas.toBlob((blob) => {
    const url = URL.createObjectURL(blob);

    document.documentElement.style.setProperty(name, `url(${url})`);
  });
}

grain(256, "--grain-square-black", "hsla(0, 100%, 0%, 1)");
grain(256, "--grain-square-black-opacity", "hsla(0, 100%, 0%, 0.2)");
grain(256, "--grain-square-white", "hsla(0, 100%, 100%, 1)");
grain(256, "--grain-square-white-opacity-blend", "hsla(25, 100%, 96%, 0.1375)");

const items = document.querySelectorAll(".accordion button");

function toggleAccordion() {
  const itemToggle = this.getAttribute('aria-expanded');
  
  for (i = 0; i < items.length; i++) {
    items[i].setAttribute('aria-expanded', 'false');
  }
  
  if (itemToggle == 'false') {
    this.setAttribute('aria-expanded', 'true');
  }
}

items.forEach(item => item.addEventListener('click', toggleAccordion));