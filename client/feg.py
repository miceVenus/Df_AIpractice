import argparse
from model import Model

def main():
    parser = argparse.ArgumentParser(description="摘要生成器")
    parser.add_argument("-i", "--input", type=str, help="输入文件位置 可以为多个文件")
    parser.add_argument("-o", "--output", type=str, help="输出文件目录 只能为一个")
    parser.add_argument("-v", "--version", action="store_true", help="feg当前版本号")
    parser.add_argument("--verbose", action="store_true", help="详细信息")
    args = parser.parse_args()
    
    if args.input:
        fileDir = args.input
        if args.output:
            outputDir = args.output
            model.ProcessUploadFile([fileDir], outputDir)
            print("Done!!!")
        else:
            model.ProcessUploadFile([fileDir])
            print("Done!!!")
    
    if args.version:
        print(f"feg version {version}")
    
    if args.verbose:
        print(f"{verbose}")
        
if __name__ == "__main__":
    version = "0.1"
    verbose = "这里面会有什么呢？"
    
    model = Model()
    
    main()