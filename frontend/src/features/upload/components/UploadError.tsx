import { AlertCircle } from "lucide-react";

type Props = {
  message: string;
};

function UploadError({ message }: Props) {
  return (
    <div className="flex items-center gap-3 text-red-600">

      <AlertCircle />

      <span>{message}</span>

    </div>
  );
}

export default UploadError;