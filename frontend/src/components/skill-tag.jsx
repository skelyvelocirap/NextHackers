import Link from "next/link";
import { Badge } from "./ui/badge";

export default function SkillTag({ children, varient }) {
  return (
    <Badge
      className={`bg-background border border-border text-foreground ${
        varient === "small" ? "text-xs" : "text-sm"
      } hover:bg-muted/50 hover:scale-105 transition-all duration-200 ease-out`}
    >
      {children}
    </Badge>
  );
}
