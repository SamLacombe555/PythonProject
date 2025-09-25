| Ligne exécutée | Fonction / Action                           | Paramètres / Variables  | Valeur retournée | Affichage                                | Condition exécutée   |
|----------------|---------------------------------------------|-------------------------|------------------|------------------------------------------|----------------------|
| 20             | —                                           | score1 = 70             | —                | —                                        | —                    |
| 21             | —                                           | score2 = 95             | —                | —                                        | —                    |
| 23             | nouveau_score1 = ajouter_points(score1, 20) | score = 70, points = 20 | 90               | —                                        | —                    |
| 24             | nouveau_score2 = ajouter_points(score2, 10) | score = 95, points = 10 | 105              | —                                        | —                    |
| 26             | haut1 = est_haut_score(nouveau_score1)      | score  = 90             | False            | —                                        | score >= 100 → False |
| 27             | haut2 = est_haut_score(nouveau_score2)      | score =  105            | True             | —                                        |                      |
| 29             |                                             | —                       | —                |                                          | —                    |
| 30             |                                             | —                       | —                | Joueur 2 : 105 points, haut score ? True | —                    |
