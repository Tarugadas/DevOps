#23/03/2026

import json
import os

ARCHIVO = "usuarios.json"

def cargar_usuarios():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            return json.load(f)
    return {}

def guardar_usuarios(usuarios):
    with open(ARCHIVO, "w") as f:
        json.dump(usuarios, f, indent=4)

def guardar_recibo(nombre, accion, monto, saldo_nuevo):
    recibo = {
        "Nombre": nombre,
        "Accion": accion,
        "Monto": monto,
        "Saldo_resultante": saldo_nuevo
    }
    with open("Recibo.txt", "w") as f:
        json.dump(recibo, f, indent=4)
    print("  Recibo guardado en 'Recibo.txt'.")

def crear_usuario(usuarios):
    print("\n=== CREAR USUARIO ===")
    nombre = input("Nombre de usuario: ").strip()

    if nombre in usuarios:
        print("  Ese nombre de usuario ya existe. Intenta con otro.")
        return

    edad = input("Edad: ").strip()
    if not edad.isdigit():
        print("  Edad inválida.")
        return

    contrasena = input("Contraseña: ").strip()
    if not contrasena:
        print("  La contraseña no puede estar vacía.")
        return

    saldo_inicial = input("Saldo inicial (ej. 1000.00): ").strip()
    try:
        saldo_inicial = float(saldo_inicial)
        if saldo_inicial < 0:
            raise ValueError
    except ValueError:
        print("  Saldo inválido.")
        return

    usuarios[nombre] = {
        "Edad": int(edad),
        "Contraseña": contrasena,
        "Saldo": saldo_inicial
    }
    guardar_usuarios(usuarios)
    print(f"  ✔ Usuario '{nombre}' creado exitosamente con saldo ${saldo_inicial:.2f}.")

def iniciar_sesion(usuarios):
    print("\n=== INICIO DE SESIÓN ===")
    nombre = input("Usuario: ").strip()
    contrasena = input("Contraseña: ").strip()

    if nombre not in usuarios:
        print("  Usuario no encontrado.")
        return None

    if usuarios[nombre]["Contraseña"] != contrasena:
        print("  Contraseña incorrecta.")
        return None

    print(f"\n  ¡Bienvenido, {nombre}!")
    return nombre

def consultar_saldo(usuarios, nombre):
    saldo = usuarios[nombre]["Saldo"]
    print(f"\n  Saldo actual: ${saldo:.2f}")

def realizar_retiro(usuarios, nombre):
    print("\n=== RETIRO ===")
    saldo = usuarios[nombre]["Saldo"]
    print(f"  Saldo disponible: ${saldo:.2f}")

    try:
        monto = float(input("  ¿Cuánto deseas retirar? $"))
    except ValueError:
        print("  Monto inválido.")
        return

    if monto <= 0:
        print("  El monto debe ser mayor a cero.")
        return
    if monto > saldo:
        print("  Fondos insuficientes.")
        return

    usuarios[nombre]["Saldo"] -= monto
    guardar_usuarios(usuarios)
    guardar_recibo(nombre, "Retiro", monto, usuarios[nombre]["Saldo"])
    print(f"  ✔ Retiro de ${monto:.2f} exitoso. Saldo restante: ${usuarios[nombre]['Saldo']:.2f}")

def realizar_deposito(usuarios, nombre):
    print("\n=== DEPÓSITO ===")
    try:
        monto = float(input("  ¿Cuánto deseas depositar? $"))
    except ValueError:
        print("  Monto inválido.")
        return

    if monto <= 0:
        print("  El monto debe ser mayor a cero.")
        return

    usuarios[nombre]["Saldo"] += monto
    guardar_usuarios(usuarios)
    guardar_recibo(nombre, "Depósito", monto, usuarios[nombre]["Saldo"])
    print(f"  ✔ Depósito de ${monto:.2f} exitoso. Saldo actual: ${usuarios[nombre]['Saldo']:.2f}")

def menu_sesion(usuarios, nombre):
    while True:
        print("\n─────────────────────────────")
        print("  ¿Qué deseas hacer?")
        print("  1. Consultar saldo")
        print("  2. Retiro")
        print("  3. Depósito")
        print("  4. Cerrar sesión")
        print("─────────────────────────────")
        opcion = input("  Opción: ").strip()

        if opcion == "1":
            consultar_saldo(usuarios, nombre)
        elif opcion == "2":
            realizar_retiro(usuarios, nombre)
        elif opcion == "3":
            realizar_deposito(usuarios, nombre)
        elif opcion == "4":
            print(f"  Sesión cerrada. ¡Hasta pronto, {nombre}!")
            break
        else:
            print("  Opción inválida. Intenta de nuevo.")

def main():
    usuarios = cargar_usuarios()

    while True:
        print("\n╔══════════════════════════════╗")
        print("║    CAJERO AUTOMÁTICO         ║")
        print("╚══════════════════════════════╝")
        print("  1. Iniciar sesión")
        print("  2. Crear usuario")
        print("  3. Salir")
        print("──────────────────────────────")
        opcion = input("  Opción: ").strip()

        if opcion == "1":
            nombre = iniciar_sesion(usuarios)
            if nombre:
                menu_sesion(usuarios, nombre)
        elif opcion == "2":
            crear_usuario(usuarios)
            usuarios = cargar_usuarios()  
        elif opcion == "3":
            print("\n  Hasta pronto.\n")
            break
        else:
            print("  Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()