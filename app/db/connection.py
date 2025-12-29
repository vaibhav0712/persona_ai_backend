from pinecone import Pinecone

from core.config import settings

pc = Pinecone(settings.pinecone_api)
inx = pc.Index(settings.pinecone_index, settings.pinecone_host)
