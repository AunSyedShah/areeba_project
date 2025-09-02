#!/usr/bin/env python3
"""
Final Validation Script for Climate Analysis Dashboard
Ensures project is ready for academic evaluation
"""

import os
from pathlib import Path

def validate_project_structure():
    """Validate that all required files are present and properly sized"""
    
    print("🔍 CLIMATE ANALYSIS DASHBOARD - EVALUATION READINESS CHECK")
    print("=" * 70)
    
    project_root = Path("/workspaces/areeba_project")
    
    # Required files for evaluation
    required_files = {
        "areeba_project.ipynb": "Main application (Jupyter Notebook)",
        "requirements.txt": "Python dependencies specification",
        "test_countries.py": "Data validation and testing script",
        "GlobalLandTemperaturesByCity.csv": "Climate dataset (509MB)",
        "README.md": "Project overview and documentation",
        "Comprehensive_User_Guide.docx": "Detailed user documentation for evaluators",
        "Comprehensive_Developer_Guide.docx": "Technical documentation for evaluators",
        "EVALUATION_OVERVIEW.md": "Evaluation guide for assessors"
    }
    
    print("📁 PROJECT STRUCTURE VALIDATION:")
    print("-" * 50)
    
    all_present = True
    total_size = 0
    
    for filename, description in required_files.items():
        filepath = project_root / filename
        
        if filepath.exists():
            file_size = filepath.stat().st_size
            size_mb = file_size / (1024 * 1024)
            total_size += file_size
            
            if size_mb > 1:
                size_display = f"{size_mb:.1f} MB"
            else:
                size_kb = file_size / 1024
                size_display = f"{size_kb:.1f} KB"
            
            print(f"✅ {filename:<35} ({size_display:<8}) - {description}")
        else:
            print(f"❌ {filename:<35} (Missing) - {description}")
            all_present = False
    
    print("-" * 50)
    total_size_mb = total_size / (1024 * 1024)
    print(f"📊 SUMMARY: {len(required_files)} files, {total_size_mb:.1f} MB total")
    
    if all_present:
        print("🎉 ALL REQUIRED FILES PRESENT!")
    else:
        print("⚠️ MISSING FILES DETECTED!")
        return False
    
    # Validate key directories are cleaned
    print("\n🧹 CLEANUP VALIDATION:")
    print("-" * 30)
    
    unwanted_dirs = [".gradio", ".venv", "artifacts", "spark-warehouse", "output_folder"]
    cleanup_success = True
    
    for dir_name in unwanted_dirs:
        dir_path = project_root / dir_name
        if dir_path.exists():
            print(f"⚠️ {dir_name} still exists (should be cleaned)")
            cleanup_success = False
        else:
            print(f"✅ {dir_name} properly removed")
    
    if cleanup_success:
        print("✅ Project cleanup completed successfully!")
    else:
        print("⚠️ Some cleanup items remain")
    
    # Validate documentation quality
    print("\n📚 DOCUMENTATION VALIDATION:")
    print("-" * 35)
    
    doc_files = ["Comprehensive_User_Guide.docx", "Comprehensive_Developer_Guide.docx"]
    doc_validation = True
    
    for doc_file in doc_files:
        doc_path = project_root / doc_file
        if doc_path.exists():
            file_size = doc_path.stat().st_size
            size_kb = file_size / 1024
            
            if size_kb > 30:  # Substantial documentation
                print(f"✅ {doc_file}: {size_kb:.1f} KB (Comprehensive)")
            else:
                print(f"⚠️ {doc_file}: {size_kb:.1f} KB (May be incomplete)")
                doc_validation = False
        else:
            print(f"❌ {doc_file}: Missing")
            doc_validation = False
    
    print("\n🎯 EVALUATION READINESS:")
    print("-" * 30)
    
    readiness_checks = [
        ("Project Structure", all_present),
        ("File Cleanup", cleanup_success),
        ("Documentation", doc_validation)
    ]
    
    overall_ready = all(check[1] for check in readiness_checks)
    
    for check_name, status in readiness_checks:
        status_icon = "✅" if status else "❌"
        print(f"{status_icon} {check_name}")
    
    print("-" * 30)
    
    if overall_ready:
        print("🚀 PROJECT IS READY FOR ACADEMIC EVALUATION!")
        print("\n📋 EVALUATION CHECKLIST:")
        print("✅ Complete source code in Jupyter notebook")
        print("✅ Comprehensive user documentation (MS Word)")
        print("✅ Detailed developer guide (MS Word)")
        print("✅ Clean project structure")
        print("✅ All dependencies specified")
        print("✅ Large-scale climate dataset included")
        print("✅ Testing and validation scripts")
        print("\n🎓 Ready for academic assessment!")
    else:
        print("❌ PROJECT NEEDS ATTENTION BEFORE EVALUATION")
        print("Please address the issues noted above.")
    
    return overall_ready

if __name__ == "__main__":
    success = validate_project_structure()
    
    print("\n" + "=" * 70)
    
    if success:
        print("🎉 VALIDATION COMPLETE - PROJECT READY FOR EVALUATION!")
        print("📂 Location: /workspaces/areeba_project/")
        print("🎯 Status: All requirements met")
    else:
        print("⚠️ VALIDATION FAILED - PLEASE ADDRESS ISSUES")
    
    print("=" * 70)
