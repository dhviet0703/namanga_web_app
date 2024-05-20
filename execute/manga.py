from execute import *


@st.cache_data
def get_manga_data():
    query = """
        SELECT m.*, 
               COALESCE(MAX(c.created_at), '1900-01-01') AS latest_chapter_create_at
        FROM public.engine_manga m
        LEFT JOIN public.engine_chapter c ON m.id = c.manga_id
        GROUP BY m.id
        ORDER BY GREATEST(m.updated_at, m.created_at, COALESCE(MAX(c.created_at), '1900-01-01')) DESC;
        """
    return pd.read_sql(query, engine)


@st.cache_data
def get_chapter_list(manga_id):
    query = """
        SELECT *
        FROM public.engine_chapter
        WHERE manga_id = %(manga_id)s
        ORDER BY number ASC;
        """
    return pd.read_sql(query, engine, params={"manga_id": manga_id})





@st.cache_data
def get_image_chapter(chapter_id):
    query = """
            SELECT *
            FROM public.engine_image
            WHERE chapter_id = %(chapter_id)s
            ORDER BY src ASC;
            """
    return pd.read_sql(query, engine, params={"chapter_id": chapter_id})

