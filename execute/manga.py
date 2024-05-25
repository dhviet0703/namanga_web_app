from execute import *
from datetime import datetime, timedelta


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
def get_manga_data_views():
    query = """
        SELECT m.*, 
               COALESCE(MAX(c.created_at), '1900-01-01') AS latest_chapter_create_at
        FROM public.engine_manga m
        LEFT JOIN public.engine_chapter c ON m.id = c.manga_id
        GROUP BY m.id
        ORDER BY GREATEST(m.updated_at, m.created_at, COALESCE(MAX(c.created_at), '1900-01-01')) DESC, 
                 m.views DESC;
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
def get_total_manga():
    query = """
        SELECT COUNT(*) AS total
        FROM public.engine_manga;
    """
    result = pd.read_sql(query, engine)
    return result.iloc[0]['total']


@st.cache_data
def get_total_manga_add_new_in_one_hour():
    one_hour_ago = datetime.now() - timedelta(hours=24)
    query = """
        SELECT COUNT(*) AS total
        FROM public.engine_manga
        WHERE created_at >= %(one_hour_ago)s OR updated_at >= %(one_hour_ago)s;
    """
    result = pd.read_sql(query, engine, params={"one_hour_ago": one_hour_ago})
    return result.iloc[0]['total']


@st.cache_data
def get_total_manga_with_genre(genre):
    query = """
        SELECT COUNT(*) AS total
        FROM public.engine_manga
        WHERE genres LIKE %(genre)s;
    """
    result = pd.read_sql(query, engine, params={"genre": f"%{genre}%"})
    return result.iloc[0]['total']


@st.cache_data
def get_total_chapter(manga_id):
    query = """
            SELECT COUNT(*) AS total
            FROM public.engine_chapter
            WHERE manga_id = %(manga_id)s
            """
    result = pd.read_sql(query, engine, params={"manga_id": manga_id})
    return result.iloc[0]['total']


@st.cache_data
def get_manga_with_genre(genre):
    query = """
        SELECT *
        FROM public.engine_manga
        WHERE genres LIKE %(genre)s;
    """
    return pd.read_sql(query, engine, params={"genre": f"%{genre}%"})


@st.cache_data
def get_image_chapter(chapter_id):
    query = """
            SELECT *
            FROM public.engine_image
            WHERE chapter_id = %(chapter_id)s
            ORDER BY src ASC;
            """
    return pd.read_sql(query, engine, params={"chapter_id": chapter_id})

