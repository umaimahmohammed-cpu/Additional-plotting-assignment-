import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import sys


#4.1 Load the penguins dataset using the seaborn module. Remove any rows with missing values. Hint: Check out how to use the dropna() function.

penguins = sns.load_dataset('penguins')
penguins_clean = penguins.dropna()
print(penguins) # to show original data with missing values (NAN)
print(penguins_clean)# to show after dropna without missing values.


#4.2 Create a scatterplot. The plot should show flipper length on the x-axis and body mass on 
#the y-axis. Add an informative title, xlabel and ylabel. Save the plot.

####In the first diagram, I see different dots, each color representing a different species. Blue is for Adelie,
####orange for chinstrap, and green for gentoo. From the diagram, I can see that Adelie and chinstrap points overlap. when gentoo,
#### have a different mass and flipper length

sns.scatterplot(data=penguins_clean, x='flipper_length_mm', y='body_mass_g', hue='species')
plt.title('Penguin Flipper Length vs Body Mass ')
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Body Mass (g)')
plt.savefig('penguin_scatterplot.png', dpi=300)
plt.show()
# 4.3 Plot a distribution plot of the penguin flipper length using a histogram.
 #What does this plot show? What are some conclusions you can draw from it?
####This plot shows the distribution of the penguin flipper length in all species. The plot is clearly showing two groups, 
####like the scatterplot above the first group comprises the Adelie and chinstrap species from 180 to 200 mm, ,
####and the second group is the gentoo species from 210 to 230 mm .The plot also shows that the highst count for penguins
####is 190 mm,  representing the length of the two species and indicating that 190 mm is the most common size.

 #What happens if you vary the amount of bins in the plot? Why?
#### with more bins we get smaller bars and it's harder to distinguish the groups that are present in the data.its also more confusing and hard to understand.
#### fewer bins like 5 showed bigger bars it is also not perfect since the species groups are also lost. 
### the reason for this is that More bins shows finer details but can show more noise, 
####while fewer bins makes the data smoother but may hide important information.

 #Add appropriate y and x-labels, as well as a title.
 #Save the plot.


plt.hist(penguins_clean['flipper_length_mm'], bins=20 , edgecolor='black')
plt.title("  Flipper Length distribution of Penguin")
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Count")
plt.grid(axis='y')
plt.savefig("hist_flipper_length.png", dpi=300)
plt.show()

#4.4

#Read the data CNV_log2_skin_melanoma.csv from the practice dugga using pandas.

 #   Create a violinplot (the seaborn package is useful for this) with chromosome on the x-axis and cnv_log2 on the y-axis.
 # Add informative titles and save the plot.

  #  What do you see? Which chromosome(s) has the largest CNV interval? Which chromosome(s) has the smallest interval?
   #### in the plot chromosome 22 has the largest CNV interval from almost -2 to +3 . several chromosoms has the samllest interval and they are showing 
   #### flat line (14, 18, 9) etc
  # Do the intervals add up with the numbers in the dataframe you used for the plot?
#### to chick if the intervals add upp to the numbers in the dataframe. i open the datafram and looked at the interval width (min and max).
#### then compare it to the figure. and similar information were found where chr 22 shows the widest range and chr 14 is amoung the smallest
   # Check the axes and labels. Is there something that could be changed to improve the plot?
   #### i made the title bold and bigger, i also add plt.grid(axis='y') which make the figure easir to understand. also rotated x label plt.xticks(rotation=45).


   # Load CNV data


cnv_file = sys.argv[1]
cnv_df = pd.read_csv(cnv_file)
plt.figure(figsize=(12,6))
sns.violinplot(x='chromosome', y='cnv_log2', data=cnv_df, inner='quartile', palette='Set2')# 
plt.title("CNV Log2 Distribution Across Chromosomes",   fontsize=16, fontweight='bold') #
plt.xlabel("Chromosome")
plt.ylabel("CNV log2")
plt.xticks(rotation=45) #
plt.grid(axis='y') #
plt.savefig("violin_cnv.png", dpi=300)
plt.show() 