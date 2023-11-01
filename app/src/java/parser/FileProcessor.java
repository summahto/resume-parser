package parser;

import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.io.File;
import java.io.FileWriter;
import java.nio.file.CopyOption;
import java.nio.file.Files;
import java.util.concurrent.Callable;

public class FileProcessor implements Callable<Boolean> {

    private Path path;
    private String[] words;

    public FileProcessor(Path path, String[] words) {
        this.path = path;
        this.words = words;
    }

    @Override
    public Boolean call() throws Exception {
        
 
        // Now calling Files.readString() method to
        // read the file
        try {
            String resume = Files.readString(path);
            // Thread.sleep(10); //Thinking 
            for (String word: this.words) {
                if(!resume.contains(word)) {
                    return null;
                }
            }
            
            System.out.println(resume);

            Path dest = Paths.get(this.path.toString().replaceAll("generatedResumes", "validResumes"));
    
            Files.copy(this.path, dest);
                
            
        } catch (Exception e){
            return null;
        }
        return null;

        // throw new UnsupportedOperationException("Unimplemented method 'call'");
    }

}
