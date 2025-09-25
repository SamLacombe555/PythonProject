# Plan de tests pour `environnement_optimal`

| Température (°C) | Poussière   | Humidité (%) | Comportement attendu                                          | Résultat attendu                        |
|------------------|-------------|--------------|---------------------------------------------------------------|-----------------------------------------|
| 25               | faible      | 40           | Tout est sous contrôle!                                       | Tout est sous contrôle!                 |
| 30               | faible      |40            | Température trop élevée                                       | Environnement non optimal               |
| 25               | faible      | 20           | Humidité trop basse                                           | Environnement non optimal               |
| 30               | moyen       | 25           | Température trop élevée/humidité trop basse/trop de poussière | Environnement non optimal               |
