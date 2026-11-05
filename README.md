# joint-calibration-sign-lab

## Français

Reproduire les erreurs de signe dans une calibration de joint.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m joint_calibration_sign_lab examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Ajuste séparément signe+offset avec échelle encodeur fixée ; compare les résidus des deux conventions au lieu de corriger le signe à l’aveugle.

### Limites

Échantillons déjà déroulés et référence indépendante nécessaires ; aucun mouvement matériel ni prise en charge des conventions propres à chaque moteur.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Reproduce sign errors in joint calibration.

Synthetic data; no network access or secret required.

```sh
python -m joint_calibration_sign_lab examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Fits sign+offset separately with fixed encoder scale; compares residuals of both conventions instead of blindly flipping signs.

### Limits

Requires already unwrapped samples and independent reference; no hardware movement or per-motor convention support.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Reproducir errores de signo en calibración de articulaciones.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m joint_calibration_sign_lab examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Ajusta signo+desplazamiento con escala fija de codificador; compara residuos de ambas convenciones sin invertir signo a ciegas.

### Límites

Requiere muestras ya desenrolladas y referencia independiente; sin movimiento físico ni convenciones específicas por motor.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://github.com/huggingface/lerobot/issues/5060
