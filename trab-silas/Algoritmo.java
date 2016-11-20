import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Random;
import java.util.Stack;

//import com.sun.xml.internal.ws.policy.privateutil.PolicyUtils.Collections;

public class Algoritmo {

	public static int ColoracaoEmLargura(Vertice[][] matriz, ArrayList<Cor> cores, int n) {

		ArrayList<Vertice> lv = Tabuleiro.matriz_to_list(matriz, n);
		int falhas = 0;

		Vertice atual;
		Vertice inicio = lv.get(0);

		Queue<Vertice> fila = new LinkedList<Vertice>();
		fila.add(inicio);

		while (!fila.isEmpty()) {

			/*for (Vertice v : fila) {
				System.out.print(v.label + "/");
			}
			System.out.println("");
			*/

			atual = fila.remove();

			if (atual.cor == 0) {
				int result = colorir_vertice(atual, cores, n, matriz);
				if (result == 1) {
					falhas = falhas + 1;
				}
			}

			for (Vertice v : atual.vizinhos) {
				if (v.cor == 0 && !fila.contains(v)) {
					fila.add(v);
				}
			}
		}

		return falhas;
	}
	
	/*
	public static int ColoracaoAleatoria(Vertice[][] matriz, ArrayList<Cor> cores, int n) {

		ArrayList<Vertice> lv = Tabuleiro.matriz_to_list(matriz, n);
		int falhas = 0;
		
		shuffle(lv);
		System.out.print("Ordem: ");
		for(Vertice v:lv){
			System.out.print(v.label + " ");
		}
		System.out.println("");

		Vertice atual;
		
		for(Vertice v:lv){
		atual = v;
			if (atual.cor == 0) {
				int result = colorir_vertice(atual, cores, n, matriz);
				if (result == 1) {
					falhas = falhas + 1;
				}
			}
		}

		return falhas;
	}
	*/

	static int colorir_vertice(Vertice v, ArrayList<Cor> cores, int n, Vertice[][] matriz) {
		int i, j;

		Vertice v_linha;
		Vertice v_coluna;
		Vertice v_bloco;
		boolean flag = true;

		for (Cor c : cores) {
			// System.out.println("Tentando cor "+c.n+ " em " +v.label);
			v_linha = Tabuleiro.verifica_linha(v.linha, c.n, n, matriz);
			v_coluna = Tabuleiro.verifica_coluna(v.coluna, c.n, n, matriz);
			v_bloco = Tabuleiro.verifica_bloco(v.linha, v.coluna, c.n, n, matriz);
			if (v_linha == null && v_coluna == null && v_bloco == null) {
				v.cor = c.n;
				//System.out.println("Coloriu " + v.label + " com a cor " + c.n);
				c.instancias++;
				break;
			}
		}

		if (v.cor == 0) {
			//System.out.println("TENTANDO RECOLORAÇÃO");
			for (Cor c : cores) {

				flag = true;
				while (flag) {
					//System.out.println("Tentando cor " + c.n + " em " + v.label);
					v_linha = Tabuleiro.verifica_linha(v.linha, c.n, n, matriz);
					v_coluna = Tabuleiro.verifica_coluna(v.coluna, c.n, n, matriz);
					v_bloco = Tabuleiro.verifica_bloco(v.linha, v.coluna, c.n, n, matriz);

					if (v_linha == null && v_coluna == null && v_bloco == null) {
						v.cor = c.n;
						//System.out.println("Coloriu " + v.label + " com a cor " + c.n);
						c.instancias++;
						flag = false;
					} else {
						if (v_linha != null) {
							//System.out.println("Conflito na linha," + v_linha.label + " com a cor " + c.n);
							if (!mudar_cor(v_linha, cores, n, matriz)) {
								flag = false;
							}
						} else if (v_coluna != null) {
							//System.out.println("Conflito na coluna," + v_coluna.label + " com a cor " + c.n);
							if (!mudar_cor(v_coluna, cores, n, matriz)) {
								flag = false;
							}
						} else if (v_bloco != null) {
							//System.out.println("Conflito no bloco," + v_bloco.label + " com a cor " + c.n);
							if (!mudar_cor(v_bloco, cores, n, matriz)) {
								flag = false;
							}
						}
					}
					//if (flag) System.out.println("Repete");
				}
				if (v.cor != 0)
					break;
			}
		}
		if (v.cor == 0) {
			//System.out.println("Fault");

			int menor_instancia = cores.get(0).instancias;
			for (Cor c : cores) {
				if (c.instancias < menor_instancia) {
					menor_instancia = c.instancias;
					// System.out.println("Melhor cor:"+c.n+" com
					// "+menor_instancia+" instancias");
				}
			}

			ArrayList<Cor> melhores_candidatas = new ArrayList<>();
			for (Cor c : cores) {
				if (c.instancias == menor_instancia) {
					melhores_candidatas.add(c);
				}
			}

			// System.out.print("E as melhores candidatas sï¿½o: ");
			// for(Cor c:melhores_candidatas){
			// System.out.print(c.n+",");
			// }
			// System.out.println("tendo "+menor_instancia+" instancias cada");

			Random random = new Random();
			int count = melhores_candidatas.size();
			int random_indice = random.nextInt(count);

			v.cor = melhores_candidatas.get(random_indice).n;
			//System.out.println("Coloriu "+v.label+" com a cor "+v.cor);
			melhores_candidatas.get(random_indice).instancias++;
			return 1;
		}
		return 0;
	}

	static boolean mudar_cor(Vertice v, ArrayList<Cor> cores, int n, Vertice[][] matriz) {
		int i, j;

		Vertice v_linha;
		Vertice v_coluna;
		Vertice v_bloco;

		for (Cor c : cores) {
			if (c.n != v.cor) {

				v_linha = Tabuleiro.verifica_linha(v.linha, c.n, n, matriz);
				v_coluna = Tabuleiro.verifica_coluna(v.coluna, c.n, n, matriz);
				v_bloco = Tabuleiro.verifica_bloco(v.linha, v.coluna, c.n, n, matriz);

				if (v_linha == null && v_coluna == null && v_bloco == null) {
					for (Cor cor_anterior : cores) {
						if (cor_anterior.n == v.cor) {
							cor_anterior.instancias--;
							//System.out.print("Mudou " + v.label + " de " + cor_anterior.n);
						}
					}
					v.cor = c.n;
					//System.out.print(" para " + c.n + "\n");
					c.instancias++;
					return true;
				}
			}
		}
		return false;
	}

	public static void shuffle(ArrayList<Vertice> array) {
		Random random = new Random();
		int count = array.size();
		for (int i = count; i > 1; i--) {
			swap(array, i - 1, random.nextInt(i));
		}
	}

	private static void swap(ArrayList<Vertice> array, int i, int j) {
		Vertice temp = array.get(i);
		array.set(i, array.get(j));
		array.set(j, temp);
	}
}
