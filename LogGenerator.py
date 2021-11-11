#Log Generator 

def log_generator(date, ip_addr, proto, src_port, dst_port):
  if len(date) != 10:
    return "Error: Incorrect date format given. Date must be formatted as mm-dd-yyyy"
  elif len(ip_addr) < 7 or len(ip_addr) > 15:
      return "Error: Impossible IP address length given"
  elif proto != "TCP" and proto != "UDP":
    return "Error: Incorrect protocol given. Must be TCP or UDP"
  elif src_port < 0 or src_port > 65535:
     return "Error: Incorrect port number given for src_port: " + str(src_port)
  elif dst_port < 0 or dst_port > 65535:
      return "Error: Incorrect port number given for dst_port: " + str(dst_port)
  else:
      return date + " | " + ip_addr + " | " + proto + " | " + str(src_port) + " | " + str(dst_port)
