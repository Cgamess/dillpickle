import cryptography as cry
import qencrypt.handle as qcry

def crypt(data, hash, key, qkey):
    st_itr=0
    qc_itr=0
    if not isinstance(key, bytes):
        if isinstance(key, (list, tuple, set)):
            for i in key:
                if not isinstance(i, bytes):
                    raise ValueError(f"Key elements must be bytes, not {type(i).__name__}")
            st_itr=1
        else:
            raise ValueError("Key must be bytes or an iterable of bytes")    
    if not isinstance(qkey, bytes):
        if isinstance(qkey, (list, tuple, set)):
            for i in qkey:
                if not isinstance(i, bytes):
                    raise ValueError(f"Key elements must be bytes, not {type(i).__name__}")
            qc_itr=1
        else:
            raise ValueError("Key must be bytes or an iterable of bytes")
