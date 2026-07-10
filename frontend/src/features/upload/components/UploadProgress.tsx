import { Progress } from "../../../components/ui/progress";

type Props = {
  value: number;
};

function UploadProgress({ value }: Props) {
  return (
    <div className="space-y-2">
      <p className="text-sm">Uploading...</p>

      <Progress value={value} />
    </div>
  );
}

export default UploadProgress;