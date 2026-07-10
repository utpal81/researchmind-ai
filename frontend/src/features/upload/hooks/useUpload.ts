import { useState } from "react";
import { uploadDocument } from "../../../api/documentsApi";

export function useUpload() {

    const [isUploading, setIsUploading] = useState(false);

    async function upload(file: File) {

        try {

            setIsUploading(true);

            const result = await uploadDocument(file);

            console.log(result);

        } finally {

            setIsUploading(false);

        }

    }

    return { upload, isUploading};

}