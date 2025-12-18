{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMr3XZ4+Vhy7p+UbLUwNDab",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ad-aditisingh/gold-jewellery-price-predictor-india/blob/main/app_py.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "mPAgaza8tNrj"
      },
      "outputs": [],
      "source": [
        "import streamlit as st\n",
        "import joblib\n",
        "import numpy as np\n",
        "\n",
        "# Load trained model\n",
        "model = joblib.load(\"linear_regression_jewellery_model.pkl\")\n",
        "\n",
        "st.title(\"Gold Jewellery Price Estimator (India 🇮🇳)\")\n",
        "\n",
        "st.write(\"Enter jewellery details to estimate price\")\n",
        "\n",
        "# User inputs\n",
        "gold_rate = st.number_input(\"Gold Rate (₹ per gram, 22K)\", min_value=1000.0)\n",
        "weight = st.number_input(\"Weight (grams)\", min_value=0.1)\n",
        "making_charge = st.number_input(\"Making Charges (%)\", min_value=0.0)\n",
        "\n",
        "# Predict button\n",
        "if st.button(\"Estimate Price\"):\n",
        "    features = np.array([[gold_rate, weight, making_charge]])\n",
        "    price = model.predict(features)[0]\n",
        "\n",
        "    st.success(f\"Estimated Jewellery Price: ₹{price:,.2f}\")\n"
      ]
    }
  ]
}
