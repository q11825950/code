package util;

import org.apache.commons.compress.archivers.tar.TarArchiveEntry;
import org.apache.commons.compress.archivers.tar.TarArchiveInputStream;
import org.apache.commons.compress.compressors.bzip2.BZip2CompressorInputStream;
import org.apache.commons.compress.compressors.gzip.GzipCompressorInputStream;
import org.apache.commons.io.FileUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.Enumeration;
import java.util.zip.ZipEntry;
import java.util.zip.ZipFile;


/**
 * @author 李文浩
 * @date 2018/7/24
 */

public class ZipUtil {

    private static final Logger LOG = LoggerFactory.getLogger(ZipUtil.class);

    private static final int BUFFER_SIZE = 1024 * 100;

    private ZipUtil() {
    }

    public static boolean decompress(String filePath, String outputDir, boolean isDeleted) {
        File file = new File(filePath);
        if (!file.exists()) {
            LOG.error("decompress file not exist.");
            return false;
        }
        try {
            if (filePath.endsWith(".zip")) {
                unZip(file, outputDir);
            }
            if (filePath.endsWith(".tar.gz") || filePath.endsWith(".tgz")) {
                decompressTarGz(file, outputDir);
            }
            if (filePath.endsWith(".tar.bz2")) {
                decompressTarBz2(file, outputDir);
            }
            filterFile(new File(outputDir));
            if (isDeleted) {
                FileUtils.deleteQuietly(file);
            }
            return true;
        } catch (IOException e) {
            LOG.error("decompress occur error.");
        }
        return false;
    }

    /**
     * 解压 .zip 文件
     *
     * @param file      要解压的zip文件对象
     * @param outputDir 要解压到某个指定的目录下
     * @throws IOException
     */
    public static void unZip(File file, String outputDir) throws IOException {
        try (ZipFile zipFile = new ZipFile(file, StandardCharsets.UTF_8)) {
            //创建输出目录
            createDirectory(outputDir, null);
            Enumeration<?> enums = zipFile.entries();
            while (enums.hasMoreElements()) {
                ZipEntry entry = (ZipEntry) enums.nextElement();
                if (entry.isDirectory()) {
                    //创建空目录
                    createDirectory(outputDir, entry.getName());
                } else {
                    try (InputStream in = zipFile.getInputStream(entry)) {
                        try (OutputStream out = new FileOutputStream(
                                new File(outputDir + File.separator + entry.getName()))){
                            writeFile(in, out);
                        }
                    }
                }
            }
        }
    }

    public static void decompressTarGz(File file, String outputDir) throws IOException {
        try (TarArchiveInputStream tarIn = new TarArchiveInputStream(
                new GzipCompressorInputStream(
                        new BufferedInputStream(
                                new FileInputStream(file))))) {
            //创建输出目录
            createDirectory(outputDir, null);
            TarArchiveEntry entry = null;
            while ((entry = tarIn.getNextTarEntry()) != null) {
                //是目录
                if (entry.isDirectory()) {
                    //创建空目录
                    createDirectory(outputDir, entry.getName());
                } else {
                    //是文件
                    try (OutputStream out = new FileOutputStream(
                            new File(outputDir + File.separator + entry.getName()))) {
                        writeFile(tarIn, out);
                    }
                }
            }
        }

    }

    /**
     * 解压缩tar.bz2文件
     *
     * @param file      压缩包文件
     * @param outputDir 目标文件夹
     */
    public static void decompressTarBz2(File file, String outputDir) throws IOException {
        try (TarArchiveInputStream tarIn =
                     new TarArchiveInputStream(
                             new BZip2CompressorInputStream(
                                     new FileInputStream(file)))) {
            createDirectory(outputDir, null);
            TarArchiveEntry entry;
            while ((entry = tarIn.getNextTarEntry()) != null) {
                if (entry.isDirectory()) {
                    createDirectory(outputDir, entry.getName());
                } else {
                    try (OutputStream out = new FileOutputStream(
                            new File(outputDir + File.separator + entry.getName()))) {
                        writeFile(tarIn, out);
                    }
                }
            }
        }
    }

    /**
     * 写文件
     *
     * @param in
     * @param out
     * @throws IOException
     */
    public static void writeFile(InputStream in, OutputStream out) throws IOException {
        int length;
        byte[] b = new byte[1024 * 10];
        while ((length = in.read(b)) != -1) {
            out.write(b, 0, length);
        }
    }

    /**
     * 创建目录
     *
     * @param outputDir
     * @param subDir
     */
    public static void createDirectory(String outputDir, String subDir) {
        File file = new File(outputDir);
        //子目录不为空
        if (!(subDir == null || subDir.trim().equals(""))) {
            file = new File(outputDir + File.separator + subDir);
        }
        if (!file.exists()) {
            if (!file.getParentFile().exists()) {
                file.getParentFile().mkdirs();
            }
            file.mkdirs();
        }
    }

    /**
     * 删除Mac压缩再解压产生的 __MACOSX 文件夹和 .开头的其他文件
     *
     * @param filteredFile
     */
    public static void filterFile(File filteredFile) {
        if (filteredFile != null) {
            File[] files = filteredFile.listFiles();
            for (File file : files) {
                if (file.getName().startsWith(".") ||
                        (file.isDirectory() && file.getName().equals("__MACOSX"))) {
                    FileUtils.deleteQuietly(file);
                }
            }
        }
    }
}
