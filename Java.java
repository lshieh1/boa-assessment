import java.io.*;

public class Java {
	public static void main(String args[]) {
		try {
			File file = new File("article.txt");
			File file2 = new File("article1.txt");
			BufferedReader in = new BufferedReader(new FileReader("article.txt"));
			BufferedWriter writer = new BufferedWriter(new FileWriter("article1.txt",true));
			String str;
			while((str=in.readLine()) != null) {
				String[] array = str.split(" ");
				writer.append(str + " " + array.length + "\n");
			}
			writer.close();
			if(file2.exists()) {
				file2.renameTo(file);
			}
		} catch(IOException e) {
			System.out.println("File does not exist");
		}
	}
}
