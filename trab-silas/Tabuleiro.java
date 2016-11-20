import java.util.ArrayList;
import java.util.Random;

public class Tabuleiro {
	public Vertice[][] matriz;
	int n;
	ArrayList<Cor> cores;
	
	public Tabuleiro(int n, ArrayList<Cor> cores) {
		int i, j, k, l;
		
		this.cores = cores;
		
		this.n = n;
		int n2 = n * n;
		
		this.matriz = new Vertice[n2][n2];

		// inicializando
		for (i = 0; i < n2; i++) {
			for (j = 0; j < n2; j++) {
				this.matriz[i][j] = new Vertice("[" + i + "][" + j + "]");
				this.matriz[i][j].linha = i;
				this.matriz[i][j].coluna = j;
			}
		}

		// Adicionando vizinhan�as da mesma linha e coluna
		for (i = 0; i < n2; i++) {
			for (j = 0; j < n2; j++) {
				// adicionando da mesma linha
				for (k = 0; k < n2; k++) {
					if (k != j)
						this.matriz[i][j].addVizinho(this.matriz[i][k]);
				}
				// adicionando da mesma coluna
				for (k = 0; k < n2; k++) {
					if (k != i)
						this.matriz[i][j].addVizinho(this.matriz[k][j]);
				}
			}
		}
		int superior = 0, inferior = 0, direito = 0, esquerdo = 0;
		// Adicionando vizinhan�as da mesma matriz nxn
		for (i = 0; i < n2; i++) {
			for (j = 0; j < n2; j++) {
				l = j + 1;
				// limite direito
				while (l % n != 0) {
					l++;
				}
				direito = l; // 2
				// limite esquerdo
				l = j;
				while (l % n != 0) {
					l--;
				}
				esquerdo = l; // 0
				// limite inferior
				l = i + 1;
				while (l % n != 0) {
					l++;
				}
				inferior = l;
				// limite superior
				l = i;
				while (l % n != 0) {
					l--;
				}
				superior = l;

				for(k=superior;k<inferior;k++){
					for(l=esquerdo;l<direito;l++){
						if(k!=i && l!=j){
							if(!this.matriz[i][j].vizinhos.contains(this.matriz[k][l])){
								this.matriz[i][j].addVizinho(this.matriz[k][l]);
							}
						}
					}
				}
			}
		}
	}
	
	void preenche(int n){
		boolean inserido = false;
		int i,j,k;
		int n2 = n*n;
		int cor;
		Vertice[][] matriz = this.matriz;

		switch(n){
			case 2: 
				matriz[1][0].cor = 4;
				break;
				
			case 3: 
				matriz[0][5].cor = 7;
				matriz[1][6].cor = 5;
				matriz[3][6].cor = 4;
				matriz[4][3].cor = 1;
				matriz[4][7].cor = 5;
				matriz[8][2].cor = 7;
				matriz[8][6].cor = 9;
				matriz[8][7].cor = 1;
				break;
				
			case 4: 
				matriz[0][4].cor = 16;
				matriz[0][9].cor = 4;
				matriz[0][10].cor = 8;
				matriz[0][12].cor = 13;
				matriz[1][5].cor = 15;
				matriz[2][0].cor = 1;
				matriz[2][9].cor = 15;
				matriz[2][14].cor = 12;
				matriz[4][7].cor = 12;
				matriz[5][15].cor = 8;
				matriz[6][15].cor = 12;
				matriz[7][0].cor = 12;
				matriz[7][1].cor = 5;
				matriz[7][6].cor = 7;
				matriz[7][9].cor = 3;
				matriz[7][11].cor = 10;
				matriz[9][13].cor = 1;
				matriz[10][15].cor = 14;
				matriz[11][0].cor = 14;
				matriz[11][4].cor = 4;
				matriz[12][6].cor = 5;
				matriz[13][4].cor = 15;
				matriz[13][13].cor = 8;
				matriz[15][13].cor = 6;
				break;
				
			case 5: 
				
				
				break;
		}
		
		for (i = 0; i < n2; i++) {
			for (j = 0; j < n2; j++) {
				if(matriz[i][j].cor!=0){
					matriz[i][j].fixed = true;
				}
			}
		}
	}
	
	static Vertice verifica_linha(int linha, int cor,int n,Vertice[][] matriz){
		int i;
		for(i=0;i<(n*n);i++){
			if(matriz[linha][i].cor == cor) return matriz[linha][i];
		}
		return null;
	}
	static Vertice verifica_coluna(int coluna, int cor,int n,Vertice[][] matriz){
		int i;
		for(i=0;i<(n*n);i++){
			if(matriz[i][coluna].cor == cor) return matriz[i][coluna];
		}
		return null;
	}
	static Vertice verifica_bloco(int linha,int coluna,int cor,int n,Vertice[][] matriz){
		int i = linha;
		int j = coluna;
		int l,k;		
		int superior = 0, inferior = 0, direito = 0, esquerdo = 0;
				l = j + 1;
				// limite direito
				while (l % n != 0) {
					l++;
				}
				direito = l; // 2
				// limite esquerdo
				l = j;
				while (l % n != 0) {
					l--;
				}
				esquerdo = l; // 0
				// limite inferior
				l = i + 1;
				while (l % n != 0) {
					l++;
				}
				inferior = l;
				// limite superior
				l = i;
				while (l % n != 0) {
					l--;
				}
				superior = l;

				for(k=superior;k<inferior;k++){
					for(l=esquerdo;l<direito;l++){
						if(matriz[k][l].cor == cor) return matriz[k][l];
					}
				}
				return null;
				}
	
	static void imprime_sudoku(Vertice[][] matriz, int n){
		int i, j;
		int n2 = n*n;
			for(i=0;i<n2;i++){
				for(j=0;j<n2;j++){
					System.out.print("|_" + matriz[i][j].cor);
				}
				System.out.println("_|");
				
			}
	}
	
	static ArrayList<Vertice> matriz_to_list(Vertice[][] v,int n){
		int n2 = n*n;
		int i,j;
		ArrayList<Vertice> list = new ArrayList<>();
		
		for (i = 0; i < n2; i++) {
			for (j = 0; j < n2; j++) {
				list.add(v[i][j]);
			}
		}
		
		return list;
	}
	
	}


