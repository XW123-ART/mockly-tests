"""
生成Allure测试报告

使用方法:
    python generate_allure_report.py
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

    # 检查allure-results目录是否存在
    if not os.path.exists(os.path.join(current_dir, "allure-results")):
        print("[错误] allure-results目录不存在!")
        print("请先运行测试生成结果:")
        print("  python -m pytest tests/ --alluredir=allure-results")
        return 1

    # 生成静态HTML报告
    print("[步骤1] 生成静态HTML报告...")
    print()

    cmd = [
        "allure", "generate", "./allure-results", 
        "-o", "./allure-report", 
        "--clean"
    ]

    print(f"执行命令: {' '.join(cmd)}")
    print()

    result = subprocess.run(cmd, cwd=current_dir, capture_output=True, text=True)
    if result.returncode != 0:
        print("[错误] 生成报告失败:")
        print(result.stderr)
        return 1

    print("[完成] 报告生成成功!")
    print(f"报告位置: {os.path.join(current_dir, 'allure-report')}")
    print()
    print("在浏览器中打开以下文件查看报告:")
    print(f"  {os.path.join(current_dir, 'allure-report', 'index.html')}")
    print()

    return 0


if __name__ == "__main__":
    sys.exit(main())
