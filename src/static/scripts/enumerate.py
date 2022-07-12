import permpy as pp


def get_basis():
    content = Element("basis").value
    basis = [pp.Perm(p.strip()) for p in content.split(",")]
    return basis


def enumerate(A):
    return [len(S) for S in A]


def get_and_enumerate(event):
    basis = get_basis()
    A = pp.Av(basis)
    enumeration = enumerate(A)
    output = f"{A} => {enumeration}"
    pyscript.write("output", output, append=True)
