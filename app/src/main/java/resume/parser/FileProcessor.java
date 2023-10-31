package resume.parser;

import java.nio.file.Path;
import java.util.concurrent.Callable;

public class FileProcessor implements Callable<Boolean> {

    private Path path;

    public FileProcessor(Path path) {
        this.path = path;
    }

    @Override
    public Boolean call() throws Exception {

        throw new UnsupportedOperationException("Unimplemented method 'call'");
    }

}
