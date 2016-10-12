// underscore

//var canvas
//var code
var myCodeMirror
var msg
var sel1, sel2, sel3
var chapter, exercise, call = ''

// a : facit
// b : student
// c : call
data = {
  Colors: {
    Background1: {
      a: "bg(0)",
      b: "bg(0,1,0)"
    },
    Background2: {
      a: "bg(1)",
      b: "bg(0,1,1)"
    },
    Background3: {
      a: "bg(1,0,0)",
      b: "bg(1,0,1)"
    },
    Background4: {
      a: "bg(1,1,0)",
      b: "bg(0.5)"
    },
  },
  Points: {
    Point1: {
      a: "point(100,100)",
      b: ""
    },
    Point2: {
      a: "point(50,50)",
      b: ""
    },
  },
  Functions: {
    ColorCube: {
      a: "function colorCube(m,n) {rect(m,n,10,10)}",
      b: "",
      c: {
        "colorCube(20,30)": 0,
        "colorCube(130,140)": 1
      }
    },
    Korg: {
      a: "function korg(m,n) {ellipse(100,100,m,n)}",
      b: "function korg(m,n) {\n  ellipse(100,100,m,n)\n}",
      c: {
        "korg(50,30)": 0,
        "korg(30,50)": 1
      }
    },
  },
}

function grid() {
  push()
  sc(1)
  for (var i in range(10)) {
    line(0, 20 * i, 200, 20 * i)
    line(20 * i, 0, 20 * i, 200)
  }
  pop()
}

function fixColor(args) {
  var n = args.length
  var r, g, b
  if (n == 1) {
    r = args[0]
    g = r
    b = r
  } else if (n == 3) {
    r = args[0]
    g = args[1]
    b = args[2]
  }
  return color(255 * r, 255 * g, 255 * b)
}

function bg() {
  fill(fixColor(arguments))
  rect(0, 0, 200, 200)
}

function fc() {
  var n = arguments.length
  if (n == 0) {
    noFill()
  } else {
    fill(fixColor(arguments))
  }
}

function sc(r, g, b) {
  var n = arguments.length
  if (n == 0) {
    noStroke()
  } else {
    stroke(fixColor(arguments))
  }
}

function range(n) {
  var a = [],
    b = 0
  while (b < n) {
    a.push(b)
    b += 1
  }
  return a
}

function fillSelect(sel, dict) {
  sel.empty()
  for (key in dict) {
    sel.append($("<option>").attr('value', key).text(key))
  }
}

function sel1change(sel) {
  chapter = sel.value
  exercise = ""
  call = ""
  fillSelect(sel2, data[chapter])
  sel3.empty()
}

function sel2change(sel) {
  exercise = sel.value
  call = ""
  fillSelect(sel3, data[chapter][exercise]["c"])
  code1 = data[chapter][exercise]["a"]
  run(1, code1)

  b = data[chapter][exercise]["b"]
  myCodeMirror.setValue(b)
}

function sel3change(sel) {
  call = sel.value

  a = data[chapter][exercise]["a"]
  run(1, a + call)

  b = data[chapter][exercise]["b"]
  run(0, b + call)
}

function setup() {
  button2 = createButton('Init')
  button2.position(507, 618)
  button2.mousePressed(init)

  msg = createInput('')
  msg.position(0, 618)
  msg.size(500)

  c = createCanvas(210, 611)
  c.parent('canvas')

  sel1 = $('#sel1')
  sel2 = $('#sel2')
  sel3 = $('#sel3')

  fillSelect(sel1, data)
}

function init() {
  var ta = document.getElementById("code")
  console.log(ta)

  myCodeMirror = CodeMirror.fromTextArea(ta, {
    lineNumbers: true,
    mode: "javascript",
    keyMap: "sublime",
    theme: "dracula",
    autoCloseBrackets: true,
    lineWiseCopyCut: true
  });
  myCodeMirror.on("change", run0)
  myCodeMirror.setSize(500, 611)
  run(0, "")
  run(1, "")
}

function run0() {
  b = myCodeMirror.getValue()
  data[chapter][exercise]["b"] = b
  run(0, b + call)
}

function reset() {
  bg(0.5, 0.5, 0.5)
  fc(0, 0, 0)
  grid()
}

function run(n, code) {
  resetMatrix()
  push()
  translate(0, n * 205)
  reset()

  try {
    msg.value('')
    console.log(code)
    eval(code)
    pop()
  } catch (err) {
    pop()
    msg.value(err)
    console.log(err.stack)
    var caller_line = err.stack.split("\n")[1];
    var index = caller_line.indexOf("at ");
    var clean = caller_line.slice(index + 2, caller_line.length);
  }
}