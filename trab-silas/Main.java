import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
	
	public static void main(String[] args) {
		int n = 4;
		int i,j;
		int n2 = n*n;
		
		int falhas;
		int menor_n_falhas;
		int tentativas = 0;
		
		Vertice[][] melhor_resultado;
		melhor_resultado = new Vertice[n2][n2];
		
		for (i = 0; i < n2; i++) {
			for (j = 0; j < n2; j++) {
				melhor_resultado[i][j] = new Vertice("[" + i + "][" + j + "]");
				melhor_resultado[i][j].linha = i;
				melhor_resultado[i][j].coluna = j;
			}
		}
		
		
		ArrayList<Cor> cores;
		cores = new ArrayList<>();
		for(i=0;i<(n*n);i++) cores.add(new Cor(i+1));
		
		Tabuleiro t = new Tabuleiro(n,cores);
		
		t.preenche(n);
		
		ArrayList<Cor> cores_estadoinicial;
		cores_estadoinicial = new ArrayList<>();
		for(i=0;i<(n*n);i++) cores_estadoinicial.add(new Cor(i+1));
		for(i=0;i<(n*n);i++) cores_estadoinicial.get(i).instancias = cores.get(i).instancias;
		
		Tabuleiro.imprime_sudoku(t.matriz,n);
		
		System.out.println("----Start----");
		
		falhas = Algoritmo.ColoracaoEmLargura(t.matriz, cores, n);		
		menor_n_falhas = falhas;
		
		for (i = 0; i < n2; i++) {
			for (j = 0; j < n2; j++) {
				melhor_resultado[i][j].cor = t.matriz[i][j].cor;
			}
		}
		
		System.out.println("Menor numero de falhas: " + menor_n_falhas);
		Tabuleiro.imprime_sudoku(t.matriz,n);
		System.out.println("Falhas: " + falhas);
		System.out.println("---------");
		
		
		//tentativas<10000
		while(menor_n_falhas!=0 && tentativas<1000){
			//Tabuleiro.imprime_sudoku(t.matriz,n);
			//System.out.println("Falhas: " + falhas);
			//System.out.println("---------");
			//System.out.println(tentativas);
			
			//RESET
			for (i = 0; i < n2; i++) {
				for (j = 0; j < n2; j++) {
					if(t.matriz[i][j].fixed==false){
						t.matriz[i][j].cor = 0;
					}
				}
			}
			for(i=0;i<(n*n);i++) cores.get(i).instancias = cores_estadoinicial.get(i).instancias;
			
			//Tabuleiro.imprime_sudoku(t.matriz,n);
			//System.out.println("---------");
			
			falhas = Algoritmo.ColoracaoEmLargura(t.matriz, cores, n);		
			
			if(falhas<menor_n_falhas){
				menor_n_falhas = falhas;
				System.out.println("Menor numero de falhas: " + menor_n_falhas);
				
				for (i = 0; i < n2; i++) {
					for (j = 0; j < n2; j++) {
						melhor_resultado[i][j].cor = t.matriz[i][j].cor;
					}
				}
			}
			
			tentativas++;
		}
		
		
		System.out.println("----Fim----");
		
		Tabuleiro.imprime_sudoku(melhor_resultado,n);
		
		System.out.println("Falhas: " + menor_n_falhas);
	}

}
