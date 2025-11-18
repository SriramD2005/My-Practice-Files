class Circle {
    constructor(pos, radius) {
      this.pos = pos;
      this.radius = radius;
      this.vel = createVector(random(-0.5, 0.5), random(-0.5, 0.5));
      this.acc = createVector(0, 1.5);
      this.color = "white";
    }
    
    draw() {
      push();
      fill(255);
      circle(this.pos.x, this.pos.y, this.radius);
      pop();
    }
    
    update() {
      this.vel.add(this.acc);
      this.pos.add(this.vel);
      this.acc.set(0, 0);
    }
    
    static isCollided({ pos: p1, radius: r1 }, { pos: p2, radius: r2 }) {
      return dist(p1.x, p1.y, p2.x, p2.y) < r1 + r2;
    }
    
    checkCollision(c2) {
      if (Circle.isCollided(this, c2)) {
        console.log('hi')
        this.color = c2.color = "red";
      }
      else {
        // c1.color = c2.color = "white";
      }
    }
  }
  
  const circles = [];
  
  function setup() {
    createCanvas(400, 400);
    
    for (let i = 0; i < 3; i++) {
      circles.push(new Circle(
        createVector(100 + i * 140, random(height * 0.25, height * 0.75)),
        random(100, 150)
      ));
    }
  }
  
  function draw() {
    background(0);
    
    circles.forEach((c, i) => {
      circles.forEach(
        (c2, j) => i == j ? null : c.checkCollision(c2)
      );
      c.update();
      c.draw();
    });
  }