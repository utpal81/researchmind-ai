import { Upload } from "lucide-react";
import { Button } from "../../../components/ui/button";
import { useUpload } from "../hooks/useUpload";

function UploadDropzone() {

    const { upload, isUploading } = useUpload();

    async function handleChange(
        event: React.ChangeEvent<HTMLInputElement>
    ) {

        const file = event.target.files?.[0];

        if (!file) return;

        await upload(file);

    }

    return (

        <div className="border-2 border-dashed rounded-xl p-16 text-center space-y-6">

            <Upload className="mx-auto h-14 w-14 text-muted-foreground" />

            <div>

                <h2 className="text-2xl font-semibold">

                    Upload Research Paper

                </h2>

                <p className="text-muted-foreground">

                    Drag & Drop your PDF here

                </p>

            </div>

            <input
                type="file"
                accept=".pdf"
                onChange={handleChange}
            />

            <Button disabled={isUploading}>

                {isUploading
                    ? "Uploading..."
                    : "Choose PDF File"}

            </Button>

        </div>

    );

}

export default UploadDropzone;