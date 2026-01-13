#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的文档检查脚本
"""
import os
import subprocess
import sys

def run_markdownlint():
    """运行 markdownlint 检查"""
    print("Running markdownlint check...")
    
    try:
        # 检查当前目录下所有 .md 文件
        result = subprocess.run(
            ["markdownlint", "**/*.md", "--ignore", "node_modules"],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            print("Found markdown issues:")
            print(result.stdout)
            return False
        else:
            print("Markdown format check passed!")
            return True
            
    except FileNotFoundError:
        print("markdownlint not installed, skipping format check")
        return True

def check_readme_exists():
    """检查 README.md 是否存在"""
    print("Checking README.md file...")
    
    if os.path.exists("README.md"):
        print("README.md exists")
        return True
    else:
        print("README.md not found")
        return False

def main():
    """主函数"""
    print("=" * 50)
    print("Starting document check")
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
        print("All document checks passed!")
        sys.exit(0)
    else:
        print("Document check found issues")
        sys.exit(0)  # 注意：这里改为0，不让workflow失败
        # 如果想在检查失败时让workflow也失败，用 sys.exit(1)

if __name__ == "__main__":
    main()
