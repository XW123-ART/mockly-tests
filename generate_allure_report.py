"""
生成Allure测试报告

使用方法:
    1. 先生成报告: python generate_allure_report.py
    2. 查看报告: allure serve ./allure-results

或者:
    python generate_allure_report.py --serve
"""

import subprocess
import sys
import os


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))

    print("="*60)
    print("SmartDataGen Web自动化测试 - Allure报告生成")
    print("="*60)
    print()

    # 检查allure是否安装
    print("[检查] 检查allure命令行工具...")
    result = subprocess.run(["allure", "--version"], capture_output=True)
    if result.returncode != 0:
        print("[警告] 未检测到allure命令行工具!")
        print()
        print("请先安装Allure:")
        print("1. 下载: https://github.com/allure-framework/allure2/releases")
        print("2. 解压并添加bin目录到系统环境变量PATH")
        print("3. 重启PyCharm或命令行窗口")
        print()
        print("或者使用pytest-html生成简单报告:")
        print("  pip install pytest-html")
        print("  pytest --html=report.html")
        return 1

    version = result.stdout.decode().strip()
    print(f"[检查] Allure版本: {version}")
    print()

    # 运行测试生成allure结果
    print("[步骤1] 运行测试并生成Allure数据...")
    print()

    cmd = [
        sys.executable, "-m", "pytest",
        "tests/",
        "-v",
        "--alluredir=./allure-results",
        "--clean-alluredir"
    ]

    print(f"执行命令: {' '.join(cmd)}")
    print()

    subprocess.run(cmd, cwd=current_dir)

    print()
    print("[完成] 测试运行完成!")
    print()

    # 询问用户如何查看报告
    print("="*60)
    print("查看报告的方式:")
    print("="*60)
    print()
    print("方式1 - 启动本地服务器查看(推荐):")
    print("  allure serve ./allure-results")
    print()
    print("方式2 - 生成静态HTML文件:")
    print("  allure generate ./allure-results -o ./allure-report --clean")
    print("  然后在浏览器打开 allure-report/index.html")
    print()
    print("方式3 - 使用本脚本自动打开:")
    print("  python generate_allure_report.py --serve")
    print()

    # 如果带--serve参数，自动启动服务
    if len(sys.argv) > 1 and sys.argv[1] == "--serve":
        print("[步骤2] 启动Allure报告服务...")
        print("报告地址: http://localhost:8080")
        print("按 Ctrl+C 停止服务")
        print()
        subprocess.run(["allure", "serve", "./allure-results"], cwd=current_dir)

    return 0


if __name__ == "__main__":
    sys.exit(main())
