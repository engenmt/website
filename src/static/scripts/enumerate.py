import permpy as pp


def get_basis() -> list[pp.Permutation]:
    content: str = Element("basis").value
    basis: list[pp.Permutation] = [pp.Perm(p.strip()) for p in content.split(",")]
    return basis


def enumerate(A: pp.PermClass) -> list[int]:
    return [len(S) for S in A]


def get_and_enumerate(event) -> None:
    basis: str = get_basis()
    A: pp.AvClass = pp.Av(basis)
    enumeration: list[int] = enumerate(A)
    output: str = f"{A} => {enumeration}"
    pyscript.write("output", output, append=True)
