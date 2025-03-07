import streamlit as st

def main():
    st.title("Ejemplo de while y for")
    
    # Ejemplo de while
    st.subheader('Ejemplo de while')
    n = st.number_input('Ingresa un número para contar hasta 5:', min_value=0, max_value=5, step=1)
    contador = 0
    resultado_while = ""
    
    while contador <= n:
        resultado_while += f"{contador} "  # Se agregó un espacio
        contador += 1
    st.write('Secuencia generada con while:', resultado_while)
    
    # Ejemplo de for
    st.subheader("Ejemplo con for")
    m = st.number_input("Ingrese un número para generar secuencia:", min_value=1, max_value=10, step=1)
    resultado_for = " ".join(str(i) for i in range(1, m + 1))  # Mejor legibilidad
    st.write("Secuencia generada con for:", resultado_for)

# Corrección en la línea final
if __name__ == "__main__":
    main()
