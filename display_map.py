import matplotlib.pyplot as plt


# TODO: this whole function needs a rewrite from the ground up.
#  Look into matplotlib options and get a better handle on all this.

def map_show(combined_df, detail_level, data_option, display_value):
    # display_value = 'latest'
    red_states_df = combined_df[combined_df.PARTY.eq('republican')]
    blue_states_df = combined_df[combined_df.PARTY.eq('democrat')]

    color_min = 0
    color_max = 200000

    # TODO: extract magic numbers
    fig, ax = plt.subplots(1, figsize=(6, 2))
    ax.axis('off')
    map_title = "covid " + data_option + " by " + detail_level
    ax.set_title(map_title.title(), fontdict={'fontsize': '25', 'fontweight': '3'})
    ax.annotate("Source: Harvard ", xy=(0.1, .08),
                xycoords='figure fraction', horizontalalignment='left',
                verticalalignment='top', fontsize=12, color='#555555')

    # Create colorbar as a legend
    # TODO: add second colorbar?
    sm = plt.cm.ScalarMappable(cmap='Greys', norm=plt.Normalize(vmin=color_min, vmax=color_max))

    # empty array for the data range
    sm._A = []
    # add the colorbar to the figure
    # TODO: pycharm tells me cbar is not used - what did I do? Is this not needed anymore?
    cbar = fig.colorbar(sm)

    # create map
    # TODO: extract magic numbers
    # ax=ax? that can't be right. rename?

    fig.tight_layout()
    # us_50_states_df.plot
    combined_df.plot(cmap='Greys', linewidth=0.8, ax=ax, edgecolor='0.8')
    red_states_df.plot(display_value, ax=ax, cmap='Reds')
    blue_states_df.plot(display_value, ax=ax, cmap='Blues')

    fig.tight_layout()

    map_name = display_value + " " + detail_level + " covid " + data_option + " choropleth.png"
    # Can't have / in filenames.
    map_name = map_name.replace(" ", "_")
    map_name = map_name.replace("/", "-")
    fig.savefig(map_name, dpi=300)

    plt.show()
    # Matplotlib gives you lots of freedom in how you save figures.
    # The code below will save the figure as a png,
    # but if you want to fiddle about some more with it in Illustrator you can also save as svg.
    # If you save as png, make sure to use a dpi of 200 or above.
    # Otherwise the map and text will look all blurry. Nobody wants that.
    # fig.savefig("map_export.png", dpi=300)

    return

# if __name__ == '__main__':
#    map_show(combined_df, display_value)
