<html>
<head>
<title>Commands page</title>
</head>
<body>

<?php   

	echo "<h1>Typical Usage</h1>";
	echo "Input -";
	echo "1) Assembled contigs/scaffolds in multi-fasta format (e.g. test_dataset/contigs.fa). Note that for Velvet and SOAPdenovo output, OPERA-LG automatically recognizes repeat contigs and filters them out. For other assemblers, the expected input is a set of non-repeat contigs.";
	echo "2) Paired-end reads to be used for scaffolding (e.g. test_dataset/lib_1_1.fa, test_dataset/lib_1_2.fa).";
	echo "";
	echo "Running OPERA-LG:";
	echo "1) Reads need to be mapped onto contigs (currently we provide a script that uses bowtie or bwa):";
	echo "";
	echo "   perl bin/preprocess_reads.pl <contig-file> <read-file-1> <read-file-2> <output-file> (<mapping-tool> <temporary-directory>)";
	echo "";
	echo "   where mapping-tool should be either bwa or bowtie (default), read-file-1 and read-file-2 contain paired-end reads in fasta or fastq format, temporary-directory is the current directory by default.";	
	echo "";
	echo "   For example:";
	echo "   perl bin/preprocess_reads.pl test_dataset/contigs.fa test_dataset/lib_1_1.fa test_dataset/lib_1_2.fa test_dataset/lib_1.map bowtie ./";
	echo "";
	echo '   The mapping file should have extension as ".sam" or ".bam", if the output format is either of them. For bowtie normal format, ".map" can be used as extension.';
	echo "";
	echo '   Note that the binaries <a href="http://bio-bwa.sourceforge.net/bwa.shtml">"bwa"</a>, <a href="http://bowtie-bio.sourceforge.net/index.shtml">"bowtie" and "bowtie-build"</a> are assumed to be in the path. If not, the third line of preprocess_reads.pl should be edited appropriately.';
	echo "";
	echo '2) There are two ways to provide parameters to OPERA-LG:';
	echo '';
	echo '   (A) Using the command line';	
	echo '	     bin/OPERA-LG <contig-file> <mapping-files> <output-folder>';
	echo '';
	echo '       <contig-file>           Multi-fasta contig file';
	echo '       <mapping-files>         Comma-separated list of files containing mapping of paired-end reads';
	echo '       <output-folder>         Folder to save the scaffold results';
	echo '';
	echo '       For example:';
	echo '       bin/OPERA-LG test_dataset/contigs.fa test_dataset/lib_1.map,test_dataset/lib_2.map test_dataset/results';
	echo '';
	echo '   (B) Using a configuration file';
	echo '       bin/OPERA-LG <config-file>';
	echo '';
	echo '	     <config-file>           Configuration file';
	echo '';
	echo '	     For example:';
	echo '	     bin/OPERA-LG test_dataset/multiLib.config';
	echo '	     where the configuration file provides information on the contig file, mapping files and output directory to use (see below for the format).';	
	echo '';
	echo 'Running OPERA-LG for long reads:';
	echo '1) The wrapper scrip "OPERA-long-read.pl" enables OPERA-LG to use long reads from third-generation sequencing technologies. The mapping of long reads (PacBio or Oxford Nanopore) is performed using blasr. The contig links are then computed using OPREA-link approach (see Supplementary Note 2 of the OPERA-LG paper) or the the SSPACE-LR approach.';
	echo '';
	echo '2) The wrapper can be called using the following command line:';
	echo 'OPERA-long-read.pl method=<OPERA-link|SSPACE-LR-link> contig-file=<fasta file of contigs> reads-file=<fasta file of long reads> output-prefix=<prefix of output mapping file> output-directory=<output directory for scaffolding results> num-of-processors=<number of processors for blasr & SSPACE>';
	echo '';
	echo '3) The wrapper assumes that blasr, SSPACE-LR and OPERA-LG binaries are found in your PATH. Otherwise, you may specify the location to the binaries by adding the respective arguments';
	echo 'OPERA-long-read.pl blasr=<Folder which contains blasr binary> sspace=<Folder which contains SSPACE perl script> opera=<Folder which contains opera binary>';

?>

</body>
</html>
