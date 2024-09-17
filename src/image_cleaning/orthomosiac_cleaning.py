import Metashape
import os

def automate_metashape_process(project_path, images_folder, chunk_name, orthomosaic_path):
    # Create a new Metashape project
    doc = Metashape.app.document
    doc.save(project_path)
    
    # Add a new chunk to the project
    chunk = doc.addChunk()
    chunk.label = chunk_name

    # Import images into the chunk
    print("Importing images...")
    images = [f"{images_folder}/{image}" for image in os.listdir(images_folder) if image.lower().endswith(('.jpg', '.jpeg', '.png'))]
    chunk.addPhotos(images)

    # Align cameras
    print("Aligning cameras...")
    chunk.matchPhotos(accuracy=Metashape.HighAccuracy, preselection=Metashape.ReferencePreselection)
    chunk.alignCameras()

    # Build dense cloud
    print("Building dense cloud...")
    chunk.buildDenseCloud()

    # Build mesh
    print("Building mesh...")
    chunk.buildModel()

    # Build texture
    print("Building texture...")
    chunk.buildTexture()

    # Build orthomosaic
    print("Building orthomosaic...")
    chunk.exportOrthomosaic(orthomosaic_path, format=Metashape.ImageFormat.Tiff)

    # Save the project
    doc.save()

    print("Process completed successfully. Orthomosaic created at:", orthomosaic_path)

# Define paths
project_path = "metashape.psx"  # Path to save the Metashape project
images_folder = "../../data/raw_images/Priority1a/100MEDIA"      # Folder containing images, test pipeline on small image batch
chunk_name = "Chunk"                      # Name of the chunk
orthomosaic_path = "../../data//Priority1a.tif"  # Path to save the orthomosaic

# Run the automation process
automate_metashape_process(project_path, images_folder, chunk_name, orthomosaic_path)
