package resume.parser;

import java.nio.file.Path;
import java.nio.file.Paths;
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
    synchronized public Boolean call() throws Exception {

        // Now calling Files.readString() method to
        // read the file
        try {

            String resume = Files.readString(path);
            // Thread.sleep(10); //Thinking
            for (String word : this.words) {
                if (!resume.contains(word)) {
                    return false;
                }
            }

            Path ValidDest = Paths.get(this.path.toString().replaceAll("generatedResumes", "validResumes"));

            Files.copy(this.path, ValidDest);

        } catch (Exception e) {

            Path inValidDest = Paths.get(this.path.toString().replaceAll("generatedResumes", "invalidResumes"));
            Files.copy(this.path, inValidDest);
            // e.printStackTrace();
        }
        return true;

        // throw new UnsupportedOperationException("Unimplemented method 'call'");
    }

}
