import java.util.ArrayList;


public class Main {
	
	public static void main(String[] args) {
		int n = Integer.parseInt(args[0]);
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
		
		System.out.println("-------------------- Start --------------------\n");
		Tabuleiro.imprime_sudoku(t.matriz,n);
		
		
		
		falhas = Algoritmo.ColoracaoEmLargura(t.matriz, cores, n);		
		menor_n_falhas = falhas;
		
		for (i = 0; i < n2; i++) {
			for (j = 0; j < n2; j++) {
				melhor_resultado[i][j].cor = t.matriz[i][j].cor;
			}
		}
		
		while(menor_n_falhas!=0 && tentativas<1000){

			for (i = 0; i < n2; i++) {
				for (j = 0; j < n2; j++) {
					if(t.matriz[i][j].fixed==false){
						t.matriz[i][j].cor = 0;
					}
				}
			}
			for(i=0;i<(n*n);i++) cores.get(i).instancias = cores_estadoinicial.get(i).instancias;
			
			falhas = Algoritmo.ColoracaoEmLargura(t.matriz, cores, n);		
			
			if(falhas<menor_n_falhas){
				menor_n_falhas = falhas;
				
				for (i = 0; i < n2; i++) {
					for (j = 0; j < n2; j++) {
						melhor_resultado[i][j].cor = t.matriz[i][j].cor;
					}
				}
			}
			
			tentativas++;
		}
		
		
		System.out.println("\n--------------------- End ---------------------\n");
		
		Tabuleiro.imprime_sudoku(melhor_resultado,n);
		
		System.out.println("\nFalhas: " + menor_n_falhas);

	}
	
	
}
