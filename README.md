## English description

This is the repo of my solution to the *Probability Calculator* project from the **Scientific Computing with Python** course from freeCodeCamp. Portuguese description down below.

### Assignment

Suppose there is a hat containing 5 blue balls, 4 red balls, and 2 green balls. What is the probability that a random draw of 4 balls will contain at least 1 red ball and 2 green balls? While it would be possible to calculate the probability using advanced mathematics, an easier way is to write a program to perform a large number of experiments to estimate an approximate probability.

For this project, you will write a program to determine the approximate probability of drawing certain balls randomly from a hat. 

First, create a `Hat` class in `prob_calculator.py`. The class should take a variable number of arguments that specify the number of balls of each color that are in the hat. For example, a class object could be created in any of these ways:
```
hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
```

A hat will always be created with at least one ball. The arguments passed into the hat object upon creation should be converted to a `contents` instance variable. `contents` should be a list of strings containing one item for each ball in the hat. Each item in the list should be a color name representing a single ball of that color. For example, if your hat is `{"red": 2, "blue": 1}`, `contents` should be `["red", "red", "blue"]`.

The `Hat` class should have a `draw` method that accepts an argument indicating the number of balls to draw from the hat. This method should remove balls at random from `contents` and return those balls as a list of strings. The balls should not go back into the hat during the draw, similar to an urn experiment without replacement. If the number of balls to draw exceeds the available quantity, return all the balls.

Next, create an `experiment` function in `prob_calculator.py` (not inside the `Hat` class). This function should accept the following arguments:
* `hat`: A hat object containing balls that should be copied inside the function.
* `expected_balls`: An object indicating the exact group of balls to attempt to draw from the hat for the experiment. For example, to determine the probability of drawing 2 blue balls and 1 red ball from the hat, set `expected_balls` to `{"blue":2, "red":1}`.
* `num_balls_drawn`: The number of balls to draw out of the hat in each experiment.
* `num_experiments`: The number of experiments to perform. (The more experiments performed, the more accurate the approximate probability will be.)

The `experiment` function should return a probability. 

For example, let's say that you want to determine the probability of getting at least 2 red balls and 1 green ball when you draw 5 balls from a hat containing 6 black, 4 red, and 3 green. To do this, we perform `N` experiments, count how many times `M` we get at least 2 red balls and 1 green ball, and estimate the probability as `M/N`. Each experiment consists of starting with a hat containing the specified balls, drawing a number of balls, and checking if we got the balls we were attempting to draw.

Here is how you would call the `experiment` function based on the example above with 2000 experiments:

```
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat, 
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
```

Since this is based on random draws, the probability will be slightly different each time the code is run.

*Hint: Consider using the modules that are already imported at the top of `prob_calculator.py`.*

### Development

Write your code in `prob_calculator.py`. For development, you can use `main.py` to test your code. Click the "run" button and `main.py` will run.

### Testing 

The unit tests for this project are in `test_module.py`. We imported the tests from `test_module.py` to `main.py` for your convenience. The tests will run automatically whenever you hit the "run" button.

### Submitting

Copy your project's URL and submit it to freeCodeCamp.

--------------------------------------------------------------------------

## Descrição em português

Esse é o repositório com a minha solução para o projeto *Probability Calculator* do curso **Scientific Computing with Python** do freeCodeCamp. A tradução é livre e feita por mim.

### Tarefa

Suponha que um chapéu contém 5 bolas azuis, 4 vermelhas e 2 verdes. Qual a probabilidade de quê uma retirada aleatória e sem reposição de 4 bolas contenha pelo menos 1 vermelha e 2 verdes? Apesar de ser possível calcular essa probabilidade à mão usando matemática, uma maneira mais fácil é escrevendo um programa para realizar um grande número de experimentos e estimar a probabilidade.

Para esse projeto, você escreverá um programa que determina a probabilidade aproximada de retirar certas bolas randomicamente de um chapéu.

Primeiro, crie uma classe `Hat` em `prob_calculator.py`. A classe deve receber um número variável de argumentos que especificam o número de bolas de cada cor que estão no chapéu. Por exemplo, um objeto da classe pode ser criado de qualquer uma dessas maneiras:

```
hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
```

Um chapéu sempre será criado com pelo menos uma bola. Os argumentos passados no objeto hat na criação devem ser convertidos em uma variável de instância `contents`, que deve ser uma lista de strings contendo um item para cada bola no chapéu. Cada item na lista deve ser um nome de uma cor representando uma única bola daquela cor. Por exemplo, se o seu chapéu é `{"red": 2, "blue": 1}`, `contents` deve ser `["red", "red", "blue"]`.

A classe `Hat` deve ter um método `draw` que recebe um argumento indicando o número de bolas a serem retiradas do chapéu. Esse método deve remover bolas aleatoriamente de `contents` e retorná-las como uma lista de strings. As bolas não devem voltar para o chapéu durante a retirada. Se o número de bolas a retirar for maior que a quantidade disponível, retorne todas as bolas.

Em seguida, crie uma função `experiment` em `prob_calculator.py` (fora da classe `Hat`). Essa função deve receber os seguintes argumentos:
* `hat`: um objeto hat contendo bolas que devem ser copiadas dentro da função.
* `expected_balls`: um objeto indicando o grupo exato de bolas a se tentar retirar do chapéu para o experimento. Por exemplo, para determinar a probabilidade de retirar 2 bolas azuis e 1 vermelha do chapéu, atribua a `expected_balls` o dicionário `{"blue":2, "red":1}`.
* `num_balls_drawn`: o número de bolas a se retirar do chapéu em cada experimento.
* `num_experiments`: o número de experimentos a realizar (quanto mais experimentos, mais acurada a probabilidade aproximada).

A função `experiment` deve retornar uma probabilidade. 

Por exemplo, digamos que queremos determinar a probabilidade de retirar pelo menos 2 bolas vermelhas e 1 verde quando retiramos 5 bolas de um chapéu contendo 6 pretas, 4 vermelhas e 3 verdes. Para tanto, performamos `N` experimentos, contamos quantas vezes `M` conseguimos o resultado desejado e estimamos a probabilidade em `M/N`. Cada experimento consiste em começar com um chapéu contendo as bolas espeficicadas, retirar o número de bolsa e checar se conseguimos o resultado desejado.

Aqui está um exemplo de chamada da função `experiment` baseado no exemplo acima com 2000 experimentos:

```
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat, 
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
```

Como isso é baseado em retiradas aleatórias, a probabilidade será levemente diferente cada vez que o código rodar.

*Dica: considere usar os módulos que já foram importados em `prob_calculator.py`.*

### Desenvolvimento

Escreve seu código em `prob_calculator.py`. Para desenvolvimento, use `main.py` para testar o código. Clique em "run" `main.py` rodará.

### Testando 

Os testes unitários para este projeto estão em `test_module.py`. Importamos os testes de `test_module.py` para `main.py` por conveniência. Os teste vão rodar automaticamente quando clicar em "run".

### Submissão

Copie a URL do projeto e submeta-a ao freeCodeCamp.
