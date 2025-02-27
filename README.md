## Завдання 2: Пошук визначеного інтеграла методом Монте-Карло

### Реалізація
Метод Монте-Карло передбачає генерування великої кількості випадкових точок у межах прямокутника, що охоплює область під графіком функції. Відсоток точок, які потрапили під криву, множиться на площу цього прямокутника, що дає наближене значення інтеграла.

### Результати
- **Інтеграл методом Монте-Карло:** ≈ 2.66784  
- **Аналітичний інтеграл (за допомогою SciPy quad):** ≈ 2.66667  
- **Абсолютна похибка:** ≈ 0.00118  

### Висновки
Невелика абсолютна похибка показує, що метод Монте-Карло досить точний для цього прикладу. Зі збільшенням кількості випадкових точок (N) наближене значення інтеграла стає ще точнішим. Аналітичне обчислення інтеграла за допомогою функції `quad` з бібліотеки SciPy є більш точним і може бути використано для перевірки результатів методу Монте-Карло. Візуалізація процесу інтегрування допомагає краще зрозуміти, як працює цей метод та як формується кінцевий результат.
