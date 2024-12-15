mport requests

def get_ip_location(ip):
    """
    查询 IP 地址的地理位置。
    :param ip: str, IP 地址
    :return: str, 地理位置信息
    """
    try:
        # 使用公开的 IP 查询接口
        response = requests.get(f"https://ipapi.co/{ip}/json/")
        data = response.json()
        
        if "error" in data:
            return f"查询失败: {data['reason']}"
        
        location = f"{data.get('city', '未知城市')}, {data.get('region', '未知地区')}, {data.get('country_name', '未知国家')}"
        return f"IP {ip} 的归属地为：{location}"
    except Exception as e:
        return f"查询失败，错误原因：{e}"

if __name__ == "__main__":
    ip = input("请输入要查询的 IP 地址：")
    print(get_ip_location(ip))
