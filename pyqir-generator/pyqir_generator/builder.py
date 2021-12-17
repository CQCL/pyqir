# Copyright(c) Microsoft Corporation.
# Licensed under the MIT License.

from typing import Any
from .pyqir_generator import *

class QirBuilder:
    """
    The QirBuilder object describes quantum circuits and emits QIR

    :param module: name of the QIR module
    :type module: str
    """

    def __init__(self, module: str):
        self.pyqir = PyQIR(module)

    def cx(self, control: str, target: str) -> None:
        """
        Applies controlled X operation to the target qubit

        :param control: name of the control qubit
        :param target: name of the target qubit
        """
        self.pyqir.cx(control, target)

    def cz(self, control: str, target: str) -> None:
        """
        Applies controlled Z operation to the target qubit

        :param control: name of the control qubit
        :param target: name of the target qubit
        """
        self.pyqir.cz(control, target)

    def h(self, target: str) -> None:
        """
        Applies H operation to the target qubit

        :param target: name of the target qubit
        """
        self.pyqir.h(target)

    def m(self, qubit: str, target: str) -> None:
        """
        Applies measurement operation or the source qubit into the target register

        :param qubit: name of the source qubit
        :param target: name of the target register
        """
        self.pyqir.m(qubit, target)

    def reset(self, target: str) -> None:
        """
        Applies Reset operation to the target qubit

        :param target: name of the target qubit
        """
        self.pyqir.reset(target)

    def rx(self, theta: float, qubit: str) -> None:
        """
        Applies Rx operation to the target qubit

        :param theta: rotation value for target qubit
        :type theta: float
        :param qubit: name of the target qubit
        """
        self.pyqir.rx(theta, qubit)

    def ry(self, theta: float, qubit: str) -> None:
        """
        Applies Ry operation to the target qubit

        :param theta: rotation value for target qubit
        :type theta: float
        :param qubit: name of the target qubit
        """
        self.pyqir.ry(theta, qubit)

    def rz(self, theta: float, qubit: str) -> None:
        """
        Applies Rz operation to the target qubit

        :param theta: rotation value for target qubit
        :type theta: float
        :param qubit: name of the target qubit
        """
        self.pyqir.rz(theta, qubit)

    def s(self, qubit: str) -> None:
        """
        Applies S operation to the target qubit

        :param qubit: name of the target qubit
        """
        self.pyqir.s(qubit)

    def s_adj(self, qubit: str) -> None:
        """
        Applies SAdj operation to the target qubit

        :param qubit: name of the target qubit
        """
        self.pyqir.s_adj(qubit)

    def t(self, qubit: str) -> None:
        """
        Applies T operation to the target qubit

        :param qubit: name of the target qubit
        """
        self.pyqir.t(qubit)

    def t_adj(self, qubit: str) -> None:
        """
        Applies TAdj operation to the target qubit

        :param qubit: name of the target qubit
        """
        self.pyqir.t_adj(qubit)

    def x(self, qubit: str) -> None:
        """
        Applies X operation to the target qubit

        :param qubit: name of the target qubit
        """
        self.pyqir.x(qubit)

    def y(self, qubit: str) -> None:
        """
        Applies Y operation to the target qubit

        :param qubit: name of the target qubit
        """
        self.pyqir.y(qubit)

    def z(self, qubit: str) -> None:
        """
        Applies Z operation to the target qubit

        :param qubit: name of the target qubit
        """
        self.pyqir.z(qubit)

    def dump_machine(self) -> None:
        """

        """
        self.pyqir.dump_machine()

    def add_classical_register(self, name: str, size: int) -> None:
        """
        Models a classical register of the given size. The individual values
        are accessed by name "<name><index>" with 0 based indicies.
        Example:
            builder = QirBuilder("Bell circuit")
            builder.add_quantum_register("qr", 2)
            builder.add_classical_register("qc", 2)
            builder.h("qr0")
            builder.cx("qr0", "qr1")
            builder.m("qr0", "qc0")
            builder.m("qr1", "qc1")
            builder.build("bell_measure.ll")

        :param name: name of the register
        :type name: str
        :param size: size of the register
        :type size: int
        """
        self.pyqir.add_classical_register(name, size)

    def add_quantum_register(self, name: str, size: int) -> None:
        """
        Models an array of qubits of the given size. The individual values
        are accessed by name "<name><index>" with 0 based indicies.
        Example:
            builder = QirBuilder("Bell circuit")
            builder.add_quantum_register("qr", 2)
            builder.add_classical_register("qc", 2)
            builder.h("qr0")
            builder.cx("qr0", "qr1")
            builder.m("qr0", "qc0")
            builder.m("qr1", "qc1")
            builder.build("bell_measure.ll")

        :param name: name of the register
        :type name: str
        :param size: size of the register
        :type size: int
        """
        self.pyqir.add_quantum_register(name, size)

    def build(self, file_path: str) -> None:
        """
        Writes the modeled circuit to the supplied file.

        :param file_path: file path of generated QIR
        :type file_path: str
        """
        self.pyqir.write(file_path)

    def get_ir_string(self) -> str:
        """
        Returns the modeled circuit as an LLVM IR module (human readable) string.
        """
        return self.pyqir.get_ir_string()

    def get_bitcode_base64_string(self) -> str:
        """
        Returns the modeled circuit as a base64 encoded LLVM bitcode module.
        """
        return self.pyqir.get_bitcode_base64_string()

    @staticmethod
    def enable_logging() -> None:
        """
        Enables the logging infrastructure
        Controlled via the RUST_LOG environment variable.
        See https://docs.rs/env_logger/0.9.0/env_logger/#enabling-logging for details

        Example:
        in tests.py:
            def test_logging():
                builder = QirBuilder("logging test")
                builder.enable_logging()
                builder.add_quantum_register("qr", 1)
                builder.h("qr0")
                builder.build("test.ll")

        PowerShell:
            $env:RUST_LOG="info"
            python -m pytest
        Bash:
            RUST_LOG=info python -m pytest

        Example Output:
        [2021-09-15T16:55:46Z INFO  pyqir::python] Adding qr[0]
        [2021-09-15T16:55:46Z INFO  pyqir::python] h => qr0
        """
        PyQIR.enable_logging()
