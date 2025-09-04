import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_weather(df, city):
    """Create simple bar plots of weather parameters."""
    numeric_cols = ["Temperature (°C)", "Feels Like (°C)", "Humidity (%)", "Pressure (hPa)", "Wind Speed (m/s)"]
    df_melted = df.melt(id_vars=["City", "Condition"], value_vars=numeric_cols,
                        var_name="Metric", value_name="Value")

    plt.figure(figsize=(8,5))
    sns.barplot(x="Metric", y="Value", hue="Metric", data=df_melted, palette="viridis", legend=False)

    # 🔹 Add condition text to the chart title
    condition = df["Condition"].iloc[0]   # take first row condition
    plt.title(f"Weather Dashboard - {city} ({condition})")

    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save plot
    os.makedirs("visuals", exist_ok=True)
    plot_path = f"visuals/{city}_weather.png"
    plt.savefig(plot_path)

    # Show for 10s then close automatically
    plt.show(block=False)
    plt.pause(10)
    plt.close()

    return plot_path
