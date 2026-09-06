# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: AuditTrail
import argparse

def main():
    parser = argparse.ArgumentParser(description="AuditTrail CLI")
    sub = parser.add_subparsers(dest="command")
    
    p_check = sub.add_parser("check", help="Проверить аудит")
    p_check.add_argument("path", help="Путь к файлу")
    
    p_log = sub.add_parser("log", help="Записать лог")
    p_log.add_argument("path", help="Путь к файлу")
    p_log.add_argument("message", help="Сообщение")
    
    p_list = sub.add_parser("list", help="Список проверок")
    p_list.add_argument("path", help="Путь к файлу")
    
    args = parser.parse_args()
    
    if args.command == "check":
        with open(args.path, "r") as f:
            print(f.read())
    elif args.command == "log":
        with open(args.path, "a") as f:
            f.write(args.message + "\n")
    elif args.command == "list":
        with open(args.path, "r") as f:
            for line in f:
                print(line.strip())
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
