class Main {
    public static void main(String[] args) {
      
      int[] vetor = {
        4434,
        4235,
        3937,
        4439,
        4040,
        3234,
        2834,
        2838,
        3339
      };
  
      for (int i : vetor) {
        System.out.print("\t"+i);   
      }
     
      quickSort(vetor, 0, 8);
      System.out.println();

      for (int i : vetor) {
        System.out.print("\t"+i);   
      }
      
    }
  
  
  
    public static void quickSort(int vetor[], int li, int ls) {
      int j;
      if (li < ls) {
        j = particiona(vetor, li, ls);
        quickSort(vetor, li, j - 1);
        quickSort(vetor, j + 1, ls);
      }
    }
  
    public static int particiona(int vetor[], int li, int ls) {
      int pivo, abaixo, temp, acima;
      pivo = vetor[ls];
      acima = ls;
      abaixo = li;
      while (abaixo < acima) {
        while (vetor[abaixo] < pivo && abaixo < ls) {
          abaixo++;
        }
        while (vetor[acima] >= pivo && acima > abaixo) {
          acima--;
        }
        if (abaixo < acima) {
          temp = vetor[abaixo];
          vetor[abaixo] = vetor[acima];
          vetor[acima] = temp;
        }
      }
      vetor[ls] = vetor[acima];
      vetor[acima] = pivo;
      return acima;
    }
  
  }