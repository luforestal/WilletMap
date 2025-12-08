#!/usr/bin/env python3
"""
Optimize tree photos for web display
- Resize to max 800px width (maintains aspect ratio)
- Compress with quality 85%
- Reduces ~360MB to ~15-20MB total
"""

from PIL import Image
from pathlib import Path
import sys

def optimize_photos(input_dir, output_dir, max_width=800, quality=85):
    """
    Optimize photos for web display
    
    Args:
        input_dir: Path to source photos
        output_dir: Path to save optimized photos
        max_width: Maximum width in pixels (default 800)
        quality: JPEG quality 1-100 (default 85)
    """
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    
    if not input_path.exists():
        print(f"❌ Error: Input directory not found: {input_dir}")
        sys.exit(1)
    
    # Create output directory
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Get all image files
    image_files = list(input_path.glob("*.jpg")) + \
                  list(input_path.glob("*.JPG")) + \
                  list(input_path.glob("*.jpeg")) + \
                  list(input_path.glob("*.JPEG")) + \
                  list(input_path.glob("*.png")) + \
                  list(input_path.glob("*.PNG"))
    
    if not image_files:
        print(f"❌ No image files found in {input_dir}")
        sys.exit(1)
    
    print(f"📸 Found {len(image_files)} photos")
    print(f"⚙️  Settings: max_width={max_width}px, quality={quality}%")
    print(f"📁 Output: {output_path}")
    print()
    
    total_original_size = 0
    total_optimized_size = 0
    
    for i, img_file in enumerate(image_files, 1):
        try:
            # Get original size
            original_size = img_file.stat().st_size
            total_original_size += original_size
            
            # Open and optimize
            with Image.open(img_file) as img:
                # Convert RGBA to RGB if needed
                if img.mode in ('RGBA', 'LA', 'P'):
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    if img.mode == 'P':
                        img = img.convert('RGBA')
                    background.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
                    img = background
                elif img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # Calculate new dimensions
                width, height = img.size
                if width > max_width:
                    new_width = max_width
                    new_height = int((max_width / width) * height)
                    img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                
                # Save optimized version
                output_file = output_path / img_file.name
                img.save(output_file, 'JPEG', quality=quality, optimize=True)
                
                # Get new size
                optimized_size = output_file.stat().st_size
                total_optimized_size += optimized_size
                
                # Calculate savings
                savings = ((original_size - optimized_size) / original_size) * 100
                
                print(f"[{i:2d}/{len(image_files)}] {img_file.name:20s} "
                      f"{original_size/1024/1024:5.1f}MB → {optimized_size/1024/1024:4.1f}MB "
                      f"({savings:4.1f}% smaller)")
        
        except Exception as e:
            print(f"❌ Error processing {img_file.name}: {e}")
            continue
    
    # Summary
    print()
    print("=" * 70)
    print(f"✅ Optimization complete!")
    print(f"   Original:  {total_original_size/1024/1024:6.1f} MB")
    print(f"   Optimized: {total_optimized_size/1024/1024:6.1f} MB")
    print(f"   Savings:   {total_original_size - total_optimized_size:,} bytes "
          f"({((total_original_size - total_optimized_size) / total_original_size) * 100:.1f}%)")
    print(f"   Files:     {len(image_files)}")
    print("=" * 70)


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Optimize tree photos for web')
    parser.add_argument('input_dir', help='Input directory with photos')
    parser.add_argument('output_dir', help='Output directory for optimized photos')
    parser.add_argument('-w', '--width', type=int, default=800, 
                       help='Maximum width in pixels (default: 800)')
    parser.add_argument('-q', '--quality', type=int, default=85,
                       help='JPEG quality 1-100 (default: 85)')
    
    args = parser.parse_args()
    
    optimize_photos(args.input_dir, args.output_dir, args.width, args.quality)
