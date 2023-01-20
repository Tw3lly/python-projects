import email

def gather_eml_artifacts(file_path):
    with open(file_path, 'r') as f:
        msg = email.message_from_file(f)
        headers = msg.items()
        body = msg.get_payload()
        metadata = {
            'file_path': file_path,
            'file_size': os.path.getsize(file_path),
            'file_created': os.path.getctime(file_path),
            'file_modified': os.path.getmtime(file_path),
            'file_hash': hashlib.md5(open(file_path,'rb').read()).hexdigest()
        }
        
    return headers, body, metadata
