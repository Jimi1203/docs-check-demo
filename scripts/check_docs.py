#!/usr/bin/env python3
"""
简单的文档检查脚本
"""
import os
import subprocess
import sys

def run_markdownlint():
    """运行 markdownlint 检查"""
    print("��� 运行 markdownlint 检查...")
    
    try:
        # 检查当前目录下所有 .md 文件
        result = subprocess.run(
            ["markdownlint", "**/*.md", "--ignore", "node_modules"],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            print("❌ 发现 markdown 格式问题：")
            print(result.stdout)
            print(result.stderr)
            return False
        else:
            print("✅ markdown 格式检查通过！")
            return True
            
    except FileNotFoundError:
        print("⚠️  markdownlint 未安装，跳过格式检查")
        return True

def check_readme_exists():
    """检查 README.md 是否存在"""
    print("��� 检查 README.md 文件...")
    
    if os.path.exists("README.md"):
        print("✅ README.md 存在")
        return True
    else:
        print("❌ README.md 不存在")
        return False

def main():
    """主函数"""
    print("=" * 50)
    print("开始文档检查")
    print("=" * 50)
    
    all_passed = True
    
    # 检查1: README 是否存在
    if not check_readme_exists():
        all_passed = False
    
    # 检查2: markdown 格式
    if not run_markdownlint():
        all_passed = False
    
    print("=" * 50)
    if all_passed:
        print("✅ 所有文档检查通过！")
        sys.exit(0)
    else:
        print("❌ 文档检查未通过，请修复问题")
        sys.exit(1)

if __name__ == "__main__":
    main()
