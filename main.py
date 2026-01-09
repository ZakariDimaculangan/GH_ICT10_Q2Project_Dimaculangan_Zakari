from js import document

# ---------- GWA CALCULATOR ----------
def calc_gwa(event):
    math = float(document.getElementById("math").value)
    eng = float(document.getElementById("english").value)
    sci = float(document.getElementById("science").value)

    gwa = (math + eng + sci) / 3

    fname = document.getElementById("first_name").value
    lname = document.getElementById("last_name").value

    document.getElementById("output").innerHTML = (
        f"Name: {fname} {lname}<br>GWA: {gwa:.2f}"
    )


# ---------- CLUB INFORMATION ----------
def show_club(event):
    club = document.getElementById("club").value
    document.getElementById("output").innerHTML = (
        f"Selected Club: {club}"
    )


# ---------- BUTTON CONNECTIONS ----------
def setup():
    if document.getElementById("btn"):
        document.getElementById("btn").addEventListener("click", calc_gwa)

    if document.getElementById("show"):
        document.getElementById("show").addEventListener("click", show_club)


setup()
