@runs_once
def do_pack():
        """Archives the static files."""
            output_dir = "versions"
                if not os.path.exists(output_dir):
                            try:
                                            os.makedirs(output_dir)
                                                    except OSError as e:
                                                                    print(f"Error creating directory {output_dir}: {e}")
                                                                                return None
                                                                                
                                                                                d_time = datetime.now()
                                                                                    output = f"{output_dir}/web_static_{d_time.strftime('%Y%m%d%H%M%S')}.tgz"
                                                                                        
                                                                                            try:
                                                                                                        print(f"Packing web_static to {output}")
                                                                                                                local(f"tar -cvzf {output} web_static")
                                                                                                                        size = os.stat(output).st_size
                                                                                                                                print(f"web_static packed: {output} -> {size} Bytes")
                                                                                                                                    except Exception as e:
                                                                                                                                                print(f"Error packing: {e}")
                                                                                                                                                        output = None
                                                                                                                                                            
                                                                                                                                                                return output
