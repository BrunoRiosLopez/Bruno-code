# Computación cuántica en átomos neutros
Esta carpeta recoge gran parte del código que he implementado durante el desarrollo de mi trabajo de fin de grado **Implementación de problemas NP en computadores cuánticos basados en átomos neutros**.

Centrado en la aplicación a finanzas, se implementan algoritmos cuánticos como el `IQAE`, `QAOA`, `QUBO` tanto en **Python** como **Julia** para la optimización de carteras y algunos otros aspectos
como el análisis de riesgos (**VaR, CVar**), demostrando ventaja cuántica replicando resultados de publicaciones recientes.

Se aborda mediante `Bloqade`, la libreria de QuEra para átomos neutros, explorando tanto la computación cuántica analógica, utilizada por su simplicidad para resolver problemas NP como el **MIS**, **MWIS**,
como la computación cuántica digital para abordar problemas tipo mochila.

## Quantum MonteCarlo
Esta carpeta contiene cuadernos que sirven de introducción a la aplicación de métodos de Monte Carlo aplicado a Computación cuántica analógica en átomos neutros. También se implementan algoritmos utilizados
en análisis de riesgos como el **IQAE**.

## Optimización de carteras
Este es el problema más interesante a nivel complejidad. Aplicado a la optimización de carteras en finanzas, se estudia cómo algoritmos cuánticos como QAOA pueden resultar útiles en estas aplicaciones. Se 
implementan soluciones analógicas y digitales, expresando sus cuellos de botella, realizando optimizaciones y analizando resultados.
