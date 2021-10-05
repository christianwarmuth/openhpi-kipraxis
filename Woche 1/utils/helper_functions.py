import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def plot_df_on_california(df, california_path):

    ax = df.plot(
        kind="scatter", 
        x="longitude", 
        y="latitude", 
        figsize=(10, 8),
        s=df['population']/100, 
        label="Population",
        c="median_house_value", 
        cmap=plt.get_cmap("jet"),
        colorbar=True, 
        alpha=0.4
    )

    x_min, x_max = ax.get_xlim()
    y_min, y_max = ax.get_ylim()
    california_img = mpimg.imread(california_path)
    plt.imshow(
        california_img, 
        extent=[-124.85, -113.8, 32.08, 42.42], 
        alpha=0.4,
        cmap=plt.get_cmap("jet")
    )

    plt.legend();