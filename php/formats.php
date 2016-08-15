<html>
<head>
<title>Formats page</title>
</head>
<body>

<?php   

	echo "<h1>Output formats</h1>";
	echo 'Scaffolds output by OPERA-LG can be found in a multi-fasta file "scaffoldSeq.fasta". Summary assembly statistics can be found in the file "statistics".';
	echo "";
	echo "<h1>Format of Configuration File</h1>";
	echo 'An example configuration file can be found in "test_dataset/singleLib.config". The main parameters that need to be specified are:';
	echo "";
	echo "a) contig_file: a multi-fasta file containing assembled contigs/scaffolds (input to OPERA-LG).";
	echo "b) map_file: the mapping file specifying the location of paired-end reads on the contigs/scaffolds (input to OPERA-LG; see bin/preprocess_reads.pl).";
	echo "c) output_folder: the directory into which all results are written.";
	echo "d) kmer: the value of kmer used to produce the assembled contigs/scaffolds (input to OPERA-LG). If not specified, OPERA-LG will try to analyze corresponding assembly file (LastGraph for Velvet assembly or <prefix>.preGraphBasic for SOAPdenovo assembly) in the same directory containing the contig_file. Kmer will be set to 100 if the file cannot be found.";

?>

</body>
</html>
