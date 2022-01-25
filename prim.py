import graph

'''
fonction prim(G, s)
      pour tout sommet t
            cout[t] := +∞
            pred[t] := null
      cout[s] := 0
      F := file de priorité contenant les sommets de G avec cout[.] comme priorité 
      tant que F ≠ vide
          t := F.defiler
          pour toute arête t--u avec u appartenant à F
              si cout[u] >= poids de l'arête entre les sommets t et u
                      pred[u] := t
                      cout[u] := poids de l'arête entre les sommets t et u
                      F.notifierDiminution(u)
      retourner pred
'''


