# Sample Movie Dataset
import pandas as pd
movies_data = {
    'Title': ['Movie1', 'Movie2', 'Movie3', 'Movie4', 'Movie5'],
    'Genre': ['Action', 'Comedy', 'Action|Adventure', 'Drama', 'Comedy|Drama']
}

movies_df = pd.DataFrame(movies_data)

# User's preferred genre
user_preference = 'Comedy'

# Filter movies based on user's preference
recommended_movies = movies_df[movies_df['Genre'].str.contains(user_preference)].head(3)

# Display recommended movies
print(f"Recommended movies based on your preference ({user_preference}):")
print(recommended_movies[['Title', 'Genre']])
