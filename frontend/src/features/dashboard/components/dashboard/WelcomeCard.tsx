import { Card, CardContent } from "../../../../components/ui/card";
import { Button } from "../../../../components/ui/button";
import { Upload } from "lucide-react";

function WelcomeCard() {
  return (
    <Card className="max-w-3xl">
      <CardContent className="p-10 text-center space-y-6">

        <h1 className="text-4xl font-bold">
          Welcome to ResearchMind AI
        </h1>

        <p className="text-muted-foreground text-lg">
          Upload your research papers and ask questions using AI.
        </p>

        <Button size="lg">

          <Upload className="mr-2 h-5 w-5" />

          Upload Document

        </Button>

      </CardContent>
    </Card>
  );
}

export default WelcomeCard;