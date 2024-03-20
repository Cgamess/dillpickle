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
    if not st_itr:
        cip=cry.fernet.Fernet(key)
        try:
            e_data=cip.encrypt(bytes(data))
        except:
            e_data=cip.encrypt(data.encode())
    else:
        cip=cry.fernet.Fernet(key[0])
        try:
            ce_data=cip.encrypt(bytes(data))
        except:
            ce_data=cip.encrypt(data.encode())
        for i in range(1,len(key-1)):
            cip=cry.fernet.Fernet(key[i])
            ce_data=cip.encrypt(ce_data)
        cip=cry.fernet.Fernet(key[-1])
        e_data=cip.encrypt(ce_data)

        # add quantom stuff later

        return e_data