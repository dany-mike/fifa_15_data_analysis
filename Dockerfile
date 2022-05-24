FROM python:3.10
RUN pip3 install streamlit && pip3 install pandas && pip3 install matplotlib
COPY players_15.csv .
COPY streamlit.py .
COPY styles.css .
COPY logo_crystal_palace.png .
COPY functions ./functions
EXPOSE 9000
ENTRYPOINT [ "streamlit", "run" ]
CMD ["streamlit.py"]