import { CheckCircle2 } from "lucide-react";

function UploadSuccess() {
  return (
    <div className="flex items-center gap-3 text-green-600">

      <CheckCircle2 />

      <span>

        Upload completed successfully.

      </span>

    </div>
  );
}

export default UploadSuccess;