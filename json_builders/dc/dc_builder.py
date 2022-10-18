import pandas as pd
from json import dump
from utils.commutativity import commutativity

def dc_builder():
  df = pd.read_csv('json_builders/dc/dc.csv')

  dict = {
    "code": get_code(df["code"]),
    "title": "Factorización por diferencia de cuadrados.",
    "contentType": "DC",
    "level": "1",
    "text": "Factorice la siguiente expresión:",
    "selectSteps": "true",
    "steps": [
      {
        "stepId": "0",
        "expression": expression_step_0(df["value_1"]),
        "stepTitle": "Identificar terminos al cuadrado",
        "displayResult": display_result_step_0(df["value_2"]),
        "KCs": kcs_step_0(df["kcs_step_0"]),
        "hints": [
          {
            "hintId": 0,
            "hint": "Calcular raices cuadradas de cada sumando"
          },
          {
            "hintId": 1,
            "hint": "x₁ es la raíz cuadrada del primer sumando"
          },
          {
            "hintId": 2,
            "hint": hint_id_2_step_0(df["value_2"])
          }
        ],
        "matchingError": [
          {
            "error": ["", ""],
            "hintId": 3,
            "hint": "No ha ingresado respuesta"
          },
          {
            "error": ["", "*"],
            "hintId": 4,
            "hint": "No ha ingresado la primera raíz cuadrada"
          },
          {
            "error": ["*", ""],
            "hintId": 5,
            "hint": "No ha ingresado la segunda raíz cuadrada"
          }
        ],
        "answers": [
          answers_step_0(df["value_2"])
        ],
        "incorrectMsg": "no se han ingresado correctamente los términos que al cuadrado dan como resultado la expresión",
        "correctMsg": "Haz encontrado los términos al cuadrado",
        "summary": "1) Para aplicar factorización por diferencia de cuadrados, se deben identificar los términos que están al cuadrado de la forma (x₁)² - (x₂)², donde:"
      },
      {
        "stepId": "1",
        "expression": expression_step_1(df["value_1"]),
        "stepTitle": "Ingresar suma por diferencia",
        "displayResult": display_result_step_1(df["value_1"]),
        "KCs": [4],
        "hints": [
          { "hintId": 0, "hint": "Primer paréntesis ingresar suma" },
          { "hintId": 1, "hint": hint_id_1_step_1(df["value_1"]) },
          { "hintId": 2, "hint": hint_id_1_step_2(df["value_3"]) }
        ],
        "matchingError": [
          {
            "error": ["", ""],
            "hintId": 3,
            "hint": "No ha ingresado respuesta"
          },
          {
            "error": ["", "*"],
            "hintId": 4,
            "hint": "No ha ingresado x₁ + x₂"
          },
          { "error": ["*", ""], "hintId": 5, "hint": "No ha ingresado x₁ - x₂" }
        ],
        "answers": [{ "answer": answers_step_1(df["value_3"]), "nextStep": "null" }],
        "incorrectMsg": "suma por diferencia mal ingresado",
        "correctMsg": "Haz encontrado la diferencia de cuadradros",
        "summary": "2) Ya identificado x₁ y x₂ se puede aplicar la fórmula que permite factorizar la expresión en suma por su diferencia  (x₁+x₂)(x₁-x₂)"
      },
      {
        "stepId": "2",
        "expression": expression_step_2(df["value_2"]),
        "stepTitle": "Ingresar suma por diferencia",
        "displayResult": display_result_step_2(df["value_2"]),
        "KCs": [4],
        "hints": [
          { "hintId": 0, "hint": "Primer paréntesis ingresar suma" },
          { "hintId": 1, "hint": "Segundo paréntesis ingresar resta" },
          { "hintId": 2, "hint": hint_id_2_step_2(df["value_3"]) }
        ],
        "matchingError": [
          {
            "error": ["", ""],
            "hintId": 3,
            "hint": "No ha ingresado respuesta"
          },
          {
            "error": ["", "*"],
            "hintId": 4,
            "hint": "No ha ingresado x₁ + x₂"
          },
          { "error": ["*", ""], "hintId": 5, "hint": "No ha ingresado x₁ - x₂" }
        ],
        "answers": [{ "answer": answers_step_2(df["value_3"]), "nextStep": "null" }],
        "incorrectMsg": "suma por diferencia mal ingresado",
        "correctMsg": "Haz encontrado la diferencia de cuadradros",
        "summary": "2) Ya identificado x₁ y x₂ se puede aplicar la fórmula que permite factorizar la expresión en suma por su diferencia  (x₁+x₂)(x₁-x₂)"
      },
      {
        "stepId": "3",
        "expression": expression_step_3(df["value_2"]),
        "stepTitle": "Ingresar suma por diferencia",
        "displayResult": display_result_step_3(df["value_2"]),
        "KCs": [4],
        "hints": [
          { "hintId": 0, "hint": "Primer paréntesis ingresar suma" },
          { "hintId": 1, "hint": hint_id_1_step_3(df["value_2"]) },
          { "hintId": 2, "hint": hint_id_2_step_3(df["value_3"]) }
        ],
        "matchingError": [
          {
            "error": ["", ""],
            "hintId": 3,
            "hint": "No ha ingresado respuesta"
          },
          {
            "error": ["", "*"],
            "hintId": 4,
            "hint": "No ha ingresado x₁ + x₂"
          },
          { "error": ["*", ""], "hintId": 5, "hint": "No ha ingresado x₁ - x₂" }
        ],
        "answers": [{ "answer": answers_step_3(df["value_3"]), "nextStep": "null" }],
        "incorrectMsg": "suma por diferencia mal ingresado",
        "correctMsg": "Haz encontrado la diferencia de cuadradros",
        "summary": "2) Ya identificado x₁ y x₂ se puede aplicar la fórmula que permite factorizar la expresión en suma por su diferencia  (x₁+x₂)(x₁-x₂)"
      },
      {
        "stepId": "4",
        "expression": expression_step_4(df["value_2"]),
        "stepTitle": "Ingresar suma por diferencia",
        "displayResult": display_result_step_4(df["value_2"]),
        "KCs": [4],
        "hints": [
          { "hintId": 0, "hint": "Primer paréntesis ingresar suma" },
          { "hintId": 1, "hint": "Segundo paréntesis ingresar resta" },
          { "hintId": 2, "hint": hint_id_2_step_4(df["value_3"])}
        ],
        "matchingError": [
          {
            "error": ["", ""],
            "hintId": 3,
            "hint": "No ha ingresado respuesta"
          },
          {
            "error": ["", "*"],
            "hintId": 4,
            "hint": "No ha ingresado x₁ + x₂"
          },
          { "error": ["*", ""], "hintId": 5, "hint": "No ha ingresado x₁ - x₂" }
        ],
        "answers": [{ "answer": answers_step_4(df["value_3"]), "nextStep": "null" }],
        "incorrectMsg": "suma por diferencia mal ingresado",
        "correctMsg": "Haz encontrado la diferencia de cuadradros",
        "summary": "2) Ya identificado x₁ y x₂ se puede aplicar la fórmula que permite factorizar la expresión en suma por su diferencia  (x₁+x₂)(x₁-x₂)"
      }
    ]
  }
  
  out_file = open("exercises/dc/" + get_code(df["code"]) + ".json", "w", encoding='utf8')
  dump(dict, out_file, indent=2, ensure_ascii=False)
  out_file.close()


def get_code(code):
  return code.to_string(index=False)

# Step 0
def expression_step_0(expression):
  return expression.to_string(index=False)

def display_result_step_0(expression):
  return expression.to_string(index=False)
  
def kcs_step_0(kcs):
  return [kcs.to_string(index=False)]

def hint_id_2_step_0(expression):
  return ""

def answers_step_0(expression):
  return ""

# Step 1
def expression_step_1(expressin):
  return ""

def display_result_step_1(expression):
  return ""

def hint_id_1_step_1(expression):
  return ""


def hint_id_2_step_1(expression):
  return ""

def answers_step_1(expression):
  return ""

# Step 2
def expression_step_2(expression):
  return ""

def display_result_step_2(expression):
  return ""

def hint_id_1_step_2(expression):
  return ""

def hint_id_2_step_2(expression):
  return ""

def answers_step_2(expression):
  return ""

# Step 3
def expression_step_3(expression):
  return ""

def display_result_step_3(expression):
  return ""

def hint_id_1_step_3(expression):
  return ""

def hint_id_2_step_3(expression):
  return ""

def answers_step_3(expression):
  return ""

# Step 4
def expression_step_4(expression):
  return ""

def display_result_step_4(expression):
  return ""

def hint_id_2_step_4(expression):
  return ""

def answers_step_4(expression):
  return ""
