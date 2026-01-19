from flask import Flask, render_template

app = Flask(__name__)

treinos = {
"A - Quadríceps e Panturrilha": [
    ("Agachamento", "https://youtu.be/zgk71dUUt0Y?si=6_0c-7_l-WInDt9D"),
    ("Leg press", "https://youtu.be/nY8UsiAqwds?si=DOCs6AM6Dtg_xjHR"),
    ("Cadeira adutora", "https://youtu.be/Wf602gn_9zU?si=SZsyuxwSpKwsZ0V2"),
    ("Cadeira extensora", "https://youtu.be/el3oHblB5DM?si=r4ZinQKKhVo843Rr"),
    ("Panturrilha na máquina", "https://youtu.be/jMWs_p-W9gY?si=3j5xnseBkPZlVAFC")
],
"B - Peito e Tríceps": [
    ("Supino declinado", "https://youtu.be/J2g6qPBJfqo?si=7sOvT2EMBHjTNUd-"),
    ("Supino máquina reto", "https://youtube.com/shorts/jBLJVkobbnw?si=0sdHYh7nBejbwHt2"),
    ("Crucifixo", "https://youtu.be/FzCnfD0gOXo?si=_--kgngF38aNpi-T"),
    ("Tríceps testa", "https://youtu.be/zznCYBVZOVA?si=iaYzbZrTKdbo-xjg"),
    ("Tríceps corda", "https://youtu.be/dTqDKC0D6P4?si=DD0xaxskJwzl5j8m")
],

"C - Costas e Bíceps": [
    ("Pulley frente", "https://youtube.com/shorts/ftcql3-AMRs?si=Mrsf3dADwdz9R6X_"),
    ("Remada baixa triângulo", "https://youtu.be/HpWWreyaBN0?si=IpF6afDzffhds_js"),
    ("Remada curvada com barra", "https://youtu.be/TfxJMertfsw?si=OtzZZgCvXHJQJiiW"),
    ("Rosca bíceps", "https://youtu.be/Q8TqfD8E7BU?si=xfxZ_yKXx4QoQFAm"),
    ("Rosca martelo", "https://youtu.be/0qkQy8V2FC0?si=5KxvjixWPGq-Y5Uj")
],

"D - Posterior, Glúteo e Panturrilha": [
    ("Cadeira abdutora", "https://youtu.be/e2gmqTG1OgQ?si=Q6pprEgvL2AGKxq7"),
    ("Agachamento búlgaro", "https://youtu.be/IGf9fR4Y7Iw?si=bZq9dcWXXJIXBD0S"),
    ("Cadeira flexora", "https://youtu.be/Zss6E3VU6X0?si=oDhINCD9J85k5K4x"),
    ("Mesa flexora", "https://youtu.be/2-ULaRrQa7c?si=-QI7ImoZEO5oCbP-"),
    ("Panturrilha no leg 45°", "https://youtu.be/wCXvfH_-BLg?si=PgtadAWzX_rBmrCZ")
],

"E - Ombro, Bíceps e Tríceps": [
    ("Elevação lateral com halter", "https://youtu.be/IwWvZ0rlNXs?si=y-iGvJZn9Qf39bou"),
    ("Desenvolvimento máquina", "https://youtu.be/EuQAfhXBEvs?si=ARbQiDcu8pXZ45Bx"),
    ("Bíceps Scott Maq", "https://youtu.be/zpTK6eihdSA?si=KnYKXLX_KGDiNvcf"),
    ("Bíceps na polia com barra", "https://youtu.be/Q8TqfD8E7BU?si=CcAneKC_5EK9giBq"),
    ("Tríceps corda", "https://youtu.be/dTqDKC0D6P4?si=DD0xaxskJwzl5j8m"),
    ("Tríceps francês", "https://youtu.be/YJ4kGE3eemY?si=jlASB7_9fFo2uxNZ")
],
    }

@app.route("/")
def index():
    return render_template("index.html", treinos=treinos)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

