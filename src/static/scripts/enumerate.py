import permpy as pp


def get_basis():
    content = Element("basis").value
    basis = [pp.Perm(p.strip()) for p in content.split(",")]
    return basis


def enumerate(basis):
    A = pp.Av(basis)
    return [len(S) for S in A]


def get_and_enumerate(event):
    basis = get_basis()
    enumeration = enumerate(basis)
    basis_str = ", ".join(f"{p}" for p in basis)
    output = f"Av({basis_str}) => {enumeration}"
    pyscript.write("output", output, append=True)
