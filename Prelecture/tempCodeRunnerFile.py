
anime_data_extracted = anime_data_extracted[anime_data_extracted["Score"] != "Unknown"].copy()
anime_data_extracted["Score"] = anime_data_extracted["Score"].astype(float)