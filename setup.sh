mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"cvorbach@mit.edu\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
" > ~/.streamlit/config.toml
