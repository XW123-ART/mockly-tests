"""
运行测试的脚本
可以直接运行这个文件来执行所有测试
"""

import subprocess
import sys
import os


def run_all_tests():
    """
    运行所有测试
    """
    print("="*60)
    print("开始运行 SmartDataGen Web自动化测试")
    print("="*60)
    print()

    # 获取当前目录
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 构建pytest命令
    # -v: 显示详细信息
    # -s: 显示print输出
    # tests/: 运行tests目录下的所有测试
    cmd = [
        sys.executable,  # Python解释器
        "-m", "pytest",  # 运行pytest模块
        "-v",  # 详细输出
        "-s",  # 显示print
        "--tb=short",  # 简化的错误信息
        "tests/"  # 测试目录
    ]

    print(f"执行命令: {' '.join(cmd)}")
    print()

    # 执行测试
    result = subprocess.run(cmd, cwd=current_dir)

    print()
    print("="*60)
    if result.returncode == 0:
        print("所有测试通过!")
    else:
        print(f"测试失败，返回码: {result.returncode}")
    print("="*60)

    return result.returncode


if __name__ == "__main__":
    exit_code = run_all_tests()
    sys.exit(exit_code)
