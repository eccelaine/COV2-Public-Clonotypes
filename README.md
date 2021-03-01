# COV2-Public-Clonotypes
This repo contains code used for the manuscript: Convergent antibody responses to the SARS-CoV-2 spike protein in convalescent and vaccinated individuals. There are two main sections of code. 

# Clustering to identify public clonotypes
1. Identification of sequence characteristics 
- Take all sequences you are interested in clustering, and run it through PyIR (https://github.com/crowelab/PyIR). Once sequences are run through you should have the V gene, J gene, and CDR3 amino acid lengths, and CDR3 amino acid sequences defined for each sequence. 

2. Create clustering file
- From this separate out your sequences and bin them by V gene, J gene, and CDR3 AA lengths. You can make these files by running it through MakeClusteringFiles.py

3. Run clustering script
- Using your output file from step 2, run it through the script Clustering.py

4. Analyze clustering results
- Using your output file from step 3, run it through the script Combine.py. Then 


# Heat Map generation
1. Identification of VJ combinations
- Run your sequences through the script VJcombos.py

2. Create heat map
- Take output file from step 1 and run it through heatmaps.py

