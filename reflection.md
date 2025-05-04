# Reflection

Student Name:  name
Sudent Email:  email

## Instructions

Reflection is a key activity of learning. It helps you build a strong metacognition, or "understanding of your own learning." A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, share your throughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

**Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 

**Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

`--- Reflection Below This Line ---`
From this code, one key learning outcome is how to perform data transformation and aggregation using pandas. The top_locations() function demonstrates how to pivot a dataset to aggregate the total amount of parking violations per location and filter those that exceed a specific threshold. For example, using violations_df.pivot_table(index='location', values='amount', aggfunc='sum') groups all violation amounts by location, while sorting and filtering ensures that only high-violation areas (e.g., over $1000) are kept. This process is foundational in turning raw tabular data into structured insights.

Another major learning point is how to make interactive data visualizations with Streamlit. In location_dashboard.py, Streamlit widgets such as st.selectbox() and st.metric() are used to build an interactive interface where users can select a location and view relevant visual analytics. For example, once a location is chosen, bar plots display tickets by hour of day and day of week using seaborn.barplot(), giving users a clear understanding of temporal violation patterns. This introduces best practices in dashboard development, where UI elements are tightly integrated with dynamic, filtered data views.
Overall a bit of a confusing lab if you ask me lol

Finally, spatial data representation and mapping were explored through geospatial libraries like GeoPandas and Folium in map_dashboard.py. The top_locations_mappable() function ensures that high-violation locations are joined with geographic coordinates, and these are then plotted on an interactive map. A GeoDataFrame is created using gpd.points_from_xy() to enable mapping, and Folium's explore() function overlays the violation amounts using a color scale. Constants like CUSE, ZOOM, VMIN, and VMAX control map centering and styling, enhancing the visualization experience and geographic insight. Would you like a visual diagram summarizing the ETL and dashboard flow?