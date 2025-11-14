#4.1 Load the penguins dataset using the seaborn module. Remove any rows with missing values. Hint: Check out how to use the dropna() function.
import seaborn as sns

penguins = sns.load_dataset('penguins')
penguins_clean = penguins.dropna()
print(penguins) # to show original data with missing values (NAN)
print(penguins_clean)# to show after dropna without missing values.


#4.2 Create a scatterplot. The plot should show flipper length on the x-axis and body mass on 
#the y-axis. Add an informative title, xlabel and ylabel. Save the plot.

#In the first diagram, I see different dots, each a different color representing a different species. Blue is for Adélie,
# orange for Shinstrop, and green for Gento. From the diagram, I can see that Adélie and Shinstrop points  overlap. when gento,
# have a different mass and flipper length
import matplotlib.pyplot as plt

sns.scatterplot(data=penguins_clean, x='flipper_length_mm', y='body_mass_g', hue='species')
plt.title('Penguin Flipper Length vs Body Mass ')
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Body Mass (g)')
plt.savefig('penguin_scatterplot.png', dpi=300)
plt.show()
# 4.3 Plot a distribution plot of the penguin flipper length using a histogram.
 #What does this plot show? What are some conclusions you can draw from it?

 #What happens if you vary the amount of bins in the plot? Why?
 #Add appropriate y and x-labels, as well as a title.
 #Save the plot.


plt.hist(penguins_clean['flipper_length_mm'], bins=20, edgecolor='black')
plt.title("  Flipper Length distribution of Penguin")
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Count")
plt.grid(axis='y')
plt.savefig("hist_flipper_length.png", dpi=300)
plt.show()

#4.4

#Read the data CNV_log2_skin_melanoma.csv from the practice dugga using pandas.

 #   Create a violinplot (the seaborn package is useful for this) with chromosome on the x-axis and cnv_log2 on the y-axis. Add informative titles and save the plot.

  #  What do you see? Which chromosome(s) has the largest CNV interval? Which chromosome(s) has the smallest interval? Do the intervals add up with the numbers in the dataframe you used for the plot?

   # Check the axes and labels. Is there something that could be changed to improve the plot?

   # Load CNV data

import pandas as pd
cnv_df = pd.read_csv("CNV_log2_skin_melanoma.csv")

plt.figure(figsize=(12,6))
sns.violinplot(x='chromosome', y='cnv_log2', data=cnv_df, inner='quartile', palette='Set2')
plt.title("CNV Log2 Distribution Across Chromosomes")
plt.xlabel("Chromosome")
plt.ylabel("CNV log2")
plt.grid(axis='y')
plt.savefig("violin_cnv.png", dpi=300)
plt.show() 