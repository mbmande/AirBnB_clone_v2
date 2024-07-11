@runs_once
def do_pack():
    """Archives the static files."""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
                            
    d_time = datetime.now()
    outp    ut = f"versions/web_static_{d_time.strftime('%Y%m%d%H%M%S')}.tgz"
                                        
    try:
        print(f"Packing web_static to {output}")
        local(f"tar -cvzf {output} web_static")
        size = os.stat(output).st_size
        print(f"web_static packed: {output} -> {size} Bytes")
    except Exception as e:
        print(f"Error packing: {e}")
        output = None
                                                                                                            
    return output

